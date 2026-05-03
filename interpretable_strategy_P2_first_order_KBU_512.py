import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(DOWN)"] <= -0.364744:
        if features["E(LEFT) - E(RIGHT)"] <= 0.329779:
            if features["E(RIGHT)"] <= 0.345813:
                if features["E(UP)"] <= 0.020964:
                    if features["E(LEFT) - T(LEFT)"] <= 0.004412:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.018016:
                            if features["T(up) - T(DOWN)"] <= -0.510883:
                                if features["E(RIGHT) - T(DOWN)"] <= -0.265298:
                                    if features["E(LEFT) - T(up)"] <= 0.328977:
                                        if features["E(RIGHT)"] <= 0.294813:
                                            if features["T(DOWN) - T(RIGHT)"] <= 0.548723:
                                                return 1
                                            else:
                                                if features["agent_row - agent_column"] <= 0.500000:
                                                    return 1
                                                else:
                                                    if features["E(UP) - time_left"] <= -0.460000:
                                                        return 3
                                                    else:
                                                        return 1
                                        else:
                                            return 3
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -6.956916:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    if features["agent_row - time_left"] <= 4.820000:
                                        return 1
                                    else:
                                        return 3
                            else:
                                return 1
                        else:
                            if features["T(LEFT) - agent_column"] <= -6.281099:
                                if features["agent_row - agent_column"] <= -7.500000:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.502804:
                                        if features["agent_row - time_left"] <= 0.960000:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(RIGHT) - T(up)"] <= 0.206418:
                                        return 1
                                    else:
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.059459:
                                            return 1
                                        else:
                                            if features["T(DOWN) - T(RIGHT)"] <= 0.616345:
                                                return 1
                                            else:
                                                return 2
                            else:
                                if features["T(LEFT) - agent_row"] <= -6.410847:
                                    return 1
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.046039:
                                        return 3
                                    else:
                                        return 1
                    else:
                        if features["agent_row - agent_column"] <= -6.500000:
                            if features["E(LEFT) - T(LEFT)"] <= 0.264119:
                                return 1
                            else:
                                return 2
                        else:
                            if features["E(LEFT) - T(DOWN)"] <= -0.123602:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.232286:
                                    if features["T(RIGHT) - agent_row"] <= -5.414282:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.264076:
                                            if features["E(DOWN) - time_left"] <= 0.206947:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 3
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.087628:
                                            if features["E(LEFT) - T(DOWN)"] <= -0.321922:
                                                return 1
                                            else:
                                                if features["E(LEFT) - agent_row"] <= -2.719918:
                                                    return 3
                                                else:
                                                    return 2
                                        else:
                                            return 1
                                else:
                                    if features["T(DOWN) - agent_row"] <= -1.294431:
                                        return 3
                                    else:
                                        return 1
                            else:
                                return 1
                else:
                    if features["E(RIGHT) - T(DOWN)"] <= -0.273395:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.189748:
                            if features["E(DOWN) - time_left"] <= 0.330626:
                                return 1
                            else:
                                return 2
                        else:
                            return 3
                    else:
                        return 0
            else:
                if features["E(RIGHT) - agent_column"] <= -11.208409:
                    if features["E(RIGHT) - T(up)"] <= 0.850646:
                        return 1
                    else:
                        return 3
                else:
                    if features["E(RIGHT) - agent_row"] <= -11.208409:
                        if features["E(LEFT)"] <= 0.189213:
                            return 3
                        else:
                            return 1
                    else:
                        if features["E(RIGHT) - agent_column"] <= -0.555235:
                            if features["E(RIGHT) - agent_column"] <= -6.533726:
                                if features["E(UP) - E(RIGHT)"] <= -0.557924:
                                    if features["E(DOWN) - T(up)"] <= 0.607003:
                                        if features["agent_row - agent_column"] <= 0.500000:
                                            if features["T(DOWN) - agent_row"] <= -5.699482:
                                                if features["E(RIGHT) - T(LEFT)"] <= 0.247242:
                                                    return 1
                                                else:
                                                    if features["E(UP) - E(RIGHT)"] <= -0.802442:
                                                        if features["T(LEFT) - agent_row"] <= -8.667659:
                                                            return 1
                                                        else:
                                                            if features["T(LEFT) - agent_row"] <= -8.521936:
                                                                return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        return 1
                                            else:
                                                return 3
                                        else:
                                            if features["E(RIGHT)"] <= 0.728881:
                                                if features["E(DOWN) - agent_row"] <= -9.316883:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= 0.488396:
                                            return 3
                                        else:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.760557:
                                                return 3
                                            else:
                                                if features["E(LEFT) - T(DOWN)"] <= -0.498081:
                                                    return 3
                                                else:
                                                    return 1
                                else:
                                    return 1
                            else:
                                if features["agent_column - time_left"] <= 2.880000:
                                    if features["E(RIGHT) - T(LEFT)"] <= 0.238579:
                                        return 1
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -0.655859:
                                            if features["E(RIGHT) - T(DOWN)"] <= -0.040477:
                                                return 3
                                            else:
                                                if features["E(LEFT) - agent_row"] <= -4.934845:
                                                    if features["E(RIGHT) - agent_row"] <= -6.166123:
                                                        if features["E(DOWN) - agent_row"] <= -9.340798:
                                                            if features["agent_row - agent_column"] <= 9.500000:
                                                                return 3
                                                            else:
                                                                return 1
                                                        else:
                                                            if features["E(DOWN)"] <= 0.522570:
                                                                return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(RIGHT)"] <= 0.728881:
                                        if features["E(DOWN) - agent_row"] <= -8.434824:
                                            if features["E(LEFT) - T(DOWN)"] <= 0.099212:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - T(up)"] <= 0.449391:
                                                if features["T(RIGHT) - agent_row"] <= 0.396095:
                                                    if features["E(LEFT) - T(LEFT)"] <= -0.554032:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -7.671366:
                                            if features["E(UP) - E(DOWN)"] <= -0.839502:
                                                if features["agent_row - agent_column"] <= 5.500000:
                                                    if features["T(LEFT) - agent_row"] <= -11.643928:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(up) - agent_row"] <= -9.843106:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                if features["E(RIGHT) - time_left"] <= 0.619390:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            if features["E(RIGHT) - T(DOWN)"] <= -0.001149:
                                                return 3
                                            else:
                                                if features["T(LEFT) - agent_row"] <= -1.773616:
                                                    if features["E(DOWN) - agent_row"] <= -3.166124:
                                                        if features["T(DOWN) - T(LEFT)"] <= 0.092162:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 3
                        else:
                            if features["T(up) - agent_row"] <= -9.455654:
                                return 3
                            else:
                                if features["agent_row - time_left"] <= 1.620000:
                                    return 3
                                else:
                                    return 1
        else:
            if features["E(LEFT) - agent_row"] <= -11.208409:
                return 2
            else:
                if features["E(RIGHT) - agent_column"] <= -12.978880:
                    if features["E(DOWN)"] <= 0.805255:
                        return 1
                    else:
                        if features["T(RIGHT) - agent_row"] <= -1.983132:
                            if features["agent_row - agent_column"] <= -3.500000:
                                return 2
                            else:
                                return 1
                        else:
                            return 1
                else:
                    if features["agent_row - time_left"] <= 2.860000:
                        if features["T(DOWN) - agent_column"] <= -1.632587:
                            if features["E(LEFT) - agent_row"] <= 0.730042:
                                if features["T(RIGHT) - agent_row"] <= -1.759487:
                                    if features["agent_row - agent_column"] <= -9.500000:
                                        return 1
                                    else:
                                        if features["time_left"] <= 0.180000:
                                            return 2
                                        else:
                                            if features["E(LEFT)"] <= 0.556893:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    if features["T(LEFT) - agent_row"] <= 0.408624:
                                        if features["E(DOWN) - agent_row"] <= -1.449438:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["T(LEFT)"] <= 0.410327:
                                            return 1
                                        else:
                                            return 2
                            else:
                                if features["T(DOWN) - agent_column"] <= -8.551264:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["T(LEFT) - agent_row"] <= -0.982522:
                                if features["E(LEFT) - T(up)"] <= 0.799360:
                                    return 1
                                else:
                                    return 2
                            else:
                                return 1
                    else:
                        if features["E(DOWN)"] <= 0.805255:
                            if features["T(up) - agent_column"] <= -2.736485:
                                if features["E(DOWN) - agent_row"] <= -9.341376:
                                    if features["E(LEFT) - E(RIGHT)"] <= 0.708946:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.017081:
                                        if features["E(LEFT) - agent_column"] <= -11.596116:
                                            return 2
                                        else:
                                            if features["E(DOWN) - agent_row"] <= -6.507849:
                                                if features["E(LEFT) - T(RIGHT)"] <= 0.542962:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                    else:
                                        if features["T(LEFT) - T(RIGHT)"] <= 0.251532:
                                            if features["T(DOWN) - T(LEFT)"] <= -0.235129:
                                                return 2
                                            else:
                                                if features["E(LEFT) - T(up)"] <= 0.728881:
                                                    if features["T(RIGHT) - agent_column"] <= -3.645097:
                                                        if features["E(DOWN) - agent_row"] <= -7.393380:
                                                            if features["E(DOWN)"] <= 0.542962:
                                                                return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["E(UP) - E(LEFT)"] <= -0.601097:
                                                            if features["T(DOWN) - agent_row"] <= -7.416812:
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
                                if features["E(LEFT) - E(RIGHT)"] <= 0.799069:
                                    if features["T(DOWN) - T(RIGHT)"] <= 0.286746:
                                        return 1
                                    else:
                                        if features["E(UP) - E(DOWN)"] <= -0.493298:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["T(up) - agent_column"] <= -1.660116:
                                        return 2
                                    else:
                                        return 1
                        else:
                            if features["T(RIGHT) - agent_row"] <= -11.432928:
                                if features["E(LEFT) - agent_column"] <= -10.160498:
                                    return 2
                                else:
                                    if features["E(UP) - E(DOWN)"] <= -0.839502:
                                        return 1
                                    else:
                                        if features["T(up) - agent_column"] <= -1.839482:
                                            return 2
                                        else:
                                            return 1
                            else:
                                if features["T(up) - agent_column"] <= -0.946005:
                                    if features["T(LEFT)"] <= 0.259680:
                                        return 2
                                    else:
                                        if features["T(LEFT) - agent_row"] <= -9.585468:
                                            return 2
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -8.747914:
                                                return 2
                                            else:
                                                return 1
                                else:
                                    if features["T(up) - agent_row"] <= -7.583854:
                                        if features["T(up) - agent_row"] <= -10.672873:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        return 2
    else:
        if features["E(LEFT) - E(RIGHT)"] <= -0.370323:
            if features["E(UP) - E(DOWN)"] <= 0.338461:
                if features["E(LEFT) - T(LEFT)"] <= 0.011180:
                    if features["E(UP) - T(up)"] <= 0.041449:
                        if features["E(UP) - T(LEFT)"] <= 0.354464:
                            if features["E(UP) - E(DOWN)"] <= -0.325962:
                                if features["T(up) - agent_column"] <= -2.979724:
                                    return 3
                                else:
                                    return 0
                            else:
                                return 3
                        else:
                            if features["T(RIGHT) - agent_column"] <= -6.269958:
                                return 3
                            else:
                                if features["T(up) - agent_column"] <= -3.286421:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.035232:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 3
                    else:
                        if features["T(LEFT) - time_left"] <= -0.280000:
                            if features["E(DOWN) - agent_column"] <= -6.735868:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.029158:
                                    if features["E(UP) - T(RIGHT)"] <= -0.360997:
                                        return 3
                                    else:
                                        return 2
                                else:
                                    return 3
                            else:
                                if features["E(DOWN)"] <= 0.240390:
                                    return 0
                                else:
                                    if features["E(UP) - T(DOWN)"] <= -0.253186:
                                        return 3
                                    else:
                                        if features["agent_row - time_left"] <= 5.600000:
                                            return 0
                                        else:
                                            return 3
                        else:
                            if features["E(DOWN) - T(DOWN)"] <= 0.280923:
                                if features["E(UP) - T(LEFT)"] <= 0.302027:
                                    if features["agent_row - time_left"] <= 1.780000:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    return 3
                            else:
                                if features["T(RIGHT) - agent_row"] <= -4.572051:
                                    return 3
                                else:
                                    return 1
                else:
                    return 2
            else:
                if features["T(LEFT) - agent_row"] <= -1.902892:
                    if features["E(UP) - agent_column"] <= -11.225466:
                        if features["T(LEFT) - time_left"] <= -0.109406:
                            if features["E(RIGHT) - T(DOWN)"] <= 0.516553:
                                return 0
                            else:
                                return 3
                        else:
                            if features["T(DOWN) - agent_row"] <= -8.919919:
                                if features["E(RIGHT) - agent_row"] <= -10.217988:
                                    return 0
                                else:
                                    if features["E(UP) - T(RIGHT)"] <= 0.810988:
                                        return 0
                                    else:
                                        return 3
                            else:
                                return 0
                    else:
                        if features["E(UP) - agent_column"] <= -4.194745:
                            if features["T(RIGHT) - agent_row"] <= -12.538887:
                                return 3
                            else:
                                if features["E(LEFT) - time_left"] <= -0.280000:
                                    return 3
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= 0.500360:
                                        if features["T(RIGHT) - agent_row"] <= -3.958578:
                                            if features["E(RIGHT) - agent_column"] <= -10.280124:
                                                return 0
                                            else:
                                                if features["T(DOWN) - agent_column"] <= -10.736485:
                                                    return 3
                                                else:
                                                    if features["E(UP) - agent_column"] <= -7.457038:
                                                        if features["E(LEFT) - E(RIGHT)"] <= -0.599123:
                                                            if features["E(UP) - agent_column"] <= -8.166124:
                                                                return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["E(RIGHT) - agent_row"] <= -4.400288:
                                                            if features["E(RIGHT) - T(LEFT)"] <= 0.657354:
                                                                return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 0
                        else:
                            if features["E(RIGHT) - agent_row"] <= -7.580481:
                                if features["E(RIGHT) - agent_column"] <= -1.166124:
                                    if features["E(RIGHT) - agent_row"] <= -8.166124:
                                        if features["T(up) - agent_column"] <= -3.607877:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT)"] <= 0.377255:
                                        return 3
                                    else:
                                        return 0
                            else:
                                if features["E(UP)"] <= 0.495034:
                                    if features["T(RIGHT) - agent_row"] <= -6.549781:
                                        if features["E(UP) - agent_column"] <= -2.543862:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.023963:
                                            return 3
                                        else:
                                            return 0
                                else:
                                    if features["E(UP) - agent_row"] <= -3.208409:
                                        return 0
                                    else:
                                        if features["E(UP) - E(DOWN)"] <= 0.719876:
                                            return 3
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= 0.839502:
                                                if features["T(LEFT) - agent_row"] <= -3.855905:
                                                    if features["E(RIGHT) - agent_column"] <= -2.166124:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                            else:
                                                return 3
                else:
                    if features["E(RIGHT) - agent_column"] <= -12.166124:
                        return 0
                    else:
                        if features["E(UP)"] <= 0.799069:
                            return 3
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= 0.524608:
                                if features["T(LEFT) - agent_row"] <= -1.773616:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.547206:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 3
                            else:
                                return 3
        else:
            if features["E(UP) - E(DOWN)"] <= 0.367862:
                if features["E(LEFT) - E(RIGHT)"] <= 0.380634:
                    if features["E(UP) - T(RIGHT)"] <= 0.066876:
                        if features["E(UP) - agent_column"] <= -9.702159:
                            if features["E(DOWN) - E(LEFT)"] <= 0.173422:
                                if features["T(up) - time_left"] <= -0.060000:
                                    if features["E(RIGHT)"] <= 0.017478:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    if features["E(DOWN) - T(RIGHT)"] <= -0.634281:
                                        if features["T(LEFT) - T(RIGHT)"] <= -0.791591:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.028927:
                                            return 2
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= 0.031832:
                                                return 1
                                            else:
                                                if features["T(LEFT)"] <= 0.373426:
                                                    return 2
                                                else:
                                                    if features["T(LEFT)"] <= 0.381395:
                                                        if features["E(RIGHT) - T(DOWN)"] <= -0.286732:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 2
                            else:
                                return 1
                        else:
                            if features["E(DOWN)"] <= 0.371879:
                                if features["T(up) - agent_row"] <= -8.675020:
                                    if features["T(up) - T(LEFT)"] <= 0.234018:
                                        if features["E(UP) - time_left"] <= 0.010614:
                                            return 3
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= 0.064657:
                                                if features["E(DOWN) - T(RIGHT)"] <= -0.143734:
                                                    if features["E(LEFT) - time_left"] <= 0.038004:
                                                        if features["E(LEFT) - T(RIGHT)"] <= -0.185563:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 0
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.240104:
                                            if features["E(DOWN)"] <= 0.022889:
                                                if features["E(RIGHT) - T(up)"] <= -0.056639:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["E(DOWN) - T(up)"] <= -0.568091:
                                                    return 0
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.198426:
                                                        return 1
                                                    else:
                                                        return 2
                                        else:
                                            if features["T(LEFT) - T(RIGHT)"] <= -0.341570:
                                                if features["T(DOWN) - agent_column"] <= -0.909213:
                                                    if features["E(LEFT) - T(RIGHT)"] <= -0.235335:
                                                        if features["E(RIGHT) - agent_column"] <= -3.650333:
                                                            if features["E(RIGHT) - time_left"] <= 0.147285:
                                                                return 2
                                                            else:
                                                                return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 0
                                            else:
                                                if features["E(DOWN) - E(LEFT)"] <= -0.016822:
                                                    if features["E(LEFT) - time_left"] <= 0.100444:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(RIGHT)"] <= 0.344004:
                                                        return 0
                                                    else:
                                                        return 3
                                else:
                                    if features["E(UP)"] <= 0.138374:
                                        if features["E(RIGHT) - T(LEFT)"] <= 0.168856:
                                            return 1
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.016179:
                                                if features["E(RIGHT) - agent_column"] <= -3.667711:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 1
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.305050:
                                            if features["T(up) - agent_row"] <= -8.670113:
                                                if features["T(DOWN) - time_left"] <= 0.069997:
                                                    return 2
                                                else:
                                                    return 3
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.285321:
                                                    if features["E(DOWN)"] <= 0.201200:
                                                        if features["T(up) - agent_row"] <= -8.419347:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["E(DOWN) - T(LEFT)"] <= 0.123875:
                                                            if features["E(UP) - agent_column"] <= -3.222715:
                                                                if features["T(LEFT)"] <= 0.324980:
                                                                    if features["T(up)"] <= 0.211556:
                                                                        if features["E(RIGHT) - time_left"] <= 0.208803:
                                                                            if features["T(up) - T(DOWN)"] <= -0.180096:
                                                                                return 0
                                                                            else:
                                                                                return 2
                                                                        else:
                                                                            return 3
                                                                    else:
                                                                        if features["E(DOWN) - T(LEFT)"] <= 0.030325:
                                                                            if features["T(DOWN) - agent_column"] <= -5.769835:
                                                                                if features["T(RIGHT) - time_left"] <= 0.271373:
                                                                                    return 2
                                                                                else:
                                                                                    return 3
                                                                            else:
                                                                                if features["E(UP) - agent_row"] <= -7.207132:
                                                                                    return 1
                                                                                else:
                                                                                    return 0
                                                                        else:
                                                                            return 2
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["T(DOWN) - time_left"] <= 0.149463:
                                                                    return 2
                                                                else:
                                                                    if features["agent_row - time_left"] <= 7.980000:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                        else:
                                                            if features["E(DOWN) - time_left"] <= -0.103867:
                                                                if features["E(DOWN) - T(LEFT)"] <= 0.283524:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["T(RIGHT) - time_left"] <= 0.390721:
                                                                    if features["E(UP) - T(up)"] <= 0.171336:
                                                                        if features["agent_row - time_left"] <= 6.960000:
                                                                            return 2
                                                                        else:
                                                                            if features["agent_row - time_left"] <= 7.720000:
                                                                                if features["E(LEFT) - T(up)"] <= -0.357018:
                                                                                    return 2
                                                                                else:
                                                                                    return 0
                                                                            else:
                                                                                return 2
                                                                    else:
                                                                        if features["E(RIGHT) - T(DOWN)"] <= 0.369059:
                                                                            return 2
                                                                        else:
                                                                            if features["T(RIGHT) - agent_row"] <= -6.477302:
                                                                                return 0
                                                                            else:
                                                                                if features["E(UP) - T(RIGHT)"] <= -0.178165:
                                                                                    return 1
                                                                                else:
                                                                                    return 2
                                                                else:
                                                                    if features["E(RIGHT) - T(DOWN)"] <= 0.156142:
                                                                        return 3
                                                                    else:
                                                                        if features["E(LEFT) - T(RIGHT)"] <= -0.571450:
                                                                            return 3
                                                                        else:
                                                                            if features["E(RIGHT) - T(DOWN)"] <= 0.276544:
                                                                                return 2
                                                                            else:
                                                                                if features["T(RIGHT) - agent_row"] <= -7.483626:
                                                                                    return 2
                                                                                else:
                                                                                    if features["T(up) - agent_row"] <= -6.345659:
                                                                                        if features["E(RIGHT) - time_left"] <= 0.327200:
                                                                                            return 2
                                                                                        else:
                                                                                            return 3
                                                                                    else:
                                                                                        if features["E(DOWN) - time_left"] <= 0.168415:
                                                                                            return 2
                                                                                        else:
                                                                                            return 1
                                                else:
                                                    if features["E(RIGHT) - time_left"] <= 0.273640:
                                                        if features["E(RIGHT) - agent_row"] <= -3.778738:
                                                            if features["T(up) - agent_row"] <= -4.788444:
                                                                if features["E(LEFT) - T(DOWN)"] <= -0.506954:
                                                                    if features["agent_column"] <= 5.500000:
                                                                        return 3
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    if features["E(LEFT) - T(RIGHT)"] <= 0.029996:
                                                                        if features["E(DOWN) - E(RIGHT)"] <= 0.030529:
                                                                            if features["agent_column - time_left"] <= 3.800000:
                                                                                return 2
                                                                            else:
                                                                                if features["T(LEFT) - time_left"] <= 0.161113:
                                                                                    return 0
                                                                                else:
                                                                                    return 1
                                                                        else:
                                                                            return 2
                                                                    else:
                                                                        return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["T(up) - time_left"] <= 0.124807:
                                                                if features["T(DOWN) - time_left"] <= 0.490299:
                                                                    if features["E(DOWN) - T(DOWN)"] <= -0.140342:
                                                                        return 2
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    return 1
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["E(DOWN) - agent_row"] <= -4.696131:
                                                            if features["T(DOWN) - agent_row"] <= -5.700685:
                                                                return 0
                                                            else:
                                                                if features["E(LEFT) - T(RIGHT)"] <= -0.453577:
                                                                    return 3
                                                                else:
                                                                    return 2
                                                        else:
                                                            if features["E(LEFT) - T(up)"] <= 0.052113:
                                                                if features["T(DOWN) - time_left"] <= 0.290273:
                                                                    return 2
                                                                else:
                                                                    if features["T(DOWN) - agent_column"] <= -5.168888:
                                                                        return 2
                                                                    else:
                                                                        return 3
                                                            else:
                                                                if features["E(LEFT) - T(DOWN)"] <= -0.439865:
                                                                    return 3
                                                                else:
                                                                    return 1
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -7.381499:
                                                return 2
                                            else:
                                                if features["E(DOWN) - T(up)"] <= 0.324980:
                                                    if features["T(RIGHT) - time_left"] <= 0.257527:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                            else:
                                if features["E(LEFT) - T(RIGHT)"] <= -0.244765:
                                    if features["T(LEFT) - T(RIGHT)"] <= -0.331168:
                                        if features["T(RIGHT) - agent_column"] <= -7.190820:
                                            return 2
                                        else:
                                            if features["E(DOWN) - time_left"] <= 0.229957:
                                                if features["T(RIGHT) - agent_column"] <= -4.532329:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.382892:
                                                    return 1
                                                else:
                                                    return 2
                                    else:
                                        return 3
                                else:
                                    if features["T(RIGHT) - time_left"] <= 0.047028:
                                        if features["T(LEFT) - agent_column"] <= -8.560237:
                                            if features["T(LEFT) - time_left"] <= 0.057482:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(LEFT) - time_left"] <= 0.169282:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        if features["E(LEFT) - T(up)"] <= 0.277247:
                                            return 0
                                        else:
                                            return 2
                    else:
                        if features["E(LEFT) - T(LEFT)"] <= 0.280541:
                            if features["T(DOWN) - T(RIGHT)"] <= -0.064657:
                                if features["E(UP)"] <= 0.382892:
                                    if features["E(LEFT) - agent_row"] <= -10.755852:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.204399:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        if features["E(DOWN) - T(LEFT)"] <= -0.182016:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    if features["E(UP) - T(DOWN)"] <= 0.364184:
                                        return 1
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.135581:
                                            return 1
                                        else:
                                            return 3
                            else:
                                if features["E(LEFT) - T(up)"] <= 0.257291:
                                    if features["E(UP) - E(DOWN)"] <= 0.263242:
                                        if features["E(DOWN) - T(up)"] <= -0.219910:
                                            if features["E(LEFT) - time_left"] <= 0.252719:
                                                if features["T(LEFT) - agent_column"] <= -5.446658:
                                                    if features["E(RIGHT) - T(up)"] <= -0.416932:
                                                        if features["E(UP) - E(RIGHT)"] <= 0.148666:
                                                            if features["E(UP) - agent_column"] <= -6.735868:
                                                                return 1
                                                            else:
                                                                return 3
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["E(RIGHT) - T(LEFT)"] <= -0.251848:
                                                            if features["E(LEFT) - agent_row"] <= -5.654619:
                                                                return 3
                                                            else:
                                                                return 1
                                                        else:
                                                            return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["T(LEFT) - agent_row"] <= -10.678112:
                                                    return 3
                                                else:
                                                    if features["E(LEFT) - time_left"] <= 0.294661:
                                                        if features["E(UP) - T(DOWN)"] <= 0.280541:
                                                            if features["E(UP) - T(RIGHT)"] <= 0.223460:
                                                                return 1
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(DOWN) - E(RIGHT)"] <= -0.030325:
                                                                return 0
                                                            else:
                                                                return 2
                                                    else:
                                                        return 2
                                        else:
                                            if features["E(UP) - E(LEFT)"] <= 0.094925:
                                                if features["T(RIGHT) - time_left"] <= 0.101336:
                                                    if features["E(LEFT) - T(LEFT)"] <= 0.240678:
                                                        if features["E(UP) - T(up)"] <= -0.269751:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["E(DOWN) - T(DOWN)"] <= -0.216724:
                                                            return 3
                                                        else:
                                                            return 0
                                                else:
                                                    if features["E(LEFT) - time_left"] <= 0.300634:
                                                        if features["T(RIGHT) - time_left"] <= 0.104807:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(up) - agent_row"] <= -6.736597:
                                                            if features["E(LEFT) - T(RIGHT)"] <= 0.237401:
                                                                if features["agent_row - time_left"] <= 9.980000:
                                                                    if features["E(DOWN) - T(RIGHT)"] <= 0.030918:
                                                                        if features["E(LEFT)"] <= 0.331112:
                                                                            return 0
                                                                        else:
                                                                            return 1
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    if features["E(LEFT) - agent_column"] <= -9.167227:
                                                                        return 2
                                                                    else:
                                                                        return 3
                                                            else:
                                                                return 3
                                                        else:
                                                            return 2
                                            else:
                                                if features["E(UP) - T(up)"] <= 0.277247:
                                                    return 3
                                                else:
                                                    return 0
                                    else:
                                        if features["E(DOWN)"] <= 0.016179:
                                            if features["T(LEFT) - agent_row"] <= -8.658086:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            if features["agent_column - time_left"] <= 10.980000:
                                                if features["E(LEFT) - time_left"] <= 0.150197:
                                                    if features["T(LEFT) - agent_column"] <= -8.595545:
                                                        return 1
                                                    else:
                                                        if features["E(LEFT) - T(LEFT)"] <= 0.138177:
                                                            return 3
                                                        else:
                                                            return 1
                                                else:
                                                    if features["E(LEFT) - T(LEFT)"] <= -0.202040:
                                                        return 0
                                                    else:
                                                        if features["E(LEFT) - T(RIGHT)"] <= 0.260255:
                                                            return 1
                                                        else:
                                                            return 2
                                            else:
                                                if features["E(DOWN) - T(LEFT)"] <= -0.377261:
                                                    return 0
                                                else:
                                                    return 2
                                else:
                                    if features["E(DOWN) - time_left"] <= 0.238727:
                                        if features["E(UP) - time_left"] <= 0.182315:
                                            if features["E(LEFT) - T(DOWN)"] <= -0.091535:
                                                if features["T(LEFT) - agent_column"] <= -7.429378:
                                                    if features["E(LEFT) - agent_column"] <= -10.629955:
                                                        if features["E(DOWN) - time_left"] <= 0.089040:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["E(DOWN) - time_left"] <= 0.029994:
                                                            return 3
                                                        else:
                                                            if features["E(UP) - T(LEFT)"] <= -0.423051:
                                                                if features["E(RIGHT) - agent_row"] <= -4.808249:
                                                                    return 0
                                                                else:
                                                                    return 1
                                                            else:
                                                                if features["E(UP) - time_left"] <= -0.083010:
                                                                    return 0
                                                                else:
                                                                    if features["E(UP) - E(DOWN)"] <= -0.057191:
                                                                        if features["T(DOWN) - agent_row"] <= -4.458931:
                                                                            return 3
                                                                        else:
                                                                            return 0
                                                                    else:
                                                                        return 0
                                                else:
                                                    if features["E(UP) - T(DOWN)"] <= -0.552599:
                                                        return 1
                                                    else:
                                                        return 3
                                            else:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.283524:
                                                    if features["E(RIGHT) - T(DOWN)"] <= -0.358657:
                                                        if features["T(LEFT) - agent_row"] <= -4.505123:
                                                            return 3
                                                        else:
                                                            return 2
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                                        else:
                                            if features["E(RIGHT)"] <= 0.015400:
                                                return 2
                                            else:
                                                if features["E(DOWN) - E(LEFT)"] <= -0.045057:
                                                    if features["E(DOWN) - E(RIGHT)"] <= 0.092162:
                                                        return 0
                                                    else:
                                                        if features["E(DOWN) - T(DOWN)"] <= -0.250435:
                                                            return 0
                                                        else:
                                                            return 3
                                                else:
                                                    return 3
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= -0.230989:
                                            if features["E(DOWN) - T(DOWN)"] <= 0.309607:
                                                if features["E(LEFT) - time_left"] <= 0.279684:
                                                    if features["E(DOWN) - agent_row"] <= -2.620002:
                                                        if features["T(DOWN) - agent_row"] <= -4.275714:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["E(LEFT) - time_left"] <= 0.245219:
                                                            return 3
                                                        else:
                                                            return 1
                                                else:
                                                    if features["T(up) - T(LEFT)"] <= -0.299822:
                                                        if features["E(RIGHT) - T(DOWN)"] <= -0.485907:
                                                            return 2
                                                        else:
                                                            if features["E(DOWN) - E(RIGHT)"] <= 0.148666:
                                                                return 0
                                                            else:
                                                                return 2
                                                    else:
                                                        return 3
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.609414:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -8.850028:
                                                return 2
                                            else:
                                                return 0
                        else:
                            if features["E(UP) - T(up)"] <= 0.276544:
                                if features["E(DOWN) - agent_column"] <= -7.707132:
                                    if features["E(DOWN) - T(up)"] <= -0.627311:
                                        return 0
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= 0.038429:
                                            return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.232643:
                                        if features["E(LEFT) - T(DOWN)"] <= -0.435769:
                                            return 1
                                        else:
                                            if features["agent_row - time_left"] <= 3.820000:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        return 1
                            else:
                                if features["E(LEFT) - time_left"] <= -0.147810:
                                    return 3
                                else:
                                    return 0
                else:
                    if features["E(LEFT) - time_left"] <= 0.336173:
                        if features["T(DOWN) - agent_column"] <= -13.662674:
                            if features["E(DOWN) - E(LEFT)"] <= -0.252227:
                                return 2
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= -0.067495:
                                    return 0
                                else:
                                    return 1
                        else:
                            if features["E(UP) - T(up)"] <= 0.274174:
                                if features["E(UP)"] <= 0.377370:
                                    if features["E(LEFT) - T(up)"] <= 0.428270:
                                        return 2
                                    else:
                                        if features["E(LEFT) - time_left"] <= 0.209445:
                                            if features["E(UP)"] <= 0.198884:
                                                if features["E(UP)"] <= 0.174996:
                                                    if features["E(LEFT) - time_left"] <= -0.087369:
                                                        if features["E(RIGHT) - T(LEFT)"] <= -0.700092:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 2
                                                else:
                                                    return 1
                                            else:
                                                return 2
                                        else:
                                            return 2
                                else:
                                    if features["T(LEFT) - agent_column"] <= -4.415489:
                                        if features["T(DOWN) - T(LEFT)"] <= -0.393206:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 0
                            else:
                                return 0
                    else:
                        if features["E(UP) - T(up)"] <= 0.310884:
                            if features["E(UP) - T(DOWN)"] <= 0.377370:
                                if features["E(DOWN) - T(RIGHT)"] <= 0.286371:
                                    if features["E(LEFT) - T(LEFT)"] <= -0.433894:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= -0.155837:
                                        if features["T(up) - T(DOWN)"] <= -0.109508:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.505524:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.123725:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        return 2
                            else:
                                if features["T(LEFT) - agent_column"] <= -4.834318:
                                    return 2
                                else:
                                    return 0
                        else:
                            return 2
            else:
                if features["E(LEFT) - E(RIGHT)"] <= 0.311758:
                    if features["E(DOWN)"] <= 0.006477:
                        if features["E(LEFT) - T(LEFT)"] <= 0.230707:
                            if features["T(up)"] <= 0.483035:
                                return 0
                            else:
                                if features["E(UP) - time_left"] <= 0.363346:
                                    if features["E(RIGHT) - T(up)"] <= -0.167079:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.038205:
                                            if features["E(UP) - time_left"] <= 0.361291:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= 0.514507:
                                                if features["E(UP) - E(LEFT)"] <= 0.331634:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["E(UP) - T(up)"] <= -0.013189:
                                                    return 0
                                                else:
                                                    if features["agent_row - time_left"] <= 7.820000:
                                                        return 3
                                                    else:
                                                        return 0
                                    else:
                                        if features["E(LEFT) - time_left"] <= -0.019191:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.043134:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 0
                                else:
                                    if features["E(LEFT)"] <= 0.259700:
                                        return 0
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.263655:
                                            return 3
                                        else:
                                            if features["T(LEFT) - agent_row"] <= -6.678193:
                                                return 0
                                            else:
                                                if features["E(DOWN) - T(up)"] <= -0.578728:
                                                    return 0
                                                else:
                                                    return 3
                        else:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.273019:
                                if features["T(DOWN) - time_left"] <= -0.160000:
                                    return 3
                                else:
                                    if features["E(LEFT) - agent_row"] <= -13.707489:
                                        return 0
                                    else:
                                        if features["E(LEFT) - T(up)"] <= -0.092927:
                                            if features["E(UP)"] <= 0.454875:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -8.725804:
                                                return 2
                                            else:
                                                return 0
                            else:
                                return 0
                    else:
                        if features["E(LEFT) - T(DOWN)"] <= 0.187068:
                            return 1
                        else:
                            if features["T(RIGHT) - time_left"] <= 0.366339:
                                if features["T(up) - T(LEFT)"] <= 0.215122:
                                    return 3
                                else:
                                    if features["E(LEFT) - time_left"] <= -0.172951:
                                        return 3
                                    else:
                                        return 1
                            else:
                                return 0
                else:
                    if features["T(DOWN) - agent_row"] <= -0.863734:
                        if features["T(up) - agent_column"] <= -1.902892:
                            if features["E(UP) - agent_row"] <= -10.194745:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.019479:
                                    if features["E(UP) - E(DOWN)"] <= 0.758371:
                                        return 2
                                    else:
                                        if features["T(LEFT) - agent_row"] <= -12.841552:
                                            return 2
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= 0.839502:
                                                return 2
                                            else:
                                                return 0
                                else:
                                    return 0
                            else:
                                if features["E(LEFT) - T(RIGHT)"] <= 0.604239:
                                    if features["T(LEFT) - agent_row"] <= -3.761669:
                                        if features["E(DOWN) - T(DOWN)"] <= -0.447237:
                                            if features["T(DOWN) - T(LEFT)"] <= 0.449481:
                                                return 2
                                            else:
                                                if features["E(RIGHT) - time_left"] <= -0.740000:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["T(DOWN) - T(LEFT)"] <= 0.148666:
                                                if features["E(LEFT) - E(RIGHT)"] <= 0.319601:
                                                    return 3
                                                else:
                                                    if features["E(LEFT) - E(RIGHT)"] <= 0.657354:
                                                        if features["T(RIGHT) - agent_column"] <= -3.837660:
                                                            if features["T(LEFT) - agent_row"] <= -4.541490:
                                                                if features["E(RIGHT) - agent_column"] <= -12.955025:
                                                                    return 0
                                                                else:
                                                                    if features["T(RIGHT) - agent_column"] <= -12.953077:
                                                                        return 2
                                                                    else:
                                                                        if features["T(up) - agent_row"] <= -9.458659:
                                                                            return 2
                                                                        else:
                                                                            if features["E(LEFT) - T(DOWN)"] <= 0.189631:
                                                                                return 2
                                                                            else:
                                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["E(LEFT)"] <= 0.805255:
                                                            return 0
                                                        else:
                                                            if features["T(RIGHT) - time_left"] <= 0.397002:
                                                                return 0
                                                            else:
                                                                return 2
                                            else:
                                                return 0
                                    else:
                                        if features["E(UP) - E(DOWN)"] <= 0.728881:
                                            if features["E(DOWN) - T(up)"] <= -0.153439:
                                                if features["E(UP) - T(up)"] <= 0.482660:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 2
                                        else:
                                            if features["E(UP) - agent_column"] <= -2.252390:
                                                return 0
                                            else:
                                                if features["E(UP) - T(RIGHT)"] <= 0.466227:
                                                    return 2
                                                else:
                                                    return 0
                                else:
                                    if features["agent_row - agent_column"] <= -2.500000:
                                        if features["agent_row - time_left"] <= 2.500000:
                                            if features["E(UP) - E(RIGHT)"] <= 0.767702:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 0
                                    else:
                                        if features["E(UP) - agent_column"] <= -3.269958:
                                            if features["E(LEFT) - T(up)"] <= 0.833876:
                                                if features["E(UP) - T(up)"] <= 0.071715:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                        else:
                                            return 0
                        else:
                            return 0
                    else:
                        if features["E(LEFT) - T(up)"] <= 0.829918:
                            return 2
                        else:
                            if features["T(DOWN) - agent_column"] <= -1.265025:
                                if features["agent_column - time_left"] <= 12.780000:
                                    if features["T(DOWN) - T(RIGHT)"] <= 0.670848:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 0
                            else:
                                return 0


def interpretable_action(evader_probability, teammate_probability, agent_position, time_left, gamma, size, valid_actions):
    input_representation = symbolic_representation(evader_probability, teammate_probability, agent_position, time_left, gamma, size)
    input_combinations   = get_feature_vector(input_representation)
    symbole_to_value     = {name: input_combinations[i] for i, name in enumerate(symbole_names)}
    action               = Index_to_Action[interpretable_strategy(symbole_to_value)]
    if action in valid_actions:
        return action
    else:
        return random.choice(valid_actions)
