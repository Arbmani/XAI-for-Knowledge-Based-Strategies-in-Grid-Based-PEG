import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(DOWN)"] <= -0.365161:
        if features["E(LEFT) - E(RIGHT)"] <= -0.354796:
            if features["E(RIGHT) - agent_row"] <= -11.208409:
                if features["E(LEFT) - E(RIGHT)"] <= -0.833876:
                    if features["T(up) - agent_column"] <= -4.855784:
                        if features["agent_column - time_left"] <= 11.510000:
                            return 1
                        else:
                            return 3
                    else:
                        return 3
                else:
                    return 3
            else:
                if features["E(RIGHT) - agent_row"] <= -3.398418:
                    if features["E(DOWN) - agent_column"] <= -11.265720:
                        if features["E(DOWN) - T(RIGHT)"] <= 0.823190:
                            return 1
                        else:
                            if features["T(up) - agent_row"] <= -9.853469:
                                return 3
                            else:
                                return 1
                    else:
                        if features["E(DOWN) - agent_row"] <= -8.400748:
                            if features["E(UP) - E(RIGHT)"] <= -0.622747:
                                if features["T(up) - agent_column"] <= -3.558817:
                                    if features["E(LEFT) - E(RIGHT)"] <= -0.805255:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                return 3
                        else:
                            if features["E(RIGHT) - T(up)"] <= 0.619138:
                                if features["E(DOWN) - agent_column"] <= -8.401045:
                                    if features["E(DOWN)"] <= 0.661541:
                                        return 1
                                    else:
                                        if features["agent_row - time_left"] <= 5.930000:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["T(up) - agent_row"] <= -5.774064:
                                        if features["E(DOWN)"] <= 0.445902:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 1
                            else:
                                return 3
                else:
                    if features["E(DOWN) - agent_column"] <= -11.360327:
                        return 1
                    else:
                        if features["E(UP) - E(DOWN)"] <= -0.448825:
                            if features["E(DOWN) - agent_column"] <= -2.275714:
                                return 3
                            else:
                                return 1
                        else:
                            return 1
        else:
            if features["E(LEFT) - E(RIGHT)"] <= 0.285376:
                if features["E(UP)"] <= 0.020964:
                    if features["E(RIGHT) - T(RIGHT)"] <= 0.000091:
                        if features["agent_row - time_left"] <= -0.170000:
                            if features["E(LEFT) - T(DOWN)"] <= -0.255762:
                                return 1
                            else:
                                return 2
                        else:
                            if features["E(RIGHT) - T(up)"] <= 0.345813:
                                if features["T(LEFT) - time_left"] <= -0.680000:
                                    return 3
                                else:
                                    return 1
                            else:
                                if features["E(RIGHT) - time_left"] <= 0.258809:
                                    if features["T(DOWN) - agent_row"] <= -5.547467:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    return 1
                    else:
                        if features["E(RIGHT) - T(up)"] <= 0.214253:
                            if features["T(DOWN) - T(LEFT)"] <= 0.259564:
                                if features["E(LEFT) - T(up)"] <= 0.313361:
                                    return 1
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.570639:
                                        return 2
                                    else:
                                        return 1
                            else:
                                return 1
                        else:
                            if features["T(RIGHT) - time_left"] <= -0.190000:
                                return 3
                            else:
                                return 1
                else:
                    if features["T(DOWN) - T(LEFT)"] <= 0.079379:
                        return 3
                    else:
                        return 0
            else:
                if features["T(up) - agent_column"] <= -2.322311:
                    if features["E(DOWN) - agent_row"] <= -11.208409:
                        return 2
                    else:
                        if features["T(RIGHT) - agent_column"] <= -10.897089:
                            if features["E(DOWN) - T(LEFT)"] <= 0.000145:
                                return 2
                            else:
                                if features["E(RIGHT) - time_left"] <= -0.716859:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["E(LEFT) - agent_row"] <= -3.454101:
                                if features["T(DOWN) - agent_column"] <= -3.464172:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.656929:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(LEFT)"] <= 0.728881:
                                        return 1
                                    else:
                                        if features["T(DOWN) - agent_row"] <= -4.854016:
                                            return 1
                                        else:
                                            return 2
                            else:
                                if features["E(LEFT)"] <= 0.415763:
                                    return 1
                                else:
                                    return 2
                else:
                    if features["E(DOWN) - agent_row"] <= -3.243484:
                        if features["E(DOWN) - agent_row"] <= -12.166124:
                            return 2
                        else:
                            return 1
                    else:
                        return 1
    else:
        if features["E(LEFT) - E(RIGHT)"] <= 0.364744:
            if features["E(LEFT) - E(RIGHT)"] <= -0.365161:
                if features["E(UP) - E(DOWN)"] <= 0.311758:
                    if features["E(DOWN) - T(up)"] <= 0.162546:
                        if features["E(LEFT)"] <= 0.028057:
                            if features["E(DOWN) - T(DOWN)"] <= 0.018016:
                                if features["T(LEFT) - time_left"] <= -0.840000:
                                    return 1
                                else:
                                    return 3
                            else:
                                return 3
                        else:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.370166:
                                return 2
                            else:
                                return 3
                    else:
                        if features["E(UP) - T(LEFT)"] <= 0.180651:
                            if features["T(RIGHT) - agent_row"] <= -2.578191:
                                return 3
                            else:
                                if features["T(DOWN) - T(RIGHT)"] <= -0.072204:
                                    if features["E(LEFT) - T(DOWN)"] <= -0.331634:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    if features["E(RIGHT) - T(DOWN)"] <= -0.199163:
                                        return 1
                                    else:
                                        if features["T(up) - agent_row"] <= -0.961795:
                                            return 3
                                        else:
                                            return 1
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.279949:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.421953:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.423691:
                                    return 0
                                else:
                                    return 3
                else:
                    if features["E(RIGHT) - agent_column"] <= -11.225466:
                        return 0
                    else:
                        if features["T(RIGHT) - agent_row"] <= -1.902892:
                            if features["T(RIGHT) - agent_row"] <= -8.623569:
                                if features["E(UP) - T(up)"] <= -0.035949:
                                    return 0
                                else:
                                    if features["E(UP) - agent_row"] <= -12.578706:
                                        return 3
                                    else:
                                        if features["E(UP) - time_left"] <= 0.295418:
                                            return 0
                                        else:
                                            if features["E(RIGHT) - T(DOWN)"] <= 0.382507:
                                                return 0
                                            else:
                                                return 3
                            else:
                                if features["E(RIGHT) - agent_column"] <= -2.387846:
                                    if features["E(RIGHT) - T(up)"] <= 0.662359:
                                        if features["E(UP) - agent_column"] <= -7.343952:
                                            if features["T(DOWN) - agent_row"] <= -3.598819:
                                                if features["E(UP) - T(DOWN)"] <= 0.599892:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        return 0
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= 0.408079:
                                        return 3
                                    else:
                                        return 0
                        else:
                            if features["E(RIGHT)"] <= 0.799069:
                                return 3
                            else:
                                if features["T(LEFT) - agent_row"] <= -1.699793:
                                    return 0
                                else:
                                    if features["T(RIGHT) - agent_column"] <= -5.544060:
                                        if features["E(RIGHT) - agent_column"] <= -7.166123:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
            else:
                if features["E(UP) - E(DOWN)"] <= 0.382014:
                    if features["E(LEFT) - T(DOWN)"] <= 0.066906:
                        if features["E(DOWN) - E(LEFT)"] <= 0.207008:
                            if features["E(UP) - time_left"] <= 0.189774:
                                if features["E(DOWN) - T(LEFT)"] <= 0.027584:
                                    if features["E(DOWN) - agent_column"] <= -6.609190:
                                        if features["E(UP)"] <= 0.042996:
                                            if features["E(DOWN) - T(up)"] <= 0.203913:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(LEFT) - T(RIGHT)"] <= 0.119807:
                                                return 0
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.302311:
                                                    if features["agent_row - time_left"] <= 4.710000:
                                                        if features["E(DOWN) - agent_row"] <= -0.603703:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(RIGHT)"] <= 0.132417:
                                                        if features["E(RIGHT) - time_left"] <= 0.083994:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 0
                                    else:
                                        if features["E(UP)"] <= 0.253024:
                                            if features["E(UP) - T(LEFT)"] <= -0.591193:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 0
                                else:
                                    if features["T(up) - T(LEFT)"] <= -0.092162:
                                        if features["E(DOWN) - E(LEFT)"] <= 0.031845:
                                            if features["T(DOWN) - time_left"] <= 0.276204:
                                                return 0
                                            else:
                                                return 1
                                        else:
                                            if features["E(UP) - time_left"] <= 0.166108:
                                                return 0
                                            else:
                                                return 2
                                    else:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.309607:
                                            if features["E(RIGHT) - agent_row"] <= -3.691553:
                                                if features["T(RIGHT) - agent_row"] <= -4.671115:
                                                    if features["T(LEFT)"] <= 0.136476:
                                                        if features["E(RIGHT) - T(LEFT)"] <= 0.243325:
                                                            return 2
                                                        else:
                                                            if features["E(LEFT) - T(RIGHT)"] <= -0.314398:
                                                                if features["E(RIGHT) - time_left"] <= 0.210120:
                                                                    return 2
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["T(DOWN) - time_left"] <= 0.187104:
                                                                    return 2
                                                                else:
                                                                    return 0
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(DOWN) - T(up)"] <= 0.356143:
                                                        if features["T(RIGHT) - agent_column"] <= -2.596596:
                                                            if features["E(DOWN) - time_left"] <= 0.249684:
                                                                if features["E(LEFT) - T(RIGHT)"] <= -0.221530:
                                                                    return 2
                                                                else:
                                                                    return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["E(UP) - time_left"] <= 0.132985:
                                                                return 2
                                                            else:
                                                                return 3
                                                    else:
                                                        return 0
                                            else:
                                                if features["T(DOWN) - agent_column"] <= -8.621525:
                                                    return 2
                                                else:
                                                    if features["T(RIGHT) - time_left"] <= 0.313141:
                                                        return 0
                                                    else:
                                                        if features["T(LEFT) - time_left"] <= 0.098352:
                                                            return 0
                                                        else:
                                                            return 1
                                        else:
                                            return 3
                            else:
                                if features["E(LEFT) - T(DOWN)"] <= 0.032521:
                                    if features["T(RIGHT) - agent_row"] <= -4.669163:
                                        if features["T(LEFT)"] <= 0.093486:
                                            if features["E(UP) - T(LEFT)"] <= 0.309834:
                                                if features["E(UP)"] <= 0.320364:
                                                    if features["E(DOWN) - agent_column"] <= -1.739745:
                                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.318727:
                                                            if features["E(UP) - T(LEFT)"] <= 0.210208:
                                                                if features["agent_row - time_left"] <= 8.990000:
                                                                    return 2
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["E(LEFT) - T(DOWN)"] <= -0.338038:
                                                                    return 2
                                                                else:
                                                                    return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(RIGHT)"] <= 0.365165:
                                                        return 3
                                                    else:
                                                        return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(DOWN) - T(up)"] <= 0.282837:
                                                if features["T(up) - T(RIGHT)"] <= -0.135850:
                                                    if features["E(DOWN) - T(up)"] <= 0.028178:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                                            else:
                                                return 3
                                    else:
                                        if features["E(LEFT) - time_left"] <= 0.057055:
                                            return 3
                                        else:
                                            return 2
                                else:
                                    if features["E(LEFT) - T(DOWN)"] <= 0.034946:
                                        return 3
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.299462:
                                            if features["T(up) - T(RIGHT)"] <= 0.060404:
                                                if features["E(UP) - T(LEFT)"] <= -0.022790:
                                                    return 1
                                                else:
                                                    return 0
                                            else:
                                                if features["time_left"] <= 0.030000:
                                                    return 3
                                                else:
                                                    return 0
                                        else:
                                            return 0
                        else:
                            if features["E(UP) - E(DOWN)"] <= -0.116583:
                                if features["E(DOWN) - T(LEFT)"] <= 0.313478:
                                    if features["E(UP) - E(DOWN)"] <= -0.356593:
                                        return 0
                                    else:
                                        if features["E(UP) - agent_row"] <= -3.861822:
                                            return 3
                                        else:
                                            if features["E(UP)"] <= 0.087884:
                                                return 1
                                            else:
                                                if features["E(UP) - time_left"] <= 0.102934:
                                                    if features["agent_column - time_left"] <= 2.930000:
                                                        if features["E(DOWN) - T(LEFT)"] <= 0.267033:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                                else:
                                    if features["E(DOWN) - T(RIGHT)"] <= -0.001399:
                                        if features["agent_row - time_left"] <= 4.700000:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        if features["T(DOWN) - time_left"] <= 0.249959:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - T(DOWN)"] <= -0.318425:
                                                return 1
                                            else:
                                                return 3
                            else:
                                if features["T(DOWN) - T(LEFT)"] <= 0.117127:
                                    return 1
                                else:
                                    return 2
                    else:
                        if features["T(DOWN)"] <= 0.112355:
                            if features["E(UP) - T(up)"] <= 0.247230:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.247230:
                                    if features["E(UP) - T(LEFT)"] <= 0.280541:
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.262870:
                                            if features["T(DOWN) - agent_column"] <= -4.930584:
                                                if features["E(UP) - T(RIGHT)"] <= 0.305050:
                                                    if features["E(LEFT) - T(DOWN)"] <= 0.128043:
                                                        if features["E(UP) - time_left"] <= 0.358997:
                                                            return 1
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["E(LEFT) - T(LEFT)"] <= 0.302596:
                                                            return 1
                                                        else:
                                                            if features["E(UP) - T(up)"] <= 0.185546:
                                                                return 1
                                                            else:
                                                                return 2
                                                else:
                                                    if features["agent_column - time_left"] <= 9.850000:
                                                        if features["T(LEFT) - agent_column"] <= -7.547322:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 2
                                            else:
                                                if features["E(UP) - agent_row"] <= -7.743302:
                                                    if features["E(UP) - time_left"] <= 0.398122:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    if features["agent_row - time_left"] <= 4.850000:
                                                        return 1
                                                    else:
                                                        if features["E(LEFT) - T(up)"] <= -0.542643:
                                                            return 3
                                                        else:
                                                            return 1
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= 0.298415:
                                                if features["E(LEFT) - T(RIGHT)"] <= 0.347533:
                                                    return 2
                                                else:
                                                    if features["T(up) - time_left"] <= 0.405902:
                                                        return 1
                                                    else:
                                                        return 2
                                            else:
                                                return 0
                                    else:
                                        if features["agent_column - time_left"] <= 9.850000:
                                            if features["E(UP) - agent_column"] <= -4.670112:
                                                if features["E(UP) - time_left"] <= 0.239957:
                                                    return 1
                                                else:
                                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.224224:
                                                        return 2
                                                    else:
                                                        return 1
                                            else:
                                                if features["agent_row - time_left"] <= 9.910000:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.296455:
                                        if features["T(LEFT) - agent_column"] <= -6.501966:
                                            return 1
                                        else:
                                            if features["E(DOWN) - T(up)"] <= 0.308886:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        return 1
                            else:
                                if features["E(UP) - T(RIGHT)"] <= -0.271445:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.153525:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["E(UP) - time_left"] <= 0.231491:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.171336:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 0
                        else:
                            if features["E(LEFT) - T(LEFT)"] <= -0.017880:
                                return 2
                            else:
                                if features["E(UP)"] <= 0.330084:
                                    if features["E(UP)"] <= 0.277247:
                                        if features["agent_row - time_left"] <= 7.890000:
                                            if features["agent_row - time_left"] <= 6.970000:
                                                return 3
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.088985:
                                                    return 3
                                                else:
                                                    if features["T(up) - T(LEFT)"] <= -0.139628:
                                                        return 2
                                                    else:
                                                        return 1
                                        else:
                                            return 2
                                    else:
                                        return 3
                                else:
                                    if features["E(UP) - E(DOWN)"] <= 0.181615:
                                        if features["time_left"] <= 0.030000:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        if features["E(RIGHT) - time_left"] <= 0.234148:
                                            if features["E(UP) - T(DOWN)"] <= 0.239317:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 3
                else:
                    if features["E(UP) - time_left"] <= 0.278692:
                        if features["E(UP) - E(LEFT)"] <= 0.232286:
                            if features["agent_row - time_left"] <= 13.650000:
                                return 2
                            else:
                                if features["agent_column - time_left"] <= 10.770000:
                                    return 3
                                else:
                                    return 0
                        else:
                            return 0
                    else:
                        if features["E(LEFT) - T(LEFT)"] <= 0.239209:
                            if features["E(UP) - time_left"] <= 0.373477:
                                if features["E(DOWN) - E(RIGHT)"] <= -0.437634:
                                    return 3
                                else:
                                    return 0
                            else:
                                return 0
                        else:
                            if features["E(RIGHT) - T(up)"] <= 0.148681:
                                if features["E(LEFT) - agent_row"] <= -9.709919:
                                    if features["T(up) - agent_column"] <= -7.453450:
                                        if features["E(LEFT) - T(up)"] <= -0.367818:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 0
                                else:
                                    return 2
                            else:
                                return 0
        else:
            if features["E(UP) - E(LEFT)"] <= -0.072204:
                if features["E(RIGHT)"] <= 0.008222:
                    if features["E(UP) - T(up)"] <= 0.014517:
                        if features["E(DOWN) - time_left"] <= 0.326535:
                            return 2
                        else:
                            return 1
                    else:
                        if features["E(UP) - T(RIGHT)"] <= 0.267490:
                            return 2
                        else:
                            if features["E(LEFT) - time_left"] <= 0.259365:
                                return 3
                            else:
                                return 2
                else:
                    if features["E(RIGHT) - T(RIGHT)"] <= 0.018007:
                        return 3
                    else:
                        return 2
            else:
                if features["T(up) - agent_row"] <= -1.915457:
                    if features["T(RIGHT) - agent_column"] <= -1.732521:
                        if features["E(LEFT) - T(DOWN)"] <= 0.599780:
                            if features["T(up) - agent_column"] <= -11.680724:
                                if features["E(LEFT) - time_left"] <= 0.324738:
                                    if features["T(LEFT) - agent_column"] <= -13.591129:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 0
                            else:
                                if features["T(RIGHT) - agent_row"] <= -11.746942:
                                    if features["T(LEFT) - agent_column"] <= -4.914564:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -2.941674:
                                        if features["E(UP) - T(RIGHT)"] <= 0.229699:
                                            return 0
                                        else:
                                            if features["E(LEFT) - T(RIGHT)"] <= 0.544331:
                                                if features["E(LEFT) - T(DOWN)"] <= 0.212411:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                    else:
                                        return 2
                        else:
                            if features["T(RIGHT) - agent_row"] <= -12.714536:
                                if features["T(LEFT) - agent_column"] <= -3.730618:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(LEFT)"] <= 0.839502:
                                    return 2
                                else:
                                    if features["T(up) - T(DOWN)"] <= 0.109962:
                                        return 0
                                    else:
                                        return 2
                    else:
                        if features["E(UP)"] <= 0.799069:
                            return 0
                        else:
                            if features["E(LEFT) - agent_column"] <= -1.160498:
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
