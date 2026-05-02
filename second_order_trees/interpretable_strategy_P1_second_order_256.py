import random
from INTERPRETER_2ND import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'T(E(UP))', 'T(E(DOWN))', 'T(E(LEFT))', 'T(E(RIGHT))', 'T(T(up))', 'T(T(DOWN))', 'T(T(LEFT))', 'T(T(RIGHT))', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - T(E(UP))', 'E(UP) - T(E(DOWN))', 'E(UP) - T(E(LEFT))', 'E(UP) - T(E(RIGHT))', 'E(UP) - T(T(up))', 'E(UP) - T(T(DOWN))', 'E(UP) - T(T(LEFT))', 'E(UP) - T(T(RIGHT))', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - T(E(UP))', 'E(DOWN) - T(E(DOWN))', 'E(DOWN) - T(E(LEFT))', 'E(DOWN) - T(E(RIGHT))', 'E(DOWN) - T(T(up))', 'E(DOWN) - T(T(DOWN))', 'E(DOWN) - T(T(LEFT))', 'E(DOWN) - T(T(RIGHT))', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - T(E(UP))', 'E(LEFT) - T(E(DOWN))', 'E(LEFT) - T(E(LEFT))', 'E(LEFT) - T(E(RIGHT))', 'E(LEFT) - T(T(up))', 'E(LEFT) - T(T(DOWN))', 'E(LEFT) - T(T(LEFT))', 'E(LEFT) - T(T(RIGHT))', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - T(E(UP))', 'E(RIGHT) - T(E(DOWN))', 'E(RIGHT) - T(E(LEFT))', 'E(RIGHT) - T(E(RIGHT))', 'E(RIGHT) - T(T(up))', 'E(RIGHT) - T(T(DOWN))', 'E(RIGHT) - T(T(LEFT))', 'E(RIGHT) - T(T(RIGHT))', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - T(E(UP))', 'T(up) - T(E(DOWN))', 'T(up) - T(E(LEFT))', 'T(up) - T(E(RIGHT))', 'T(up) - T(T(up))', 'T(up) - T(T(DOWN))', 'T(up) - T(T(LEFT))', 'T(up) - T(T(RIGHT))', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - T(E(UP))', 'T(DOWN) - T(E(DOWN))', 'T(DOWN) - T(E(LEFT))', 'T(DOWN) - T(E(RIGHT))', 'T(DOWN) - T(T(up))', 'T(DOWN) - T(T(DOWN))', 'T(DOWN) - T(T(LEFT))', 'T(DOWN) - T(T(RIGHT))', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - T(E(UP))', 'T(LEFT) - T(E(DOWN))', 'T(LEFT) - T(E(LEFT))', 'T(LEFT) - T(E(RIGHT))', 'T(LEFT) - T(T(up))', 'T(LEFT) - T(T(DOWN))', 'T(LEFT) - T(T(LEFT))', 'T(LEFT) - T(T(RIGHT))', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - T(E(UP))', 'T(RIGHT) - T(E(DOWN))', 'T(RIGHT) - T(E(LEFT))', 'T(RIGHT) - T(E(RIGHT))', 'T(RIGHT) - T(T(up))', 'T(RIGHT) - T(T(DOWN))', 'T(RIGHT) - T(T(LEFT))', 'T(RIGHT) - T(T(RIGHT))', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'T(E(UP)) - T(E(DOWN))', 'T(E(UP)) - T(E(LEFT))', 'T(E(UP)) - T(E(RIGHT))', 'T(E(UP)) - T(T(up))', 'T(E(UP)) - T(T(DOWN))', 'T(E(UP)) - T(T(LEFT))', 'T(E(UP)) - T(T(RIGHT))', 'T(E(UP)) - agent_row', 'T(E(UP)) - agent_column', 'T(E(UP)) - time_left', 'T(E(DOWN)) - T(E(LEFT))', 'T(E(DOWN)) - T(E(RIGHT))', 'T(E(DOWN)) - T(T(up))', 'T(E(DOWN)) - T(T(DOWN))', 'T(E(DOWN)) - T(T(LEFT))', 'T(E(DOWN)) - T(T(RIGHT))', 'T(E(DOWN)) - agent_row', 'T(E(DOWN)) - agent_column', 'T(E(DOWN)) - time_left', 'T(E(LEFT)) - T(E(RIGHT))', 'T(E(LEFT)) - T(T(up))', 'T(E(LEFT)) - T(T(DOWN))', 'T(E(LEFT)) - T(T(LEFT))', 'T(E(LEFT)) - T(T(RIGHT))', 'T(E(LEFT)) - agent_row', 'T(E(LEFT)) - agent_column', 'T(E(LEFT)) - time_left', 'T(E(RIGHT)) - T(T(up))', 'T(E(RIGHT)) - T(T(DOWN))', 'T(E(RIGHT)) - T(T(LEFT))', 'T(E(RIGHT)) - T(T(RIGHT))', 'T(E(RIGHT)) - agent_row', 'T(E(RIGHT)) - agent_column', 'T(E(RIGHT)) - time_left', 'T(T(up)) - T(T(DOWN))', 'T(T(up)) - T(T(LEFT))', 'T(T(up)) - T(T(RIGHT))', 'T(T(up)) - agent_row', 'T(T(up)) - agent_column', 'T(T(up)) - time_left', 'T(T(DOWN)) - T(T(LEFT))', 'T(T(DOWN)) - T(T(RIGHT))', 'T(T(DOWN)) - agent_row', 'T(T(DOWN)) - agent_column', 'T(T(DOWN)) - time_left', 'T(T(LEFT)) - T(T(RIGHT))', 'T(T(LEFT)) - agent_row', 'T(T(LEFT)) - agent_column', 'T(T(LEFT)) - time_left', 'T(T(RIGHT)) - agent_row', 'T(T(RIGHT)) - agent_column', 'T(T(RIGHT)) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(RIGHT)"] <= -0.000050:
        if features["E(DOWN) - E(RIGHT)"] <= -0.000047:
            if features["E(LEFT)"] <= 0.061204:
                if features["E(RIGHT) - T(E(DOWN))"] <= 0.080373:
                    if features["E(UP) - agent_row"] <= -0.998703:
                        if features["E(LEFT)"] <= 0.003362:
                            if features["T(up) - agent_row"] <= -1.998790:
                                if features["E(LEFT)"] <= 0.000011:
                                    if features["T(E(DOWN)) - agent_column"] <= -0.210392:
                                        if features["E(UP) - E(RIGHT)"] <= -0.799798:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN) - T(E(RIGHT))"] <= 0.017200:
                                        if features["T(E(DOWN)) - T(E(LEFT))"] <= 0.364177:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 1
                            else:
                                return 3
                        else:
                            if features["T(LEFT)"] <= 0.004884:
                                if features["E(RIGHT) - time_left"] <= 0.344115:
                                    return 1
                                else:
                                    return 3
                            else:
                                if features["agent_column - time_left"] <= 0.970000:
                                    return 3
                                else:
                                    if features["T(RIGHT) - time_left"] <= 0.218403:
                                        return 3
                                    else:
                                        return 1
                    else:
                        return 1
                else:
                    if features["E(DOWN) - T(E(LEFT))"] <= 0.121102:
                        if features["E(UP) - T(T(up))"] <= 0.058139:
                            if features["E(LEFT) - T(DOWN)"] <= 0.002232:
                                if features["E(RIGHT) - time_left"] <= 0.235900:
                                    if features["E(LEFT)"] <= 0.040027:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 3
                            else:
                                return 3
                        else:
                            if features["T(E(DOWN)) - time_left"] <= -0.043254:
                                if features["E(LEFT)"] <= 0.000153:
                                    if features["E(RIGHT) - T(LEFT)"] <= 0.857890:
                                        if features["T(LEFT) - time_left"] <= -0.557550:
                                            if features["E(LEFT) - T(up)"] <= -0.000084:
                                                return 0
                                            else:
                                                return 1
                                        else:
                                            return 3
                                    else:
                                        return 3
                                else:
                                    return 3
                            else:
                                return 3
                    else:
                        if features["E(RIGHT) - agent_column"] <= -10.274547:
                            if features["E(RIGHT) - agent_column"] <= -11.211621:
                                return 1
                            else:
                                if features["E(DOWN) - agent_column"] <= -11.151483:
                                    return 3
                                else:
                                    return 1
                        else:
                            if features["T(LEFT) - time_left"] <= -0.099999:
                                if features["E(RIGHT) - agent_row"] <= -11.259671:
                                    return 3
                                else:
                                    if features["E(DOWN) - E(LEFT)"] <= 0.857394:
                                        if features["E(LEFT)"] <= 0.000026:
                                            if features["E(RIGHT) - agent_column"] <= 0.374475:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["E(RIGHT) - T(E(UP))"] <= 0.342290:
                                                if features["T(T(up)) - time_left"] <= -0.605125:
                                                    return 2
                                                else:
                                                    if features["E(RIGHT) - time_left"] <= 0.335284:
                                                        if features["T(E(UP)) - agent_column"] <= -3.592927:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                            else:
                                                return 1
                                    else:
                                        return 1
                            else:
                                if features["E(LEFT) - time_left"] <= 0.045504:
                                    if features["E(DOWN) - E(LEFT)"] <= 0.855993:
                                        if features["E(RIGHT) - agent_column"] <= 0.431864:
                                            if features["E(LEFT)"] <= 0.024746:
                                                return 3
                                            else:
                                                if features["E(DOWN) - T(E(RIGHT))"] <= -0.059309:
                                                    return 3
                                                else:
                                                    return 1
                                        else:
                                            if features["T(E(RIGHT)) - time_left"] <= 0.406985:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        if features["T(up) - agent_row"] <= -12.398816:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["T(T(RIGHT)) - agent_column"] <= -0.606984:
                                        return 1
                                    else:
                                        return 2
            else:
                if features["T(E(UP)) - T(T(up))"] <= 0.006004:
                    if features["E(DOWN) - T(E(RIGHT))"] <= -0.175264:
                        if features["E(LEFT) - agent_column"] <= -1.922942:
                            if features["E(RIGHT) - T(E(DOWN))"] <= 0.199647:
                                return 1
                            else:
                                return 3
                        else:
                            return 2
                    else:
                        if features["E(LEFT) - T(up)"] <= 0.061435:
                            if features["E(RIGHT) - T(DOWN)"] <= 0.224390:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.344662:
                                    return 3
                                else:
                                    return 1
                            else:
                                return 1
                        else:
                            if features["E(RIGHT) - T(RIGHT)"] <= 0.036017:
                                return 1
                            else:
                                return 3
                else:
                    if features["E(RIGHT) - T(RIGHT)"] <= 0.003896:
                        if features["E(UP) - E(LEFT)"] <= 0.205114:
                            if features["T(DOWN) - T(E(UP))"] <= -0.216875:
                                if features["T(up) - T(T(RIGHT))"] <= 0.382293:
                                    if features["E(RIGHT) - agent_row"] <= -6.659473:
                                        if features["E(RIGHT) - agent_column"] <= -1.630550:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                if features["E(RIGHT) - T(T(RIGHT))"] <= -0.028091:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["T(LEFT) - T(E(LEFT))"] <= -0.005105:
                                return 3
                            else:
                                return 2
                    else:
                        if features["T(up) - T(LEFT)"] <= -0.000016:
                            return 3
                        else:
                            if features["E(UP) - E(LEFT)"] <= 0.111892:
                                return 1
                            else:
                                if features["T(E(RIGHT)) - agent_column"] <= -6.693895:
                                    return 1
                                else:
                                    return 3
        else:
            if features["E(LEFT) - T(E(RIGHT))"] <= 0.139963:
                if features["E(DOWN) - agent_row"] <= -12.131877:
                    return 3
                else:
                    if features["E(UP) - T(LEFT)"] <= 0.077409:
                        if features["E(RIGHT) - T(T(DOWN))"] <= 0.081216:
                            return 1
                        else:
                            if features["T(up) - T(T(DOWN))"] <= -0.290154:
                                return 3
                            else:
                                if features["T(RIGHT) - T(E(RIGHT))"] <= -0.320476:
                                    if features["E(UP) - agent_row"] <= -3.992832:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    return 1
                    else:
                        if features["T(up) - T(RIGHT)"] <= -0.000015:
                            if features["E(RIGHT) - T(E(UP))"] <= 0.065341:
                                return 2
                            else:
                                if features["T(DOWN) - T(E(RIGHT))"] <= 0.032093:
                                    return 1
                                else:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.255457:
                                        return 2
                                    else:
                                        return 3
                        else:
                            return 1
            else:
                if features["T(up) - agent_row"] <= -12.332148:
                    if features["T(LEFT) - agent_column"] <= -0.999992:
                        return 2
                    else:
                        return 1
                else:
                    if features["agent_row - agent_column"] <= -6.500000:
                        if features["E(UP) - T(LEFT)"] <= -0.295640:
                            if features["E(DOWN) - time_left"] <= 0.352678:
                                if features["T(DOWN) - time_left"] <= 0.289566:
                                    return 1
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.274416:
                                        return 1
                                    else:
                                        return 2
                            else:
                                if features["E(UP) - T(up)"] <= 0.001236:
                                    return 1
                                else:
                                    return 2
                        else:
                            if features["E(UP) - agent_column"] <= -8.998733:
                                return 2
                            else:
                                if features["T(T(LEFT)) - agent_row"] <= -1.700301:
                                    return 1
                                else:
                                    return 2
                    else:
                        if features["E(UP) - T(LEFT)"] <= 0.000054:
                            if features["T(up) - agent_row"] <= -11.321499:
                                return 1
                            else:
                                if features["T(up) - T(E(LEFT))"] <= -0.385370:
                                    if features["E(DOWN) - time_left"] <= 0.248977:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 1
                        else:
                            if features["E(DOWN) - agent_row"] <= -7.589257:
                                return 2
                            else:
                                return 1
    else:
        if features["E(UP) - E(LEFT)"] <= -0.000007:
            if features["E(DOWN) - E(LEFT)"] <= -0.151117:
                if features["E(UP)"] <= 0.662776:
                    if features["E(RIGHT) - T(DOWN)"] <= 0.000262:
                        if features["E(RIGHT) - T(up)"] <= 0.000089:
                            if features["T(E(LEFT)) - agent_column"] <= -13.651110:
                                return 2
                            else:
                                if features["E(UP) - agent_column"] <= -0.458824:
                                    return 2
                                else:
                                    return 0
                        else:
                            return 2
                    else:
                        if features["T(E(DOWN)) - agent_column"] <= -8.826958:
                            return 2
                        else:
                            if features["T(up) - T(RIGHT)"] <= -0.000037:
                                return 2
                            else:
                                if features["E(DOWN) - E(LEFT)"] <= -0.212062:
                                    return 2
                                else:
                                    return 1
                else:
                    if features["E(RIGHT) - agent_column"] <= -1.999885:
                        if features["E(DOWN) - E(RIGHT)"] <= -0.000003:
                            return 2
                        else:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.802466:
                                return 2
                            else:
                                if features["agent_row - agent_column"] <= 8.500000:
                                    return 2
                                else:
                                    return 0
                    else:
                        return 0
            else:
                if features["E(DOWN) - E(LEFT)"] <= 0.000009:
                    if features["E(RIGHT)"] <= 0.000129:
                        if features["T(LEFT) - agent_column"] <= -1.189887:
                            if features["E(UP) - E(LEFT)"] <= -0.802710:
                                if features["agent_row - agent_column"] <= -0.500000:
                                    return 1
                                else:
                                    return 2
                            else:
                                if features["T(E(DOWN)) - agent_column"] <= -13.745383:
                                    return 1
                                else:
                                    return 2
                        else:
                            return 1
                    else:
                        if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.089367:
                            if features["E(LEFT) - T(T(up))"] <= -0.011601:
                                if features["T(RIGHT) - T(E(RIGHT))"] <= -0.096986:
                                    if features["T(up) - T(LEFT)"] <= 0.000611:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= -0.000004:
                                        return 1
                                    else:
                                        return 2
                            else:
                                if features["T(RIGHT) - T(T(DOWN))"] <= -0.143932:
                                    if features["E(LEFT) - T(T(LEFT))"] <= -0.208122:
                                        return 3
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.019873:
                                            return 2
                                        else:
                                            if features["T(E(LEFT)) - T(T(DOWN))"] <= 0.132219:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    if features["T(E(RIGHT)) - time_left"] <= -0.089251:
                                        return 2
                                    else:
                                        if features["E(DOWN) - T(T(up))"] <= -0.108348:
                                            return 0
                                        else:
                                            return 2
                        else:
                            if features["E(LEFT) - T(T(LEFT))"] <= 0.073445:
                                if features["T(E(LEFT)) - T(T(up))"] <= 0.278773:
                                    if features["T(T(DOWN)) - T(T(LEFT))"] <= -0.099884:
                                        if features["T(RIGHT) - T(E(UP))"] <= -0.251653:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["T(RIGHT) - agent_column"] <= -12.997694:
                                            return 2
                                        else:
                                            if features["T(DOWN) - time_left"] <= 0.336596:
                                                return 1
                                            else:
                                                return 3
                                else:
                                    return 2
                            else:
                                if features["T(up) - T(RIGHT)"] <= 0.178257:
                                    if features["T(LEFT) - agent_column"] <= -9.511697:
                                        return 2
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= 0.000001:
                                            if features["E(RIGHT) - T(E(DOWN))"] <= -0.215354:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(up) - T(RIGHT)"] <= 0.125522:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    if features["E(RIGHT) - agent_column"] <= -8.997561:
                                        return 2
                                    else:
                                        return 1
                else:
                    if features["T(T(DOWN)) - agent_row"] <= -11.995933:
                        return 2
                    else:
                        if features["E(RIGHT) - T(T(up))"] <= -0.000057:
                            if features["E(LEFT)"] <= 0.862667:
                                if features["E(RIGHT) - T(up)"] <= 0.000058:
                                    return 1
                                else:
                                    return 2
                            else:
                                if features["T(T(up)) - agent_column"] <= -0.994895:
                                    if features["E(UP) - agent_column"] <= -4.000000:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    return 1
                        else:
                            return 2
        else:
            if features["E(DOWN)"] <= 0.016515:
                if features["E(UP) - E(LEFT)"] <= 0.267126:
                    if features["E(LEFT) - time_left"] <= 0.144690:
                        if features["T(RIGHT) - time_left"] <= -0.133377:
                            if features["T(E(UP)) - agent_row"] <= -12.641949:
                                if features["T(E(DOWN)) - time_left"] <= -0.559028:
                                    if features["T(RIGHT) - T(E(UP))"] <= -0.413960:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["E(UP) - T(DOWN)"] <= 0.300176:
                                        return 0
                                    else:
                                        return 2
                            else:
                                return 0
                        else:
                            if features["T(DOWN) - agent_row"] <= -8.997094:
                                if features["T(E(DOWN)) - agent_column"] <= -6.999242:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 2
                    else:
                        if features["E(UP) - E(DOWN)"] <= 0.803015:
                            if features["E(DOWN)"] <= 0.000022:
                                if features["E(DOWN) - agent_row"] <= -1.999997:
                                    return 0
                                else:
                                    return 2
                            else:
                                if features["E(LEFT) - T(T(up))"] <= 0.000918:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.002882:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["E(UP) - T(T(up))"] <= 0.050716:
                                        return 2
                                    else:
                                        if features["T(DOWN) - time_left"] <= -0.059999:
                                            if features["agent_row - agent_column"] <= 3.500000:
                                                if features["T(LEFT) - T(T(RIGHT))"] <= 0.145428:
                                                    return 2
                                                else:
                                                    if features["E(UP) - agent_row"] <= -9.571779:
                                                        if features["T(T(up)) - agent_row"] <= -10.691257:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 0
                                            else:
                                                return 0
                                        else:
                                            if features["E(RIGHT) - agent_row"] <= -2.999123:
                                                return 0
                                            else:
                                                return 2
                        else:
                            if features["E(DOWN) - agent_column"] <= -1.999998:
                                if features["T(E(RIGHT)) - agent_row"] <= -0.995641:
                                    if features["E(RIGHT) - agent_row"] <= -4.999991:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 2
                            else:
                                if features["T(T(LEFT)) - agent_row"] <= -1.940643:
                                    return 0
                                else:
                                    return 2
                else:
                    if features["E(RIGHT) - T(T(RIGHT))"] <= 0.035683:
                        if features["E(LEFT) - T(T(LEFT))"] <= 0.003451:
                            if features["E(UP) - time_left"] <= 0.321023:
                                if features["E(DOWN)"] <= 0.000249:
                                    return 0
                                else:
                                    return 3
                            else:
                                return 0
                        else:
                            if features["E(RIGHT) - T(DOWN)"] <= 0.308548:
                                return 0
                            else:
                                return 3
                    else:
                        if features["E(DOWN) - E(RIGHT)"] <= -0.866033:
                            return 3
                        else:
                            if features["E(LEFT) - T(DOWN)"] <= 0.000635:
                                if features["T(E(RIGHT)) - agent_row"] <= -1.832422:
                                    if features["E(UP) - agent_row"] <= -13.132438:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 3
                            else:
                                if features["E(LEFT) - agent_row"] <= -13.997240:
                                    return 3
                                else:
                                    if features["E(RIGHT) - time_left"] <= -0.518597:
                                        return 2
                                    else:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.013519:
                                            if features["T(up) - T(DOWN)"] <= 0.444720:
                                                return 0
                                            else:
                                                if features["E(DOWN) - T(DOWN)"] <= -0.000774:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["E(UP) - time_left"] <= 0.396126:
                                                return 3
                                            else:
                                                return 0
            else:
                if features["E(RIGHT) - T(RIGHT)"] <= 0.175073:
                    if features["E(LEFT) - T(T(LEFT))"] <= 0.009345:
                        if features["E(UP) - time_left"] <= 0.309150:
                            if features["T(E(LEFT)) - T(T(LEFT))"] <= -0.119052:
                                if features["E(DOWN) - agent_row"] <= -8.840587:
                                    if features["E(LEFT) - T(E(UP))"] <= -0.315944:
                                        return 0
                                    else:
                                        if features["T(LEFT) - time_left"] <= -0.237146:
                                            return 2
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.180931:
                                                return 3
                                            else:
                                                if features["T(RIGHT)"] <= 0.395938:
                                                    return 3
                                                else:
                                                    return 1
                                else:
                                    return 2
                            else:
                                if features["T(E(DOWN)) - time_left"] <= 0.153965:
                                    if features["E(RIGHT) - T(E(LEFT))"] <= 0.289311:
                                        if features["E(DOWN) - T(T(DOWN))"] <= -0.019252:
                                            if features["E(UP) - E(LEFT)"] <= 0.282058:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["agent_row - agent_column"] <= 2.500000:
                                                return 2
                                            else:
                                                if features["T(up)"] <= 0.317309:
                                                    return 1
                                                else:
                                                    return 2
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -8.683153:
                                        return 0
                                    else:
                                        return 1
                        else:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.132730:
                                if features["T(RIGHT) - T(T(up))"] <= -0.034122:
                                    if features["T(DOWN) - agent_row"] <= -8.938471:
                                        if features["T(up) - T(T(DOWN))"] <= 0.369190:
                                            if features["T(up) - T(E(UP))"] <= 0.003806:
                                                return 1
                                            else:
                                                return 0
                                        else:
                                            return 1
                                    else:
                                        if features["E(UP) - T(DOWN)"] <= 0.213364:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    if features["T(E(UP)) - T(E(RIGHT))"] <= 0.002053:
                                        return 3
                                    else:
                                        if features["T(T(up))"] <= 0.338901:
                                            if features["T(T(RIGHT)) - agent_row"] <= -8.690289:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            if features["T(E(DOWN)) - T(T(LEFT))"] <= -0.065122:
                                                return 0
                                            else:
                                                return 2
                            else:
                                return 2
                    else:
                        if features["E(UP) - T(E(DOWN))"] <= 0.311550:
                            if features["T(DOWN)"] <= 0.000094:
                                if features["agent_column - time_left"] <= 8.770000:
                                    if features["T(up) - T(RIGHT)"] <= -0.000240:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 2
                            else:
                                if features["T(up) - time_left"] <= 0.113471:
                                    return 2
                                else:
                                    if features["T(T(up)) - time_left"] <= 0.359161:
                                        if features["T(RIGHT) - time_left"] <= -0.014913:
                                            return 1
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -1.464456:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        return 0
                        else:
                            if features["T(up) - T(E(DOWN))"] <= 0.329724:
                                if features["time_left"] <= 0.070000:
                                    return 0
                                else:
                                    return 2
                            else:
                                if features["T(E(LEFT)) - T(T(up))"] <= -0.122789:
                                    return 2
                                else:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.006375:
                                        return 0
                                    else:
                                        return 2
                else:
                    if features["T(up) - T(LEFT)"] <= 0.000014:
                        return 3
                    else:
                        if features["E(UP) - T(E(LEFT))"] <= 0.249248:
                            if features["E(DOWN) - T(E(LEFT))"] <= -0.258312:
                                if features["T(LEFT) - agent_column"] <= -2.999667:
                                    return 2
                                else:
                                    return 3
                            else:
                                if features["E(LEFT) - T(up)"] <= -0.465791:
                                    return 3
                                else:
                                    return 1
                        else:
                            if features["T(up) - agent_column"] <= -7.446975:
                                return 1
                            else:
                                return 3


def interpretable_action(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability,agent_position, time_left, gamma, size, valid_actions):
    input_representation = symbolic_representation(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability, agent_position, time_left, gamma, size)
    input_combinations   = get_feature_vector(input_representation)
    symbole_to_value     = {name: input_combinations[i] for i, name in enumerate(symbole_names)}
    action               = Index_to_Action[interpretable_strategy(symbole_to_value)]
    if action in valid_actions:
        return action
    else:
        return random.choice(valid_actions)
