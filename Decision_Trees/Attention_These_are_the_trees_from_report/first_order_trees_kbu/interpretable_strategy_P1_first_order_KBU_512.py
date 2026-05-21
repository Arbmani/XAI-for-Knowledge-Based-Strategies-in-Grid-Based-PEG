import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(DOWN)"] <= -0.317568:
        if features["E(DOWN) - E(RIGHT)"] <= 0.034822:
            if features["E(DOWN) - agent_column"] <= -11.265720:
                if features["T(up) - agent_row"] <= -10.456306:
                    if features["E(UP) - E(DOWN)"] <= -0.833876:
                        return 3
                    else:
                        return 1
                else:
                    return 1
            else:
                if features["E(DOWN) - agent_row"] <= -11.208409:
                    if features["E(UP) - E(RIGHT)"] <= -0.833876:
                        if features["T(up) - agent_column"] <= -4.855784:
                            if features["T(RIGHT) - agent_column"] <= -11.464478:
                                return 3
                            else:
                                return 1
                        else:
                            return 3
                    else:
                        return 3
                else:
                    if features["E(DOWN) - agent_row"] <= -3.398903:
                        if features["E(RIGHT) - agent_column"] <= -2.451911:
                            if features["E(RIGHT) - agent_column"] <= -8.341704:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.719876:
                                    if features["E(DOWN) - agent_column"] <= -10.271120:
                                        return 3
                                    else:
                                        if features["agent_row - time_left"] <= 5.930000:
                                            return 3
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -9.160498:
                                                if features["T(RIGHT) - agent_row"] <= -10.941674:
                                                    return 1
                                                else:
                                                    if features["agent_row - time_left"] <= 9.540000:
                                                        return 1
                                                    else:
                                                        return 3
                                            else:
                                                return 3
                                else:
                                    if features["E(RIGHT)"] <= 0.600467:
                                        return 1
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -5.826843:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -9.338459:
                                                return 1
                                            else:
                                                return 3
                            else:
                                if features["T(up) - agent_column"] <= -8.503754:
                                    return 3
                                else:
                                    if features["E(UP) - time_left"] <= -0.130000:
                                        if features["E(RIGHT)"] <= 0.805255:
                                            if features["E(DOWN) - agent_row"] <= -4.505594:
                                                if features["E(RIGHT) - agent_row"] <= -9.338459:
                                                    if features["E(UP) - E(DOWN)"] <= -0.724471:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -5.747023:
                                                if features["T(up) - agent_column"] <= -7.505001:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                    else:
                                        return 3
                        else:
                            if features["E(UP) - E(RIGHT)"] <= -0.422931:
                                if features["T(up) - T(DOWN)"] <= 0.263632:
                                    if features["T(RIGHT) - agent_row"] <= -7.617568:
                                        return 1
                                    else:
                                        if features["E(DOWN) - time_left"] <= 0.721591:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.543017:
                                        return 3
                                    else:
                                        return 1
                            else:
                                return 3
                    else:
                        if features["E(DOWN) - time_left"] <= 0.339673:
                            if features["T(RIGHT) - agent_column"] <= -1.634250:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.209107:
                                    if features["E(LEFT) - E(RIGHT)"] <= -0.498300:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 3
                            else:
                                return 1
                        else:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.542549:
                                if features["E(DOWN) - E(LEFT)"] <= 0.662952:
                                    if features["T(up) - agent_row"] <= -0.965654:
                                        if features["E(DOWN) - E(LEFT)"] <= 0.601097:
                                            if features["E(DOWN) - agent_column"] <= -8.436682:
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
                                if features["E(DOWN) - agent_column"] <= -2.275714:
                                    return 3
                                else:
                                    if features["T(RIGHT) - agent_column"] <= -1.659894:
                                        return 1
                                    else:
                                        return 3
        else:
            if features["E(DOWN) - E(LEFT)"] <= 0.070150:
                if features["E(LEFT) - agent_column"] <= -2.160498:
                    if features["E(LEFT) - agent_row"] <= -11.208409:
                        return 2
                    else:
                        if features["T(DOWN) - agent_column"] <= -11.676896:
                            if features["E(DOWN) - T(LEFT)"] <= -0.067547:
                                return 2
                            else:
                                if features["E(LEFT) - agent_row"] <= -11.160498:
                                    return 2
                                else:
                                    if features["T(DOWN) - T(RIGHT)"] <= 0.371944:
                                        if features["E(DOWN) - T(up)"] <= 0.140060:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.447465:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 1
                                    else:
                                        if features["E(RIGHT) - agent_row"] <= -3.978880:
                                            return 1
                                        else:
                                            if features["T(DOWN) - T(RIGHT)"] <= 0.397352:
                                                return 2
                                            else:
                                                return 1
                        else:
                            if features["E(LEFT) - agent_row"] <= -3.454101:
                                if features["E(LEFT) - T(RIGHT)"] <= 0.662656:
                                    if features["T(DOWN) - agent_column"] <= -3.418061:
                                        if features["E(DOWN) - agent_row"] <= -8.402986:
                                            if features["E(DOWN) - E(RIGHT)"] <= 0.657557:
                                                return 2
                                            else:
                                                if features["agent_row - agent_column"] <= 4.500000:
                                                    if features["E(LEFT)"] <= 0.749843:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    if features["T(RIGHT) - agent_column"] <= -3.522556:
                                                        return 2
                                                    else:
                                                        return 1
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -6.275714:
                                                if features["T(RIGHT) - time_left"] <= -0.270000:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["E(DOWN)"] <= 0.596730:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -7.223281:
                                                        return 1
                                                    else:
                                                        return 2
                                    else:
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.728881:
                                            return 1
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -5.305472:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    return 1
                            else:
                                if features["E(RIGHT) - T(up)"] <= 0.017468:
                                    if features["E(LEFT)"] <= 0.408188:
                                        return 1
                                    else:
                                        if features["T(RIGHT) - agent_column"] <= -10.511095:
                                            if features["E(LEFT) - T(DOWN)"] <= 0.002917:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -2.531039:
                                                if features["E(LEFT) - T(RIGHT)"] <= 0.528867:
                                                    return 2
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -0.166124:
                                                        return 2
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -0.758342:
                                                            return 1
                                                        else:
                                                            return 2
                                            else:
                                                if features["E(UP) - E(LEFT)"] <= -0.719876:
                                                    return 2
                                                else:
                                                    return 1
                                else:
                                    if features["E(RIGHT) - T(up)"] <= 0.068724:
                                        return 0
                                    else:
                                        return 1
                else:
                    if features["T(up) - agent_column"] <= -1.842238:
                        if features["E(LEFT)"] <= 0.743591:
                            return 1
                        else:
                            if features["T(DOWN) - agent_row"] <= -4.844718:
                                if features["T(LEFT) - agent_row"] <= -11.424698:
                                    return 2
                                else:
                                    return 1
                            else:
                                if features["agent_row - agent_column"] <= 0.500000:
                                    if features["E(LEFT) - E(RIGHT)"] <= 0.839502:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 2
                    else:
                        if features["E(LEFT) - agent_row"] <= -12.166124:
                            return 2
                        else:
                            if features["agent_row - agent_column"] <= 11.500000:
                                return 1
                            else:
                                return 2
            else:
                if features["E(UP)"] <= 0.044846:
                    if features["E(RIGHT) - T(RIGHT)"] <= 0.000056:
                        if features["E(LEFT) - T(LEFT)"] <= 0.041396:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.285376:
                                if features["T(up) - T(DOWN)"] <= -0.466655:
                                    if features["E(LEFT) - E(RIGHT)"] <= -0.174657:
                                        if features["T(up) - T(RIGHT)"] <= -0.369727:
                                            if features["E(DOWN) - time_left"] <= 0.319961:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 2
                                    else:
                                        if features["T(DOWN) - agent_row"] <= -2.515692:
                                            if features["E(DOWN) - agent_row"] <= -8.396917:
                                                if features["E(RIGHT) - T(DOWN)"] <= -0.387989:
                                                    return 1
                                                else:
                                                    if features["T(RIGHT) - agent_row"] <= -8.685121:
                                                        if features["agent_column - time_left"] <= 9.770000:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                            else:
                                                return 1
                                        else:
                                            if features["E(UP) - E(LEFT)"] <= -0.238071:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - time_left"] <= 0.183782:
                                                    return 1
                                                else:
                                                    return 3
                                else:
                                    if features["T(up) - agent_row"] <= -12.719791:
                                        return 2
                                    else:
                                        return 1
                            else:
                                if features["E(LEFT)"] <= 0.382149:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["agent_row - time_left"] <= -0.070000:
                                if features["E(LEFT) - T(RIGHT)"] <= -0.255817:
                                    return 1
                                else:
                                    return 2
                            else:
                                return 1
                    else:
                        if features["E(LEFT) - time_left"] <= 0.118007:
                            if features["E(RIGHT) - T(up)"] <= 0.198884:
                                if features["T(up)"] <= 0.450293:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.226883:
                                        if features["E(DOWN) - T(up)"] <= 0.557069:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        return 2
                                else:
                                    return 1
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= -0.294410:
                                    return 1
                                else:
                                    if features["T(DOWN) - T(RIGHT)"] <= 0.123298:
                                        if features["T(RIGHT) - agent_row"] <= -7.650540:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 3
                        else:
                            if features["T(up) - agent_column"] <= -10.832173:
                                if features["E(RIGHT) - T(LEFT)"] <= -0.567933:
                                    return 2
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.088509:
                                        return 1
                                    else:
                                        return 2
                            else:
                                if features["E(DOWN) - T(up)"] <= 0.564106:
                                    if features["T(DOWN) - T(LEFT)"] <= 0.259564:
                                        return 1
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.297585:
                                            return 1
                                        else:
                                            if features["E(LEFT) - agent_row"] <= 0.204923:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.448275:
                                        return 1
                                    else:
                                        return 3
                else:
                    if features["T(up) - agent_row"] <= -0.977111:
                        if features["E(LEFT) - T(LEFT)"] <= 0.197551:
                            if features["E(RIGHT) - T(RIGHT)"] <= 0.233165:
                                if features["T(RIGHT) - time_left"] <= -0.150000:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.245872:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    if features["E(DOWN)"] <= 0.413227:
                                        return 1
                                    else:
                                        return 3
                            else:
                                if features["E(RIGHT) - T(LEFT)"] <= -0.575774:
                                    return 1
                                else:
                                    return 3
                        else:
                            if features["T(RIGHT) - time_left"] <= 0.486887:
                                if features["E(LEFT) - T(DOWN)"] <= -0.105685:
                                    return 0
                                else:
                                    return 2
                            else:
                                return 1
                    else:
                        if features["T(DOWN) - time_left"] <= 0.091273:
                            return 1
                        else:
                            return 0
    else:
        if features["E(LEFT) - E(RIGHT)"] <= 0.365161:
            if features["E(LEFT) - E(RIGHT)"] <= -0.365034:
                if features["E(UP) - E(DOWN)"] <= 0.311758:
                    if features["E(LEFT)"] <= 0.020964:
                        if features["E(DOWN) - T(LEFT)"] <= 0.319262:
                            if features["E(UP) - T(up)"] <= 0.184032:
                                if features["E(DOWN) - T(DOWN)"] <= 0.037414:
                                    if features["E(RIGHT) - time_left"] <= -0.036695:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -3.573954:
                                        return 3
                                    else:
                                        return 1
                            else:
                                if features["T(LEFT) - time_left"] <= -0.170000:
                                    if features["T(DOWN) - time_left"] <= 0.005916:
                                        return 3
                                    else:
                                        if features["T(DOWN) - agent_row"] <= -4.331678:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    if features["E(DOWN) - T(RIGHT)"] <= -0.174892:
                                        if features["T(RIGHT) - agent_row"] <= -11.649624:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 3
                        else:
                            if features["E(UP) - T(up)"] <= 0.155837:
                                if features["agent_row - agent_column"] <= 0.500000:
                                    if features["agent_row - agent_column"] <= -5.500000:
                                        return 1
                                    else:
                                        if features["E(UP) - T(DOWN)"] <= -0.569541:
                                            return 1
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= -0.351870:
                                                if features["E(DOWN) - time_left"] <= 0.260370:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                else:
                                    if features["T(RIGHT) - time_left"] <= 0.373564:
                                        return 3
                                    else:
                                        return 1
                            else:
                                if features["agent_column - time_left"] <= 3.770000:
                                    return 0
                                else:
                                    return 3
                    else:
                        if features["E(RIGHT) - T(LEFT)"] <= 0.370166:
                            return 2
                        else:
                            if features["agent_column - time_left"] <= 0.830000:
                                return 2
                            else:
                                if features["E(UP) - T(up)"] <= 0.199515:
                                    return 3
                                else:
                                    return 0
                else:
                    if features["E(RIGHT) - agent_column"] <= -11.225466:
                        return 0
                    else:
                        if features["T(RIGHT) - agent_row"] <= -1.902892:
                            if features["T(RIGHT) - agent_row"] <= -8.635766:
                                if features["E(UP) - T(up)"] <= -0.020770:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.048984:
                                        return 0
                                    else:
                                        return 1
                                else:
                                    if features["E(UP) - agent_row"] <= -12.578706:
                                        return 3
                                    else:
                                        if features["E(UP) - time_left"] <= 0.295418:
                                            if features["E(UP) - T(up)"] <= 0.000025:
                                                if features["T(LEFT) - T(RIGHT)"] <= -0.464338:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["E(RIGHT) - time_left"] <= -0.220223:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["E(RIGHT) - T(DOWN)"] <= 0.382507:
                                                if features["E(RIGHT) - T(up)"] <= 0.031942:
                                                    return 0
                                                else:
                                                    if features["T(up) - T(RIGHT)"] <= 0.107665:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(UP)"] <= 0.441571:
                                                    return 3
                                                else:
                                                    if features["E(UP) - T(DOWN)"] <= 0.663063:
                                                        if features["E(UP) - agent_column"] <= -9.340798:
                                                            return 0
                                                        else:
                                                            if features["agent_column - time_left"] <= 4.890000:
                                                                return 0
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -10.736485:
                                                            return 3
                                                        else:
                                                            if features["E(UP) - E(LEFT)"] <= 0.839502:
                                                                if features["T(up) - agent_column"] <= -4.460814:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                return 3
                            else:
                                if features["E(UP) - agent_column"] <= -2.454101:
                                    if features["E(RIGHT)"] <= 0.603100:
                                        if features["E(RIGHT) - agent_column"] <= -6.507849:
                                            if features["T(LEFT) - agent_row"] <= -4.329922:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        if features["T(up) - agent_row"] <= -6.156573:
                                            return 3
                                        else:
                                            if features["T(LEFT) - agent_row"] <= -2.794031:
                                                if features["E(UP) - T(DOWN)"] <= 0.636179:
                                                    if features["E(LEFT) - E(RIGHT)"] <= -0.839502:
                                                        return 0
                                                    else:
                                                        if features["T(up) - agent_row"] <= -3.823458:
                                                            return 0
                                                        else:
                                                            if features["E(UP) - E(LEFT)"] <= 0.678974:
                                                                return 3
                                                            else:
                                                                return 0
                                                else:
                                                    return 0
                                            else:
                                                if features["E(RIGHT)"] <= 0.728881:
                                                    return 3
                                                else:
                                                    if features["E(UP) - agent_column"] <= -8.252013:
                                                        if features["E(RIGHT) - T(DOWN)"] <= 0.502184:
                                                            if features["agent_row - agent_column"] <= -9.500000:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            return 3
                                                    else:
                                                        return 0
                                else:
                                    if features["E(UP) - T(LEFT)"] <= 0.407660:
                                        return 3
                                    else:
                                        return 0
                        else:
                            if features["T(LEFT) - agent_row"] <= -1.699793:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.791591:
                                    return 0
                                else:
                                    return 3
                            else:
                                if features["T(up) - agent_column"] <= -11.980521:
                                    return 0
                                else:
                                    return 3
            else:
                if features["E(UP) - E(DOWN)"] <= 0.382014:
                    if features["E(LEFT) - T(DOWN)"] <= 0.066116:
                        if features["E(UP)"] <= 0.211271:
                            if features["E(UP) - E(DOWN)"] <= -0.117575:
                                if features["E(LEFT)"] <= 0.168398:
                                    if features["E(LEFT) - T(RIGHT)"] <= 0.033047:
                                        if features["time_left"] <= 0.070000:
                                            if features["E(UP) - agent_row"] <= -3.926988:
                                                return 3
                                            else:
                                                if features["E(DOWN) - agent_row"] <= -2.655478:
                                                    if features["E(RIGHT) - time_left"] <= 0.354460:
                                                        if features["E(DOWN) - T(LEFT)"] <= 0.264005:
                                                            if features["E(RIGHT) - T(DOWN)"] <= 0.033014:
                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= -0.228033:
                                                if features["E(LEFT) - T(DOWN)"] <= -0.259576:
                                                    return 1
                                                else:
                                                    return 0
                                            else:
                                                if features["E(UP) - agent_row"] <= -3.861822:
                                                    return 3
                                                else:
                                                    if features["E(LEFT) - T(LEFT)"] <= 0.087884:
                                                        return 2
                                                    else:
                                                        return 1
                                    else:
                                        if features["E(UP) - T(DOWN)"] <= -0.692335:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(DOWN)"] <= 0.365281:
                                        if features["E(UP) - T(DOWN)"] <= -0.180096:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.207405:
                                                if features["E(UP) - time_left"] <= 0.104544:
                                                    if features["E(RIGHT)"] <= 0.063100:
                                                        if features["E(LEFT) - agent_column"] <= -11.685003:
                                                            if features["E(LEFT) - T(DOWN)"] <= 0.034598:
                                                                return 2
                                                            else:
                                                                return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["E(RIGHT) - T(up)"] <= 0.063056:
                                                            return 0
                                                        else:
                                                            if features["T(RIGHT) - time_left"] <= -0.150000:
                                                                return 0
                                                            else:
                                                                return 2
                                                else:
                                                    if features["E(DOWN) - T(up)"] <= 0.341778:
                                                        if features["E(RIGHT) - agent_row"] <= -3.747157:
                                                            if features["T(DOWN) - time_left"] <= 0.343022:
                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            return 2
                                                    else:
                                                        return 2
                                            else:
                                                if features["T(LEFT) - agent_column"] <= -5.383520:
                                                    if features["T(LEFT) - agent_row"] <= -4.494479:
                                                        if features["E(LEFT) - T(LEFT)"] <= 0.126641:
                                                            return 3
                                                        else:
                                                            return 2
                                                    else:
                                                        return 0
                                                else:
                                                    return 3
                                        else:
                                            if features["T(DOWN) - time_left"] <= 0.332838:
                                                if features["E(RIGHT) - T(DOWN)"] <= -0.133229:
                                                    if features["agent_column - time_left"] <= 8.930000:
                                                        return 0
                                                    else:
                                                        if features["E(RIGHT)"] <= 0.110125:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    return 0
                                            else:
                                                return 1
                                    else:
                                        if features["E(UP) - T(up)"] <= 0.043121:
                                            return 0
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.211438:
                                                if features["E(RIGHT) - T(RIGHT)"] <= 0.238354:
                                                    if features["T(DOWN) - time_left"] <= 0.364306:
                                                        if features["T(LEFT) - agent_row"] <= -1.550234:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(UP) - T(DOWN)"] <= -0.563729:
                                                        return 1
                                                    else:
                                                        if features["E(LEFT) - T(up)"] <= 0.251336:
                                                            return 3
                                                        else:
                                                            return 0
                                            else:
                                                if features["T(DOWN) - agent_column"] <= -8.621525:
                                                    return 2
                                                else:
                                                    if features["E(LEFT) - T(DOWN)"] <= -0.109222:
                                                        return 0
                                                    else:
                                                        return 2
                            else:
                                if features["T(RIGHT) - agent_row"] <= -4.721649:
                                    if features["E(RIGHT) - T(DOWN)"] <= -0.426494:
                                        if features["E(DOWN) - T(DOWN)"] <= -0.308602:
                                            if features["agent_column - time_left"] <= 9.830000:
                                                return 3
                                            else:
                                                return 2
                                        else:
                                            return 0
                                    else:
                                        if features["E(UP) - E(LEFT)"] <= -0.240425:
                                            return 2
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.262984:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.348708:
                                                    if features["E(LEFT) - time_left"] <= 0.253081:
                                                        if features["E(RIGHT) - time_left"] <= -0.240584:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 0
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                else:
                                    if features["E(UP) - E(RIGHT)"] <= -0.240425:
                                        return 3
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.352667:
                                            if features["T(up) - T(DOWN)"] <= -0.051946:
                                                if features["E(DOWN) - T(up)"] <= 0.114660:
                                                    return 2
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.026598:
                                                        return 2
                                                    else:
                                                        if features["T(DOWN) - time_left"] <= 0.261515:
                                                            if features["E(LEFT) - time_left"] <= 0.032682:
                                                                return 2
                                                            else:
                                                                return 0
                                                        else:
                                                            return 2
                                            else:
                                                return 1
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -2.342646:
                                                if features["E(LEFT) - T(RIGHT)"] <= -0.531057:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["E(DOWN) - T(RIGHT)"] <= -0.106711:
                                                    if features["T(LEFT) - T(RIGHT)"] <= -0.384030:
                                                        if features["E(LEFT) - T(DOWN)"] <= -0.401348:
                                                            if features["E(LEFT) - T(DOWN)"] <= -0.533578:
                                                                return 3
                                                            else:
                                                                return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 2
                                                else:
                                                    return 3
                        else:
                            if features["T(RIGHT)"] <= 0.369490:
                                if features["E(UP) - T(RIGHT)"] <= 0.033601:
                                    if features["E(UP) - time_left"] <= 0.357444:
                                        if features["T(LEFT) - time_left"] <= 0.285050:
                                            return 0
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= 0.015061:
                                                if features["T(RIGHT) - agent_row"] <= -5.254570:
                                                    return 1
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.001142:
                                            return 3
                                        else:
                                            return 0
                                else:
                                    if features["E(DOWN) - agent_column"] <= -7.679686:
                                        if features["T(DOWN) - agent_row"] <= -7.240827:
                                            if features["T(up) - time_left"] <= -0.150000:
                                                return 1
                                            else:
                                                return 0
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.247230:
                                                if features["T(RIGHT) - time_left"] <= 0.204155:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["E(UP) - T(DOWN)"] <= -0.488020:
                                                    return 2
                                                else:
                                                    if features["E(LEFT) - T(DOWN)"] <= -0.086054:
                                                        if features["T(RIGHT) - time_left"] <= -0.150000:
                                                            return 1
                                                        else:
                                                            return 0
                                                    else:
                                                        return 3
                                    else:
                                        if features["E(DOWN) - time_left"] <= 0.031803:
                                            if features["E(RIGHT) - T(LEFT)"] <= 0.299117:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["E(UP) - T(up)"] <= 0.276544:
                                                if features["E(LEFT) - T(LEFT)"] <= 0.213635:
                                                    if features["E(DOWN) - T(LEFT)"] <= -0.062540:
                                                        if features["T(up) - time_left"] <= 0.369487:
                                                            if features["agent_column - time_left"] <= 6.790000:
                                                                if features["agent_column - time_left"] <= 3.970000:
                                                                    if features["agent_row - time_left"] <= 6.870000:
                                                                        return 3
                                                                    else:
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
                                                    return 0
                                            else:
                                                return 0
                            else:
                                if features["E(DOWN)"] <= 0.276544:
                                    if features["E(RIGHT) - T(DOWN)"] <= 0.274515:
                                        if features["E(DOWN) - E(RIGHT)"] <= -0.266805:
                                            return 3
                                        else:
                                            if features["E(UP) - time_left"] <= 0.121175:
                                                return 2
                                            else:
                                                if features["T(RIGHT)"] <= 0.373220:
                                                    return 2
                                                else:
                                                    if features["E(RIGHT) - T(LEFT)"] <= 0.379998:
                                                        if features["E(UP) - E(LEFT)"] <= 0.060198:
                                                            return 2
                                                        else:
                                                            if features["E(RIGHT) - T(DOWN)"] <= 0.178233:
                                                                return 0
                                                            else:
                                                                if features["T(DOWN) - agent_row"] <= -8.817140:
                                                                    return 0
                                                                else:
                                                                    if features["T(up) - time_left"] <= 0.287173:
                                                                        return 2
                                                                    else:
                                                                        return 0
                                                    else:
                                                        return 0
                                    else:
                                        if features["E(DOWN) - T(RIGHT)"] <= -0.371545:
                                            return 3
                                        else:
                                            return 2
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= 0.321035:
                                        if features["E(LEFT) - T(RIGHT)"] <= -0.242014:
                                            if features["T(DOWN) - agent_row"] <= -6.299237:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 0
                                    else:
                                        return 0
                    else:
                        if features["T(DOWN)"] <= 0.112355:
                            if features["E(UP) - T(up)"] <= 0.247230:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.247230:
                                    if features["E(UP) - T(LEFT)"] <= 0.280541:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.016179:
                                            if features["E(UP) - E(DOWN)"] <= 0.299822:
                                                if features["E(LEFT) - time_left"] <= 0.366208:
                                                    if features["E(LEFT) - agent_row"] <= -12.700178:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                        else:
                                            if features["T(LEFT) - agent_row"] <= -12.838320:
                                                if features["T(LEFT) - time_left"] <= 0.136024:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                if features["E(LEFT) - T(DOWN)"] <= 0.346080:
                                                    if features["E(UP) - T(LEFT)"] <= 0.186932:
                                                        if features["E(UP) - T(RIGHT)"] <= 0.300166:
                                                            if features["E(UP) - T(LEFT)"] <= 0.178494:
                                                                return 1
                                                            else:
                                                                if features["T(DOWN) - time_left"] <= 0.060590:
                                                                    return 1
                                                                else:
                                                                    return 0
                                                        else:
                                                            if features["T(up) - agent_column"] <= -7.547879:
                                                                if features["E(UP) - time_left"] <= 0.300846:
                                                                    if features["T(LEFT)"] <= 0.405974:
                                                                        return 1
                                                                    else:
                                                                        if features["E(UP) - E(LEFT)"] <= 0.128047:
                                                                            return 1
                                                                        else:
                                                                            return 3
                                                                else:
                                                                    if features["E(LEFT) - T(LEFT)"] <= -0.109558:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["T(DOWN)"] <= 0.069773:
                                                            if features["T(up) - T(RIGHT)"] <= -0.577671:
                                                                if features["T(RIGHT) - agent_column"] <= -1.361575:
                                                                    return 2
                                                                else:
                                                                    return 3
                                                            else:
                                                                if features["E(UP) - agent_column"] <= -3.775125:
                                                                    if features["T(up) - time_left"] <= 0.326535:
                                                                        if features["E(DOWN) - agent_column"] <= -4.684152:
                                                                            return 2
                                                                        else:
                                                                            return 1
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    if features["E(RIGHT) - T(up)"] <= -0.329010:
                                                                        return 3
                                                                    else:
                                                                        if features["E(DOWN) - T(RIGHT)"] <= -0.165226:
                                                                            return 1
                                                                        else:
                                                                            if features["T(RIGHT) - agent_row"] <= -4.692499:
                                                                                return 3
                                                                            else:
                                                                                return 1
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.199040:
                                                        if features["T(LEFT) - agent_row"] <= -7.505594:
                                                            if features["E(RIGHT) - T(up)"] <= -0.458968:
                                                                return 2
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(RIGHT) - T(LEFT)"] <= -0.558733:
                                                                if features["E(LEFT) - time_left"] <= 0.325281:
                                                                    return 1
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["E(UP) - T(LEFT)"] <= -0.093291:
                                                                    return 1
                                                                else:
                                                                    return 2
                                                    else:
                                                        if features["T(up) - time_left"] <= 0.365993:
                                                            return 3
                                                        else:
                                                            return 2
                                    else:
                                        if features["agent_column - time_left"] <= 8.930000:
                                            if features["T(RIGHT) - agent_column"] <= -4.349346:
                                                if features["T(RIGHT) - time_left"] <= 0.451447:
                                                    if features["E(UP) - E(RIGHT)"] <= 0.185944:
                                                        if features["agent_row - time_left"] <= 12.870000:
                                                            if features["E(DOWN) - time_left"] <= -0.269410:
                                                                return 0
                                                            else:
                                                                return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(RIGHT) - agent_row"] <= -10.921688:
                                                        return 0
                                                    else:
                                                        return 2
                                            else:
                                                if features["agent_row - time_left"] <= 9.890000:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["E(DOWN) - T(DOWN)"] <= 0.015400:
                                                return 0
                                            else:
                                                return 2
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.193121:
                                        if features["E(DOWN) - T(up)"] <= 0.308886:
                                            if features["T(up) - agent_column"] <= -6.503725:
                                                return 1
                                            else:
                                                if features["E(DOWN) - T(LEFT)"] <= 0.314830:
                                                    if features["E(DOWN) - T(up)"] <= -0.525140:
                                                        if features["E(UP) - E(RIGHT)"] <= -0.067287:
                                                            return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                                        else:
                                            if features["E(RIGHT) - time_left"] <= 0.175149:
                                                return 3
                                            else:
                                                if features["agent_row - time_left"] <= 2.950000:
                                                    return 3
                                                else:
                                                    return 1
                                    else:
                                        if features["E(UP) - E(LEFT)"] <= 0.104902:
                                            return 1
                                        else:
                                            if features["T(up) - agent_column"] <= -6.527043:
                                                return 1
                                            else:
                                                return 3
                            else:
                                if features["E(UP) - T(RIGHT)"] <= -0.273785:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.153525:
                                        if features["agent_row - time_left"] <= 8.900000:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -11.664931:
                                            return 3
                                        else:
                                            return 2
                                else:
                                    if features["E(UP) - time_left"] <= 0.230964:
                                        if features["E(DOWN) - E(RIGHT)"] <= 0.030121:
                                            if features["T(LEFT) - time_left"] <= -0.112967:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(RIGHT) - T(LEFT)"] <= -0.408362:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        return 0
                        else:
                            if features["E(LEFT) - T(LEFT)"] <= -0.010479:
                                return 2
                            else:
                                if features["E(LEFT) - agent_column"] <= -11.603653:
                                    if features["T(up) - time_left"] <= 0.330400:
                                        return 3
                                    else:
                                        return 2
                                else:
                                    if features["T(DOWN) - agent_column"] <= -11.739745:
                                        if features["T(up) - time_left"] <= 0.170255:
                                            if features["agent_row - time_left"] <= 7.870000:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["agent_row - time_left"] <= 6.970000:
                                                return 3
                                            else:
                                                return 2
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -10.755852:
                                            if features["E(LEFT) - agent_row"] <= -10.679036:
                                                return 1
                                            else:
                                                if features["E(LEFT) - agent_column"] <= -10.157361:
                                                    return 3
                                                else:
                                                    return 0
                                        else:
                                            if features["T(LEFT) - agent_row"] <= -8.684153:
                                                if features["E(LEFT) - time_left"] <= 0.269670:
                                                    if features["E(RIGHT) - time_left"] <= 0.201238:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                            else:
                                                if features["E(DOWN) - E(LEFT)"] <= -0.092162:
                                                    return 3
                                                else:
                                                    return 0
                else:
                    if features["E(UP) - time_left"] <= 0.263160:
                        if features["E(UP) - E(LEFT)"] <= 0.220946:
                            if features["E(RIGHT) - time_left"] <= -0.300592:
                                return 2
                            else:
                                if features["E(LEFT) - agent_row"] <= -13.689745:
                                    if features["T(LEFT) - time_left"] <= -0.099082:
                                        return 2
                                    else:
                                        if features["agent_column - time_left"] <= 10.750000:
                                            return 3
                                        else:
                                            return 0
                                else:
                                    if features["E(LEFT) - E(RIGHT)"] <= 0.253218:
                                        return 0
                                    else:
                                        return 1
                        else:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.302767:
                                if features["E(UP) - time_left"] <= -0.011403:
                                    if features["T(LEFT) - T(RIGHT)"] <= 0.438146:
                                        if features["E(UP) - agent_row"] <= -10.537309:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 2
                                else:
                                    return 0
                            else:
                                if features["T(RIGHT)"] <= 0.395852:
                                    return 3
                                else:
                                    if features["E(UP) - T(RIGHT)"] <= -0.004942:
                                        return 0
                                    else:
                                        return 2
                    else:
                        if features["E(LEFT) - T(LEFT)"] <= 0.239209:
                            if features["E(UP) - time_left"] <= 0.373477:
                                if features["E(LEFT) - agent_row"] <= -13.726799:
                                    if features["E(DOWN) - E(LEFT)"] <= -0.252227:
                                        return 3
                                    else:
                                        if features["E(UP) - time_left"] <= 0.314418:
                                            if features["E(UP) - T(up)"] <= 0.130247:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 0
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.001643:
                                        return 0
                                    else:
                                        if features["E(UP) - T(DOWN)"] <= 0.518160:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.437634:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 0
                            else:
                                return 0
                        else:
                            if features["E(RIGHT) - T(up)"] <= 0.148681:
                                if features["E(LEFT) - T(up)"] <= -0.476754:
                                    return 0
                                else:
                                    if features["E(LEFT) - T(DOWN)"] <= 0.259700:
                                        if features["E(LEFT)"] <= 0.241681:
                                            return 2
                                        else:
                                            if features["T(up) - agent_row"] <= -12.453450:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.686223:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.214253:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 0
                            else:
                                return 0
        else:
            if features["E(UP) - E(LEFT)"] <= -0.074155:
                if features["E(RIGHT)"] <= 0.006477:
                    if features["E(UP) - T(up)"] <= 0.014517:
                        if features["E(DOWN) - time_left"] <= 0.326535:
                            if features["E(LEFT) - time_left"] <= 0.203985:
                                if features["T(DOWN) - agent_column"] <= -12.585855:
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
                                return 2
                            else:
                                if features["T(LEFT) - agent_column"] <= -13.548040:
                                    return 1
                                else:
                                    return 2
                        else:
                            if features["E(LEFT) - time_left"] <= 0.242555:
                                if features["E(UP) - agent_row"] <= -8.732239:
                                    return 2
                                else:
                                    if features["agent_row - time_left"] <= 8.570000:
                                        return 1
                                    else:
                                        return 3
                            else:
                                if features["T(DOWN) - time_left"] <= 0.476580:
                                    if features["E(DOWN) - T(LEFT)"] <= -0.620076:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(LEFT) - agent_column"] <= -9.208409:
                                        return 0
                                    else:
                                        return 2
                else:
                    if features["E(RIGHT) - T(RIGHT)"] <= 0.014700:
                        return 3
                    else:
                        if features["E(UP) - T(up)"] <= 0.198643:
                            if features["E(UP) - T(up)"] <= -0.313144:
                                return 2
                            else:
                                return 1
                        else:
                            return 3
            else:
                if features["agent_row - time_left"] <= 1.190000:
                    return 2
                else:
                    if features["T(RIGHT) - agent_column"] <= -1.863260:
                        if features["E(LEFT) - T(DOWN)"] <= 0.576111:
                            if features["T(RIGHT) - agent_row"] <= -2.898553:
                                if features["E(UP) - T(RIGHT)"] <= 0.608535:
                                    if features["E(LEFT) - T(RIGHT)"] <= 0.230717:
                                        if features["T(up) - T(LEFT)"] <= -0.015061:
                                            return 2
                                        else:
                                            if features["T(up) - agent_column"] <= -4.918152:
                                                return 0
                                            else:
                                                if features["E(LEFT) - T(up)"] <= 0.728881:
                                                    return 0
                                                else:
                                                    return 2
                                    else:
                                        if features["T(up) - agent_column"] <= -13.627703:
                                            if features["E(LEFT) - time_left"] <= 0.325055:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(UP) - T(DOWN)"] <= 0.213000:
                                                return 2
                                            else:
                                                if features["E(UP) - agent_row"] <= -10.606121:
                                                    if features["E(LEFT) - T(LEFT)"] <= -0.041308:
                                                        return 0
                                                    else:
                                                        if features["E(UP) - agent_column"] <= -5.340798:
                                                            return 2
                                                        else:
                                                            return 0
                                                else:
                                                    if features["agent_column - time_left"] <= 10.850000:
                                                        if features["E(RIGHT) - T(LEFT)"] <= -0.131069:
                                                            return 2
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["E(LEFT) - T(LEFT)"] <= -0.000085:
                                                            return 2
                                                        else:
                                                            return 0
                                else:
                                    return 0
                            else:
                                if features["E(UP)"] <= 0.664454:
                                    return 2
                                else:
                                    if features["T(LEFT) - agent_column"] <= -7.870563:
                                        return 0
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -1.208409:
                                            if features["T(up) - agent_row"] <= -2.863524:
                                                if features["E(UP) - agent_column"] <= -3.208409:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 2
                                        else:
                                            return 0
                        else:
                            if features["T(LEFT) - agent_row"] <= -8.286422:
                                if features["T(RIGHT) - agent_row"] <= -13.701958:
                                    return 2
                                else:
                                    if features["E(UP)"] <= 0.805255:
                                        if features["T(RIGHT) - agent_row"] <= -12.714536:
                                            if features["T(LEFT) - agent_column"] <= -3.825466:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                                    else:
                                        if features["agent_row - agent_column"] <= 2.500000:
                                            return 2
                                        else:
                                            if features["agent_row - agent_column"] <= 3.500000:
                                                return 0
                                            else:
                                                return 2
                            else:
                                if features["E(LEFT) - T(LEFT)"] <= 0.839502:
                                    return 0
                                else:
                                    return 2
                    else:
                        if features["E(UP) - E(RIGHT)"] <= 0.799069:
                            return 0
                        else:
                            if features["E(LEFT) - agent_column"] <= -1.160498:
                                return 2
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
