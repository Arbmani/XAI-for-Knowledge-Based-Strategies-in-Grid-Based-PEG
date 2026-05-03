import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(DOWN)"] <= -0.316339:
        if features["E(LEFT) - E(RIGHT)"] <= -0.320198:
            if features["E(DOWN) - agent_column"] <= -11.265720:
                if features["T(up) - agent_row"] <= -10.522265:
                    if features["E(DOWN) - T(RIGHT)"] <= 0.811832:
                        if features["T(DOWN) - T(LEFT)"] <= 0.370409:
                            return 1
                        else:
                            return 3
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.358123:
                            return 1
                        else:
                            return 3
                else:
                    if features["E(RIGHT) - T(up)"] <= 0.643826:
                        return 1
                    else:
                        if features["T(DOWN) - agent_column"] <= -12.270116:
                            if features["T(RIGHT) - agent_row"] <= -5.523737:
                                if features["E(RIGHT) - agent_row"] <= -5.166123:
                                    return 1
                                else:
                                    return 3
                            else:
                                return 1
                        else:
                            if features["E(DOWN) - agent_row"] <= -3.328393:
                                return 1
                            else:
                                return 3
            else:
                if features["E(RIGHT) - agent_row"] <= -11.208409:
                    if features["E(UP) - E(DOWN)"] <= -0.833876:
                        if features["T(up) - agent_column"] <= -4.863734:
                            if features["T(RIGHT) - agent_column"] <= -11.464478:
                                return 3
                            else:
                                if features["E(RIGHT) - T(up)"] <= 0.143837:
                                    return 3
                                else:
                                    return 1
                        else:
                            return 3
                    else:
                        return 3
                else:
                    if features["E(RIGHT) - agent_row"] <= -3.398903:
                        if features["E(DOWN) - agent_column"] <= -2.448804:
                            if features["E(DOWN) - agent_column"] <= -8.343952:
                                if features["E(UP) - E(DOWN)"] <= -0.724468:
                                    if features["E(RIGHT) - agent_column"] <= -10.271120:
                                        return 3
                                    else:
                                        if features["agent_row - time_left"] <= 5.930000:
                                            if features["E(DOWN) - agent_row"] <= -4.166123:
                                                return 3
                                            else:
                                                if features["T(LEFT) - agent_column"] <= -9.832060:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -9.160498:
                                                if features["agent_row - agent_column"] <= 0.500000:
                                                    if features["T(up) - agent_row"] <= -9.190820:
                                                        if features["agent_row - agent_column"] <= -0.500000:
                                                            return 3
                                                        else:
                                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.730042:
                                                                return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                                            else:
                                                if features["T(up) - agent_row"] <= -9.336697:
                                                    return 3
                                                else:
                                                    if features["agent_row - time_left"] <= 7.810000:
                                                        return 3
                                                    else:
                                                        return 1
                                else:
                                    if features["E(DOWN) - agent_column"] <= -9.338459:
                                        if features["T(LEFT) - time_left"] <= -0.550000:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(DOWN) - E(LEFT)"] <= 0.600146:
                                            return 1
                                        else:
                                            if features["T(up) - agent_row"] <= -6.237815:
                                                if features["E(DOWN)"] <= 0.601097:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                            else:
                                if features["T(up) - agent_column"] <= -8.517287:
                                    return 3
                                else:
                                    if features["time_left"] <= 0.130000:
                                        if features["E(DOWN) - agent_row"] <= -8.401386:
                                            return 3
                                        else:
                                            if features["T(DOWN) - time_left"] <= 0.160191:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -7.457038:
                                                    return 1
                                                else:
                                                    return 3
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -10.280124:
                                            if features["E(RIGHT) - agent_row"] <= -11.194745:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["E(DOWN) - agent_row"] <= -4.505594:
                                                if features["E(DOWN) - T(up)"] <= 0.662308:
                                                    if features["E(DOWN) - E(LEFT)"] <= 0.404188:
                                                        return 3
                                                    else:
                                                        if features["E(RIGHT) - agent_row"] <= -8.406623:
                                                            if features["E(DOWN) - E(LEFT)"] <= 0.649600:
                                                                if features["T(up) - agent_row"] <= -8.513600:
                                                                    return 3
                                                                else:
                                                                    return 1
                                                            else:
                                                                if features["E(RIGHT)"] <= 0.791591:
                                                                    return 1
                                                                else:
                                                                    if features["agent_row - agent_column"] <= 1.500000:
                                                                        return 3
                                                                    else:
                                                                        if features["E(RIGHT) - T(up)"] <= 0.496648:
                                                                            return 1
                                                                        else:
                                                                            return 3
                                                        else:
                                                            if features["E(DOWN) - agent_row"] <= -7.342646:
                                                                return 1
                                                            else:
                                                                if features["T(up) - time_left"] <= 0.337019:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                else:
                                                    return 3
                                            else:
                                                if features["E(RIGHT) - T(up)"] <= 0.004607:
                                                    return 3
                                                else:
                                                    if features["E(LEFT) - E(RIGHT)"] <= -0.492151:
                                                        if features["E(DOWN) - T(DOWN)"] <= 0.791591:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                        else:
                            if features["E(DOWN) - time_left"] <= 0.319506:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.417815:
                                    if features["E(LEFT) - time_left"] <= -0.897760:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["T(up) - agent_column"] <= -1.591956:
                                        if features["E(RIGHT) - T(RIGHT)"] <= -0.180607:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -9.457244:
                                            return 3
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.021092:
                                                return 3
                                            else:
                                                return 1
                            else:
                                if features["T(up) - agent_column"] <= -2.666502:
                                    if features["E(RIGHT) - time_left"] <= 0.733876:
                                        return 1
                                    else:
                                        if features["T(RIGHT)"] <= 0.379998:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["T(up) - agent_row"] <= -8.716942:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.639596:
                                            return 3
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -1.912116:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= 0.713313:
                                                    if features["E(UP) - E(RIGHT)"] <= -0.805255:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                                    else:
                                        if features["E(RIGHT) - T(up)"] <= 0.601715:
                                            if features["E(DOWN)"] <= 0.419441:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["T(up)"] <= 0.195698:
                                                return 1
                                            else:
                                                return 3
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.332020:
                            if features["T(RIGHT) - agent_column"] <= -1.634492:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.208712:
                                    if features["E(RIGHT) - T(up)"] <= 0.449784:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT) - T(DOWN)"] <= -0.105843:
                                        return 1
                                    else:
                                        return 3
                            else:
                                return 1
                        else:
                            if features["T(RIGHT)"] <= 0.360169:
                                if features["E(DOWN) - T(LEFT)"] <= 0.621587:
                                    if features["agent_row - agent_column"] <= -10.500000:
                                        if features["T(up) - agent_column"] <= -11.776887:
                                            if features["E(UP) - E(DOWN)"] <= -0.774534:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 1
                                    else:
                                        if features["T(DOWN) - time_left"] <= 0.358942:
                                            if features["E(RIGHT) - T(LEFT)"] <= 0.197038:
                                                if features["E(UP) - T(up)"] <= -0.039794:
                                                    if features["E(DOWN) - T(DOWN)"] <= 0.518678:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                            else:
                                                if features["T(LEFT) - agent_row"] <= -2.764088:
                                                    return 3
                                                else:
                                                    if features["T(DOWN) - T(RIGHT)"] <= -0.123298:
                                                        return 1
                                                    else:
                                                        return 3
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.574701:
                                                if features["T(up) - agent_row"] <= -0.977955:
                                                    if features["E(RIGHT) - T(LEFT)"] <= 0.309547:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                else:
                                    if features["T(up) - agent_column"] <= -3.462998:
                                        if features["T(RIGHT) - agent_row"] <= -0.887223:
                                            return 3
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= -0.167797:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        if features["T(RIGHT) - agent_column"] <= -1.655223:
                                            return 1
                                        else:
                                            return 3
                            else:
                                if features["E(DOWN) - agent_column"] <= -2.275714:
                                    return 3
                                else:
                                    if features["E(DOWN) - agent_column"] <= -1.638505:
                                        return 1
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= 0.745345:
                                            return 1
                                        else:
                                            return 3
        else:
            if features["E(DOWN) - E(LEFT)"] <= 0.070150:
                if features["E(LEFT) - agent_column"] <= -2.160498:
                    if features["E(LEFT) - agent_row"] <= -11.208409:
                        return 2
                    else:
                        if features["T(RIGHT) - agent_column"] <= -10.863524:
                            if features["E(UP)"] <= 0.040430:
                                if features["E(DOWN) - T(LEFT)"] <= -0.000072:
                                    if features["E(UP) - T(up)"] <= -0.180710:
                                        if features["E(DOWN)"] <= 0.475967:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= -0.164733:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    if features["T(DOWN) - agent_column"] <= -12.603092:
                                        if features["E(LEFT) - agent_row"] <= -11.160498:
                                            return 2
                                        else:
                                            if features["E(DOWN) - time_left"] <= 0.324361:
                                                if features["T(LEFT) - agent_row"] <= -2.619041:
                                                    if features["E(DOWN) - T(up)"] <= 0.016087:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                    else:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.445902:
                                            if features["T(up) - T(LEFT)"] <= -0.378870:
                                                return 2
                                            else:
                                                if features["T(up) - T(LEFT)"] <= -0.355439:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - T(up)"] <= 0.222144:
                                                        return 2
                                                    else:
                                                        if features["T(DOWN)"] <= 0.298558:
                                                            return 1
                                                        else:
                                                            return 2
                                        else:
                                            if features["T(DOWN) - agent_row"] <= -1.294431:
                                                if features["E(UP) - E(DOWN)"] <= -0.839502:
                                                    if features["agent_row - agent_column"] <= -1.500000:
                                                        if features["T(LEFT) - time_left"] <= 0.034874:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -10.271120:
                                                        return 2
                                                    else:
                                                        if features["T(DOWN) - T(RIGHT)"] <= -0.041422:
                                                            return 2
                                                        else:
                                                            return 1
                                            else:
                                                if features["E(LEFT) - agent_column"] <= -10.166124:
                                                    return 2
                                                else:
                                                    return 1
                            else:
                                if features["T(up) - agent_row"] <= -0.979049:
                                    if features["T(LEFT) - time_left"] <= 0.239901:
                                        if features["E(DOWN) - T(LEFT)"] <= 0.055816:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 1
                                else:
                                    return 0
                        else:
                            if features["E(LEFT) - agent_row"] <= -3.454101:
                                if features["T(DOWN) - agent_column"] <= -3.457370:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.662656:
                                        if features["E(DOWN) - agent_row"] <= -8.402229:
                                            if features["E(DOWN)"] <= 0.657557:
                                                return 2
                                            else:
                                                if features["T(up) - T(LEFT)"] <= 0.483331:
                                                    if features["T(up) - T(LEFT)"] <= 0.123875:
                                                        if features["E(LEFT) - agent_row"] <= -10.275729:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 2
                                                else:
                                                    return 1
                                        else:
                                            if features["E(LEFT) - agent_column"] <= -6.275714:
                                                if features["E(LEFT) - T(DOWN)"] <= -0.030962:
                                                    return 1
                                                else:
                                                    if features["T(RIGHT) - agent_row"] <= -8.747914:
                                                        return 1
                                                    else:
                                                        if features["E(DOWN) - agent_row"] <= -7.457038:
                                                            return 2
                                                        else:
                                                            if features["E(DOWN) - T(LEFT)"] <= 0.237391:
                                                                if features["T(LEFT) - agent_row"] <= -7.418490:
                                                                    return 1
                                                                else:
                                                                    if features["E(DOWN) - T(RIGHT)"] <= 0.180318:
                                                                        return 1
                                                                    else:
                                                                        return 2
                                                            else:
                                                                return 2
                                            else:
                                                if features["E(UP) - E(LEFT)"] <= -0.598112:
                                                    if features["T(RIGHT) - agent_row"] <= -4.679131:
                                                        if features["E(DOWN) - agent_row"] <= -4.166123:
                                                            if features["E(DOWN) - agent_row"] <= -7.282117:
                                                                if features["E(DOWN) - agent_row"] <= -8.166124:
                                                                    if features["T(RIGHT) - agent_column"] <= -5.856068:
                                                                        return 1
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    return 1
                                                            else:
                                                                return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["E(DOWN) - T(LEFT)"] <= 0.791591:
                                                            return 2
                                                        else:
                                                            if features["T(RIGHT) - agent_column"] <= -4.269126:
                                                                return 1
                                                            else:
                                                                return 2
                                                else:
                                                    if features["T(DOWN) - agent_column"] <= -5.375929:
                                                        if features["E(UP) - E(DOWN)"] <= -0.542962:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -7.208409:
                                            if features["T(up) - agent_row"] <= -10.113520:
                                                if features["E(DOWN) - agent_row"] <= -11.160498:
                                                    if features["agent_column - time_left"] <= 9.540000:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(UP) - E(DOWN)"] <= -0.724468:
                                                        if features["T(up) - agent_column"] <= -6.843096:
                                                            return 1
                                                        else:
                                                            if features["agent_column - time_left"] <= 5.460000:
                                                                return 1
                                                            else:
                                                                return 2
                                                    else:
                                                        return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - agent_row"] <= -4.166123:
                                                if features["E(LEFT) - T(DOWN)"] <= 0.750539:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                else:
                                    if features["E(UP) - E(DOWN)"] <= -0.728881:
                                        if features["T(RIGHT) - agent_row"] <= -5.375089:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 1
                            else:
                                if features["E(DOWN)"] <= 0.413514:
                                    if features["T(RIGHT) - agent_column"] <= -8.825903:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["agent_column - time_left"] <= 3.530000:
                                        if features["E(LEFT) - agent_column"] <= -2.280124:
                                            if features["E(UP)"] <= 0.108438:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 2
                                    else:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.540633:
                                            return 2
                                        else:
                                            if features["E(DOWN) - agent_row"] <= -0.166124:
                                                if features["E(DOWN) - agent_column"] <= -9.166124:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - T(DOWN)"] <= 0.833876:
                                                        if features["T(up) - time_left"] <= -0.250000:
                                                            return 2
                                                        else:
                                                            if features["E(LEFT) - E(RIGHT)"] <= 0.833876:
                                                                return 2
                                                            else:
                                                                if features["T(up) - agent_row"] <= -1.906514:
                                                                    if features["T(DOWN) - agent_row"] <= -1.533470:
                                                                        return 2
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    return 1
                                                    else:
                                                        return 1
                                            else:
                                                if features["T(LEFT) - T(RIGHT)"] <= -0.049912:
                                                    return 1
                                                else:
                                                    return 2
                else:
                    if features["T(up) - agent_column"] <= -1.842238:
                        if features["E(UP) - E(LEFT)"] <= -0.743591:
                            if features["T(DOWN) - agent_column"] <= -1.682142:
                                if features["agent_row - time_left"] <= 11.790000:
                                    return 1
                                else:
                                    if features["T(RIGHT) - time_left"] <= -0.025336:
                                        return 1
                                    else:
                                        return 2
                            else:
                                if features["T(DOWN) - agent_row"] <= -7.237815:
                                    return 1
                                else:
                                    if features["E(LEFT) - agent_row"] <= -1.194745:
                                        if features["E(DOWN) - agent_row"] <= -3.194745:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(UP) - E(DOWN)"] <= -0.839502:
                                            if features["T(LEFT) - time_left"] <= -0.350000:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 2
                        else:
                            return 1
                    else:
                        if features["E(DOWN) - agent_row"] <= -12.166124:
                            return 2
                        else:
                            if features["agent_row - agent_column"] <= 11.500000:
                                if features["E(DOWN) - agent_column"] <= -1.160498:
                                    if features["E(LEFT)"] <= 0.791591:
                                        return 1
                                    else:
                                        if features["agent_row - time_left"] <= 8.880000:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    return 1
                            else:
                                return 2
            else:
                if features["E(UP)"] <= 0.044846:
                    if features["E(RIGHT) - T(RIGHT)"] <= 0.001684:
                        if features["agent_row - time_left"] <= -0.170000:
                            if features["E(LEFT) - T(LEFT)"] <= 0.119655:
                                return 1
                            else:
                                if features["E(LEFT) - T(DOWN)"] <= -0.260528:
                                    return 1
                                else:
                                    if features["E(RIGHT) - time_left"] <= -0.197773:
                                        return 1
                                    else:
                                        return 2
                        else:
                            if features["E(RIGHT) - T(up)"] <= 0.346760:
                                if features["E(LEFT) - E(RIGHT)"] <= 0.285376:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.112355:
                                        if features["T(up) - time_left"] <= -0.550000:
                                            if features["agent_row - agent_column"] <= -4.500000:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["T(up) - T(DOWN)"] <= -0.467535:
                                                if features["T(DOWN) - agent_row"] <= -2.515479:
                                                    if features["E(DOWN) - agent_row"] <= -8.398373:
                                                        if features["E(RIGHT) - T(DOWN)"] <= -0.387989:
                                                            return 1
                                                        else:
                                                            if features["agent_column - time_left"] <= 9.770000:
                                                                if features["T(LEFT)"] <= 0.271375:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(LEFT)"] <= 0.238071:
                                                        if features["E(LEFT) - time_left"] <= 0.183782:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                            else:
                                                if features["T(up) - agent_row"] <= -12.719791:
                                                    if features["agent_column - time_left"] <= 3.590000:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                                    else:
                                        if features["E(DOWN) - agent_row"] <= 0.430672:
                                            if features["T(up) - time_left"] <= -0.110000:
                                                return 1
                                            else:
                                                if features["agent_row - agent_column"] <= 6.500000:
                                                    return 1
                                                else:
                                                    if features["E(LEFT) - agent_row"] <= -12.719181:
                                                        return 3
                                                    else:
                                                        return 1
                                        else:
                                            if features["E(LEFT) - T(RIGHT)"] <= -0.234531:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    return 2
                            else:
                                if features["E(RIGHT) - time_left"] <= 0.258809:
                                    if features["T(LEFT) - time_left"] <= -0.680000:
                                        return 3
                                    else:
                                        if features["T(DOWN) - agent_row"] <= -5.547467:
                                            if features["E(LEFT) - T(RIGHT)"] <= -0.365611:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["agent_row - time_left"] <= 3.530000:
                                                return 1
                                            else:
                                                if features["E(LEFT) - T(RIGHT)"] <= -0.395132:
                                                    return 3
                                                else:
                                                    return 2
                                else:
                                    return 1
                    else:
                        if features["E(LEFT) - time_left"] <= 0.118007:
                            if features["E(RIGHT) - T(up)"] <= 0.123791:
                                if features["E(LEFT) - agent_row"] <= -12.590674:
                                    return 3
                                else:
                                    if features["agent_column - time_left"] <= 11.180000:
                                        return 1
                                    else:
                                        return 2
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= -0.283777:
                                    if features["agent_row - agent_column"] <= -1.500000:
                                        if features["E(RIGHT) - T(up)"] <= 0.149887:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.471146:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.235129:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT) - T(DOWN)"] <= -0.169043:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.195698:
                                            return 1
                                        else:
                                            if features["T(DOWN) - agent_row"] <= 0.472957:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.241836:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.216015:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.056267:
                                                return 3
                                            else:
                                                if features["T(DOWN) - agent_row"] <= -0.639021:
                                                    if features["E(DOWN) - T(RIGHT)"] <= 0.562780:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(DOWN) - agent_row"] <= -0.565707:
                                                        return 3
                                                    else:
                                                        return 1
                        else:
                            if features["T(up) - agent_column"] <= -10.826757:
                                if features["E(RIGHT) - T(LEFT)"] <= -0.566356:
                                    if features["T(LEFT) - agent_row"] <= -1.113520:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.089848:
                                        if features["T(up) - T(LEFT)"] <= -0.549012:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.265819:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(up) - agent_row"] <= -8.779983:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        if features["T(DOWN) - agent_row"] <= 0.259042:
                                            if features["E(DOWN) - agent_row"] <= -9.442678:
                                                return 2
                                            else:
                                                if features["E(RIGHT) - T(DOWN)"] <= 0.118991:
                                                    return 1
                                                else:
                                                    return 2
                                        else:
                                            if features["T(DOWN) - T(RIGHT)"] <= 0.522698:
                                                return 2
                                            else:
                                                return 1
                            else:
                                if features["T(DOWN) - T(LEFT)"] <= 0.259564:
                                    if features["E(DOWN) - T(up)"] <= 0.564106:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.465400:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.054653:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.382468:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - T(up)"] <= 0.434435:
                                                        return 1
                                                    else:
                                                        return 3
                                            else:
                                                if features["E(LEFT) - T(LEFT)"] <= 0.298151:
                                                    return 1
                                                else:
                                                    return 2
                                        else:
                                            if features["E(DOWN) - T(LEFT)"] <= 0.613213:
                                                return 1
                                            else:
                                                return 2
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= -0.061702:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT) - T(DOWN)"] <= -0.106027:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.287397:
                                            return 1
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -6.556767:
                                                return 1
                                            else:
                                                if features["E(LEFT) - T(RIGHT)"] <= 0.195698:
                                                    return 1
                                                else:
                                                    return 3
                                    else:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.439304:
                                            return 2
                                        else:
                                            return 1
                else:
                    if features["T(up) - agent_row"] <= -0.977111:
                        if features["E(LEFT) - T(LEFT)"] <= 0.197551:
                            if features["T(DOWN) - time_left"] <= -0.680000:
                                return 2
                            else:
                                if features["T(RIGHT) - time_left"] <= 0.336394:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.460048:
                                        return 1
                                    else:
                                        if features["T(DOWN) - time_left"] <= 0.304998:
                                            if features["E(DOWN) - T(LEFT)"] <= 0.000060:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - T(RIGHT)"] <= 0.231280:
                                                    return 0
                                                else:
                                                    return 3
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.181393:
                                                return 1
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.599202:
                                                    return 3
                                                else:
                                                    return 1
                                else:
                                    return 1
                        else:
                            if features["T(DOWN) - T(LEFT)"] <= 0.136266:
                                return 1
                            else:
                                if features["T(DOWN) - agent_column"] <= -7.663669:
                                    if features["E(UP) - T(DOWN)"] <= -0.560155:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.235928:
                                        if features["T(up) - T(DOWN)"] <= -0.301281:
                                            if features["E(LEFT) - T(DOWN)"] <= -0.336789:
                                                return 1
                                            else:
                                                return 0
                                        else:
                                            return 2
                                    else:
                                        return 3
                    else:
                        if features["T(DOWN) - agent_row"] <= -0.798727:
                            return 1
                        else:
                            return 0
    else:
        if features["E(LEFT) - E(RIGHT)"] <= 0.365161:
            if features["E(LEFT) - E(RIGHT)"] <= -0.365161:
                if features["E(UP) - E(DOWN)"] <= 0.362817:
                    if features["E(UP) - T(up)"] <= 0.002664:
                        if features["E(LEFT)"] <= 0.028057:
                            if features["E(DOWN) - T(DOWN)"] <= 0.036742:
                                if features["E(DOWN) - T(up)"] <= 0.207302:
                                    if features["E(UP) - T(LEFT)"] <= 0.409675:
                                        if features["E(RIGHT) - time_left"] <= -0.035970:
                                            if features["T(RIGHT) - time_left"] <= -0.489208:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.380533:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        return 1
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= 0.396321:
                                        return 3
                                    else:
                                        if features["T(up) - time_left"] <= 0.034429:
                                            if features["E(DOWN) - T(up)"] <= 0.268295:
                                                return 3
                                            else:
                                                if features["T(DOWN) - agent_row"] <= -1.630061:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            return 1
                            else:
                                if features["T(LEFT) - time_left"] <= -0.290000:
                                    if features["E(UP)"] <= 0.276919:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.482346:
                                            if features["E(UP) - agent_column"] <= -0.738855:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["E(UP) - E(RIGHT)"] <= -0.369727:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        if features["agent_column - time_left"] <= 5.610000:
                                            if features["E(RIGHT) - agent_column"] <= -2.529322:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["agent_row - agent_column"] <= 0.500000:
                                                return 3
                                            else:
                                                return 1
                                else:
                                    if features["E(UP) - E(DOWN)"] <= 0.311758:
                                        if features["E(DOWN) - agent_row"] <= -4.626466:
                                            if features["E(UP) - T(LEFT)"] <= 0.293111:
                                                return 3
                                            else:
                                                if features["T(up) - agent_column"] <= 0.603543:
                                                    if features["E(UP) - agent_column"] <= -2.676214:
                                                        if features["E(RIGHT) - time_left"] <= 0.185901:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                        else:
                                            return 3
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= 0.405007:
                                            return 3
                                        else:
                                            return 0
                        else:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.369832:
                                return 2
                            else:
                                if features["T(RIGHT) - agent_column"] <= -0.579102:
                                    return 3
                                else:
                                    if features["E(DOWN) - T(up)"] <= -0.260364:
                                        return 3
                                    else:
                                        return 1
                    else:
                        if features["E(UP) - T(LEFT)"] <= 0.180651:
                            if features["E(DOWN) - T(LEFT)"] <= 0.285925:
                                if features["E(UP) - E(DOWN)"] <= 0.272125:
                                    if features["agent_row - agent_column"] <= -6.500000:
                                        return 3
                                    else:
                                        if features["E(UP) - T(LEFT)"] <= -0.717216:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    return 0
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.119111:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.155837:
                                        if features["T(DOWN) - time_left"] <= 0.311934:
                                            if features["T(DOWN) - agent_column"] <= -5.458970:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 3
                                    else:
                                        if features["E(RIGHT) - time_left"] <= 0.284202:
                                            if features["agent_column - time_left"] <= 8.530000:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["E(UP) - T(DOWN)"] <= -0.724161:
                                                return 1
                                            else:
                                                return 3
                                else:
                                    return 1
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.279956:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.371676:
                                    if features["agent_column - time_left"] <= 2.710000:
                                        if features["E(DOWN) - agent_column"] <= -0.821629:
                                            return 3
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= -0.286015:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= -0.400670:
                                            return 1
                                        else:
                                            return 0
                                else:
                                    return 2
                            else:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.399485:
                                    if features["T(DOWN) - agent_column"] <= -6.208409:
                                        if features["E(UP) - T(RIGHT)"] <= -0.191156:
                                            if features["T(RIGHT) - agent_row"] <= -4.378515:
                                                return 0
                                            else:
                                                return 1
                                        else:
                                            return 3
                                    else:
                                        return 3
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -5.863734:
                                        if features["E(UP) - T(RIGHT)"] <= -0.349901:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 2
                else:
                    if features["E(RIGHT) - agent_column"] <= -11.225466:
                        if features["T(RIGHT) - agent_row"] <= -13.946573:
                            return 3
                        else:
                            if features["T(up) - agent_column"] <= -11.537632:
                                if features["T(DOWN) - T(LEFT)"] <= -0.623033:
                                    return 0
                                else:
                                    if features["T(DOWN) - time_left"] <= -0.570000:
                                        return 3
                                    else:
                                        return 0
                            else:
                                return 0
                    else:
                        if features["T(RIGHT) - agent_row"] <= -1.269958:
                            if features["T(RIGHT) - agent_row"] <= -8.620933:
                                if features["E(UP) - T(DOWN)"] <= 0.605912:
                                    if features["E(RIGHT) - agent_column"] <= -7.457038:
                                        if features["T(DOWN) - T(RIGHT)"] <= -0.365460:
                                            if features["E(RIGHT) - T(RIGHT)"] <= -0.111321:
                                                return 0
                                            else:
                                                if features["agent_row - time_left"] <= 12.850000:
                                                    if features["agent_row - agent_column"] <= -0.500000:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 3
                                        else:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.598614:
                                                if features["E(RIGHT) - agent_column"] <= -9.340798:
                                                    if features["E(UP) - E(DOWN)"] <= 0.715108:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                            else:
                                                if features["E(UP) - E(RIGHT)"] <= -0.025021:
                                                    return 3
                                                else:
                                                    return 0
                                    else:
                                        if features["T(LEFT) - time_left"] <= -0.690000:
                                            return 2
                                        else:
                                            if features["E(UP)"] <= 0.374936:
                                                if features["T(up) - agent_column"] <= 0.368961:
                                                    if features["E(RIGHT) - agent_column"] <= -3.634250:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                            else:
                                                if features["E(LEFT) - T(up)"] <= -0.560610:
                                                    return 0
                                                else:
                                                    if features["T(up) - T(DOWN)"] <= 0.301281:
                                                        if features["agent_column - time_left"] <= 4.890000:
                                                            if features["E(RIGHT) - time_left"] <= 0.344794:
                                                                return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            if features["E(UP)"] <= 0.462565:
                                                                return 0
                                                            else:
                                                                if features["T(up) - T(RIGHT)"] <= 0.312521:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                    else:
                                                        return 3
                                else:
                                    if features["agent_column - time_left"] <= 3.870000:
                                        if features["T(up) - agent_row"] <= -12.503725:
                                            if features["E(RIGHT) - T(up)"] <= 0.444177:
                                                if features["T(up) - agent_row"] <= -12.606164:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                        else:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.833876:
                                                if features["T(up) - agent_row"] <= -11.447831:
                                                    if features["T(RIGHT) - agent_column"] <= -2.212421:
                                                        if features["agent_column - time_left"] <= 3.610000:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                            else:
                                                if features["T(up) - agent_row"] <= -10.849119:
                                                    return 3
                                                else:
                                                    return 0
                                    else:
                                        if features["agent_row - time_left"] <= 13.330000:
                                            if features["E(RIGHT) - agent_column"] <= -9.316883:
                                                if features["E(UP)"] <= 0.719876:
                                                    return 0
                                                else:
                                                    if features["agent_row - agent_column"] <= -0.500000:
                                                        return 3
                                                    else:
                                                        if features["agent_row - agent_column"] <= 1.500000:
                                                            if features["E(RIGHT) - agent_column"] <= -10.166124:
                                                                if features["T(up) - agent_row"] <= -12.511055:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            return 3
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -8.208409:
                                                    if features["T(up) - time_left"] <= 0.546223:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    if features["agent_row - agent_column"] <= 0.500000:
                                                        return 0
                                                    else:
                                                        return 3
                                        else:
                                            return 3
                            else:
                                if features["T(LEFT) - agent_row"] <= -2.873604:
                                    if features["E(UP) - agent_column"] <= -2.387846:
                                        if features["T(up) - agent_column"] <= -7.697324:
                                            if features["E(RIGHT) - T(DOWN)"] <= 0.600038:
                                                if features["T(up) - T(RIGHT)"] <= -0.030918:
                                                    if features["E(RIGHT)"] <= 0.839502:
                                                        if features["E(DOWN) - time_left"] <= -0.150000:
                                                            return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        return 0
                                                else:
                                                    if features["T(DOWN) - T(LEFT)"] <= -0.155495:
                                                        return 0
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -5.679686:
                                                            if features["E(DOWN) - E(RIGHT)"] <= -0.656048:
                                                                return 0
                                                            else:
                                                                if features["T(DOWN) - time_left"] <= -0.270000:
                                                                    return 1
                                                                else:
                                                                    return 0
                                                        else:
                                                            return 0
                                            else:
                                                if features["T(up) - T(LEFT)"] <= 0.587626:
                                                    if features["T(LEFT) - agent_column"] <= -11.452642:
                                                        return 3
                                                    else:
                                                        if features["T(up) - T(LEFT)"] <= -0.705569:
                                                            return 3
                                                        else:
                                                            if features["T(up) - T(LEFT)"] <= -0.092162:
                                                                return 0
                                                            else:
                                                                return 3
                                                else:
                                                    if features["T(up) - agent_column"] <= -9.263995:
                                                        return 1
                                                    else:
                                                        return 0
                                        else:
                                            if features["E(RIGHT) - T(LEFT)"] <= 0.556411:
                                                if features["T(DOWN) - T(LEFT)"] <= 0.015061:
                                                    if features["T(RIGHT) - time_left"] <= -0.150000:
                                                        return 0
                                                    else:
                                                        if features["E(LEFT) - time_left"] <= -0.430000:
                                                            return 2
                                                        else:
                                                            if features["E(UP) - agent_column"] <= -7.457038:
                                                                return 0
                                                            else:
                                                                if features["E(RIGHT) - T(up)"] <= 0.724286:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                else:
                                                    if features["E(RIGHT) - T(DOWN)"] <= 0.264251:
                                                        if features["E(RIGHT) - agent_column"] <= -6.507849:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(up) - T(RIGHT)"] <= -0.106065:
                                                            if features["T(RIGHT) - agent_row"] <= -4.636748:
                                                                return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            return 3
                                            else:
                                                if features["T(RIGHT) - agent_row"] <= -6.514312:
                                                    return 3
                                                else:
                                                    if features["E(UP) - time_left"] <= -0.189101:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - T(up)"] <= 0.662359:
                                                            if features["T(DOWN) - agent_row"] <= -2.827416:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            return 0
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= 0.407660:
                                            return 3
                                        else:
                                            if features["T(DOWN) - agent_row"] <= -7.775776:
                                                if features["E(UP) - agent_row"] <= -7.208409:
                                                    return 0
                                                else:
                                                    if features["E(UP) - agent_column"] <= -1.166124:
                                                        return 0
                                                    else:
                                                        return 3
                                            else:
                                                if features["E(RIGHT) - time_left"] <= 0.088039:
                                                    return 2
                                                else:
                                                    if features["E(UP) - T(LEFT)"] <= 0.447841:
                                                        if features["agent_row - agent_column"] <= 6.500000:
                                                            return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        return 0
                                else:
                                    if features["E(UP)"] <= 0.719876:
                                        return 3
                                    else:
                                        if features["E(DOWN) - E(RIGHT)"] <= -0.791591:
                                            if features["E(UP) - T(DOWN)"] <= 0.502600:
                                                if features["agent_row - agent_column"] <= -9.500000:
                                                    return 0
                                                else:
                                                    if features["T(DOWN) - agent_column"] <= -8.642543:
                                                        if features["T(LEFT) - agent_column"] <= -9.848379:
                                                            if features["E(UP) - agent_column"] <= -10.194745:
                                                                return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(DOWN) - agent_column"] <= -5.602967:
                                                            return 0
                                                        else:
                                                            if features["E(UP) - T(LEFT)"] <= 0.805255:
                                                                return 0
                                                            else:
                                                                return 3
                                            else:
                                                if features["T(DOWN) - agent_column"] <= -10.836494:
                                                    return 3
                                                else:
                                                    if features["agent_column - time_left"] <= 1.930000:
                                                        return 3
                                                    else:
                                                        return 0
                                        else:
                                            if features["agent_row - time_left"] <= 2.630000:
                                                if features["T(up) - T(RIGHT)"] <= -0.532952:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(DOWN) - T(RIGHT)"] <= 0.339609:
                                                    if features["E(UP) - T(RIGHT)"] <= 0.528000:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                        else:
                            if features["T(DOWN) - agent_column"] <= -4.850028:
                                if features["E(RIGHT) - T(up)"] <= 0.805255:
                                    return 3
                                else:
                                    if features["T(DOWN) - agent_column"] <= -8.556113:
                                        if features["T(up) - agent_column"] <= -11.983132:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        if features["agent_column - time_left"] <= 5.790000:
                                            return 3
                                        else:
                                            return 0
                            else:
                                return 3
            else:
                if features["E(UP) - E(DOWN)"] <= 0.382643:
                    if features["E(LEFT) - T(DOWN)"] <= 0.066116:
                        if features["E(UP)"] <= 0.211556:
                            if features["E(DOWN)"] <= 0.365281:
                                if features["T(RIGHT) - agent_row"] <= -4.808249:
                                    if features["E(RIGHT) - T(DOWN)"] <= -0.391037:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.496573:
                                            if features["T(LEFT) - agent_column"] <= -8.269958:
                                                return 2
                                            else:
                                                return 3
                                        else:
                                            if features["E(LEFT) - time_left"] <= 0.176992:
                                                return 3
                                            else:
                                                if features["E(DOWN) - T(LEFT)"] <= 0.315860:
                                                    return 0
                                                else:
                                                    return 2
                                    else:
                                        if features["E(RIGHT)"] <= 0.023487:
                                            return 2
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.269400:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.292527:
                                                    if features["E(DOWN) - time_left"] <= 0.145015:
                                                        return 3
                                                    else:
                                                        if features["E(LEFT) - agent_row"] <= -4.730599:
                                                            return 3
                                                        else:
                                                            return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(DOWN) - agent_column"] <= -9.527043:
                                                    return 0
                                                else:
                                                    return 2
                                else:
                                    if features["E(DOWN) - E(LEFT)"] <= 0.253813:
                                        if features["E(UP) - E(DOWN)"] <= -0.117575:
                                            if features["E(UP) - T(DOWN)"] <= -0.179318:
                                                if features["E(RIGHT) - T(RIGHT)"] <= 0.221262:
                                                    if features["E(RIGHT) - agent_row"] <= -2.814151:
                                                        if features["T(up) - time_left"] <= 0.101411:
                                                            if features["T(up)"] <= 0.166366:
                                                                if features["E(LEFT) - T(LEFT)"] <= 0.207405:
                                                                    if features["E(RIGHT) - time_left"] <= 0.216836:
                                                                        if features["E(RIGHT) - time_left"] <= -0.094122:
                                                                            return 3
                                                                        else:
                                                                            if features["T(up) - T(LEFT)"] <= -0.446867:
                                                                                if features["E(RIGHT) - T(DOWN)"] <= -0.411693:
                                                                                    return 2
                                                                                else:
                                                                                    return 0
                                                                            else:
                                                                                return 2
                                                                    else:
                                                                        if features["T(RIGHT) - agent_row"] <= -4.242629:
                                                                            return 3
                                                                        else:
                                                                            return 1
                                                                else:
                                                                    if features["E(RIGHT) - T(DOWN)"] <= -0.366732:
                                                                        return 2
                                                                    else:
                                                                        if features["T(RIGHT) - agent_column"] <= -5.396442:
                                                                            return 0
                                                                        else:
                                                                            return 2
                                                            else:
                                                                if features["E(RIGHT) - T(up)"] <= 0.105314:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                        else:
                                                            if features["T(RIGHT) - agent_row"] <= -3.747157:
                                                                if features["agent_column - time_left"] <= 7.990000:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                            else:
                                                                return 2
                                                    else:
                                                        if features["T(LEFT) - time_left"] <= 0.066858:
                                                            if features["T(up) - T(DOWN)"] <= -0.223607:
                                                                if features["T(RIGHT) - time_left"] <= 0.284801:
                                                                    if features["E(RIGHT) - time_left"] <= 0.006868:
                                                                        return 1
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    return 1
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["E(LEFT)"] <= 0.335663:
                                                                if features["agent_column - time_left"] <= 11.930000:
                                                                    return 1
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["T(LEFT) - agent_column"] <= -12.517854:
                                                                    return 3
                                                                else:
                                                                    if features["E(DOWN) - T(RIGHT)"] <= 0.309175:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                else:
                                                    if features["T(LEFT) - agent_column"] <= -5.398672:
                                                        return 0
                                                    else:
                                                        if features["E(RIGHT) - T(DOWN)"] <= -0.503210:
                                                            return 1
                                                        else:
                                                            return 3
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.332838:
                                                    if features["T(up)"] <= 0.159235:
                                                        if features["E(LEFT) - time_left"] <= 0.305264:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["T(RIGHT)"] <= 0.207405:
                                                            if features["agent_row - time_left"] <= 3.930000:
                                                                return 0
                                                            else:
                                                                return 1
                                                        else:
                                                            if features["T(RIGHT) - time_left"] <= 0.316596:
                                                                return 0
                                                            else:
                                                                if features["E(DOWN)"] <= 0.338801:
                                                                    if features["E(RIGHT) - time_left"] <= 0.337200:
                                                                        return 0
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    return 1
                                                else:
                                                    return 1
                                        else:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.188480:
                                                return 3
                                            else:
                                                if features["E(LEFT) - T(RIGHT)"] <= -0.509469:
                                                    if features["T(DOWN) - agent_column"] <= -3.166124:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(DOWN) - T(RIGHT)"] <= -0.278351:
                                                        return 1
                                                    else:
                                                        if features["E(DOWN) - T(up)"] <= 0.114660:
                                                            if features["E(RIGHT) - time_left"] <= 0.352644:
                                                                return 2
                                                            else:
                                                                if features["E(RIGHT) - time_left"] <= 0.353869:
                                                                    return 3
                                                                else:
                                                                    if features["E(DOWN) - agent_column"] <= -2.196132:
                                                                        return 2
                                                                    else:
                                                                        if features["E(RIGHT) - agent_row"] <= -4.597356:
                                                                            return 3
                                                                        else:
                                                                            return 2
                                                        else:
                                                            if features["E(DOWN) - time_left"] <= 0.139165:
                                                                return 2
                                                            else:
                                                                if features["T(DOWN) - time_left"] <= 0.261515:
                                                                    if features["E(LEFT) - time_left"] <= 0.032682:
                                                                        return 2
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    if features["T(RIGHT) - agent_column"] <= -3.458144:
                                                                        return 2
                                                                    else:
                                                                        if features["E(RIGHT) - time_left"] <= 0.313081:
                                                                            return 2
                                                                        else:
                                                                            if features["T(RIGHT)"] <= 0.532620:
                                                                                return 3
                                                                            else:
                                                                                return 2
                                    else:
                                        if features["agent_column - time_left"] <= 0.950000:
                                            if features["E(DOWN) - time_left"] <= 0.249060:
                                                if features["T(DOWN)"] <= 0.289816:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= 0.033470:
                                                if features["E(RIGHT) - agent_row"] <= -3.598070:
                                                    if features["T(LEFT) - agent_column"] <= -1.970776:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                            else:
                                if features["T(up)"] <= 0.087884:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.238354:
                                        if features["E(RIGHT) - time_left"] <= 0.230014:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.314830:
                                                if features["E(UP) - T(LEFT)"] <= -0.362133:
                                                    if features["E(LEFT) - time_left"] <= 0.155219:
                                                        if features["E(DOWN) - T(RIGHT)"] <= 0.376593:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(DOWN) - agent_row"] <= -1.302153:
                                                            if features["E(DOWN)"] <= 0.371879:
                                                                return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(UP) - T(DOWN)"] <= -0.241017:
                                                        if features["E(UP) - T(RIGHT)"] <= -0.463385:
                                                            return 1
                                                        else:
                                                            if features["E(LEFT) - T(RIGHT)"] <= 0.303868:
                                                                return 0
                                                            else:
                                                                if features["E(LEFT) - time_left"] <= 0.171888:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                    else:
                                                        return 2
                                            else:
                                                return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= -0.344471:
                                            return 1
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -5.671009:
                                                if features["T(LEFT) - agent_row"] <= -1.693124:
                                                    if features["E(LEFT) - T(DOWN)"] <= -0.109506:
                                                        if features["T(LEFT) - T(RIGHT)"] <= 0.550562:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 2
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                else:
                                    if features["E(RIGHT) - time_left"] <= 0.311888:
                                        return 0
                                    else:
                                        return 1
                        else:
                            if features["E(UP) - T(RIGHT)"] <= 0.033601:
                                if features["T(RIGHT)"] <= 0.372210:
                                    if features["E(UP) - time_left"] <= 0.357444:
                                        if features["time_left"] <= 0.150000:
                                            if features["T(LEFT) - time_left"] <= 0.285050:
                                                if features["E(DOWN) - T(LEFT)"] <= -0.030325:
                                                    if features["E(RIGHT) - agent_row"] <= -9.673739:
                                                        if features["E(RIGHT) - T(LEFT)"] <= 0.219832:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                            else:
                                                if features["T(up) - agent_row"] <= -5.754570:
                                                    return 0
                                                else:
                                                    if features["T(RIGHT) - agent_column"] <= -7.754570:
                                                        return 0
                                                    else:
                                                        return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.001142:
                                            return 3
                                        else:
                                            return 0
                                else:
                                    if features["E(DOWN)"] <= 0.276544:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.276771:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.256912:
                                                if features["T(LEFT) - agent_row"] <= -10.924625:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["E(UP) - time_left"] <= 0.121175:
                                                    if features["E(RIGHT) - agent_row"] <= -9.827806:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    if features["T(RIGHT)"] <= 0.373220:
                                                        return 2
                                                    else:
                                                        if features["E(RIGHT) - T(up)"] <= 0.382892:
                                                            if features["E(UP) - E(LEFT)"] <= 0.060198:
                                                                return 2
                                                            else:
                                                                if features["E(RIGHT) - T(DOWN)"] <= 0.178233:
                                                                    return 0
                                                                else:
                                                                    if features["E(LEFT) - T(up)"] <= -0.217442:
                                                                        return 0
                                                                    else:
                                                                        if features["agent_row - time_left"] <= 8.990000:
                                                                            return 2
                                                                        else:
                                                                            return 0
                                                        else:
                                                            return 3
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= -0.371545:
                                                if features["E(RIGHT) - agent_column"] <= -2.668832:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(RIGHT) - agent_column"] <= -0.597154:
                                                    return 2
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.261764:
                                                        return 2
                                                    else:
                                                        return 0
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= 0.307929:
                                            if features["E(LEFT) - T(RIGHT)"] <= -0.242099:
                                                if features["T(RIGHT) - agent_row"] <= -6.310897:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                        else:
                                            return 0
                            else:
                                if features["E(DOWN) - agent_column"] <= -7.679686:
                                    if features["T(DOWN) - agent_row"] <= -7.255361:
                                        if features["T(up) - time_left"] <= -0.171433:
                                            return 1
                                        else:
                                            return 0
                                    else:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.247230:
                                            if features["E(DOWN) - time_left"] <= 0.264560:
                                                return 2
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.275149:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            if features["T(DOWN) - T(RIGHT)"] <= 0.447081:
                                                return 3
                                            else:
                                                if features["E(UP) - T(DOWN)"] <= -0.489837:
                                                    if features["T(LEFT) - agent_column"] <= -7.625770:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    if features["time_left"] <= 0.150000:
                                                        return 0
                                                    else:
                                                        return 1
                                else:
                                    if features["E(DOWN)"] <= 0.017478:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.315458:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        if features["E(UP) - T(up)"] <= 0.276544:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.213635:
                                                if features["E(DOWN) - T(LEFT)"] <= -0.062540:
                                                    if features["T(up) - time_left"] <= 0.369487:
                                                        if features["T(DOWN) - agent_column"] <= -6.443406:
                                                            if features["E(RIGHT) - T(LEFT)"] <= -0.217396:
                                                                if features["T(DOWN) - agent_column"] <= -7.454889:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                return 0
                                                        else:
                                                            if features["agent_column - time_left"] <= 3.970000:
                                                                if features["agent_row - time_left"] <= 6.870000:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["agent_column - time_left"] <= 6.750000:
                                                                    return 3
                                                                else:
                                                                    if features["E(LEFT) - T(LEFT)"] <= -0.455483:
                                                                        return 0
                                                                    else:
                                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(RIGHT) - time_left"] <= 0.119192:
                                                return 1
                                            else:
                                                return 0
                    else:
                        if features["T(DOWN)"] <= 0.112355:
                            if features["E(UP) - T(up)"] <= 0.247230:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.270277:
                                    if features["E(UP) - T(LEFT)"] <= 0.280541:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.033001:
                                            if features["E(UP) - E(DOWN)"] <= 0.298863:
                                                if features["E(LEFT) - time_left"] <= 0.366208:
                                                    if features["E(UP) - agent_column"] <= -10.868011:
                                                        if features["E(DOWN) - T(up)"] <= 0.299822:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["E(UP) - agent_row"] <= -7.361481:
                                                            return 0
                                                        else:
                                                            return 1
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(LEFT) - T(DOWN)"] <= 0.114012:
                                                if features["T(RIGHT) - agent_column"] <= -2.433837:
                                                    if features["E(UP) - time_left"] <= 0.398122:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(DOWN) - T(RIGHT)"] <= -0.267867:
                                                        if features["T(RIGHT) - time_left"] <= 0.530354:
                                                            if features["E(DOWN) - time_left"] <= 0.026125:
                                                                return 1
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["E(DOWN) - T(LEFT)"] <= 0.347055:
                                                                return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["T(up) - agent_row"] <= -5.531751:
                                                            if features["E(DOWN) - T(RIGHT)"] <= -0.134185:
                                                                return 1
                                                            else:
                                                                return 3
                                                        else:
                                                            return 1
                                            else:
                                                if features["E(UP) - T(RIGHT)"] <= 0.278036:
                                                    if features["E(LEFT) - T(LEFT)"] <= 0.324980:
                                                        if features["E(RIGHT) - T(LEFT)"] <= 0.355628:
                                                            if features["E(LEFT) - T(DOWN)"] <= 0.125855:
                                                                if features["E(UP) - time_left"] <= 0.358997:
                                                                    if features["T(up) - T(RIGHT)"] <= -0.705569:
                                                                        return 2
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["E(UP) - T(up)"] <= 0.177156:
                                                                    if features["E(RIGHT) - T(LEFT)"] <= -0.686929:
                                                                        if features["agent_column - time_left"] <= 9.970000:
                                                                            return 1
                                                                        else:
                                                                            return 2
                                                                    else:
                                                                        if features["E(LEFT)"] <= 0.372976:
                                                                            if features["E(UP) - time_left"] <= 0.077344:
                                                                                if features["E(RIGHT) - T(RIGHT)"] <= 0.247230:
                                                                                    if features["T(LEFT) - time_left"] <= -0.250000:
                                                                                        return 2
                                                                                    else:
                                                                                        return 1
                                                                                else:
                                                                                    return 3
                                                                            else:
                                                                                return 1
                                                                        else:
                                                                            if features["T(LEFT) - time_left"] <= 0.578614:
                                                                                if features["T(up) - agent_row"] <= -6.600080:
                                                                                    if features["E(DOWN) - T(up)"] <= -0.216350:
                                                                                        return 1
                                                                                    else:
                                                                                        return 3
                                                                                else:
                                                                                    return 1
                                                                            else:
                                                                                return 2
                                                                else:
                                                                    if features["E(DOWN) - T(RIGHT)"] <= -0.281551:
                                                                        return 2
                                                                    else:
                                                                        if features["E(UP) - T(LEFT)"] <= 0.211556:
                                                                            if features["E(UP) - time_left"] <= 0.057650:
                                                                                return 3
                                                                            else:
                                                                                if features["E(RIGHT) - T(LEFT)"] <= -0.576076:
                                                                                    if features["E(DOWN) - E(RIGHT)"] <= 0.133640:
                                                                                        return 1
                                                                                    else:
                                                                                        return 2
                                                                                else:
                                                                                    if features["T(LEFT) - agent_row"] <= -5.572051:
                                                                                        return 3
                                                                                    else:
                                                                                        return 1
                                                                        else:
                                                                            if features["E(LEFT) - T(RIGHT)"] <= -0.304403:
                                                                                return 1
                                                                            else:
                                                                                if features["agent_row - time_left"] <= 5.890000:
                                                                                    return 2
                                                                                else:
                                                                                    return 0
                                                        else:
                                                            if features["T(up) - T(RIGHT)"] <= -0.522698:
                                                                if features["E(DOWN) - T(RIGHT)"] <= -0.245661:
                                                                    return 2
                                                                else:
                                                                    return 1
                                                            else:
                                                                if features["E(DOWN) - T(RIGHT)"] <= -0.404405:
                                                                    if features["T(RIGHT) - agent_row"] <= -4.275714:
                                                                        return 3
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    if features["T(RIGHT) - agent_row"] <= -5.471453:
                                                                        if features["E(DOWN) - time_left"] <= 0.151856:
                                                                            return 1
                                                                        else:
                                                                            return 3
                                                                    else:
                                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.190434:
                                                            if features["E(LEFT) - E(RIGHT)"] <= 0.303791:
                                                                if features["E(DOWN) - T(RIGHT)"] <= -0.360980:
                                                                    return 2
                                                                else:
                                                                    return 1
                                                            else:
                                                                return 2
                                                        else:
                                                            return 1
                                                else:
                                                    if features["E(LEFT) - time_left"] <= 0.249121:
                                                        if features["T(LEFT) - agent_column"] <= -7.532316:
                                                            if features["E(RIGHT) - T(LEFT)"] <= -0.225612:
                                                                if features["E(UP) - T(DOWN)"] <= 0.411262:
                                                                    if features["agent_column - time_left"] <= 9.830000:
                                                                        if features["E(DOWN) - T(LEFT)"] <= -0.284423:
                                                                            return 1
                                                                        else:
                                                                            return 3
                                                                    else:
                                                                        if features["E(DOWN) - T(up)"] <= -0.432615:
                                                                            return 2
                                                                        else:
                                                                            if features["T(up) - time_left"] <= -0.047656:
                                                                                return 2
                                                                            else:
                                                                                if features["E(UP) - time_left"] <= 0.119131:
                                                                                    return 1
                                                                                else:
                                                                                    if features["E(LEFT) - T(up)"] <= -0.059829:
                                                                                        return 1
                                                                                    else:
                                                                                        return 3
                                                                else:
                                                                    if features["E(LEFT) - T(up)"] <= -0.166956:
                                                                        return 3
                                                                    else:
                                                                        return 1
                                                            else:
                                                                if features["E(RIGHT) - T(LEFT)"] <= -0.102054:
                                                                    if features["E(LEFT) - T(RIGHT)"] <= 0.324980:
                                                                        return 1
                                                                    else:
                                                                        return 3
                                                                else:
                                                                    return 2
                                                        else:
                                                            if features["E(DOWN) - T(up)"] <= -0.450631:
                                                                return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["E(DOWN) - E(LEFT)"] <= -0.303565:
                                                            return 0
                                                        else:
                                                            if features["E(LEFT) - T(DOWN)"] <= 0.336294:
                                                                if features["E(UP) - T(RIGHT)"] <= 0.318006:
                                                                    return 1
                                                                else:
                                                                    if features["E(DOWN) - T(LEFT)"] <= -0.363646:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                            else:
                                                                if features["T(LEFT) - time_left"] <= 0.309743:
                                                                    if features["E(UP) - E(DOWN)"] <= 0.114660:
                                                                        return 3
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    return 2
                                    else:
                                        if features["agent_column - time_left"] <= 8.930000:
                                            if features["E(UP) - agent_column"] <= -4.669916:
                                                if features["T(RIGHT) - time_left"] <= 0.466227:
                                                    if features["E(UP) - E(RIGHT)"] <= 0.207008:
                                                        if features["agent_row - time_left"] <= 12.890000:
                                                            if features["E(LEFT) - agent_column"] <= -7.700685:
                                                                if features["T(up) - agent_row"] <= -10.383335:
                                                                    return 1
                                                                else:
                                                                    if features["E(DOWN) - T(up)"] <= -0.429678:
                                                                        return 1
                                                                    else:
                                                                        return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["E(UP) - T(DOWN)"] <= 0.370601:
                                                            return 0
                                                        else:
                                                            return 2
                                                else:
                                                    if features["E(UP) - agent_row"] <= -10.635965:
                                                        return 0
                                                    else:
                                                        if features["agent_column - time_left"] <= 4.890000:
                                                            return 1
                                                        else:
                                                            return 2
                                            else:
                                                if features["agent_row - time_left"] <= 9.890000:
                                                    if features["E(LEFT) - T(RIGHT)"] <= -0.577123:
                                                        return 0
                                                    else:
                                                        if features["T(RIGHT) - agent_column"] <= -4.464484:
                                                            return 1
                                                        else:
                                                            if features["T(up) - agent_row"] <= -7.530500:
                                                                return 2
                                                            else:
                                                                return 1
                                                else:
                                                    if features["time_left"] <= 0.210000:
                                                        if features["E(UP) - agent_column"] <= -3.645007:
                                                            if features["E(UP) - T(RIGHT)"] <= -0.172841:
                                                                return 2
                                                            else:
                                                                return 0
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["agent_column - time_left"] <= 4.650000:
                                                            return 2
                                                        else:
                                                            return 1
                                        else:
                                            if features["E(DOWN)"] <= 0.015400:
                                                return 0
                                            else:
                                                if features["E(DOWN) - T(up)"] <= -0.751177:
                                                    return 0
                                                else:
                                                    if features["E(RIGHT) - T(up)"] <= -0.118334:
                                                        return 2
                                                    else:
                                                        return 1
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.296455:
                                        if features["E(DOWN) - T(up)"] <= 0.308886:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.211556:
                                                if features["E(DOWN) - T(up)"] <= -0.531475:
                                                    if features["E(UP) - E(RIGHT)"] <= -0.077807:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    if features["T(up) - agent_column"] <= -6.505173:
                                                        return 1
                                                    else:
                                                        if features["E(DOWN) - E(LEFT)"] <= 0.180616:
                                                            if features["E(UP) - T(LEFT)"] <= 0.376208:
                                                                return 3
                                                            else:
                                                                if features["E(RIGHT) - T(up)"] <= -0.092723:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                        else:
                                                            return 1
                                            else:
                                                if features["T(up) - agent_row"] <= -9.361574:
                                                    return 3
                                                else:
                                                    return 1
                                        else:
                                            if features["E(UP) - E(LEFT)"] <= -0.047025:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        if features["T(up) - agent_column"] <= -3.138216:
                                            if features["E(UP) - T(up)"] <= 0.189159:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["E(UP) - T(LEFT)"] <= 0.192985:
                                                return 1
                                            else:
                                                return 3
                            else:
                                if features["E(UP) - T(RIGHT)"] <= -0.273785:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.153525:
                                        if features["T(RIGHT) - time_left"] <= 0.518425:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -11.691866:
                                            return 3
                                        else:
                                            if features["E(LEFT) - T(RIGHT)"] <= -0.639309:
                                                return 0
                                            else:
                                                return 2
                                else:
                                    if features["E(RIGHT) - time_left"] <= 0.121498:
                                        if features["agent_row - time_left"] <= 8.970000:
                                            if features["E(RIGHT) - T(LEFT)"] <= -0.408362:
                                                if features["agent_column - time_left"] <= 10.830000:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["E(DOWN) - T(LEFT)"] <= -0.083918:
                                                    return 3
                                                else:
                                                    return 2
                                        else:
                                            if features["T(RIGHT) - time_left"] <= -0.150000:
                                                return 1
                                            else:
                                                return 0
                                    else:
                                        if features["T(LEFT) - agent_row"] <= -6.422329:
                                            if features["T(LEFT) - time_left"] <= -0.090000:
                                                return 2
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.543701:
                                                    if features["E(LEFT) - agent_row"] <= -9.778738:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                        else:
                                            if features["E(RIGHT) - agent_row"] <= -6.678193:
                                                return 0
                                            else:
                                                return 3
                        else:
                            if features["E(LEFT) - T(LEFT)"] <= -0.010479:
                                return 2
                            else:
                                if features["E(RIGHT) - agent_column"] <= -11.907444:
                                    if features["T(LEFT) - agent_row"] <= -10.618571:
                                        if features["agent_column - time_left"] <= 11.970000:
                                            return 3
                                        else:
                                            return 2
                                    else:
                                        return 3
                                else:
                                    if features["agent_column - time_left"] <= 11.890000:
                                        if features["T(RIGHT) - agent_row"] <= -10.755852:
                                            if features["E(LEFT) - agent_row"] <= -10.679036:
                                                return 1
                                            else:
                                                if features["agent_row - agent_column"] <= 0.500000:
                                                    return 3
                                                else:
                                                    return 0
                                        else:
                                            if features["agent_column - time_left"] <= 11.870000:
                                                if features["E(UP)"] <= 0.330084:
                                                    if features["T(DOWN) - agent_row"] <= -7.759322:
                                                        return 3
                                                    else:
                                                        if features["E(RIGHT)"] <= 0.195046:
                                                            if features["T(up) - time_left"] <= 0.223404:
                                                                return 3
                                                            else:
                                                                if features["T(DOWN)"] <= 0.276897:
                                                                    return 1
                                                                else:
                                                                    return 2
                                                        else:
                                                            return 0
                                                else:
                                                    if features["E(LEFT) - time_left"] <= 0.269670:
                                                        if features["E(RIGHT) - time_left"] <= 0.201238:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 0
                                            else:
                                                return 1
                                    else:
                                        if features["agent_row - time_left"] <= 6.970000:
                                            return 3
                                        else:
                                            return 2
                else:
                    if features["E(UP) - time_left"] <= 0.264779:
                        if features["E(DOWN) - E(LEFT)"] <= -0.075614:
                            if features["E(RIGHT) - time_left"] <= -0.296376:
                                if features["T(up) - T(RIGHT)"] <= 0.360756:
                                    if features["E(UP) - T(up)"] <= 0.530596:
                                        if features["E(LEFT) - agent_row"] <= -12.762268:
                                            return 0
                                        else:
                                            if features["E(LEFT) - T(up)"] <= -0.257549:
                                                if features["E(LEFT) - E(RIGHT)"] <= -0.227218:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 2
                                    else:
                                        if features["E(UP) - E(RIGHT)"] <= 0.348309:
                                            return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.469746:
                                        return 0
                                    else:
                                        return 2
                            else:
                                if features["E(LEFT) - agent_row"] <= -13.689745:
                                    if features["E(UP) - T(LEFT)"] <= 0.136376:
                                        if features["agent_column - time_left"] <= 10.770000:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        if features["agent_column - time_left"] <= 7.690000:
                                            return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(LEFT) - E(RIGHT)"] <= 0.253218:
                                        if features["E(LEFT) - T(RIGHT)"] <= -0.291745:
                                            if features["E(UP) - E(LEFT)"] <= 0.280923:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -12.593743:
                                                if features["agent_column - time_left"] <= 10.790000:
                                                    if features["T(up) - agent_column"] <= -9.626521:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(DOWN) - time_left"] <= -0.330000:
                                                        return 2
                                                    else:
                                                        return 0
                                            else:
                                                return 0
                                    else:
                                        return 1
                        else:
                            if features["E(UP) - T(DOWN)"] <= 0.779774:
                                return 0
                            else:
                                return 2
                    else:
                        if features["E(LEFT) - T(LEFT)"] <= 0.259700:
                            if features["E(UP) - time_left"] <= 0.373496:
                                if features["E(LEFT) - agent_row"] <= -13.726799:
                                    if features["E(LEFT) - agent_row"] <= -13.747773:
                                        if features["T(up) - time_left"] <= 0.313689:
                                            if features["E(UP) - T(up)"] <= 0.104550:
                                                if features["T(LEFT) - agent_column"] <= -7.879344:
                                                    return 2
                                                else:
                                                    if features["E(LEFT) - T(RIGHT)"] <= -0.118022:
                                                        return 0
                                                    else:
                                                        return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= -0.198198:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.001643:
                                        if features["T(DOWN) - T(LEFT)"] <= -0.402027:
                                            if features["E(LEFT) - T(DOWN)"] <= 0.373335:
                                                return 0
                                            else:
                                                if features["T(up) - T(DOWN)"] <= 0.511429:
                                                    if features["E(UP) - T(LEFT)"] <= -0.332379:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(RIGHT) - time_left"] <= -0.076090:
                                                        return 1
                                                    else:
                                                        return 2
                                        else:
                                            return 0
                                    else:
                                        if features["E(UP) - T(DOWN)"] <= 0.511219:
                                            if features["E(RIGHT) - agent_row"] <= -1.574026:
                                                if features["E(RIGHT) - agent_row"] <= -12.791785:
                                                    return 2
                                                else:
                                                    if features["E(DOWN) - E(LEFT)"] <= -0.091812:
                                                        if features["T(LEFT) - time_left"] <= 0.238170:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["T(DOWN) - time_left"] <= 0.239989:
                                                            return 0
                                                        else:
                                                            return 3
                                            else:
                                                return 3
                                        else:
                                            if features["T(up) - T(LEFT)"] <= 0.492236:
                                                return 0
                                            else:
                                                if features["T(up) - agent_row"] <= -7.286422:
                                                    return 2
                                                else:
                                                    return 0
                            else:
                                if features["T(up) - T(DOWN)"] <= 0.587988:
                                    if features["E(UP) - T(LEFT)"] <= -0.471342:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    if features["E(LEFT) - T(up)"] <= -0.260049:
                                        return 0
                                    else:
                                        return 2
                        else:
                            if features["E(RIGHT) - T(up)"] <= 0.039755:
                                if features["T(up) - time_left"] <= 0.629607:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.214253:
                                        if features["T(up) - time_left"] <= 0.469989:
                                            return 2
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -11.707384:
                                                return 0
                                            else:
                                                return 2
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.273969:
                                            return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(LEFT) - agent_row"] <= -9.709919:
                                        return 0
                                    else:
                                        if features["E(LEFT) - T(up)"] <= -0.529858:
                                            return 0
                                        else:
                                            return 2
                            else:
                                return 0
        else:
            if features["E(UP) - E(LEFT)"] <= -0.074155:
                if features["E(RIGHT)"] <= 0.006477:
                    if features["E(UP) - T(up)"] <= 0.014517:
                        if features["E(DOWN) - E(LEFT)"] <= -0.053427:
                            if features["E(LEFT) - time_left"] <= 0.224044:
                                if features["T(DOWN) - agent_column"] <= -12.914565:
                                    if features["E(UP) - agent_column"] <= -12.814950:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["T(up) - time_left"] <= -0.780000:
                                        return 0
                                    else:
                                        return 2
                            else:
                                if features["T(LEFT) - agent_column"] <= -13.659548:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.178445:
                                        return 2
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= -0.279167:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    return 2
                        else:
                            return 1
                    else:
                        if features["E(UP) - T(RIGHT)"] <= 0.250595:
                            if features["T(LEFT) - agent_row"] <= -3.876701:
                                if features["E(DOWN) - agent_column"] <= -1.598758:
                                    if features["T(DOWN) - agent_column"] <= -12.850150:
                                        if features["T(DOWN) - time_left"] <= -0.070000:
                                            if features["E(UP) - T(DOWN)"] <= 0.221617:
                                                if features["E(UP) - T(LEFT)"] <= -0.281532:
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
                                    if features["T(DOWN) - agent_column"] <= -1.410143:
                                        return 1
                                    else:
                                        return 0
                            else:
                                if features["T(LEFT) - agent_column"] <= -13.591747:
                                    return 1
                                else:
                                    if features["E(UP) - T(LEFT)"] <= -0.574259:
                                        if features["agent_column - time_left"] <= 10.910000:
                                            if features["T(DOWN) - agent_column"] <= -7.275714:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 2
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -12.595104:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.288161:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -2.797838:
                                                return 2
                                            else:
                                                return 1
                        else:
                            if features["E(LEFT) - time_left"] <= 0.259445:
                                if features["E(UP) - agent_row"] <= -8.732239:
                                    if features["agent_row - time_left"] <= 8.670000:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    if features["agent_row - time_left"] <= 8.570000:
                                        return 1
                                    else:
                                        return 3
                            else:
                                if features["T(DOWN) - time_left"] <= 0.476479:
                                    if features["E(UP) - T(LEFT)"] <= -0.289949:
                                        if features["E(LEFT) - agent_row"] <= -10.541533:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 2
                                else:
                                    if features["T(LEFT) - agent_column"] <= -9.208409:
                                        if features["T(LEFT) - agent_column"] <= -12.305472:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        return 2
                else:
                    if features["T(DOWN) - time_left"] <= 0.038533:
                        if features["E(DOWN) - time_left"] <= -0.606864:
                            return 2
                        else:
                            if features["E(UP) - T(LEFT)"] <= -0.325692:
                                return 2
                            else:
                                if features["E(UP) - T(LEFT)"] <= -0.044478:
                                    if features["E(UP) - T(up)"] <= 0.219926:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    return 2
                    else:
                        if features["T(DOWN) - time_left"] <= 0.366778:
                            return 3
                        else:
                            return 2
            else:
                if features["T(up) - agent_row"] <= -1.917574:
                    if features["T(RIGHT) - agent_column"] <= -1.871349:
                        if features["E(LEFT) - T(DOWN)"] <= 0.576016:
                            if features["E(LEFT) - T(RIGHT)"] <= 0.609301:
                                if features["T(LEFT) - agent_row"] <= -3.698257:
                                    if features["agent_column - time_left"] <= 13.950000:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.229568:
                                            if features["T(DOWN) - T(RIGHT)"] <= 0.015061:
                                                if features["T(up) - agent_column"] <= -4.918152:
                                                    if features["T(RIGHT) - agent_row"] <= -11.280124:
                                                        if features["E(LEFT)"] <= 0.449283:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(LEFT) - T(up)"] <= 0.659202:
                                                        return 0
                                                    else:
                                                        if features["agent_row - time_left"] <= 4.930000:
                                                            return 0
                                                        else:
                                                            return 2
                                            else:
                                                return 2
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -10.614709:
                                                if features["E(LEFT) - T(LEFT)"] <= -0.084502:
                                                    return 0
                                                else:
                                                    if features["E(LEFT) - agent_column"] <= -5.340798:
                                                        return 2
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(UP) - T(DOWN)"] <= 0.212329:
                                                    if features["E(LEFT) - T(RIGHT)"] <= 0.492151:
                                                        if features["T(RIGHT) - agent_row"] <= -7.931931:
                                                            if features["T(up) - agent_column"] <= -7.850928:
                                                                return 2
                                                            else:
                                                                return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["E(RIGHT) - agent_column"] <= -4.500000:
                                                            if features["T(LEFT) - agent_column"] <= -9.506784:
                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            return 0
                                                else:
                                                    if features["T(up) - agent_column"] <= -10.711107:
                                                        if features["E(LEFT) - T(LEFT)"] <= -0.013702:
                                                            return 2
                                                        else:
                                                            if features["T(LEFT) - time_left"] <= -0.150000:
                                                                return 2
                                                            else:
                                                                return 0
                                                    else:
                                                        if features["E(UP) - agent_row"] <= -3.166124:
                                                            if features["T(RIGHT) - agent_column"] <= -7.781620:
                                                                if features["T(LEFT) - agent_row"] <= -6.453505:
                                                                    return 2
                                                                else:
                                                                    if features["E(UP) - E(DOWN)"] <= 0.553024:
                                                                        return 2
                                                                    else:
                                                                        return 0
                                                            else:
                                                                if features["E(LEFT) - time_left"] <= 0.745838:
                                                                    if features["E(LEFT) - T(up)"] <= -0.096827:
                                                                        return 0
                                                                    else:
                                                                        if features["E(LEFT) - agent_column"] <= -2.260175:
                                                                            return 0
                                                                        else:
                                                                            return 2
                                                                else:
                                                                    if features["T(up) - agent_column"] <= -5.737128:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                        else:
                                                            return 0
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.018016:
                                            return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(UP)"] <= 0.602914:
                                        return 2
                                    else:
                                        if features["T(up) - agent_row"] <= -2.863524:
                                            if features["E(UP) - agent_column"] <= -2.252390:
                                                if features["E(UP) - T(LEFT)"] <= 0.670186:
                                                    if features["T(DOWN) - time_left"] <= 0.341891:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                                            else:
                                                return 2
                                        else:
                                            if features["E(UP) - agent_row"] <= -1.208409:
                                                return 2
                                            else:
                                                if features["E(UP) - agent_column"] <= -2.194745:
                                                    return 0
                                                else:
                                                    return 2
                            else:
                                if features["T(LEFT) - agent_row"] <= -1.611970:
                                    return 0
                                else:
                                    if features["T(DOWN) - agent_column"] <= -8.275714:
                                        return 0
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.805255:
                                            return 2
                                        else:
                                            return 0
                        else:
                            if features["T(LEFT) - agent_row"] <= -8.240827:
                                if features["T(RIGHT) - agent_row"] <= -13.699147:
                                    if features["agent_column - time_left"] <= 3.850000:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["E(UP)"] <= 0.805255:
                                        if features["T(DOWN) - time_left"] <= -0.168338:
                                            if features["agent_row - agent_column"] <= 8.500000:
                                                if features["agent_row - agent_column"] <= 3.500000:
                                                    return 2
                                                else:
                                                    if features["agent_row - agent_column"] <= 6.500000:
                                                        return 2
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -12.900385:
                                                            return 2
                                                        else:
                                                            if features["E(UP) - E(RIGHT)"] <= 0.728881:
                                                                return 0
                                                            else:
                                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -12.708146:
                                                if features["T(LEFT) - agent_column"] <= -3.923062:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                if features["T(up) - T(RIGHT)"] <= -0.071532:
                                                    return 0
                                                else:
                                                    return 2
                                    else:
                                        if features["agent_row - agent_column"] <= 2.500000:
                                            if features["T(up) - T(DOWN)"] <= 0.109962:
                                                if features["T(LEFT) - agent_column"] <= -11.816060:
                                                    return 2
                                                else:
                                                    if features["T(LEFT) - agent_column"] <= -11.294431:
                                                        return 0
                                                    else:
                                                        return 2
                                            else:
                                                return 2
                                        else:
                                            if features["agent_row - agent_column"] <= 3.500000:
                                                if features["T(LEFT) - agent_row"] <= -12.853469:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                if features["T(DOWN) - agent_row"] <= -11.907444:
                                                    if features["T(RIGHT) - agent_row"] <= -11.698407:
                                                        return 2
                                                    else:
                                                        if features["T(DOWN) - agent_column"] <= -4.956859:
                                                            if features["agent_column - time_left"] <= 6.930000:
                                                                return 2
                                                            else:
                                                                return 0
                                                        else:
                                                            return 0
                                                else:
                                                    if features["T(up) - agent_column"] <= -4.546142:
                                                        if features["T(DOWN) - agent_row"] <= -10.860373:
                                                            return 2
                                                        else:
                                                            if features["E(LEFT) - agent_column"] <= -4.631876:
                                                                return 0
                                                            else:
                                                                return 2
                                                    else:
                                                        return 2
                            else:
                                if features["E(LEFT) - T(LEFT)"] <= 0.730042:
                                    if features["T(LEFT) - time_left"] <= -0.187423:
                                        return 0
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -10.628786:
                                            if features["E(UP) - T(RIGHT)"] <= 0.791591:
                                                return 0
                                            else:
                                                if features["E(UP) - agent_column"] <= -11.194745:
                                                    if features["T(up) - agent_column"] <= -13.770504:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["E(LEFT) - agent_column"] <= -9.315202:
                                                return 2
                                            else:
                                                if features["E(LEFT) - T(up)"] <= 0.839502:
                                                    return 2
                                                else:
                                                    return 0
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -4.265144:
                                        if features["E(LEFT) - agent_column"] <= -2.166124:
                                            if features["T(up) - agent_row"] <= -7.432376:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 2
                                    else:
                                        if features["agent_row - agent_column"] <= -3.500000:
                                            return 2
                                        else:
                                            return 0
                    else:
                        if features["E(LEFT) - E(RIGHT)"] <= 0.799069:
                            if features["E(DOWN) - T(up)"] <= -0.609589:
                                if features["E(UP) - T(up)"] <= 0.015037:
                                    return 0
                                else:
                                    return 2
                            else:
                                return 0
                        else:
                            if features["E(UP) - agent_column"] <= -1.160498:
                                if features["agent_row - time_left"] <= 12.540000:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(DOWN) - T(up)"] <= -0.519659:
                                    if features["E(LEFT) - T(RIGHT)"] <= 0.833876:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["agent_row - time_left"] <= 7.690000:
                                        return 0
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -10.336697:
                                            if features["E(DOWN) - time_left"] <= -0.510000:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["agent_row - agent_column"] <= 8.500000:
                                                if features["T(LEFT) - agent_row"] <= -7.947616:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["E(UP)"] <= 0.833876:
                                                    return 0
                                                else:
                                                    return 2
                else:
                    if features["agent_row - time_left"] <= 1.230000:
                        if features["E(UP) - T(RIGHT)"] <= 0.850646:
                            return 2
                        else:
                            if features["T(up) - agent_column"] <= -11.980521:
                                if features["T(DOWN) - agent_column"] <= -11.682950:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 2
                    else:
                        if features["E(UP)"] <= 0.791591:
                            return 2
                        else:
                            if features["E(LEFT) - T(LEFT)"] <= 0.805255:
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
