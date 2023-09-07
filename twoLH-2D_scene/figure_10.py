# Yes, I copy-pasted the Distances errors calculated with "twoLH_2Dscene.py" for every single experiment captured with blender.
# And use it to plot the error histogram.
# It was easier than trying to cleanly process all the data in a single script.


import pandas as pd
from datetime import datetime
from dateutil import parser
import numpy as np
import json

# Fix to avoid Type 3 fonts on the figures
# http://phyletica.org/matplotlib-fonts/
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import cv2


import seaborn as sns

errors = np.array([ 8.96709775,  9.48813162, 10.1128299 ,  8.79067917,  8.69783374,   # experiment 1
       10.72547084,  9.57945014,  9.9769595 , 10.08815274,  4.83449008,
        6.36685276,  4.46445687,  4.85650631,  3.39487254,  5.79308883,
        2.94729475,  4.37562248,  3.41771837,  4.27575505,  4.7990617 ,
        5.5160487 ,  5.0598412 ,  4.08583475,  4.40230892,  4.49222723,
        4.62463358,  4.97273921,  4.0022452 ,  4.4327672 ,  3.80216365,
        3.95588879,  4.66475034,  5.29121676,  5.46081249,  6.8959304 ,
        4.08036368,  5.45848111,  5.00273179,  5.57396413,  3.17190424,
        2.93743703,  4.53358727,  4.15194689,  4.36543589,  6.3919092 ,
        4.81987187,  4.757127  ,  4.65671174,  4.83696893,  4.93153479,
        5.40876322,  4.20996925,  4.57711262,  3.68855556,  4.06966304,
        4.27765224,  4.7165015 ,  3.27396711,  3.56422836,  4.64720967,
        1.54903427,  4.23888352,  3.15952485,  3.06332987,  3.58811393,
        2.93736103,  1.19874898,  1.4370042 ,  2.20102265,  1.70098901,
        0.79313569,  0.76406571,  1.48441089,  0.16328336,  1.18312641,
        1.02403091,  1.16997512,  1.2552097 ,  0.57799527,  1.12574955,
        1.57260349,  0.53768053,  0.69210116,  0.98703597,  1.08631082,
        0.45663441,  1.91615184,  0.62954177,  2.07295704,  1.45445588,
        1.70692773,  0.59443333,  2.39113439,  3.00781467,  3.09481092,
        2.66272911,  3.39675886,  3.626918  ,  2.94613709,  3.56740465,
        4.12634086,  2.88398306,  4.38084425,  4.75723939,  5.66270632,
        6.18022809,  6.309372  ,  5.31536974,  5.61606328,  4.6204842 ,
        4.94985693,  4.65255422,  4.75810645,  5.43387294,  4.66506941,
        5.59825965,  4.4377262 ,  4.6550935 ,  3.72832493,  4.26582491,
        6.02061153,  4.69052646,  4.71744475,  6.40574659,  4.5947613 ,
        4.67484837,  5.08941129,  4.89709146,  4.32707805,  5.07940466,
        5.79394396,  4.03091213,  3.96992048,  5.12660166,  5.05741874,
        4.80534088,  5.21456166,  5.83168392,  6.22427816,  5.14778786,
        6.31102648,  5.52319539,  6.35617502,  5.1838351 ,  5.54288737,
        7.31323264,  5.21664814,  5.68911248,  5.48421948,  5.80064088,
        6.55755434,  5.68898621,  5.95156866,  6.16752745,  5.20324514,
        5.87588865,  6.05887343,  5.18456804,  6.46168547,  5.18565179,
        4.57722549,  4.2409048 ,  4.67256355,  4.79322074,  4.515124  ,
        5.37554732,  5.82219831,  4.33775802,  5.15676162,  4.87663172,
        4.74033077,  5.53375553,  3.37048306,  5.54685072,  4.59578907,
        5.37988027,  3.85184085,  4.38449929,  3.6831873 ,  5.01137623,
        4.88153619,  3.58613342,  2.23093301,  3.07675326,  1.40385226,
        1.40829153,  1.01004358,  0.9162736 ,  1.8763298 ,  1.13952256,
        1.06572666,  2.55707994,  1.39756207,  1.26436461,  0.77313151,
        1.02448628,  1.45436066,  1.6222258 ,  0.96549132,  1.03067903,
        1.06599371,  1.11421635,  1.54036774,  2.01083562,  0.79811912,
        2.19265607,  1.63141419,  3.36306403,  1.86167729,  2.01974914,
        0.96811067,  1.79385314,  0.95070671,  0.33411074,  0.88268015,
        0.93201536,  2.10676847,  0.53863607,  0.23290797,  1.39259533,
        0.82121336,  1.91543946,  0.67618253,  0.05351459,  1.27592415,
        0.23901488,  1.54377638,  1.40238044,  0.85013343,  1.7702496 ,
        0.95831873,  2.45009818,  1.8818107 ,  3.44986823,  1.79446528,
        1.85466856,  2.16303346,  1.59094621,  1.6855847 ,  1.336786  ,
        1.78877318,  1.24272481,  2.62893616,  3.07537242,  2.79687768,
        1.91649146,  2.54295489,  3.17077469,  1.84023249,  1.48198805,
        1.8793392 ,  1.26846999,  0.26381651,  1.86466917, 5.45277929,   # Experiment 2
        4.34858985, 4.05085254, 4.71837632, 5.63693451,
       3.20035684, 3.41938507, 2.14186173, 2.98722245, 1.90138501,
       1.78220598, 1.66531444, 1.70046798, 1.3982357 , 3.3764498 ,
       3.83377635, 3.62970239, 2.33505563, 1.68929625, 2.17828226,
       1.70131238, 3.22053355, 3.44256188, 3.11765989, 1.62528686,
       2.50528748, 3.78586267, 3.93288315, 2.62608085, 2.39005395,
       1.96932842, 0.99496556, 2.55619257, 0.63333555, 0.91323482,
       3.72780823, 3.33102067, 3.67471462, 3.72289658, 2.49875107,
       0.81329757, 3.40608262, 3.02877359, 5.07005886, 9.76958787,
       5.36378032, 4.21983253, 3.89039523, 5.07865436, 3.21458048,
       6.52791637, 6.84910657, 5.22040933, 8.43694926, 2.19049354,
       4.14616835, 2.75401146, 2.48651702, 3.14483016, 1.71452129,
       3.93871927, 1.38645954, 1.2405883 , 4.30084611, 0.72910093,
       0.80354756, 0.19889558, 4.97294406, 1.79827125, 4.4224626 ,
       5.43593708, 2.96845009, 3.1041498 , 2.90752432, 1.90549965,
       0.85597201, 2.34418676, 2.89491107, 3.27002566, 9.72913142, 
       5.51354487, 3.3097141 , 1.93993061, 4.0310259 ,                  # Experiment 3 - Red
       4.32040921, 0.83701462, 3.27436841, 3.18747308, 3.15999473,
       1.019075  , 3.62752516, 1.93985436, 5.07379741, 3.55745538,
       1.84864566, 2.59955737, 2.02435835, 3.95645001, 2.39649762,
       1.34722451, 2.11752421, 2.93232177, 4.09948224, 3.5766583 ,
       3.01054101, 4.01072557, 4.32875965, 4.1379616 , 3.14955734,
       4.63836937, 2.03641944, 2.93188369, 3.86760209, 3.87994205,
       3.96945407, 0.60621429, 1.16442922, 1.49566355, 3.2000906 ,
       2.96698752, 1.53242455, 2.27593523, 2.87935725, 2.7436809 ,
       3.42890206, 1.79942607, 9.30155384,  9.0203712 ,  9.26072522,  # Experiment 3 - Green
       10.11520236,  9.03450563,
        9.0179262 , 11.05251461, 10.90457176,  8.7177136 ,  9.64955337,
       10.32426324,  8.67795984,  9.89965131,  9.61090224,  8.39924302,
        8.25610876, 10.09854568,  8.41404063,  7.97417807,  8.86790586,
        7.38505305,  6.39176972,  6.61117192,  5.27087803,  5.24500197,
        5.8644165 ,  7.20483228,  4.72052195,  4.6716546 ,  4.28920166,
        3.52755279,  4.27211312,  3.67008271,  4.60527867,  1.55393231,
        4.56792267,  4.41014339,  3.6132272 ,  5.73973887,  4.29428903,
        4.68922189,  4.04256705,  2.33282558,  4.99899043,  5.41432048,
        3.69431544,  4.29884882,  2.76532212,  3.35867448,  5.7319949 ,
        5.29816174,  5.47433103,  3.27217991,  2.43949784,  3.2465618 ,
        7.2264659 ,  6.94967139,  2.55788726,  3.18300454,  4.45363635,
        4.53213565,  2.59285804,  3.08990083,  2.86726108,  2.78410893,
        3.87321168,  3.72763655,  5.63075665,  5.36719602,  3.04434468,
        4.30141956,  3.83756697,  4.7293294 ,  4.21294818,  3.41607857,
        3.63964135,  4.75441747,  5.86680096,  6.2775    ,  3.67817583,
        4.04395787,  4.98745909,  7.72668786,  8.50118354,  6.06639149,
        8.58871487,  7.16595   ,  6.86110403,  8.35208346,  9.78412549,
        3.90976167, 13.96346674, 11.4348252 ,  6.41830997, 12.67143157,
       12.24449122, 10.57385154, 14.05528639,  8.32106965, 11.43822465,
       11.59251659, 12.08110933, 2.22520377, 1.19647909, 1.78739899,    # Experiment 4 - Red
       1.48635462, 0.61964333,
       2.781644  , 0.39042986, 0.99933796, 3.15179823, 3.2513947 ,
       1.99678863, 2.01354383, 0.88994254, 2.18523658, 1.78466379,
       2.5225179 , 2.41592723, 1.98532874, 1.5547653 , 1.5863883 ,
       2.22705731, 1.35104511, 2.0642938 , 2.14460676, 2.67434192,
       1.92704437, 4.76340157, 4.85304979, 2.0680257 , 0.85039199,
       3.81060726, 1.56622421, 3.25538626, 3.30094753, 0.87782648,
       0.94243546, 1.63375873, 1.10560117, 1.70421921, 1.7465014 ,
       0.71515879, 1.62634767, 2.91586971, 0.86379296, 0.79284501,
       2.42090801, 2.23680806, 1.98688168, 3.29415711, 0.92134688,
       3.50252041, 2.44453008, 3.53627992, 1.06217389, 2.96858605,
       2.12680988, 3.5381384 , 1.51941178, 4.06581314, 4.59819387,
       2.93500945, 4.04734724, 4.02913111, 1.89526565, 6.31974606,
       3.44171713, 5.17916446, 5.42857803, 6.07394536, 7.03731765,
       7.26111814, 6.20664693, 6.13610949, 7.11009381, 7.80461402,
       7.17863668, 9.93083566,  9.02475368,  8.22768775, 10.95796141,    # Experiment 4 - Blue
       11.39548786,
       14.11547457,  9.89311779, 14.14476809, 22.78893294, 19.38216705,
        9.36959649, 10.4972306 ,  7.80345271,  8.30039757,  6.71780263,
        6.69059105,  6.97607086,  6.6773993 ,  5.73076036,  4.99317844,
        3.94822121,  1.71500841,  2.40156936,  2.80402575,  1.6986923 ,
        1.71780288,  2.36968485,  2.57152848,  2.35866307,  3.17907608,
        3.13862764,  3.76570128,  4.06928707,  3.39890264,  3.68942133,
        1.29072848,  4.30143627,  5.72009419,  4.40537328,  4.63733841,
        4.53796913,  4.96708965,  5.07216247,  1.47057147,  1.60175776,
        3.2293409 ,  0.70151163,  0.90062881,  2.50157055,  4.61206062,
        4.11332683,  3.94333512,  4.06143363,  4.80757853,  3.44475391,
        3.7817147 ,  4.96728354,  6.56856424,  6.38921401,  6.71828064,
        6.07523554,  5.94593282,  7.04124371,  6.84542372,  8.98879236,
        8.51999588,  8.59154144,  8.38050615,  8.93755159, 10.3201447 ,
        4.62047847,  6.19713577,  5.87761942,  9.6992713 , 15.57719557,
       10.07324369,  8.40271897,  7.66193495,  7.13894815,  8.28799245,
        8.41086279,  7.9122787 ,  7.99436455,  8.38282237,  7.84198031,
        9.54967859,  9.50647729,  7.60181273,  7.87965406,  6.94358053,
        7.69956669,  3.80552437,  3.58447977,  2.73756872,  2.23569548,
        2.01439556,  3.52204097,  3.24112721,  3.35896349,  3.8262867 ,
        2.46266169,  3.84926017,  3.5869706 ,  3.63764517,  5.71344219,
        3.22142952,  2.67730712,  2.23501097,  1.6219313 ,  2.15977812,
        2.74448091,  2.69375241,  2.92368939,  3.81125724,  3.15751309,
        2.10126743,  4.08427068,  2.07770853,  1.63593299,  1.22989126,
        4.02252638,  3.42231571,  1.21573864,  0.79370748,  1.9281582 ,
        1.21120299,  2.8982111 ,  1.21542645,  2.03248244,  2.08893229,
        1.28120655,  1.01794102,  0.54782683,  0.92547607,  1.40942077,
        1.67272513,  4.59628946,  4.87111122,  6.06324498,  6.74059787,
        8.52416492,  8.34000023,  7.82240188,  6.92272673,  6.0316608 ,
        5.32743119,  6.50723007,  6.04262135,  6.11368876,  4.75610033,
        6.1503377 ,  5.34189288,  4.4920712 ,  3.70885005,  4.94766585,
        4.99743344,  5.69978231,  4.45285939,  5.33720061,  4.46704744,
        9.78218842,  7.81854557,  6.63372261,  4.28054306,  4.6752485 ,
        5.03472   ,  5.18839195,  6.6652012 ,  6.64254203,  7.33577182,
        7.95390691,  8.45402358,  7.88698355,  7.64716828,  8.16030577,
        6.98850246,  8.34237547,  7.3966076 ,  7.39123473,  7.31567951,
        7.67848965,  7.57438676,  8.25293122,  8.05912367, 6.86718473,   # Experiment 4 - Green
        8.19038661,  6.90541974,  6.16186684,  8.2891338 ,
        6.56118747,  6.79121241,  7.19453111,  6.84831566,  7.84365341,
        6.22447931,  7.16513701,  5.90940117,  7.59461108,  8.4143433 ,
        7.32237489,  6.6392116 ,  8.2596864 ,  7.61703831,  7.34107118,
        7.15459563,  6.55003332,  7.02564656,  6.5427418 ,  6.89371122,
        6.67073866,  7.13382795,  7.75559913,  4.25581136,  5.21943851,
        6.3624652 ,  5.38070958,  4.66707034,  4.96378014,  5.59054948,
        5.71341988,  5.18827928,  5.43584858,  3.54205667,  6.38464976,
        5.55416334,  5.88762846,  3.90496248,  5.46754857,  6.53596319,
        5.54544724,  5.88632565,  2.28689871,  3.82365938,  1.92115974,
        2.06267948,  2.75685756,  1.63977757,  1.72478837,  2.2760003 ,
        2.24528693,  1.03192648,  1.75662898,  1.51650792,  3.12811347,
        2.57368538,  1.90102754,  1.79671634,  2.51834557,  3.13898805,
        4.42972729,  2.05862796,  1.84549951,  2.06467549,  1.64104801,
        2.48001581,  2.02985658,  2.84137965,  3.19660604,  1.22251033,
        4.20298617,  3.21575676,  0.85789675,  4.68021692,  2.7864973 ,
        2.93461474,  3.96697179,  3.87835842,  3.34181259,  6.33467838,
        3.12404037,  2.23766513,  1.82043616,  2.37723702,  4.12735153,
        5.32611998,  7.06637548,  4.13171879, 17.10353481,  7.85753582,
        7.23406076,  7.02720351,  8.04524528,  7.76438678,  6.41437236,
        6.81593821,  4.50396147,  4.38551581,  5.65729514,  8.37050343,
       10.7238853 , 11.99824317, 10.30339271,  7.63321665,  5.21018451,
        5.85881981,  5.56806803,  6.21650311,  6.99465892,  8.5221466 ,
        9.63800058,  9.45388615,  9.62954966,  8.88319785,  9.45585177,
        7.38840704,  9.64445777, 10.67752796,  6.89524348,  8.564537  ,
        6.18722407,  7.06776574,  7.71642644, 3.19234763, 4.91044513,   # Experiment 5 - Red
        4.86010864, 4.77608355, 3.9371199 ,
       5.32945275, 1.80652086, 4.23925581, 2.39842222, 1.28003418,
       0.51328781, 0.82525769, 1.88303309, 0.97341504, 1.10430841,
       0.73348548, 0.95261689, 0.29424509, 3.91464651, 1.33505557,
       2.12091615, 0.41381341, 2.82982772, 2.57542596, 1.41935536,
       2.15586443, 2.78489441, 2.9260892 , 2.04151377, 1.74556215,
       1.7618088 , 2.97125341, 2.42823602, 2.65313235, 2.66843002,
       2.33736906, 2.42953064, 2.41797969, 3.33408658, 2.92536583,
       3.77969849, 2.87042551, 4.82118326, 5.27163944, 1.25700759,
       4.31306447, 1.38998831, 4.00527126, 2.52136463, 5.68128814,
       7.88058875, 4.95512694, 5.49974416, 1.2706562 , 2.32889731,
       2.52386733, 2.83358317, 3.22235764, 4.49075914, 2.86101721,
       1.37834768, 1.70758296, 2.76442509, 2.86674607, 2.04708827,
       1.51459422, 2.01078454, 1.88123341, 2.39305875, 4.28675534,
       3.47041634, 1.59044644, 0.3560293 , 0.88658196, 0.36505378,
       1.904912  , 3.31646087, 0.27227445, 2.93684398, 1.67312275,
       2.02928747, 1.95794632, 2.05218576, 2.38016205, 1.80507196,
       2.65650543, 2.93934703, 5.81734853, 2.23166025, 9.97601037,
       3.60900317, 4.59784985, 6.27482403, 2.41800786, 8.82663392,
       6.28902643, 8.41174053, 6.43344628, 6.76554019, 6.04819638,
       8.81125305, 6.41765952, 7.24034845, 7.66023303, 6.06836243,
       6.11683223, 5.6226795 , 4.95282605, 4.38782236, 5.47340004,
       3.58272941, 3.81563897, 4.48679051, 4.25776829, 2.98995155,
       3.82324175, 5.64406893, 4.06707426, 3.06463394, 3.82448305,
       3.26883191, 2.84309702, 4.79561299, 2.80736689, 2.22186039,
       2.82546852, 2.62200153, 1.92052154, 3.83581882, 1.83500401,
       1.60218917, 2.34269088, 1.35079584, 2.51869054, 1.72214815,
       0.7522229 , 1.98122931, 0.79875321, 1.98500128, 0.8198243 ,
       3.53672597, 1.04018573, 2.7264624 , 1.44373511, 1.54230822,
       1.52154974, 1.0595886 , 1.43106397, 1.57454946, 1.00108431,
       1.91263388, 1.30114853, 1.22150893, 2.16923454, 1.97566025,
       2.23467312, 2.24520163, 1.83927731, 2.09945692, 1.25953234,
       2.10006242, 4.18647837, 3.28402348, 1.3879787 , 0.42279174,
       2.12235196, 2.34253171, 1.08245663, 1.92625086, 1.72375797,
       1.50609764, 1.1674506 , 0.46971211, 1.18715712, 1.64444948,
       1.31272713, 1.27609735, 0.98978577, 1.92013945, 1.66935848,
         2.11746981,  2.89605136,  2.77177309,  4.74440579,  3.06705373,  # Experiment 5 - Green
        3.07047051,  2.83492672,  1.86967779,  4.43161709,  3.27848246,
        2.78144373,  5.57247438,  4.4833549 ,  4.4889927 ,  5.4921109 ,
        6.96215002,  6.84607383,  6.60590502,  5.54113988,  5.72427798,
        6.73063285,  4.57312142,  6.16959427,  7.68399735,  5.59927441,
        6.76068313,  7.33326226,  4.95709519,  4.16929331,  4.86483539,
        4.77055382,  6.15091137,  4.21710782,  8.48504193,  5.28563891,
        7.1174294 ,  5.31709075,  7.36305579,  8.15897628,  6.28048885,
        7.00572758,  4.3257806 ,  5.03468387,  6.03372445,  3.43111076,
        6.24938674,  4.96450888,  7.77100284,  2.28202095,  6.44411513,
        5.53283355,  8.04092055,  2.87192562,  7.02005592,  4.99664966,
        4.2384429 ,  4.75252303,  5.06763507,  6.03474206,  4.82797839,
        1.3881052 ,  7.46143213,  5.81303325,  4.48971694,  6.87932595,
        8.75075553,  5.84601574,  8.38023243,  9.34325728,  8.32138353,
        8.81808588,  8.0471979 ,  8.58343167,  9.64245567,  8.98005365,
       10.1442669 ,  6.85200752,  7.2223062 ,  6.8937441 ,  6.44529077,
        7.80587837,  5.53890261,  6.84814312, 14.28611871, 10.84327783,
        7.5293804 ,  7.21703125,  6.85904586,  6.85424805,  8.91440819,
        7.38033156,  6.47083083,  7.89167433,  8.75102882,  6.1893224 ,
        7.7776618 ,  7.91139693,  5.05534923,  4.96289892,  5.10765957,
        3.00977535,  5.27644739,  5.84391977,  2.24637516,  5.62065864,
        1.71511097,  3.188384  ,  3.6492929 ,  4.21163984,  3.37154076,
        2.13875427,  0.73849007,  0.73461033,  0.36824286,  0.82591297,
        0.63892331,  0.26853063,  0.36879238,  0.66670623,  0.85698313,
        1.05629346,  1.74849971,  0.5137283 ,  1.64484877,  3.74484873,
        3.39633395])

