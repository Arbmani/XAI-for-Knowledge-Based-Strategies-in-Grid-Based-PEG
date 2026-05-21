import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(RIGHT)"] <= -0.000000:
        if features["E(LEFT) - E(RIGHT)"] <= -0.326080:
            if features["E(DOWN) - E(RIGHT)"] <= -0.210205:
                if features["E(UP) - E(RIGHT)"] <= -0.163696:
                    return 3
                else:
                    if features["E(LEFT)"] <= 0.000000:
                        if features["E(UP) - agent_column"] <= 0.355189:
                            if features["E(RIGHT)"] <= 0.801673:
                                if features["T(RIGHT) - agent_column"] <= 0.439309:
                                    return 3
                                else:
                                    return 0
                            else:
                                return 3
                        else:
                            return 0
                    else:
                        if features["E(UP) - E(DOWN)"] <= 0.667545:
                            if features["E(LEFT)"] <= 0.000095:
                                return 3
                            else:
                                if features["E(RIGHT) - agent_row"] <= -12.599815:
                                    return 0
                                else:
                                    if features["E(LEFT)"] <= 0.019740:
                                        return 3
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -2.530398:
                                            return 3
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -1.817435:
                                                return 0
                                            else:
                                                return 3
                        else:
                            if features["T(RIGHT) - agent_row"] <= -9.487266:
                                if features["T(DOWN) - agent_column"] <= -10.951567:
                                    return 0
                                else:
                                    return 3
                            else:
                                if features["T(up) - T(RIGHT)"] <= 0.588331:
                                    if features["agent_row - agent_column"] <= 3.500000:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 3
            else:
                if features["E(DOWN) - E(RIGHT)"] <= 0.000006:
                    if features["E(LEFT)"] <= 0.000342:
                        if features["E(RIGHT) - agent_column"] <= -11.216132:
                            if features["E(RIGHT) - agent_row"] <= -4.134466:
                                return 1
                            else:
                                return 3
                        else:
                            if features["agent_column - time_left"] <= -0.030000:
                                return 1
                            else:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.729816:
                                    if features["E(DOWN) - time_left"] <= -0.062953:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    return 3
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.370804:
                            if features["T(DOWN) - T(RIGHT)"] <= -0.000029:
                                if features["T(LEFT) - agent_column"] <= -3.000000:
                                    if features["T(LEFT) - time_left"] <= -0.179928:
                                        if features["E(LEFT) - agent_row"] <= -9.949421:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(UP) - time_left"] <= 0.127338:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -3.576498:
                                                return 1
                                            else:
                                                return 3
                                else:
                                    if features["T(LEFT) - agent_column"] <= -0.994457:
                                        if features["T(RIGHT) - agent_column"] <= -1.591593:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        if features["E(RIGHT) - T(RIGHT)"] <= -0.000195:
                                            return 1
                                        else:
                                            return 3
                            else:
                                if features["time_left"] <= 0.580000:
                                    return 3
                                else:
                                    return 1
                        else:
                            return 3
                else:
                    if features["E(DOWN) - agent_row"] <= -11.224349:
                        return 3
                    else:
                        if features["E(RIGHT) - agent_row"] <= -0.292160:
                            if features["E(UP) - E(RIGHT)"] <= -0.860452:
                                if features["T(LEFT) - agent_row"] <= -6.724626:
                                    return 1
                                else:
                                    if features["agent_row - agent_column"] <= -6.500000:
                                        return 1
                                    else:
                                        return 3
                            else:
                                if features["E(UP)"] <= 0.000000:
                                    return 1
                                else:
                                    if features["T(DOWN) - agent_column"] <= -11.766685:
                                        return 1
                                    else:
                                        if features["E(RIGHT)"] <= 0.620474:
                                            if features["E(UP) - T(LEFT)"] <= 0.003236:
                                                return 1
                                            else:
                                                if features["E(DOWN) - agent_column"] <= -1.594986:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            return 1
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.312497:
                                return 1
                            else:
                                return 3
        else:
            if features["E(DOWN) - time_left"] <= 0.324517:
                if features["E(UP) - T(up)"] <= 0.011439:
                    if features["E(DOWN) - time_left"] <= 0.098382:
                        if features["E(LEFT) - time_left"] <= 0.083626:
                            if features["E(DOWN)"] <= 0.060800:
                                return 3
                            else:
                                if features["E(UP) - T(DOWN)"] <= 0.304677:
                                    if features["T(DOWN) - time_left"] <= -0.487301:
                                        return 1
                                    else:
                                        if features["E(LEFT) - E(RIGHT)"] <= -0.211348:
                                            if features["T(DOWN) - agent_column"] <= 0.000068:
                                                if features["T(up) - T(DOWN)"] <= 0.266997:
                                                    if features["T(LEFT) - agent_column"] <= -1.908380:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.100280:
                                                return 1
                                            else:
                                                return 3
                                else:
                                    return 3
                        else:
                            return 2
                    else:
                        if features["E(UP) - T(RIGHT)"] <= 0.237629:
                            if features["E(LEFT)"] <= 0.347112:
                                if features["E(LEFT) - agent_column"] <= -2.851243:
                                    if features["T(RIGHT) - agent_row"] <= -4.751594:
                                        if features["T(LEFT)"] <= 0.000000:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.134259:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 1
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -4.661954:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    if features["E(UP) - E(DOWN)"] <= -0.228586:
                                        return 1
                                    else:
                                        if features["E(LEFT) - T(up)"] <= -0.187473:
                                            if features["T(LEFT)"] <= 0.000001:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.199822:
                                                return 0
                                            else:
                                                return 2
                            else:
                                if features["E(UP)"] <= 0.000004:
                                    return 1
                                else:
                                    return 2
                        else:
                            if features["T(up) - T(LEFT)"] <= -0.000114:
                                return 3
                            else:
                                return 1
                else:
                    if features["E(LEFT) - E(RIGHT)"] <= -0.108335:
                        if features["E(DOWN) - T(DOWN)"] <= -0.198176:
                            if features["E(DOWN) - T(RIGHT)"] <= 0.230944:
                                if features["E(UP) - E(RIGHT)"] <= -0.207974:
                                    return 1
                                else:
                                    if features["T(up) - T(LEFT)"] <= -0.000074:
                                        return 0
                                    else:
                                        if features["E(LEFT) - T(DOWN)"] <= -0.389220:
                                            return 0
                                        else:
                                            return 2
                            else:
                                return 3
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= -0.000005:
                                if features["E(UP) - T(up)"] <= 0.215018:
                                    if features["E(RIGHT)"] <= 0.313226:
                                        if features["T(up) - agent_column"] <= -0.999717:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(RIGHT) - agent_row"] <= -2.632978:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.032141:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - agent_row"] <= -4.676164:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT) - E(RIGHT)"] <= -0.216714:
                                        return 0
                                    else:
                                        return 2
                            else:
                                if features["T(up) - T(RIGHT)"] <= -0.000005:
                                    if features["E(UP) - E(DOWN)"] <= -0.218303:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 3
                    else:
                        if features["E(DOWN) - T(RIGHT)"] <= 0.147405:
                            if features["E(RIGHT) - agent_row"] <= -3.784469:
                                if features["agent_row - time_left"] <= 5.930000:
                                    return 2
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= -0.007124:
                                        return 1
                                    else:
                                        if features["E(DOWN) - T(up)"] <= 0.074996:
                                            return 0
                                        else:
                                            return 2
                            else:
                                if features["E(UP) - E(DOWN)"] <= -0.208316:
                                    return 1
                                else:
                                    return 0
                        else:
                            if features["E(DOWN)"] <= 0.327774:
                                if features["T(DOWN) - T(LEFT)"] <= -0.000049:
                                    return 3
                                else:
                                    return 0
                            else:
                                if features["T(up) - agent_column"] <= -8.999981:
                                    return 2
                                else:
                                    return 1
            else:
                if features["E(UP) - E(LEFT)"] <= -0.315767:
                    if features["E(LEFT) - agent_row"] <= -12.132387:
                        return 2
                    else:
                        if features["T(up)"] <= 0.000000:
                            if features["E(RIGHT) - agent_column"] <= -11.986044:
                                return 2
                            else:
                                return 1
                        else:
                            if features["E(UP)"] <= 0.000000:
                                return 1
                            else:
                                if features["E(LEFT)"] <= 0.657364:
                                    if features["E(UP) - T(LEFT)"] <= 0.000666:
                                        if features["E(UP)"] <= 0.045901:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 2
                                else:
                                    if features["E(DOWN) - agent_column"] <= -2.212872:
                                        if features["E(UP) - agent_column"] <= -5.999918:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.867804:
                                            return 1
                                        else:
                                            if features["T(up) - agent_column"] <= -0.999810:
                                                return 1
                                            else:
                                                return 2
                else:
                    if features["E(LEFT) - T(LEFT)"] <= 0.030361:
                        return 1
                    else:
                        if features["T(DOWN) - T(RIGHT)"] <= 0.000383:
                            return 1
                        else:
                            if features["E(DOWN) - agent_column"] <= -6.504752:
                                return 1
                            else:
                                if features["T(DOWN) - time_left"] <= 0.669933:
                                    return 3
                                else:
                                    return 1
    else:
        if features["E(UP) - E(LEFT)"] <= -0.000019:
            if features["E(DOWN) - T(RIGHT)"] <= 0.102864:
                if features["E(UP)"] <= 0.662893:
                    if features["E(LEFT) - time_left"] <= 0.325109:
                        if features["E(UP) - T(RIGHT)"] <= 0.328268:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.062442:
                                if features["T(up) - T(RIGHT)"] <= -0.000005:
                                    return 2
                                else:
                                    if features["E(UP) - time_left"] <= 0.231835:
                                        return 1
                                    else:
                                        return 0
                            else:
                                return 2
                        else:
                            if features["E(RIGHT)"] <= 0.000254:
                                return 2
                            else:
                                if features["T(up) - agent_column"] <= -11.999457:
                                    return 0
                                else:
                                    return 2
                    else:
                        if features["E(UP) - T(DOWN)"] <= 0.314746:
                            return 2
                        else:
                            if features["E(LEFT) - T(LEFT)"] <= 0.008504:
                                if features["E(RIGHT) - T(LEFT)"] <= -0.385360:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(RIGHT) - agent_column"] <= -2.999274:
                                    return 2
                                else:
                                    return 0
                else:
                    if features["E(RIGHT) - agent_column"] <= -1.999998:
                        return 2
                    else:
                        return 0
            else:
                if features["E(LEFT)"] <= 0.388978:
                    if features["T(RIGHT)"] <= 0.016242:
                        if features["E(LEFT) - time_left"] <= 0.279347:
                            if features["E(RIGHT) - T(up)"] <= 0.015253:
                                if features["E(LEFT) - E(RIGHT)"] <= 0.091608:
                                    return 1
                                else:
                                    if features["T(DOWN)"] <= 0.000000:
                                        return 1
                                    else:
                                        return 2
                            else:
                                if features["T(DOWN) - T(LEFT)"] <= -0.000050:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.512397:
                                        return 2
                                    else:
                                        return 3
                                else:
                                    return 2
                        else:
                            if features["T(up) - T(LEFT)"] <= -0.344492:
                                if features["E(DOWN) - agent_row"] <= -5.697178:
                                    if features["E(UP) - T(LEFT)"] <= -0.374295:
                                        return 2
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -8.614368:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    if features["E(UP)"] <= 0.030592:
                                        return 2
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= -0.064350:
                                            return 2
                                        else:
                                            return 1
                            else:
                                return 2
                    else:
                        if features["E(DOWN) - agent_row"] <= -7.766846:
                            if features["E(DOWN) - agent_column"] <= -7.755091:
                                if features["E(LEFT) - T(up)"] <= 0.178138:
                                    return 2
                                else:
                                    return 1
                            else:
                                return 1
                        else:
                            if features["E(UP) - time_left"] <= 0.205448:
                                if features["E(DOWN) - T(DOWN)"] <= -0.048537:
                                    return 2
                                else:
                                    if features["E(RIGHT) - time_left"] <= -0.019038:
                                        return 2
                                    else:
                                        return 1
                            else:
                                if features["agent_row - agent_column"] <= -3.500000:
                                    return 2
                                else:
                                    return 1
                else:
                    if features["E(UP) - time_left"] <= 0.163754:
                        if features["E(RIGHT)"] <= 0.000001:
                            if features["E(UP) - agent_column"] <= -13.996937:
                                return 1
                            else:
                                return 2
                        else:
                            if features["E(LEFT) - agent_column"] <= -2.201778:
                                if features["E(LEFT) - T(LEFT)"] <= 0.002879:
                                    if features["T(RIGHT) - time_left"] <= -0.032581:
                                        if features["T(up) - agent_column"] <= -8.999818:
                                            if features["E(UP) - agent_row"] <= -3.900791:
                                                return 2
                                            else:
                                                if features["T(LEFT)"] <= 0.600321:
                                                    return 1
                                                else:
                                                    return 2
                                        else:
                                            return 1
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN) - E(RIGHT)"] <= 0.764227:
                                        return 2
                                    else:
                                        return 1
                            else:
                                if features["E(UP) - agent_row"] <= -11.999987:
                                    return 2
                                else:
                                    if features["E(RIGHT)"] <= 0.000004:
                                        return 2
                                    else:
                                        return 1
                    else:
                        if features["T(RIGHT)"] <= 0.090927:
                            return 2
                        else:
                            return 1
        else:
            if features["E(UP) - E(DOWN)"] <= 0.358045:
                if features["E(UP) - E(LEFT)"] <= 0.127119:
                    if features["T(up) - T(LEFT)"] <= -0.000058:
                        if features["E(UP) - T(up)"] <= 0.246829:
                            if features["T(up) - T(DOWN)"] <= 0.304725:
                                return 2
                            else:
                                if features["E(LEFT) - time_left"] <= 0.201675:
                                    return 3
                                else:
                                    return 0
                        else:
                            if features["T(DOWN) - T(LEFT)"] <= -0.000134:
                                if features["E(UP) - time_left"] <= 0.271460:
                                    return 3
                                else:
                                    return 0
                            else:
                                return 0
                    else:
                        if features["T(up) - agent_row"] <= -12.619908:
                            return 0
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.230549:
                                if features["E(LEFT) - T(up)"] <= -0.084398:
                                    if features["E(UP)"] <= 0.389559:
                                        if features["T(up) - T(RIGHT)"] <= -0.000028:
                                            return 2
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= 0.140578:
                                                return 1
                                            else:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.120922:
                                                    if features["T(up)"] <= 0.365085:
                                                        return 2
                                                    else:
                                                        if features["E(DOWN) - T(DOWN)"] <= 0.000142:
                                                            return 0
                                                        else:
                                                            return 2
                                                else:
                                                    return 1
                                    else:
                                        if features["T(DOWN) - time_left"] <= -0.028749:
                                            if features["T(up) - agent_column"] <= -8.506096:
                                                return 3
                                            else:
                                                return 2
                                        else:
                                            return 0
                                else:
                                    return 2
                            else:
                                if features["T(DOWN) - time_left"] <= 0.187321:
                                    if features["E(LEFT) - T(RIGHT)"] <= -0.076763:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 0
                else:
                    if features["E(UP) - time_left"] <= 0.259197:
                        if features["E(DOWN)"] <= 0.034873:
                            return 0
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= -0.000020:
                                if features["E(LEFT) - T(up)"] <= -0.189097:
                                    if features["E(UP)"] <= 0.349513:
                                        return 1
                                    else:
                                        return 0
                                else:
                                    return 2
                            else:
                                if features["T(DOWN) - T(LEFT)"] <= -0.001940:
                                    return 3
                                else:
                                    return 0
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.324136:
                            if features["T(LEFT) - agent_row"] <= -10.762495:
                                if features["E(DOWN)"] <= 0.059434:
                                    return 0
                                else:
                                    if features["T(DOWN) - agent_column"] <= -2.981102:
                                        if features["T(LEFT) - agent_row"] <= -10.810001:
                                            if features["E(UP) - time_left"] <= 0.359632:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 1
                                    else:
                                        return 1
                            else:
                                return 0
                        else:
                            if features["E(DOWN) - T(up)"] <= -0.295126:
                                return 3
                            else:
                                return 1
            else:
                if features["E(LEFT) - T(LEFT)"] <= 0.255562:
                    if features["E(RIGHT) - agent_row"] <= -0.564129:
                        if features["E(UP) - time_left"] <= 0.340183:
                            if features["E(DOWN)"] <= 0.000025:
                                if features["E(DOWN) - time_left"] <= -0.810000:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.340994:
                                    if features["E(RIGHT) - time_left"] <= -0.018148:
                                        if features["T(RIGHT)"] <= 0.001219:
                                            return 0
                                        else:
                                            if features["T(LEFT) - time_left"] <= 0.300284:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.001109:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 2
                                    else:
                                        return 0
                                else:
                                    return 0
                        else:
                            if features["E(RIGHT)"] <= 0.799917:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.303005:
                                    if features["E(LEFT) - agent_row"] <= -0.595656:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["E(DOWN)"] <= 0.000206:
                                        if features["E(LEFT) - agent_row"] <= -13.984049:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 0
                            else:
                                if features["agent_row - agent_column"] <= 0.500000:
                                    return 0
                                else:
                                    return 3
                    else:
                        if features["E(RIGHT) - agent_column"] <= -11.338999:
                            return 0
                        else:
                            return 3
                else:
                    if features["E(DOWN) - agent_row"] <= -1.999969:
                        if features["E(DOWN) - T(DOWN)"] <= -0.000000:
                            if features["E(UP) - E(DOWN)"] <= 0.803290:
                                return 0
                            else:
                                if features["T(DOWN) - agent_column"] <= -1.827807:
                                    return 2
                                else:
                                    return 0
                        else:
                            if features["E(RIGHT) - agent_column"] <= -7.998130:
                                return 2
                            else:
                                if features["E(UP) - time_left"] <= 0.289614:
                                    return 2
                                else:
                                    return 0
                    else:
                        return 2


def interpretable_action(evader_probability, teammate_probability, agent_position, time_left, gamma, size, valid_actions):
    input_representation = symbolic_representation(evader_probability, teammate_probability, agent_position, time_left, gamma, size)
    input_combinations   = get_feature_vector(input_representation)
    symbole_to_value     = {name: input_combinations[i] for i, name in enumerate(symbole_names)}
    action               = Index_to_Action[interpretable_strategy(symbole_to_value)]
    if action in valid_actions:
        return action
    else:
        return random.choice(valid_actions)
