import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(RIGHT)"] <= -0.000000:
        if features["E(LEFT) - E(RIGHT)"] <= -0.326260:
            if features["E(DOWN) - E(RIGHT)"] <= -0.000006:
                if features["E(LEFT)"] <= 0.000156:
                    if features["E(UP) - E(DOWN)"] <= 0.803652:
                        if features["E(DOWN)"] <= 0.800790:
                            if features["agent_column - time_left"] <= -0.010000:
                                if features["E(UP) - time_left"] <= 0.146961:
                                    if features["E(RIGHT) - time_left"] <= 0.167410:
                                        if features["T(RIGHT) - time_left"] <= 0.155775:
                                            if features["T(DOWN) - agent_row"] <= -8.916741:
                                                return 3
                                            else:
                                                if features["E(DOWN) - E(RIGHT)"] <= -0.323753:
                                                    return 3
                                                else:
                                                    return 1
                                        else:
                                            return 3
                                    else:
                                        return 3
                                else:
                                    if features["T(up) - agent_row"] <= -12.643846:
                                        return 3
                                    else:
                                        return 0
                            else:
                                if features["E(UP)"] <= 0.602233:
                                    if features["E(UP) - agent_column"] <= 0.350375:
                                        if features["E(DOWN)"] <= 0.662581:
                                            if features["E(UP) - time_left"] <= -0.759999:
                                                if features["E(UP) - T(DOWN)"] <= -0.536120:
                                                    return 1
                                                else:
                                                    if features["E(RIGHT) - agent_row"] <= 0.399278:
                                                        return 3
                                                    else:
                                                        return 2
                                            else:
                                                return 3
                                        else:
                                            if features["E(LEFT)"] <= 0.000004:
                                                return 3
                                            else:
                                                if features["E(DOWN) - agent_row"] <= -11.240196:
                                                    return 3
                                                else:
                                                    if features["T(DOWN) - agent_column"] <= -10.730184:
                                                        return 1
                                                    else:
                                                        return 3
                                    else:
                                        return 0
                                else:
                                    if features["E(UP) - agent_column"] <= -11.214703:
                                        return 0
                                    else:
                                        return 3
                        else:
                            if features["E(LEFT) - agent_column"] <= -12.999999:
                                return 1
                            else:
                                if features["T(up) - agent_row"] <= -11.999872:
                                    return 3
                                else:
                                    if features["T(LEFT) - agent_row"] <= -7.730496:
                                        if features["E(RIGHT) - agent_row"] <= -9.132251:
                                            if features["E(RIGHT) - agent_row"] <= -11.132071:
                                                return 1
                                            else:
                                                if features["T(up) - T(LEFT)"] <= 0.412896:
                                                    return 3
                                                else:
                                                    return 1
                                        else:
                                            return 1
                                    else:
                                        return 3
                    else:
                        if features["T(up) - T(DOWN)"] <= 0.243560:
                            return 0
                        else:
                            if features["T(up) - agent_column"] <= -11.325884:
                                return 0
                            else:
                                if features["T(DOWN) - agent_column"] <= -3.999974:
                                    return 3
                                else:
                                    return 0
                else:
                    if features["E(DOWN) - E(RIGHT)"] <= -0.210304:
                        if features["E(UP) - E(RIGHT)"] <= -0.138244:
                            if features["E(LEFT)"] <= 0.013494:
                                return 3
                            else:
                                if features["T(LEFT) - time_left"] <= -0.068067:
                                    if features["T(LEFT)"] <= 0.021237:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 3
                        else:
                            if features["E(UP) - T(RIGHT)"] <= 0.005822:
                                if features["E(UP) - agent_row"] <= -9.548552:
                                    if features["E(RIGHT) - time_left"] <= 0.335300:
                                        if features["E(LEFT) - time_left"] <= -0.118568:
                                            if features["T(LEFT)"] <= 0.026862:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT) - time_left"] <= 0.236630:
                                        return 3
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -1.971278:
                                            return 3
                                        else:
                                            if features["E(UP)"] <= 0.280383:
                                                return 3
                                            else:
                                                return 0
                            else:
                                if features["T(DOWN)"] <= 0.003249:
                                    if features["agent_row - agent_column"] <= 11.500000:
                                        if features["E(LEFT) - agent_row"] <= -11.999180:
                                            if features["T(RIGHT) - agent_column"] <= -9.999993:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        return 0
                                else:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.028755:
                                        return 0
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -2.994167:
                                            if features["T(up) - agent_row"] <= -5.808195:
                                                if features["T(RIGHT) - agent_column"] <= -2.689636:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                        else:
                                            return 3
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.370131:
                            if features["E(UP) - T(up)"] <= 0.089989:
                                if features["T(up) - agent_column"] <= -2.990783:
                                    if features["T(LEFT) - agent_column"] <= -3.999829:
                                        if features["E(RIGHT)"] <= 0.484393:
                                            if features["T(DOWN) - T(RIGHT)"] <= -0.000015:
                                                if features["T(LEFT) - agent_row"] <= -9.999952:
                                                    return 3
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.136280:
                                                        return 1
                                                    else:
                                                        return 3
                                            else:
                                                return 3
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= -0.358509:
                                                if features["E(RIGHT) - time_left"] <= 0.010709:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                    else:
                                        if features["T(DOWN) - T(RIGHT)"] <= -0.000057:
                                            if features["T(LEFT) - time_left"] <= -0.199910:
                                                return 1
                                            else:
                                                if features["T(RIGHT) - time_left"] <= 0.369171:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - E(RIGHT)"] <= -0.161967:
                                                        return 3
                                                    else:
                                                        return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT) - agent_column"] <= -0.986214:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.003028:
                                            if features["T(LEFT)"] <= 0.000048:
                                                if features["T(DOWN) - time_left"] <= 0.381009:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                        else:
                                            if features["E(RIGHT) - T(DOWN)"] <= 0.082584:
                                                return 1
                                            else:
                                                if features["T(LEFT) - agent_column"] <= -1.999276:
                                                    if features["E(LEFT) - agent_row"] <= -9.991201:
                                                        return 3
                                                    else:
                                                        if features["E(DOWN) - T(LEFT)"] <= 0.181826:
                                                            return 3
                                                        else:
                                                            if features["T(RIGHT) - agent_column"] <= -2.561192:
                                                                return 1
                                                            else:
                                                                if features["E(LEFT) - T(LEFT)"] <= 0.000842:
                                                                    return 3
                                                                else:
                                                                    return 1
                                                else:
                                                    return 3
                                    else:
                                        if features["E(UP) - time_left"] <= 0.151278:
                                            return 1
                                        else:
                                            return 3
                            else:
                                if features["T(DOWN) - T(RIGHT)"] <= -0.000102:
                                    if features["E(RIGHT) - T(RIGHT)"] <= -0.051524:
                                        if features["agent_row - agent_column"] <= 1.500000:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        return 1
                                else:
                                    if features["E(UP) - T(DOWN)"] <= -0.342403:
                                        return 3
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.057594:
                                            return 0
                                        else:
                                            return 3
                        else:
                            return 3
            else:
                if features["E(DOWN) - agent_row"] <= -11.224183:
                    return 3
                else:
                    if features["E(RIGHT) - agent_row"] <= -0.200529:
                        if features["E(LEFT) - E(RIGHT)"] <= -0.858626:
                            if features["T(LEFT) - agent_row"] <= -6.676358:
                                if features["T(LEFT) - agent_row"] <= -11.655115:
                                    return 1
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -7.853611:
                                        if features["T(up) - T(LEFT)"] <= 0.539007:
                                            if features["E(DOWN) - agent_column"] <= -11.133139:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 1
                                    else:
                                        return 1
                            else:
                                if features["agent_row - agent_column"] <= -6.500000:
                                    return 1
                                else:
                                    if features["T(up) - T(RIGHT)"] <= -0.576838:
                                        return 1
                                    else:
                                        return 3
                        else:
                            if features["E(UP)"] <= 0.000000:
                                return 1
                            else:
                                if features["T(DOWN) - agent_column"] <= -11.790131:
                                    return 1
                                else:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.291583:
                                        if features["E(UP) - T(LEFT)"] <= 0.000019:
                                            return 1
                                        else:
                                            if features["E(UP) - agent_column"] <= -1.994791:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        if features["E(UP)"] <= 0.000106:
                                            return 1
                                        else:
                                            return 3
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.312497:
                            if features["agent_row - time_left"] <= -0.550000:
                                return 3
                            else:
                                return 1
                        else:
                            return 3
        else:
            if features["E(UP) - T(up)"] <= 0.011775:
                if features["E(DOWN) - E(LEFT)"] <= 0.169415:
                    if features["E(DOWN) - time_left"] <= 0.097347:
                        if features["E(LEFT) - time_left"] <= 0.083080:
                            if features["E(LEFT)"] <= 0.028520:
                                if features["E(DOWN) - T(DOWN)"] <= 0.031594:
                                    if features["T(RIGHT) - time_left"] <= -0.188030:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 3
                            else:
                                if features["E(UP) - T(RIGHT)"] <= 0.237270:
                                    if features["T(LEFT)"] <= 0.000001:
                                        if features["E(UP) - time_left"] <= 0.214565:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["T(DOWN) - agent_row"] <= -8.907546:
                                            if features["E(DOWN) - T(RIGHT)"] <= -0.371030:
                                                return 3
                                            else:
                                                if features["T(LEFT)"] <= 0.000057:
                                                    return 1
                                                else:
                                                    if features["T(LEFT) - agent_column"] <= -1.905623:
                                                        return 1
                                                    else:
                                                        return 2
                                        else:
                                            if features["E(DOWN) - time_left"] <= -0.139880:
                                                return 1
                                            else:
                                                if features["T(RIGHT)"] <= 0.468728:
                                                    if features["T(LEFT) - time_left"] <= 0.068883:
                                                        return 2
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                                else:
                                    return 3
                        else:
                            return 2
                    else:
                        if features["E(DOWN) - agent_row"] <= -11.210165:
                            if features["T(up) - agent_column"] <= -0.999837:
                                if features["T(up) - agent_row"] <= -12.331216:
                                    if features["E(UP)"] <= 0.000000:
                                        if features["T(RIGHT) - agent_column"] <= -8.698997:
                                            return 2
                                        else:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.000329:
                                                return 2
                                            else:
                                                if features["E(DOWN) - agent_column"] <= -3.132537:
                                                    return 1
                                                else:
                                                    return 2
                                    else:
                                        return 2
                                else:
                                    if features["E(DOWN) - E(LEFT)"] <= 0.085942:
                                        return 2
                                    else:
                                        return 1
                            else:
                                return 1
                        else:
                            if features["E(RIGHT) - T(RIGHT)"] <= 0.272413:
                                if features["E(LEFT) - agent_row"] <= 0.319950:
                                    if features["T(up) - T(LEFT)"] <= -0.113478:
                                        if features["E(RIGHT) - time_left"] <= 0.018149:
                                            if features["E(UP)"] <= 0.000008:
                                                return 1
                                            else:
                                                if features["E(DOWN) - agent_row"] <= -4.588748:
                                                    if features["E(UP) - time_left"] <= -0.052672:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    if features["T(RIGHT)"] <= 0.012118:
                                                        if features["T(RIGHT) - agent_row"] <= -1.988557:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        return 1
                                        else:
                                            if features["T(up) - agent_row"] <= -9.839527:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        if features["E(UP)"] <= 0.000000:
                                            if features["E(DOWN) - E(LEFT)"] <= -0.000054:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(RIGHT)"] <= 0.251253:
                                                if features["E(DOWN) - agent_column"] <= -2.219023:
                                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.135802:
                                                        if features["E(UP)"] <= 0.000014:
                                                            if features["E(DOWN)"] <= 0.670776:
                                                                return 1
                                                            else:
                                                                if features["T(DOWN) - agent_column"] <= -5.181284:
                                                                    if features["T(up) - agent_column"] <= -7.539990:
                                                                        if features["E(DOWN) - agent_column"] <= -9.132405:
                                                                            return 1
                                                                        else:
                                                                            return 2
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    if features["E(RIGHT) - agent_column"] <= -4.999726:
                                                                        return 2
                                                                    else:
                                                                        return 1
                                                        else:
                                                            if features["E(RIGHT) - agent_row"] <= -3.857430:
                                                                if features["T(up) - T(RIGHT)"] <= -0.023842:
                                                                    return 2
                                                                else:
                                                                    if features["E(LEFT) - time_left"] <= 0.211710:
                                                                        if features["T(LEFT)"] <= 0.000001:
                                                                            return 2
                                                                        else:
                                                                            if features["agent_row - time_left"] <= 10.730000:
                                                                                return 1
                                                                            else:
                                                                                return 2
                                                                    else:
                                                                        return 2
                                                            else:
                                                                if features["T(DOWN) - agent_column"] <= -10.461493:
                                                                    return 2
                                                                else:
                                                                    return 1
                                                    else:
                                                        if features["E(RIGHT) - agent_row"] <= -9.797199:
                                                            return 2
                                                        else:
                                                            if features["E(DOWN) - agent_column"] <= -9.672685:
                                                                return 3
                                                            else:
                                                                return 1
                                                else:
                                                    if features["agent_row - agent_column"] <= 10.500000:
                                                        if features["E(RIGHT)"] <= 0.000009:
                                                            if features["T(RIGHT) - agent_column"] <= -1.607405:
                                                                return 1
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["E(UP) - E(DOWN)"] <= -0.317064:
                                                                return 1
                                                            else:
                                                                return 2
                                                    else:
                                                        return 2
                                            else:
                                                if features["E(LEFT) - agent_column"] <= -2.851319:
                                                    if features["T(LEFT)"] <= 0.000000:
                                                        if features["E(UP) - E(RIGHT)"] <= -0.073786:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["T(up)"] <= 0.156511:
                                                            if features["E(DOWN) - T(up)"] <= 0.218273:
                                                                return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            if features["T(up) - agent_column"] <= -2.399516:
                                                                return 1
                                                            else:
                                                                return 3
                                                else:
                                                    if features["E(LEFT) - T(up)"] <= -0.186987:
                                                        if features["T(LEFT)"] <= 0.000003:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["E(DOWN) - E(RIGHT)"] <= -0.197068:
                                                            return 0
                                                        else:
                                                            return 2
                                else:
                                    if features["E(RIGHT) - agent_column"] <= -11.984122:
                                        return 2
                                    else:
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.370716:
                                            return 1
                                        else:
                                            return 2
                            else:
                                if features["T(DOWN) - T(RIGHT)"] <= -0.000000:
                                    if features["E(RIGHT) - agent_column"] <= -3.620577:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    return 3
                else:
                    if features["E(DOWN) - time_left"] <= 0.207812:
                        if features["E(LEFT) - agent_row"] <= -4.959189:
                            return 1
                        else:
                            if features["E(DOWN) - time_left"] <= -0.421677:
                                return 3
                            else:
                                if features["E(UP)"] <= 0.044615:
                                    return 1
                                else:
                                    return 2
                    else:
                        if features["E(UP) - T(up)"] <= 0.001495:
                            if features["E(LEFT) - T(LEFT)"] <= 0.014290:
                                return 1
                            else:
                                if features["E(RIGHT) - agent_column"] <= -2.634094:
                                    return 1
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.269812:
                                        if features["T(RIGHT) - agent_row"] <= -4.933607:
                                            return 3
                                        else:
                                            return 2
                                    else:
                                        return 1
                        else:
                            if features["T(up) - time_left"] <= -0.120000:
                                return 1
                            else:
                                if features["T(up)"] <= 0.000000:
                                    return 1
                                else:
                                    if features["T(up) - T(LEFT)"] <= 0.037173:
                                        return 1
                                    else:
                                        if features["E(UP) - T(LEFT)"] <= 0.046152:
                                            return 2
                                        else:
                                            if features["E(UP) - T(up)"] <= 0.009251:
                                                return 3
                                            else:
                                                return 1
            else:
                if features["E(RIGHT) - T(RIGHT)"] <= 0.155039:
                    if features["E(LEFT) - E(RIGHT)"] <= -0.106574:
                        if features["E(UP) - T(up)"] <= 0.120028:
                            if features["E(RIGHT) - time_left"] <= 0.249785:
                                if features["T(LEFT) - time_left"] <= 0.010594:
                                    if features["T(DOWN) - agent_row"] <= -4.552992:
                                        return 1
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -5.000000:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    return 2
                            else:
                                if features["T(DOWN) - agent_column"] <= -1.854399:
                                    if features["T(DOWN) - T(RIGHT)"] <= 0.000389:
                                        return 1
                                    else:
                                        if features["T(up) - time_left"] <= 0.052977:
                                            return 3
                                        else:
                                            return 2
                                else:
                                    if features["T(up) - time_left"] <= -0.019876:
                                        return 1
                                    else:
                                        return 3
                        else:
                            if features["T(up) - T(LEFT)"] <= -0.000002:
                                if features["E(LEFT) - agent_column"] <= -3.945935:
                                    return 0
                                else:
                                    if features["E(LEFT) - agent_row"] <= -0.972603:
                                        if features["E(RIGHT) - time_left"] <= 0.307347:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 2
                            else:
                                if features["E(DOWN) - T(RIGHT)"] <= -0.244580:
                                    if features["E(RIGHT) - agent_column"] <= -2.654146:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.288610:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= -0.467404:
                                            return 3
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -0.999954:
                                                return 0
                                            else:
                                                return 3
                                else:
                                    if features["agent_column - time_left"] <= 0.770000:
                                        return 1
                                    else:
                                        if features["T(up) - agent_row"] <= -4.999858:
                                            return 2
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= -0.134258:
                                                return 2
                                            else:
                                                return 1
                    else:
                        if features["E(DOWN) - agent_row"] <= -4.600426:
                            if features["T(RIGHT) - agent_row"] <= -5.691088:
                                if features["E(LEFT) - T(LEFT)"] <= -0.007124:
                                    if features["E(UP) - T(RIGHT)"] <= 0.008627:
                                        return 1
                                    else:
                                        if features["T(up) - time_left"] <= -0.197736:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    if features["E(DOWN) - T(up)"] <= 0.075100:
                                        if features["E(LEFT) - time_left"] <= 0.251633:
                                            return 1
                                        else:
                                            return 0
                                    else:
                                        return 2
                            else:
                                if features["T(up)"] <= 0.000016:
                                    if features["T(DOWN) - T(RIGHT)"] <= -0.000004:
                                        return 2
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -4.347344:
                                            if features["E(DOWN) - T(DOWN)"] <= -0.109651:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 0
                                else:
                                    return 2
                        else:
                            if features["E(DOWN)"] <= 0.329469:
                                if features["agent_row - agent_column"] <= -2.500000:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(DOWN) - time_left"] <= 0.339933:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.262948:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    return 1
                else:
                    if features["E(DOWN)"] <= 0.350745:
                        if features["T(up) - T(RIGHT)"] <= -0.000000:
                            if features["agent_row - agent_column"] <= 0.500000:
                                if features["E(LEFT)"] <= 0.264514:
                                    if features["E(UP) - T(LEFT)"] <= -0.355916:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 2
                            else:
                                if features["E(UP) - E(DOWN)"] <= -0.000678:
                                    return 3
                                else:
                                    return 0
                        else:
                            if features["E(DOWN) - time_left"] <= 0.288570:
                                if features["E(DOWN) - agent_row"] <= -8.836060:
                                    return 0
                                else:
                                    return 3
                            else:
                                return 1
                    else:
                        if features["T(DOWN) - time_left"] <= 0.100307:
                            return 1
                        else:
                            if features["E(LEFT)"] <= 0.187559:
                                if features["E(UP) - T(DOWN)"] <= -0.639947:
                                    return 1
                                else:
                                    return 3
                            else:
                                if features["E(DOWN) - time_left"] <= 0.323532:
                                    if features["E(DOWN) - agent_column"] <= -7.616231:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 1
    else:
        if features["E(UP) - E(LEFT)"] <= -0.000012:
            if features["E(DOWN) - E(LEFT)"] <= -0.166318:
                if features["E(UP)"] <= 0.662681:
                    if features["E(RIGHT) - T(RIGHT)"] <= 0.000000:
                        if features["E(LEFT) - time_left"] <= 0.355000:
                            if features["E(LEFT) - time_left"] <= 0.354784:
                                if features["E(LEFT) - T(LEFT)"] <= 0.004504:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.004462:
                                        if features["T(LEFT) - time_left"] <= 0.182723:
                                            if features["agent_row - time_left"] <= 10.710000:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(up) - agent_column"] <= -13.925279:
                                                return 0
                                            else:
                                                if features["E(DOWN) - T(RIGHT)"] <= 0.152188:
                                                    return 2
                                                else:
                                                    if features["T(LEFT) - agent_column"] <= -8.571157:
                                                        return 2
                                                    else:
                                                        return 1
                                    else:
                                        return 0
                                else:
                                    return 2
                            else:
                                return 0
                        else:
                            if features["E(UP) - agent_column"] <= -0.519548:
                                return 2
                            else:
                                return 0
                    else:
                        if features["E(UP) - T(up)"] <= 0.299069:
                            if features["E(LEFT) - time_left"] <= 0.325440:
                                if features["agent_column - time_left"] <= 12.930000:
                                    if features["agent_row - time_left"] <= 7.890000:
                                        if features["T(up) - agent_column"] <= -8.999249:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["T(RIGHT)"] <= 0.000078:
                                            if features["E(UP) - E(LEFT)"] <= -0.000502:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                                else:
                                    return 0
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.252180:
                                    if features["T(RIGHT)"] <= 0.000000:
                                        if features["E(UP) - E(DOWN)"] <= 0.103193:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        return 2
                                else:
                                    return 2
                        else:
                            if features["E(UP) - time_left"] <= 0.237148:
                                return 2
                            else:
                                if features["E(DOWN) - T(LEFT)"] <= -0.537256:
                                    return 2
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.008622:
                                        return 0
                                    else:
                                        return 2
                else:
                    if features["E(RIGHT) - agent_column"] <= -1.999997:
                        if features["E(RIGHT)"] <= 0.000002:
                            if features["E(UP)"] <= 0.799523:
                                return 2
                            else:
                                if features["T(RIGHT) - time_left"] <= 0.177063:
                                    return 0
                                else:
                                    return 2
                        else:
                            if features["E(DOWN) - agent_row"] <= -1.999012:
                                if features["E(UP) - E(LEFT)"] <= -0.020818:
                                    return 2
                                else:
                                    if features["E(RIGHT) - agent_column"] <= -2.999907:
                                        if features["T(LEFT)"] <= 0.000264:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        return 0
                            else:
                                return 2
                    else:
                        if features["T(RIGHT) - time_left"] <= 0.464500:
                            return 0
                        else:
                            return 2
            else:
                if features["E(UP) - T(RIGHT)"] <= 0.000000:
                    if features["E(RIGHT) - agent_column"] <= -1.999997:
                        if features["E(DOWN) - E(LEFT)"] <= 0.000015:
                            if features["E(RIGHT)"] <= 0.000000:
                                return 2
                            else:
                                if features["E(UP) - T(up)"] <= 0.144517:
                                    if features["E(RIGHT) - T(DOWN)"] <= 0.193898:
                                        if features["E(RIGHT) - agent_row"] <= -3.929700:
                                            if features["E(DOWN) - E(RIGHT)"] <= 0.756094:
                                                if features["E(LEFT) - T(LEFT)"] <= 0.012387:
                                                    return 1
                                                else:
                                                    if features["T(DOWN)"] <= 0.000000:
                                                        if features["E(RIGHT) - T(LEFT)"] <= 0.109234:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 2
                                            else:
                                                return 2
                                        else:
                                            return 2
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= 0.000028:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    return 2
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.255957:
                                if features["E(DOWN)"] <= 0.415050:
                                    return 2
                                else:
                                    if features["E(UP) - E(RIGHT)"] <= -0.000000:
                                        return 1
                                    else:
                                        if features["E(UP) - agent_column"] <= -5.999999:
                                            if features["E(LEFT) - agent_column"] <= -6.254774:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 2
                            else:
                                return 0
                    else:
                        if features["E(DOWN)"] <= 0.452801:
                            return 2
                        else:
                            if features["E(UP) - agent_row"] <= -11.999981:
                                return 2
                            else:
                                if features["E(RIGHT)"] <= 0.000003:
                                    return 2
                                else:
                                    return 1
                else:
                    if features["E(UP) - T(up)"] <= 0.134811:
                        if features["E(UP) - time_left"] <= 0.224432:
                            if features["E(LEFT) - T(RIGHT)"] <= 0.352035:
                                if features["T(up)"] <= 0.185564:
                                    if features["T(up)"] <= 0.001237:
                                        if features["E(DOWN) - T(up)"] <= 0.347331:
                                            if features["T(up) - T(RIGHT)"] <= 0.000015:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 1
                                    else:
                                        if features["T(DOWN) - agent_row"] <= -6.684187:
                                            if features["T(DOWN)"] <= 0.309282:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 1
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.348333:
                                        if features["E(RIGHT) - T(up)"] <= -0.001813:
                                            if features["E(DOWN) - agent_row"] <= -7.764033:
                                                if features["T(up) - agent_column"] <= -8.731441:
                                                    if features["T(DOWN) - T(LEFT)"] <= -0.161393:
                                                        if features["E(DOWN) - T(up)"] <= 0.013109:
                                                            if features["E(DOWN)"] <= 0.204545:
                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(LEFT) - agent_row"] <= -9.671798:
                                                        if features["T(DOWN)"] <= 0.000000:
                                                            return 1
                                                        else:
                                                            if features["T(RIGHT) - agent_row"] <= -9.806704:
                                                                return 2
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["T(LEFT) - agent_column"] <= -5.691437:
                                                            return 1
                                                        else:
                                                            return 2
                                            else:
                                                if features["E(DOWN) - time_left"] <= 0.130652:
                                                    if features["E(UP) - T(DOWN)"] <= 0.194547:
                                                        return 2
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.216466:
                                                        if features["E(UP) - T(up)"] <= 0.051442:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        return 2
                                        else:
                                            return 2
                                    else:
                                        return 2
                            else:
                                if features["agent_column - time_left"] <= 13.990000:
                                    if features["agent_column - time_left"] <= 12.950000:
                                        if features["T(LEFT) - agent_column"] <= -8.623911:
                                            if features["T(RIGHT)"] <= 0.000000:
                                                if features["E(RIGHT) - time_left"] <= 0.024295:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["E(DOWN) - T(RIGHT)"] <= 0.255737:
                                                    if features["T(up) - T(DOWN)"] <= -0.049615:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    if features["T(up) - time_left"] <= -0.216527:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - T(RIGHT)"] <= -0.013479:
                                                            return 1
                                                        else:
                                                            return 2
                                        else:
                                            if features["E(RIGHT)"] <= 0.000000:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.361049:
                                            return 2
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= -0.000106:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.010244:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["T(RIGHT)"] <= 0.000000:
                                                    if features["E(UP) - agent_row"] <= -12.999951:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 2
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= -0.267767:
                                        return 1
                                    else:
                                        return 2
                        else:
                            if features["T(DOWN) - T(LEFT)"] <= -0.114979:
                                return 2
                            else:
                                if features["E(DOWN) - T(LEFT)"] <= -0.066092:
                                    if features["T(DOWN)"] <= 0.222767:
                                        return 0
                                    else:
                                        return 1
                                else:
                                    if features["T(up) - agent_column"] <= -7.718354:
                                        return 2
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -6.999999:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - agent_row"] <= -6.766748:
                                                return 2
                                            else:
                                                return 0
                    else:
                        if features["E(LEFT) - time_left"] <= 0.287748:
                            if features["T(DOWN) - T(LEFT)"] <= 0.000036:
                                if features["E(UP) - E(LEFT)"] <= -0.171717:
                                    if features["T(RIGHT) - time_left"] <= -0.219836:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.556321:
                                        return 2
                                    else:
                                        if features["T(up) - agent_row"] <= -7.999997:
                                            return 2
                                        else:
                                            return 3
                            else:
                                if features["E(UP) - agent_row"] <= -4.746748:
                                    if features["T(LEFT) - agent_column"] <= -6.999102:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 0
                        else:
                            return 2
        else:
            if features["E(UP) - E(DOWN)"] <= 0.330281:
                if features["T(up) - T(LEFT)"] <= -0.000028:
                    if features["T(DOWN) - time_left"] <= -0.099792:
                        if features["E(DOWN) - T(DOWN)"] <= 0.000026:
                            return 0
                        else:
                            if features["E(RIGHT) - agent_row"] <= -7.763288:
                                return 3
                            else:
                                if features["agent_row - time_left"] <= 5.670000:
                                    return 1
                                else:
                                    return 3
                    else:
                        if features["E(DOWN) - E(RIGHT)"] <= -0.015704:
                            if features["E(LEFT) - agent_column"] <= -7.747181:
                                if features["E(UP) - time_left"] <= 0.278879:
                                    if features["T(DOWN) - T(LEFT)"] <= -0.000133:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 0
                            else:
                                return 0
                        else:
                            if features["T(RIGHT)"] <= 0.072422:
                                return 0
                            else:
                                return 2
                else:
                    if features["E(UP) - E(LEFT)"] <= 0.127108:
                        if features["E(RIGHT) - time_left"] <= 0.230549:
                            if features["E(LEFT) - T(up)"] <= -0.084395:
                                if features["T(up) - T(RIGHT)"] <= -0.000029:
                                    if features["E(DOWN)"] <= 0.077017:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["E(UP) - E(DOWN)"] <= 0.143558:
                                        return 1
                                    else:
                                        if features["E(UP) - agent_row"] <= -8.620555:
                                            if features["E(UP) - T(DOWN)"] <= 0.240952:
                                                return 2
                                            else:
                                                if features["E(DOWN) - E(LEFT)"] <= -0.140420:
                                                    if features["E(UP) - time_left"] <= 0.356727:
                                                        if features["E(RIGHT) - time_left"] <= -0.015323:
                                                            if features["E(RIGHT) - T(DOWN)"] <= 0.000285:
                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            return 2
                                                    else:
                                                        return 0
                                                else:
                                                    return 1
                                        else:
                                            if features["T(DOWN) - time_left"] <= -0.023356:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.014825:
                                                    return 3
                                                else:
                                                    return 2
                                            else:
                                                if features["E(RIGHT) - T(up)"] <= -0.131751:
                                                    return 0
                                                else:
                                                    return 2
                            else:
                                if features["E(LEFT) - E(RIGHT)"] <= 0.320047:
                                    if features["E(DOWN)"] <= 0.233019:
                                        if features["agent_row - agent_column"] <= -2.500000:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.220772:
                                                return 3
                                            else:
                                                return 2
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.032802:
                                                if features["E(UP) - time_left"] <= 0.385645:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 2
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.017442:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    return 0
                        else:
                            if features["T(DOWN) - time_left"] <= 0.187321:
                                if features["T(up) - time_left"] <= 0.313757:
                                    if features["T(DOWN)"] <= 0.215985:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.007838:
                                        return 0
                                    else:
                                        if features["E(DOWN) - time_left"] <= 0.169913:
                                            return 0
                                        else:
                                            return 1
                            else:
                                return 0
                    else:
                        if features["E(UP) - E(DOWN)"] <= 0.271233:
                            if features["E(DOWN) - agent_row"] <= -10.867599:
                                if features["E(LEFT) - T(up)"] <= -0.274865:
                                    return 0
                                else:
                                    if features["T(up) - T(RIGHT)"] <= 0.010698:
                                        if features["T(LEFT)"] <= 0.000026:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(LEFT) - agent_column"] <= -5.779058:
                                            return 1
                                        else:
                                            if features["T(up)"] <= 0.358078:
                                                return 2
                                            else:
                                                return 0
                            else:
                                if features["E(LEFT) - agent_column"] <= -3.850189:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.028063:
                                        if features["T(up) - time_left"] <= 0.230663:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= -0.000075:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    return 2
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.322584:
                                if features["agent_row - time_left"] <= 6.850000:
                                    if features["E(DOWN) - T(up)"] <= -0.371477:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    if features["E(UP)"] <= 0.386689:
                                        if features["E(DOWN)"] <= 0.016188:
                                            return 0
                                        else:
                                            if features["E(RIGHT) - T(DOWN)"] <= 0.239618:
                                                if features["T(DOWN) - time_left"] <= -0.180000:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["T(LEFT)"] <= 0.000000:
                                                    return 0
                                                else:
                                                    if features["E(LEFT) - T(up)"] <= -0.256874:
                                                        if features["T(LEFT)"] <= 0.060549:
                                                            return 3
                                                        else:
                                                            return 0
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
                if features["E(LEFT) - T(LEFT)"] <= 0.226781:
                    if features["E(RIGHT) - agent_row"] <= -0.564392:
                        if features["E(UP) - time_left"] <= 0.345448:
                            if features["E(DOWN)"] <= 0.000025:
                                if features["T(RIGHT) - time_left"] <= -0.769998:
                                    return 3
                                else:
                                    return 0
                            else:
                                if features["E(DOWN) - E(RIGHT)"] <= -0.041647:
                                    if features["time_left"] <= 0.150000:
                                        if features["T(up) - agent_column"] <= -2.570257:
                                            if features["E(UP) - T(up)"] <= -0.023738:
                                                if features["E(LEFT) - T(up)"] <= -0.134399:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(DOWN) - T(DOWN)"] <= -0.002732:
                                                if features["E(UP) - T(up)"] <= 0.016817:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                    else:
                                        if features["E(LEFT) - E(RIGHT)"] <= -0.214978:
                                            if features["T(LEFT) - time_left"] <= -0.180000:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(UP) - agent_column"] <= -8.487256:
                                                return 3
                                            else:
                                                return 0
                                else:
                                    if features["T(up)"] <= 0.373239:
                                        return 0
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -10.583668:
                                            if features["T(up)"] <= 0.413403:
                                                return 2
                                            else:
                                                if features["T(up)"] <= 0.425808:
                                                    return 0
                                                else:
                                                    return 2
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -8.600607:
                                                return 0
                                            else:
                                                return 2
                        else:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.303012:
                                if features["E(UP) - E(DOWN)"] <= 0.355134:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.001117:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.022951:
                                            return 0
                                        else:
                                            if features["E(UP)"] <= 0.391822:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -9.669077:
                                            if features["T(LEFT)"] <= 0.386206:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(up) - T(LEFT)"] <= 0.156331:
                                                return 0
                                            else:
                                                if features["E(LEFT) - agent_row"] <= -11.813684:
                                                    return 3
                                                else:
                                                    return 1
                                else:
                                    if features["E(LEFT) - agent_row"] <= -0.581853:
                                        return 0
                                    else:
                                        return 2
                            else:
                                if features["E(UP) - T(DOWN)"] <= 0.799903:
                                    if features["E(DOWN)"] <= 0.000203:
                                        if features["E(LEFT) - agent_row"] <= -13.984049:
                                            return 3
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= 0.807980:
                                                return 0
                                            else:
                                                if features["agent_row - agent_column"] <= -3.500000:
                                                    return 0
                                                else:
                                                    return 3
                                    else:
                                        if features["E(DOWN) - time_left"] <= 0.015126:
                                            if features["T(up) - agent_row"] <= -11.595650:
                                                return 0
                                            else:
                                                if features["T(LEFT) - agent_column"] <= -3.000000:
                                                    return 0
                                                else:
                                                    if features["E(DOWN)"] <= 0.005063:
                                                        return 0
                                                    else:
                                                        return 3
                                        else:
                                            return 3
                                else:
                                    if features["E(DOWN) - agent_column"] <= -11.999973:
                                        return 0
                                    else:
                                        return 3
                    else:
                        if features["E(RIGHT) - agent_column"] <= -11.847899:
                            return 0
                        else:
                            if features["T(LEFT) - time_left"] <= -0.599998:
                                return 1
                            else:
                                return 3
                else:
                    if features["E(DOWN) - agent_row"] <= -1.999950:
                        if features["E(DOWN) - T(DOWN)"] <= -0.000000:
                            if features["E(UP) - E(DOWN)"] <= 0.803303:
                                if features["E(DOWN)"] <= 0.000371:
                                    return 0
                                else:
                                    if features["E(UP) - time_left"] <= 0.297085:
                                        return 2
                                    else:
                                        return 0
                            else:
                                if features["T(DOWN) - agent_column"] <= -1.862604:
                                    if features["E(LEFT) - agent_row"] <= -12.132014:
                                        return 2
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.330259:
                                            return 0
                                        else:
                                            return 2
                                else:
                                    return 0
                        else:
                            if features["E(RIGHT) - agent_column"] <= -7.999213:
                                if features["E(UP) - E(LEFT)"] <= 0.105031:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(UP) - time_left"] <= 0.297978:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.003358:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.581777:
                                        return 0
                                    else:
                                        if features["T(RIGHT) - agent_column"] <= -1.498681:
                                            return 2
                                        else:
                                            return 0
                    else:
                        if features["E(RIGHT) - agent_column"] <= -1.999992:
                            if features["E(DOWN) - E(RIGHT)"] <= -0.181428:
                                return 0
                            else:
                                return 2
                        else:
                            if features["E(DOWN) - agent_row"] <= -0.999999:
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