print(f"Mean Absolute Error = {errors.mean()} mm")
print(f"Root Mean Square Error = {np.sqrt((errors**2).mean())} mm")
print(f"Error Standard Deviation = {errors.std()} mm")

# prepare the plot
fig = plt.figure(layout="constrained", figsize=(5,4))
gs = GridSpec(3, 3, figure = fig)
hist_ax    = fig.add_subplot(gs[0:3, 0:3])
axs = (hist_ax,)


# Sea-born KDE histogram plot
sns.histplot(data=errors,  bins=50, ax=hist_ax, linewidth=0, color="xkcd:baby blue")
hist_ax.set_xlim((0, 20))
ax2 = hist_ax.twinx()
sns.kdeplot(data=errors, ax=ax2, label="density", color="xkcd:black", linewidth=1, linestyle='--')

hist_ax.axvline(x=errors.mean(), color='xkcd:red', label="Mean")
# Trick to get the legend  unified between the TwinX plots
hist_ax.plot([], [], color="xkcd:black", linestyle='--', label = 'density')

xticks_locs = np.linspace(0, 20, 5)  # 5 x-ticks from 0 to 10
hist_ax.set_xticks(xticks_locs)

for ax in axs:
    # ax.grid()
    ax.legend()

# hist_ax.set_title('twoLH-2D Accuracy Analysis')
hist_ax.set_xlabel('Distance Error [mm]')
hist_ax.set_ylabel('Measurements')

plt.savefig('Result-D-2lh_2d-histogram.pdf')

plt.show()
