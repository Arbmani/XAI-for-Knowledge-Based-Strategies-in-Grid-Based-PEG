import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(DOWN) - E(LEFT)"] <= 0.000000:
        if features["E(UP) - E(LEFT)"] <= -0.260686:
            if features["E(DOWN)"] <= 0.168356:
                return 2
            else:
                if features["E(RIGHT)"] <= 0.000019:
                    if features["E(LEFT) - E(RIGHT)"] <= 0.800671:
                        if features["E(RIGHT) - T(RIGHT)"] <= -0.000000:
                            return 2
                        else:
                            if features["T(LEFT) - time_left"] <= 0.302956:
                                return 1
                            else:
                                return 2
                    else:
                        if features["E(RIGHT)"] <= 0.000001:
                            return 1
                        else:
                            if features["T(up) - agent_column"] <= -1.999919:
                                return 2
                            else:
                                return 1
                else:
                    if features["E(DOWN)"] <= 0.380153:
                        if features["E(RIGHT) - time_left"] <= -0.046396:
                            return 2
                        else:
                            if features["T(up) - T(RIGHT)"] <= 0.026356:
                                return 2
                            else:
                                return 0
                    else:
                        if features["E(RIGHT)"] <= 0.014386:
                            if features["E(UP) - agent_column"] <= -1.999941:
                                return 2
                            else:
                                if features["T(up) - agent_row"] <= -10.934025:
                                    return 2
                                else:
                                    return 1
                        else:
                            return 1
        else:
            if features["E(UP) - E(LEFT)"] <= 0.000086:
                if features["E(LEFT)"] <= 0.439617:
                    if features["E(RIGHT) - T(DOWN)"] <= 0.050824:
                        if features["E(RIGHT)"] <= 0.001363:
                            if features["E(DOWN) - T(up)"] <= 0.149730:
                                if features["E(RIGHT) - T(RIGHT)"] <= -0.000000:
                                    return 2
                                else:
                                    if features["E(UP) - T(LEFT)"] <= -0.049954:
                                        if features["T(up) - time_left"] <= 0.234357:
                                            if features["agent_row - time_left"] <= 5.880000:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                                    else:
                                        if features["E(DOWN) - T(up)"] <= -0.387208:
                                            return 2
                                        else:
                                            return 0
                            else:
                                if features["E(RIGHT) - T(LEFT)"] <= -0.378711:
                                    return 2
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -8.999627:
                                        return 2
                                    else:
                                        return 1
                        else:
                            if features["E(UP) - time_left"] <= 0.033819:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.076570:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.532199:
                                        return 2
                                    else:
                                        if features["T(DOWN) - T(LEFT)"] <= 0.004450:
                                            if features["T(DOWN) - agent_row"] <= -3.865717:
                                                if features["E(DOWN) - T(up)"] <= 0.150114:
                                                    if features["E(DOWN) - agent_row"] <= -5.868376:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 1
                                            else:
                                                return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(DOWN) - agent_row"] <= -2.763800:
                                        if features["E(LEFT) - agent_row"] <= -7.751307:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 0
                            else:
                                if features["E(DOWN) - T(up)"] <= 0.172129:
                                    if features["E(RIGHT) - T(up)"] <= -0.309011:
                                        if features["T(DOWN) - agent_column"] <= -11.947303:
                                            if features["T(LEFT) - time_left"] <= 0.349207:
                                                return 0
                                            else:
                                                if features["E(RIGHT)"] <= 0.006766:
                                                    if features["T(RIGHT) - time_left"] <= -0.028067:
                                                        if features["E(DOWN) - T(DOWN)"] <= 0.046082:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                                        else:
                                            return 2
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.189051:
                                            return 0
                                        else:
                                            if features["T(LEFT) - time_left"] <= 0.218291:
                                                return 0
                                            else:
                                                return 3
                                else:
                                    if features["T(RIGHT)"] <= 0.000000:
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.401396:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["T(up)"] <= 0.121059:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.324481:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 3
                    else:
                        if features["E(DOWN) - T(DOWN)"] <= 0.245385:
                            if features["E(UP) - T(LEFT)"] <= 0.236173:
                                if features["E(UP) - E(RIGHT)"] <= 0.158625:
                                    return 3
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.288131:
                                        return 3
                                    else:
                                        return 0
                            else:
                                return 2
                        else:
                            if features["T(RIGHT) - agent_row"] <= -8.999946:
                                return 3
                            else:
                                if features["E(UP) - agent_column"] <= -8.755359:
                                    return 1
                                else:
                                    return 2
                else:
                    if features["E(RIGHT)"] <= 0.000002:
                        if features["E(UP) - T(RIGHT)"] <= 0.799589:
                            if features["E(UP) - E(LEFT)"] <= 0.000001:
                                return 2
                            else:
                                if features["agent_row - agent_column"] <= 1.500000:
                                    return 0
                                else:
                                    return 2
                        else:
                            return 0
                    else:
                        if features["E(DOWN) - agent_row"] <= -0.999999:
                            if features["E(DOWN) - agent_column"] <= -10.930734:
                                if features["E(UP) - T(DOWN)"] <= -0.023180:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(UP) - E(DOWN)"] <= 0.678226:
                                    return 2
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -9.999569:
                                        return 2
                                    else:
                                        return 0
                        else:
                            return 2
            else:
                if features["E(UP) - E(RIGHT)"] <= 0.115772:
                    if features["E(DOWN) - T(DOWN)"] <= 0.057928:
                        if features["E(DOWN) - agent_row"] <= -2.000000:
                            if features["E(UP) - E(RIGHT)"] <= -0.000001:
                                if features["E(LEFT)"] <= 0.106141:
                                    if features["T(RIGHT) - agent_row"] <= -12.623340:
                                        if features["E(RIGHT) - agent_column"] <= 0.351991:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 0
                                else:
                                    return 0
                            else:
                                if features["E(DOWN) - T(LEFT)"] <= 0.000004:
                                    if features["E(UP) - E(DOWN)"] <= 0.800943:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.000120:
                                            if features["E(LEFT)"] <= 0.285972:
                                                if features["T(LEFT) - time_left"] <= 0.052103:
                                                    if features["E(DOWN) - E(RIGHT)"] <= -0.275448:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                            else:
                                                if features["agent_row - time_left"] <= 6.940000:
                                                    return 0
                                                else:
                                                    return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                                else:
                                    if features["T(LEFT)"] <= 0.076646:
                                        if features["E(DOWN)"] <= 0.084911:
                                            if features["E(DOWN) - agent_row"] <= -7.985453:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                        else:
                            if features["E(UP) - E(RIGHT)"] <= 0.022865:
                                return 3
                            else:
                                return 0
                    else:
                        if features["E(LEFT) - agent_column"] <= -6.747890:
                            return 3
                        else:
                            if features["E(DOWN) - T(LEFT)"] <= 0.141180:
                                if features["T(up) - agent_row"] <= -8.594569:
                                    if features["T(DOWN)"] <= 0.000000:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 3
                            else:
                                if features["T(DOWN) - T(LEFT)"] <= 0.000000:
                                    return 3
                                else:
                                    if features["T(up) - agent_row"] <= -8.619022:
                                        return 0
                                    else:
                                        return 2
                else:
                    if features["E(LEFT) - E(RIGHT)"] <= 0.671679:
                        if features["E(DOWN) - T(DOWN)"] <= 0.052365:
                            if features["E(UP) - time_left"] <= 0.234948:
                                return 0
                            else:
                                if features["E(RIGHT)"] <= 0.338931:
                                    if features["E(DOWN) - E(RIGHT)"] <= 0.003055:
                                        return 0
                                    else:
                                        return 1
                                else:
                                    return 0
                        else:
                            if features["E(UP) - time_left"] <= 0.320537:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.120299:
                                    return 0
                                else:
                                    return 3
                            else:
                                return 0
                    else:
                        if features["E(DOWN) - agent_row"] <= -1.999910:
                            if features["E(UP) - E(DOWN)"] <= 0.800589:
                                return 0
                            else:
                                if features["T(up) - T(LEFT)"] <= -0.000000:
                                    return 0
                                else:
                                    return 2
                        else:
                            if features["E(DOWN) - agent_row"] <= -0.999997:
                                return 0
                            else:
                                return 2
    else:
        if features["E(DOWN) - E(RIGHT)"] <= 0.000011:
            if features["E(UP) - E(RIGHT)"] <= -0.136316:
                if features["E(DOWN) - E(RIGHT)"] <= -0.171920:
                    if features["E(DOWN) - time_left"] <= -0.719493:
                        return 0
                    else:
                        return 3
                else:
                    if features["E(DOWN) - agent_column"] <= -11.215729:
                        if features["T(RIGHT) - agent_row"] <= -3.268605:
                            if features["E(UP) - agent_column"] <= -12.999946:
                                return 1
                            else:
                                return 3
                        else:
                            return 1
                    else:
                        if features["E(LEFT) - agent_column"] <= -1.933603:
                            if features["E(LEFT) - time_left"] <= 0.104123:
                                if features["T(LEFT)"] <= 0.000005:
                                    if features["T(DOWN) - T(RIGHT)"] <= -0.000008:
                                        if features["E(LEFT) - T(RIGHT)"] <= -0.439394:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT)"] <= 0.347567:
                                        if features["E(RIGHT) - agent_row"] <= -4.654235:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                            else:
                                if features["T(up) - T(LEFT)"] <= 0.025948:
                                    return 1
                                else:
                                    return 2
                        else:
                            if features["E(RIGHT) - agent_row"] <= -3.591678:
                                if features["E(LEFT) - agent_row"] <= -5.898325:
                                    if features["E(RIGHT) - T(DOWN)"] <= 0.152959:
                                        return 3
                                    else:
                                        if features["E(LEFT) - T(up)"] <= -0.311921:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["T(DOWN) - T(RIGHT)"] <= -0.000035:
                                        if features["T(LEFT) - agent_row"] <= -3.970291:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        return 3
                            else:
                                if features["E(LEFT) - T(up)"] <= -0.001545:
                                    return 3
                                else:
                                    if features["E(UP) - E(LEFT)"] <= 0.016856:
                                        if features["E(LEFT) - T(LEFT)"] <= -0.000000:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 3
            else:
                if features["E(LEFT) - agent_column"] <= -4.926052:
                    if features["E(RIGHT) - agent_column"] <= -11.200390:
                        if features["E(UP) - agent_row"] <= -6.370381:
                            return 3
                        else:
                            return 0
                    else:
                        if features["E(DOWN) - T(DOWN)"] <= 0.134967:
                            if features["E(RIGHT)"] <= 0.300125:
                                if features["T(RIGHT) - agent_column"] <= -7.999988:
                                    return 3
                                else:
                                    return 0
                            else:
                                return 3
                        else:
                            return 3
                else:
                    if features["E(LEFT) - E(RIGHT)"] <= -0.242261:
                        if features["E(LEFT) - agent_column"] <= -0.976496:
                            if features["E(LEFT) - T(up)"] <= 0.085820:
                                if features["E(UP) - T(DOWN)"] <= 0.354790:
                                    if features["E(DOWN) - time_left"] <= 0.194877:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 3
                            else:
                                if features["T(LEFT) - agent_column"] <= -4.000000:
                                    return 0
                                else:
                                    return 3
                        else:
                            if features["E(UP) - time_left"] <= 0.274267:
                                if features["E(DOWN) - agent_column"] <= -0.865018:
                                    return 0
                                else:
                                    return 3
                            else:
                                if features["T(up) - time_left"] <= 0.323326:
                                    if features["E(RIGHT) - T(up)"] <= 0.062674:
                                        return 0
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -9.878860:
                                            if features["T(LEFT) - time_left"] <= 0.003139:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 0
                                else:
                                    return 3
                    else:
                        if features["E(RIGHT) - T(LEFT)"] <= 0.237497:
                            if features["E(DOWN) - T(RIGHT)"] <= 0.002347:
                                if features["T(RIGHT) - agent_column"] <= -3.656336:
                                    return 0
                                else:
                                    if features["T(RIGHT) - agent_column"] <= -3.651851:
                                        return 3
                                    else:
                                        return 0
                            else:
                                return 3
                        else:
                            if features["E(LEFT) - agent_column"] <= -3.852197:
                                if features["T(up) - T(RIGHT)"] <= -0.000012:
                                    if features["E(LEFT) - T(DOWN)"] <= 0.159259:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 3
                            else:
                                if features["T(up) - agent_row"] <= -8.645368:
                                    return 3
                                else:
                                    if features["E(RIGHT)"] <= 0.332338:
                                        return 2
                                    else:
                                        return 1
        else:
            if features["E(DOWN) - E(RIGHT)"] <= 0.189079:
                if features["E(UP) - E(DOWN)"] <= -0.330230:
                    if features["E(UP) - E(DOWN)"] <= -0.800575:
                        if features["E(UP) - T(LEFT)"] <= -0.000001:
                            return 3
                        else:
                            return 1
                    else:
                        if features["E(UP)"] <= 0.000001:
                            return 1
                        else:
                            if features["E(DOWN) - E(RIGHT)"] <= 0.069085:
                                if features["T(LEFT) - agent_column"] <= -1.974769:
                                    if features["E(RIGHT) - agent_column"] <= -10.322656:
                                        return 1
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -1.999949:
                                            if features["T(up) - agent_row"] <= -10.999999:
                                                return 3
                                            else:
                                                if features["E(LEFT) - T(DOWN)"] <= -0.314080:
                                                    return 3
                                                else:
                                                    return 1
                                        else:
                                            return 3
                                else:
                                    return 1
                            else:
                                if features["E(UP) - T(RIGHT)"] <= 0.044665:
                                    if features["E(UP) - agent_row"] <= -1.976273:
                                        if features["T(up) - agent_row"] <= -9.943312:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(UP) - T(up)"] <= 0.001294:
                                            return 1
                                        else:
                                            if features["T(up)"] <= 0.020305:
                                                return 1
                                            else:
                                                if features["T(RIGHT) - agent_column"] <= -6.718724:
                                                    return 1
                                                else:
                                                    return 3
                                else:
                                    if features["E(DOWN) - agent_row"] <= -8.507362:
                                        return 3
                                    else:
                                        return 1
                else:
                    if features["E(UP) - agent_row"] <= -3.855874:
                        if features["T(LEFT)"] <= 0.000270:
                            if features["T(DOWN) - agent_row"] <= -9.000000:
                                return 3
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.287195:
                                    if features["T(DOWN) - T(RIGHT)"] <= -0.000013:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 1
                        else:
                            if features["E(DOWN) - E(RIGHT)"] <= 0.088270:
                                if features["T(up)"] <= 0.000000:
                                    return 0
                                else:
                                    if features["T(up) - time_left"] <= 0.412518:
                                        if features["E(UP) - time_left"] <= 0.196141:
                                            if features["E(UP) - T(up)"] <= 0.008921:
                                                return 3
                                            else:
                                                if features["E(LEFT) - T(LEFT)"] <= -0.274393:
                                                    return 3
                                                else:
                                                    return 1
                                        else:
                                            if features["E(RIGHT) - T(DOWN)"] <= 0.003434:
                                                return 0
                                            else:
                                                return 3
                                    else:
                                        return 1
                            else:
                                if features["T(RIGHT) - agent_row"] <= -8.999758:
                                    return 3
                                else:
                                    if features["T(up) - T(RIGHT)"] <= 0.000181:
                                        if features["E(UP) - T(up)"] <= 0.009034:
                                            if features["T(LEFT) - agent_row"] <= -4.723070:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 1
                                    else:
                                        return 1
                    else:
                        if features["E(UP) - E(RIGHT)"] <= -0.127499:
                            if features["T(DOWN) - T(LEFT)"] <= 0.207027:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.312031:
                                    return 1
                                else:
                                    return 3
                            else:
                                if features["T(LEFT)"] <= 0.000000:
                                    return 1
                                else:
                                    return 3
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= 0.003983:
                                if features["E(LEFT) - time_left"] <= 0.164711:
                                    return 0
                                else:
                                    return 1
                            else:
                                if features["E(UP) - T(LEFT)"] <= -0.371866:
                                    return 0
                                else:
                                    if features["E(UP) - time_left"] <= -0.098696:
                                        return 1
                                    else:
                                        return 0
            else:
                if features["E(LEFT)"] <= 0.728946:
                    if features["E(UP) - time_left"] <= -0.002634:
                        if features["E(UP) - T(RIGHT)"] <= 0.000149:
                            if features["E(DOWN) - E(LEFT)"] <= 0.097334:
                                if features["E(UP)"] <= 0.000016:
                                    return 1
                                else:
                                    if features["E(UP) - E(RIGHT)"] <= -0.008535:
                                        if features["T(up) - agent_row"] <= -0.982148:
                                            if features["T(DOWN) - agent_row"] <= -8.533792:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -11.960259:
                                                    return 3
                                                else:
                                                    return 1
                                        else:
                                            return 2
                                    else:
                                        if features["T(LEFT) - agent_row"] <= -1.695209:
                                            return 1
                                        else:
                                            if features["agent_row - agent_column"] <= -11.500000:
                                                return 1
                                            else:
                                                return 2
                            else:
                                return 1
                        else:
                            if features["agent_row - agent_column"] <= -9.500000:
                                if features["E(DOWN) - T(LEFT)"] <= 0.005029:
                                    if features["T(LEFT) - time_left"] <= 0.212379:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    return 1
                            else:
                                if features["E(DOWN) - agent_row"] <= -8.517423:
                                    if features["E(UP) - T(RIGHT)"] <= 0.045346:
                                        return 1
                                    else:
                                        if features["T(DOWN) - T(RIGHT)"] <= -0.000004:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= 0.000012:
                                        return 1
                                    else:
                                        if features["E(UP) - E(DOWN)"] <= -0.342761:
                                            return 1
                                        else:
                                            return 0
                    else:
                        if features["T(DOWN) - T(RIGHT)"] <= 0.188414:
                            return 1
                        else:
                            if features["T(up) - time_left"] <= -0.002796:
                                if features["T(LEFT) - agent_column"] <= -9.847864:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 0
                else:
                    if features["E(RIGHT) - agent_row"] <= -1.999986:
                        if features["E(DOWN) - agent_row"] <= -11.213543:
                            return 2
                        else:
                            if features["E(UP) - agent_row"] <= -7.000000:
                                return 1
                            else:
                                if features["E(RIGHT) - agent_column"] <= -1.999997:
                                    if features["E(RIGHT) - agent_column"] <= -10.999999:
                                        return 1
                                    else:
                                        if features["E(UP)"] <= 0.000000:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    return 1
                    else:
                        if features["E(UP) - agent_column"] <= -1.999129:
                            return 2
                        else:
                            return 1


def interpretable_action(evader_probability, teammate_probability, agent_position, time_left, gamma, size, valid_actions):
    input_representation = symbolic_representation(evader_probability, teammate_probability, agent_position, time_left, gamma, size)
    input_combinations   = get_feature_vector(input_representation)
    symbole_to_value     = {name: input_combinations[i] for i, name in enumerate(symbole_names)}
    action               = Index_to_Action[interpretable_strategy(symbole_to_value)]
    if action in valid_actions:
        return action
    else:
        return random.choice(valid_actions)
