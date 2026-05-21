import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(DOWN)"] <= -0.364744:
        if features["E(LEFT) - E(RIGHT)"] <= 0.329779:
            if features["E(RIGHT)"] <= 0.345813:
                if features["E(UP)"] <= 0.020964:
                    if features["E(LEFT) - T(LEFT)"] <= 0.000777:
                        if features["E(UP) - T(DOWN)"] <= -0.510883:
                            if features["E(DOWN) - E(RIGHT)"] <= 0.261835:
                                if features["agent_row - time_left"] <= 4.840000:
                                    if features["T(LEFT) - time_left"] <= 0.080528:
                                        return 1
                                    else:
                                        if features["agent_row - agent_column"] <= -5.500000:
                                            return 1
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.479300:
                                                return 3
                                            else:
                                                return 1
                                else:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.553089:
                                        return 3
                                    else:
                                        return 1
                            else:
                                if features["E(LEFT) - T(up)"] <= 0.328750:
                                    if features["E(LEFT) - T(RIGHT)"] <= 0.302767:
                                        if features["E(UP) - E(RIGHT)"] <= -0.294813:
                                            if features["T(RIGHT) - time_left"] <= -0.080183:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(DOWN) - T(RIGHT)"] <= 0.548723:
                                                return 1
                                            else:
                                                if features["agent_column - time_left"] <= 4.860000:
                                                    if features["E(DOWN) - time_left"] <= 0.417671:
                                                        if features["T(DOWN) - time_left"] <= 0.511232:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(RIGHT) - T(LEFT)"] <= -0.522531:
                                                        return 1
                                                    else:
                                                        if features["E(LEFT) - T(LEFT)"] <= -0.456073:
                                                            return 3
                                                        else:
                                                            if features["T(DOWN) - agent_row"] <= -4.263995:
                                                                if features["E(LEFT) - T(LEFT)"] <= -0.442354:
                                                                    return 3
                                                                else:
                                                                    return 1
                                                            else:
                                                                return 1
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -7.396805:
                                            if features["E(UP) - E(LEFT)"] <= -0.305946:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(LEFT) - agent_row"] <= -9.286422:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    if features["agent_row - time_left"] <= 7.490000:
                                        if features["T(DOWN) - agent_column"] <= -11.223280:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(DOWN) - T(LEFT)"] <= 0.187570:
                                            if features["E(RIGHT) - T(DOWN)"] <= -0.372021:
                                                return 2
                                            else:
                                                if features["agent_row - time_left"] <= 7.740000:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            return 2
                        else:
                            if features["E(RIGHT) - T(RIGHT)"] <= 0.018016:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.251913:
                                    if features["E(RIGHT) - time_left"] <= 0.307463:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                if features["T(LEFT) - agent_column"] <= -6.345659:
                                    if features["E(DOWN) - agent_row"] <= -2.520700:
                                        if features["T(up) - T(DOWN)"] <= 0.659202:
                                            if features["E(LEFT) - T(up)"] <= 0.409116:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(LEFT) - time_left"] <= 0.108276:
                                            if features["T(LEFT) - agent_column"] <= -6.556947:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -8.592842:
                                                if features["E(RIGHT) - T(DOWN)"] <= -0.240823:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                else:
                                    if features["T(up) - T(LEFT)"] <= -0.705569:
                                        return 3
                                    else:
                                        return 1
                    else:
                        if features["agent_row - agent_column"] <= -6.500000:
                            if features["E(LEFT) - time_left"] <= -0.078855:
                                return 1
                            else:
                                if features["E(LEFT) - T(LEFT)"] <= 0.282625:
                                    if features["T(DOWN) - agent_row"] <= 0.407993:
                                        if features["T(DOWN) - agent_row"] <= -1.662328:
                                            return 1
                                        else:
                                            if features["E(LEFT) - T(DOWN)"] <= -0.293052:
                                                return 1
                                            else:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.155024:
                                                    if features["T(RIGHT) - agent_column"] <= -6.620107:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.560238:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    if features["T(DOWN) - agent_row"] <= -0.324051:
                                        return 2
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= -0.136646:
                                            return 1
                                        else:
                                            return 2
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= 0.350375:
                                if features["E(RIGHT) - T(up)"] <= 0.241836:
                                    if features["E(DOWN) - time_left"] <= -0.075294:
                                        return 3
                                    else:
                                        if features["T(DOWN) - time_left"] <= 0.206058:
                                            if features["T(RIGHT) - agent_column"] <= -2.324374:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 1
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -4.484254:
                                        if features["E(RIGHT) - agent_row"] <= -6.705747:
                                            if features["T(DOWN) - time_left"] <= 0.226782:
                                                return 1
                                            else:
                                                if features["agent_row - time_left"] <= 8.700000:
                                                    if features["T(LEFT) - time_left"] <= -0.340000:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    return 3
                                        else:
                                            if features["E(LEFT) - T(RIGHT)"] <= -0.354483:
                                                if features["T(DOWN) - agent_column"] <= -4.335779:
                                                    if features["E(RIGHT) - T(DOWN)"] <= 0.329406:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                            else:
                                                if features["E(LEFT) - T(DOWN)"] <= 0.235129:
                                                    return 3
                                                else:
                                                    return 1
                                    else:
                                        if features["E(LEFT) - time_left"] <= -0.144703:
                                            return 2
                                        else:
                                            if features["E(DOWN) - T(up)"] <= 0.465997:
                                                return 1
                                            else:
                                                if features["E(LEFT) - T(RIGHT)"] <= -0.687263:
                                                    return 3
                                                else:
                                                    if features["T(RIGHT) - agent_column"] <= -2.393453:
                                                        if features["E(RIGHT) - T(DOWN)"] <= -0.089605:
                                                            if features["T(LEFT) - T(RIGHT)"] <= -0.405020:
                                                                return 1
                                                            else:
                                                                return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 3
                            else:
                                if features["E(RIGHT)"] <= 0.230707:
                                    if features["T(DOWN) - agent_column"] <= -7.422329:
                                        return 2
                                    else:
                                        if features["E(UP) - T(DOWN)"] <= -0.427949:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    if features["T(DOWN) - agent_row"] <= -0.361575:
                                        if features["E(LEFT) - agent_row"] <= -2.832200:
                                            if features["E(RIGHT) - T(DOWN)"] <= -0.509526:
                                                if features["E(DOWN) - T(DOWN)"] <= -0.407974:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(DOWN) - agent_row"] <= -1.294431:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        return 1
                else:
                    if features["E(RIGHT) - T(DOWN)"] <= -0.231502:
                        if features["E(LEFT) - T(LEFT)"] <= -0.189067:
                            if features["agent_column - time_left"] <= 7.960000:
                                return 3
                            else:
                                return 1
                        else:
                            if features["T(LEFT) - agent_column"] <= -8.855705:
                                return 2
                            else:
                                if features["T(RIGHT)"] <= 0.301685:
                                    return 0
                                else:
                                    if features["E(RIGHT) - time_left"] <= -0.034147:
                                        return 2
                                    else:
                                        if features["agent_row - time_left"] <= 0.920000:
                                            return 1
                                        else:
                                            return 2
                    else:
                        if features["T(DOWN) - time_left"] <= 0.050534:
                            return 1
                        else:
                            if features["T(up)"] <= 0.023844:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.237511:
                                    if features["T(DOWN) - agent_column"] <= -8.667882:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 3
                            else:
                                return 0
            else:
                if features["E(RIGHT) - agent_column"] <= -11.208409:
                    if features["E(RIGHT) - T(up)"] <= 0.850646:
                        if features["E(RIGHT) - T(up)"] <= 0.678658:
                            return 1
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= 0.692720:
                                if features["T(up) - agent_column"] <= -12.895088:
                                    return 1
                                else:
                                    if features["E(DOWN) - agent_row"] <= -8.243484:
                                        return 1
                                    else:
                                        if features["E(DOWN) - T(up)"] <= 0.751568:
                                            return 1
                                        else:
                                            return 3
                            else:
                                if features["agent_row - time_left"] <= 8.820000:
                                    return 3
                                else:
                                    return 1
                    else:
                        if features["agent_row"] <= 2.500000:
                            return 1
                        else:
                            if features["T(DOWN) - agent_row"] <= -8.743783:
                                return 1
                            else:
                                return 3
                else:
                    if features["E(RIGHT) - agent_row"] <= -11.208409:
                        if features["E(DOWN) - E(RIGHT)"] <= 0.189213:
                            if features["E(DOWN)"] <= 0.851000:
                                return 3
                            else:
                                if features["agent_row - agent_column"] <= 8.500000:
                                    if features["T(LEFT) - agent_column"] <= -5.445747:
                                        if features["T(LEFT) - agent_column"] <= -10.571299:
                                            if features["T(up) - agent_column"] <= -11.359986:
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
                            return 1
                    else:
                        if features["E(RIGHT) - agent_column"] <= -0.555235:
                            if features["E(RIGHT) - agent_column"] <= -6.533428:
                                if features["E(DOWN) - E(LEFT)"] <= 0.557924:
                                    if features["T(LEFT) - time_left"] <= -0.200000:
                                        if features["T(RIGHT) - agent_row"] <= -1.819657:
                                            return 1
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -8.508991:
                                                return 2
                                            else:
                                                return 3
                                    else:
                                        if features["E(RIGHT) - agent_column"] <= -7.457038:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -7.454101:
                                                return 3
                                            else:
                                                return 1
                                else:
                                    if features["E(RIGHT) - T(up)"] <= 0.601945:
                                        if features["E(DOWN) - agent_column"] <= -9.338459:
                                            if features["E(LEFT) - E(RIGHT)"] <= -0.691442:
                                                if features["T(up) - agent_row"] <= -9.551047:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 1
                                        else:
                                            if features["E(RIGHT) - agent_row"] <= -9.303427:
                                                if features["E(UP) - E(RIGHT)"] <= -0.728881:
                                                    if features["E(DOWN) - agent_row"] <= -10.166124:
                                                        if features["E(DOWN) - agent_column"] <= -7.194745:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -9.341376:
                                                        return 3
                                                    else:
                                                        if features["E(DOWN) - agent_column"] <= -8.316883:
                                                            if features["T(up)"] <= 0.330280:
                                                                return 1
                                                            else:
                                                                return 3
                                                        else:
                                                            return 1
                                            else:
                                                if features["E(UP) - T(LEFT)"] <= -0.389032:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - T(LEFT)"] <= 0.750539:
                                                        if features["T(up) - time_left"] <= 0.421919:
                                                            if features["T(DOWN) - time_left"] <= 0.065923:
                                                                return 3
                                                            else:
                                                                if features["T(DOWN) - agent_row"] <= -6.723456:
                                                                    if features["E(RIGHT) - T(up)"] <= 0.537012:
                                                                        return 3
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= 0.487691:
                                            if features["agent_row - time_left"] <= -0.120000:
                                                return 1
                                            else:
                                                if features["E(DOWN) - agent_row"] <= -4.337692:
                                                    if features["T(LEFT) - time_left"] <= 0.459091:
                                                        if features["E(LEFT) - agent_row"] <= -10.500000:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(RIGHT) - agent_row"] <= -3.160498:
                                                        return 3
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -1.443387:
                                                            if features["T(DOWN) - agent_column"] <= -10.843106:
                                                                return 3
                                                            else:
                                                                if features["T(LEFT) - agent_row"] <= -2.711107:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                        else:
                                                            return 3
                                        else:
                                            if features["E(DOWN) - time_left"] <= 0.630899:
                                                if features["T(DOWN) - agent_row"] <= -1.501149:
                                                    return 3
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= 0.749390:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                if features["T(RIGHT) - agent_row"] <= 0.035412:
                                                    if features["T(DOWN) - agent_column"] <= -7.666854:
                                                        if features["E(DOWN) - agent_column"] <= -9.166124:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                            else:
                                if features["E(DOWN) - agent_column"] <= -4.402229:
                                    if features["E(DOWN) - agent_row"] <= -7.457038:
                                        if features["E(RIGHT) - agent_row"] <= -10.622621:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        if features["E(DOWN) - T(LEFT)"] <= -0.092552:
                                            if features["E(RIGHT) - T(up)"] <= 0.437997:
                                                return 1
                                            else:
                                                if features["T(LEFT) - agent_row"] <= -2.198859:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            if features["T(RIGHT) - time_left"] <= 0.197609:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.297070:
                                                    if features["T(LEFT) - time_left"] <= -0.760000:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= 0.833876:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                if features["E(UP) - E(DOWN)"] <= -0.444457:
                                                    if features["E(RIGHT) - time_left"] <= 0.296294:
                                                        if features["E(LEFT) - T(up)"] <= 0.111159:
                                                            return 3
                                                        else:
                                                            return 2
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(up) - agent_row"] <= -5.596029:
                                                        return 3
                                                    else:
                                                        return 1
                                else:
                                    if features["T(up) - agent_row"] <= -1.253996:
                                        if features["E(LEFT) - agent_row"] <= -4.934845:
                                            if features["T(up) - T(DOWN)"] <= 0.501607:
                                                if features["E(DOWN) - E(LEFT)"] <= 0.366297:
                                                    return 3
                                                else:
                                                    if features["E(LEFT) - E(RIGHT)"] <= -0.240698:
                                                        if features["E(RIGHT) - agent_row"] <= -9.341376:
                                                            if features["E(UP) - E(RIGHT)"] <= -0.728881:
                                                                if features["E(RIGHT) - agent_column"] <= -4.194745:
                                                                    return 1
                                                                else:
                                                                    if features["agent_row - agent_column"] <= 9.500000:
                                                                        return 3
                                                                    else:
                                                                        return 1
                                                            else:
                                                                if features["E(RIGHT) - time_left"] <= 0.042195:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                        else:
                                                            if features["E(LEFT) - agent_row"] <= -6.976037:
                                                                if features["E(UP) - E(DOWN)"] <= -0.492151:
                                                                    if features["T(DOWN) - T(LEFT)"] <= -0.015654:
                                                                        return 3
                                                                    else:
                                                                        if features["T(RIGHT) - time_left"] <= 0.278618:
                                                                            return 1
                                                                        else:
                                                                            return 3
                                                                else:
                                                                    return 3
                                                            else:
                                                                if features["E(RIGHT) - agent_row"] <= -5.554097:
                                                                    return 3
                                                                else:
                                                                    if features["E(RIGHT) - T(LEFT)"] <= 0.655647:
                                                                        if features["T(DOWN) - T(RIGHT)"] <= 0.106266:
                                                                            return 1
                                                                        else:
                                                                            return 3
                                                                    else:
                                                                        return 3
                                                    else:
                                                        if features["E(RIGHT) - T(DOWN)"] <= -0.150631:
                                                            return 2
                                                        else:
                                                            if features["T(RIGHT) - agent_column"] <= -2.622354:
                                                                return 1
                                                            else:
                                                                return 3
                                            else:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.520312:
                                                    return 3
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -9.338459:
                                                        if features["E(DOWN) - T(DOWN)"] <= 0.728881:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -6.242629:
                                                            return 1
                                                        else:
                                                            return 3
                                        else:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.833876:
                                                if features["E(LEFT) - T(DOWN)"] <= -0.366886:
                                                    if features["E(LEFT) - agent_column"] <= -0.960245:
                                                        if features["E(DOWN) - T(DOWN)"] <= 0.347120:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(LEFT) - T(DOWN)"] <= -0.354623:
                                                        if features["E(LEFT) - time_left"] <= 0.006250:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(up) - T(LEFT)"] <= -0.015654:
                                                            return 3
                                                        else:
                                                            return 1
                                            else:
                                                if features["T(RIGHT) - agent_column"] <= -1.608864:
                                                    return 1
                                                else:
                                                    return 3
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -3.599996:
                                            if features["T(LEFT) - time_left"] <= -0.240000:
                                                return 3
                                            else:
                                                if features["T(RIGHT) - agent_row"] <= 0.381307:
                                                    if features["E(DOWN) - agent_row"] <= 0.730042:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                                        else:
                                            return 3
                        else:
                            if features["E(RIGHT) - agent_row"] <= -8.399529:
                                if features["T(up) - agent_row"] <= -11.326777:
                                    if features["E(DOWN) - agent_column"] <= 0.333876:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    return 3
                            else:
                                if features["T(DOWN) - agent_row"] <= -1.482240:
                                    return 1
                                else:
                                    return 3
        else:
            if features["E(LEFT) - agent_row"] <= -11.208409:
                if features["E(UP) - T(LEFT)"] <= -0.478897:
                    if features["T(up) - time_left"] <= -0.500000:
                        return 1
                    else:
                        return 2
                else:
                    return 2
            else:
                if features["E(DOWN) - agent_column"] <= -11.194745:
                    if features["E(LEFT) - E(RIGHT)"] <= 0.376818:
                        return 2
                    else:
                        if features["E(DOWN) - T(up)"] <= 0.658801:
                            if features["agent_row - agent_column"] <= -1.500000:
                                if features["E(LEFT) - T(RIGHT)"] <= 0.482654:
                                    if features["E(LEFT) - T(up)"] <= 0.226090:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.820793:
                                        if features["T(DOWN) - T(RIGHT)"] <= -0.020276:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["agent_row - agent_column"] <= -3.500000:
                                            if features["agent_row - agent_column"] <= -4.500000:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 1
                            else:
                                if features["E(DOWN) - E(RIGHT)"] <= 0.728881:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["T(LEFT) - agent_row"] <= -2.398398:
                                if features["agent_row - agent_column"] <= -10.500000:
                                    if features["E(DOWN)"] <= 0.833876:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    if features["E(RIGHT) - T(up)"] <= -0.167797:
                                        return 2
                                    else:
                                        if features["E(UP) - time_left"] <= -0.440000:
                                            return 2
                                        else:
                                            return 1
                            else:
                                return 1
                else:
                    if features["T(up) - agent_column"] <= -2.736485:
                        if features["agent_row - time_left"] <= 2.860000:
                            if features["T(LEFT) - agent_row"] <= 0.408624:
                                if features["E(LEFT) - agent_row"] <= 0.730042:
                                    if features["T(RIGHT) - agent_row"] <= -1.746941:
                                        if features["E(UP) - E(LEFT)"] <= -0.422717:
                                            if features["agent_row - agent_column"] <= -9.500000:
                                                return 1
                                            else:
                                                if features["E(UP) - time_left"] <= -0.160000:
                                                    return 2
                                                else:
                                                    if features["E(LEFT) - agent_column"] <= -6.530195:
                                                        return 1
                                                    else:
                                                        return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -1.444896:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    if features["agent_column"] <= 8.500000:
                                        return 1
                                    else:
                                        return 2
                            else:
                                if features["E(DOWN) - time_left"] <= 0.301201:
                                    return 1
                                else:
                                    return 2
                        else:
                            if features["E(LEFT) - agent_row"] <= -9.341376:
                                if features["E(UP) - E(LEFT)"] <= -0.708946:
                                    if features["E(DOWN) - agent_row"] <= -10.166124:
                                        if features["E(DOWN) - agent_column"] <= -10.271120:
                                            return 2
                                        else:
                                            if features["T(LEFT) - agent_row"] <= -11.699793:
                                                if features["E(DOWN) - agent_column"] <= -3.160498:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["E(DOWN)"] <= 0.839502:
                                                    if features["E(DOWN) - agent_column"] <= -3.280124:
                                                        if features["E(DOWN) - T(RIGHT)"] <= 0.728881:
                                                            return 2
                                                        else:
                                                            if features["time_left"] <= 0.910000:
                                                                return 1
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["E(LEFT) - T(DOWN)"] <= -0.052020:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    if features["agent_column - time_left"] <= 5.850000:
                                                        return 2
                                                    else:
                                                        return 1
                                    else:
                                        if features["T(up) - T(LEFT)"] <= -0.145348:
                                            return 1
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -3.477510:
                                                return 2
                                            else:
                                                return 1
                                else:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.612019:
                                        return 2
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -5.303315:
                                            if features["T(LEFT) - agent_column"] <= -6.808753:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 2
                            else:
                                if features["E(UP) - E(DOWN)"] <= -0.791591:
                                    if features["E(LEFT) - agent_column"] <= -5.166123:
                                        if features["T(LEFT) - agent_column"] <= -11.405715:
                                            return 2
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -10.666502:
                                                if features["E(LEFT) - agent_column"] <= -10.166124:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["T(up) - T(LEFT)"] <= -0.045650:
                                                    if features["E(LEFT) - T(LEFT)"] <= 0.532702:
                                                        return 2
                                                    else:
                                                        if features["T(RIGHT) - agent_row"] <= -2.749404:
                                                            return 1
                                                        else:
                                                            return 2
                                                else:
                                                    return 2
                                    else:
                                        if features["agent_row - agent_column"] <= 5.500000:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.022759:
                                        if features["E(DOWN) - agent_row"] <= -6.507849:
                                            if features["E(LEFT)"] <= 0.542962:
                                                return 2
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.469583:
                                                    return 1
                                                else:
                                                    return 2
                                        else:
                                            if features["agent_column - time_left"] <= 5.720000:
                                                if features["E(LEFT)"] <= 0.542613:
                                                    if features["T(LEFT) - time_left"] <= 0.438195:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["E(LEFT) - T(up)"] <= -0.157004:
                                                    return 2
                                                else:
                                                    return 1
                                    else:
                                        if features["T(DOWN) - T(LEFT)"] <= -0.394333:
                                            return 1
                                        else:
                                            if features["T(DOWN) - T(LEFT)"] <= -0.081656:
                                                if features["E(LEFT) - T(up)"] <= 0.263866:
                                                    return 2
                                                else:
                                                    if features["T(LEFT) - agent_column"] <= -9.582811:
                                                        return 1
                                                    else:
                                                        if features["agent_column - time_left"] <= 7.960000:
                                                            return 1
                                                        else:
                                                            return 2
                                            else:
                                                if features["E(LEFT) - T(up)"] <= 0.545653:
                                                    if features["T(RIGHT) - agent_column"] <= -4.668888:
                                                        if features["E(LEFT) - agent_row"] <= -7.457038:
                                                            if features["E(UP) - E(LEFT)"] <= -0.594275:
                                                                return 1
                                                            else:
                                                                return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["E(LEFT) - E(RIGHT)"] <= 0.598614:
                                                            return 1
                                                        else:
                                                            if features["E(DOWN) - agent_row"] <= -6.323245:
                                                                return 1
                                                            else:
                                                                return 2
                                                else:
                                                    if features["T(DOWN) - agent_column"] <= -8.477712:
                                                        return 1
                                                    else:
                                                        if features["agent_row - time_left"] <= 4.820000:
                                                            if features["T(DOWN) - time_left"] <= 0.390164:
                                                                return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            if features["T(LEFT) - agent_column"] <= -8.838076:
                                                                return 2
                                                            else:
                                                                if features["T(LEFT) - time_left"] <= -0.420000:
                                                                    return 2
                                                                else:
                                                                    if features["T(up) - time_left"] <= -0.120000:
                                                                        return 1
                                                                    else:
                                                                        return 2
                    else:
                        if features["E(UP) - E(LEFT)"] <= -0.799069:
                            if features["T(up) - agent_column"] <= -1.656802:
                                if features["E(LEFT) - agent_column"] <= -1.160498:
                                    if features["T(up) - T(DOWN)"] <= 0.190319:
                                        if features["E(LEFT) - agent_row"] <= -0.194745:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -7.815614:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.727630:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 2
                                else:
                                    if features["T(DOWN) - agent_row"] <= -0.847906:
                                        return 2
                                    else:
                                        return 1
                            else:
                                if features["E(LEFT) - agent_row"] <= -10.160498:
                                    if features["T(DOWN) - T(RIGHT)"] <= -0.612701:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["T(RIGHT) - agent_column"] <= -0.863734:
                                        if features["E(UP) - E(DOWN)"] <= -0.839502:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(RIGHT) - T(RIGHT)"] <= -0.577922:
                                            return 2
                                        else:
                                            if features["T(up) - agent_row"] <= -7.580294:
                                                if features["T(up) - agent_row"] <= -10.672748:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["agent_row - agent_column"] <= 1.500000:
                                                    if features["E(DOWN) - time_left"] <= 0.523876:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(UP) - E(LEFT)"] <= -0.833876:
                                                        if features["agent_row - time_left"] <= 2.920000:
                                                            return 2
                                                        else:
                                                            if features["T(DOWN) - agent_row"] <= -3.855784:
                                                                return 2
                                                            else:
                                                                return 1
                                                    else:
                                                        return 1
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= 0.252778:
                                if features["T(up) - agent_column"] <= -1.773616:
                                    if features["E(UP) - E(DOWN)"] <= -0.728881:
                                        if features["E(DOWN) - agent_column"] <= -2.269958:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                if features["E(LEFT) - T(RIGHT)"] <= 0.493298:
                                    return 3
                                else:
                                    return 1
    else:
        if features["E(LEFT) - E(RIGHT)"] <= -0.371418:
            if features["E(UP) - E(DOWN)"] <= 0.338461:
                if features["E(UP) - T(up)"] <= 0.041449:
                    if features["E(UP) - T(LEFT)"] <= 0.354464:
                        if features["E(UP) - E(DOWN)"] <= -0.325962:
                            if features["T(up) - time_left"] <= -0.049724:
                                return 3
                            else:
                                return 0
                        else:
                            if features["E(DOWN) - T(DOWN)"] <= 0.258209:
                                if features["T(LEFT) - time_left"] <= -0.640000:
                                    if features["T(LEFT) - agent_row"] <= -3.500000:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    if features["T(DOWN) - T(RIGHT)"] <= -0.496556:
                                        return 3
                                    else:
                                        if features["agent_column - time_left"] <= -0.220000:
                                            if features["E(RIGHT) - T(DOWN)"] <= 0.292511:
                                                if features["T(up) - agent_column"] <= 0.203017:
                                                    if features["E(UP) - E(LEFT)"] <= 0.150022:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                        else:
                                            return 3
                            else:
                                if features["T(RIGHT) - agent_row"] <= -5.455944:
                                    if features["T(up) - agent_column"] <= -12.475394:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 3
                    else:
                        if features["E(RIGHT) - T(DOWN)"] <= 0.356895:
                            return 0
                        else:
                            if features["T(RIGHT) - agent_column"] <= -5.505224:
                                return 3
                            else:
                                if features["T(up) - agent_column"] <= -3.286421:
                                    if features["E(DOWN) - T(RIGHT)"] <= -0.320749:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 3
                else:
                    if features["T(LEFT) - time_left"] <= -0.280000:
                        if features["agent_column - time_left"] <= 7.230000:
                            if features["E(DOWN) - E(LEFT)"] <= 0.285562:
                                if features["E(UP) - E(DOWN)"] <= 0.049912:
                                    if features["agent_row - time_left"] <= 5.600000:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(DOWN) - time_left"] <= -0.247430:
                                        return 3
                                    else:
                                        return 0
                            else:
                                return 3
                        else:
                            if features["E(DOWN) - T(RIGHT)"] <= -0.213785:
                                if features["E(UP) - T(RIGHT)"] <= -0.360997:
                                    return 3
                                else:
                                    if features["T(LEFT) - time_left"] <= -0.620000:
                                        return 1
                                    else:
                                        return 2
                            else:
                                return 3
                    else:
                        if features["E(DOWN) - T(DOWN)"] <= 0.280923:
                            if features["E(UP) - T(LEFT)"] <= 0.295652:
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
                                if features["E(RIGHT) - T(RIGHT)"] <= -0.295827:
                                    return 3
                                else:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.165569:
                                        return 1
                                    else:
                                        return 3
            else:
                if features["T(LEFT) - agent_row"] <= -1.902892:
                    if features["E(UP) - agent_column"] <= -11.208409:
                        if features["T(up) - T(LEFT)"] <= 0.095719:
                            if features["T(DOWN) - agent_row"] <= -8.919919:
                                if features["E(RIGHT) - agent_row"] <= -10.208970:
                                    if features["agent_row - agent_column"] <= 1.500000:
                                        if features["E(LEFT) - T(LEFT)"] <= -0.544346:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(UP) - E(DOWN)"] <= 0.833876:
                                        return 0
                                    else:
                                        return 3
                            else:
                                if features["E(RIGHT) - agent_row"] <= -2.225466:
                                    if features["agent_column - time_left"] <= 11.580000:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    if features["T(LEFT) - agent_column"] <= -11.651063:
                                        if features["E(UP) - T(DOWN)"] <= 0.833876:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 3
                        else:
                            if features["E(UP) - agent_column"] <= -11.386315:
                                return 0
                            else:
                                return 3
                    else:
                        if features["T(DOWN) - agent_column"] <= -2.764088:
                            if features["T(RIGHT) - agent_row"] <= -12.841552:
                                return 3
                            else:
                                if features["E(UP) - agent_column"] <= -4.160498:
                                    if features["T(LEFT) - agent_row"] <= -3.371965:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.469933:
                                            if features["T(up) - T(RIGHT)"] <= 0.140713:
                                                if features["E(RIGHT) - agent_column"] <= -10.280124:
                                                    return 0
                                                else:
                                                    if features["E(UP) - T(LEFT)"] <= 0.600046:
                                                        if features["T(up) - T(RIGHT)"] <= -0.120480:
                                                            if features["T(DOWN) - agent_row"] <= -5.493643:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["E(DOWN) - time_left"] <= -0.260000:
                                                            return 3
                                                        else:
                                                            return 0
                                            else:
                                                if features["E(UP) - agent_column"] <= -5.554097:
                                                    return 0
                                                else:
                                                    return 3
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= -0.039557:
                                                return 3
                                            else:
                                                if features["T(up) - agent_row"] <= -6.740320:
                                                    if features["T(LEFT) - agent_column"] <= -7.694950:
                                                        if features["T(DOWN) - time_left"] <= -0.246156:
                                                            if features["E(RIGHT) - agent_column"] <= -8.269958:
                                                                if features["E(LEFT) - E(RIGHT)"] <= -0.602157:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["E(UP) - E(DOWN)"] <= 0.833876:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                        else:
                                                            if features["T(DOWN) - agent_column"] <= -9.958578:
                                                                if features["E(UP) - agent_column"] <= -10.275529:
                                                                    if features["E(UP) - agent_column"] <= -11.194745:
                                                                        return 3
                                                                    else:
                                                                        if features["T(up) - T(RIGHT)"] <= 0.546550:
                                                                            return 0
                                                                        else:
                                                                            return 3
                                                                else:
                                                                    return 3
                                                            else:
                                                                if features["E(UP)"] <= 0.833876:
                                                                    if features["E(UP) - E(LEFT)"] <= 0.557567:
                                                                        return 0
                                                                    else:
                                                                        if features["T(LEFT) - agent_column"] <= -8.445508:
                                                                            return 0
                                                                        else:
                                                                            if features["E(RIGHT) - T(LEFT)"] <= 0.791591:
                                                                                return 3
                                                                            else:
                                                                                return 0
                                                                else:
                                                                    return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(UP) - agent_column"] <= -8.166124:
                                                        if features["T(DOWN) - T(LEFT)"] <= -0.078418:
                                                            if features["E(UP) - agent_column"] <= -10.301609:
                                                                return 0
                                                            else:
                                                                if features["E(UP) - T(DOWN)"] <= 0.612524:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(up) - agent_column"] <= -8.237815:
                                                            return 0
                                                        else:
                                                            if features["E(UP) - T(DOWN)"] <= 0.643096:
                                                                if features["E(RIGHT) - agent_column"] <= -4.444896:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                return 0
                                    else:
                                        if features["E(LEFT) - E(RIGHT)"] <= -0.728881:
                                            if features["T(DOWN) - agent_column"] <= -8.630254:
                                                if features["T(up) - T(DOWN)"] <= -0.540894:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["agent_row - agent_column"] <= -3.500000:
                                                    if features["E(UP) - time_left"] <= 0.378291:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    return 3
                                        else:
                                            if features["T(DOWN) - T(RIGHT)"] <= -0.425432:
                                                if features["E(RIGHT) - T(RIGHT)"] <= -0.035952:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 3
                                else:
                                    if features["E(UP) - agent_row"] <= -7.539837:
                                        if features["T(RIGHT) - agent_column"] <= -3.665454:
                                            if features["E(UP) - T(up)"] <= 0.321419:
                                                if features["E(RIGHT) - T(DOWN)"] <= 0.613425:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(LEFT) - agent_row"] <= -8.900731:
                                                    return 0
                                                else:
                                                    return 3
                                        else:
                                            if features["E(UP) - E(LEFT)"] <= 0.833876:
                                                if features["T(up) - agent_row"] <= -12.614487:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                    else:
                                        if features["E(UP)"] <= 0.448688:
                                            return 3
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -4.229776:
                                                return 0
                                            else:
                                                if features["T(DOWN) - agent_row"] <= -2.538585:
                                                    if features["T(up) - agent_row"] <= -7.348658:
                                                        if features["E(RIGHT) - time_left"] <= 0.575121:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["E(DOWN) - E(RIGHT)"] <= -0.553982:
                                                            return 0
                                                        else:
                                                            if features["T(up) - agent_row"] <= -5.208409:
                                                                return 0
                                                            else:
                                                                return 3
                                                else:
                                                    if features["E(UP) - E(LEFT)"] <= 0.791591:
                                                        return 3
                                                    else:
                                                        return 0
                        else:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.384356:
                                return 3
                            else:
                                if features["T(LEFT) - agent_column"] <= -1.915457:
                                    if features["T(DOWN) - agent_row"] <= -1.666466:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["T(DOWN) - agent_column"] <= 0.252227:
                                        if features["E(DOWN) - T(RIGHT)"] <= -0.441216:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.005475:
                                                if features["T(RIGHT) - agent_column"] <= -0.517753:
                                                    return 3
                                                else:
                                                    if features["E(UP) - agent_row"] <= -5.414000:
                                                        return 0
                                                    else:
                                                        return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(UP) - T(up)"] <= 0.839502:
                                                return 0
                                            else:
                                                if features["T(RIGHT) - agent_row"] <= -4.848202:
                                                    return 0
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -3.500000:
                                                        return 3
                                                    else:
                                                        return 0
                                    else:
                                        if features["E(RIGHT) - agent_row"] <= -4.324293:
                                            return 0
                                        else:
                                            if features["E(UP) - T(LEFT)"] <= 0.839502:
                                                if features["T(RIGHT) - agent_row"] <= -3.665415:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 3
                else:
                    if features["E(UP) - agent_column"] <= -12.166124:
                        return 0
                    else:
                        if features["E(LEFT) - E(RIGHT)"] <= -0.799069:
                            if features["agent_row - time_left"] <= 1.540000:
                                if features["E(LEFT) - T(DOWN)"] <= -0.659202:
                                    if features["T(RIGHT) - agent_column"] <= -7.286422:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    if features["T(LEFT) - agent_column"] <= -5.653448:
                                        return 3
                                    else:
                                        if features["T(RIGHT) - agent_column"] <= -4.220226:
                                            return 0
                                        else:
                                            return 3
                            else:
                                return 3
                        else:
                            return 3
        else:
            if features["E(UP) - E(DOWN)"] <= 0.359301:
                if features["E(LEFT) - E(RIGHT)"] <= 0.380634:
                    if features["E(UP) - T(RIGHT)"] <= 0.066876:
                        if features["T(LEFT) - agent_column"] <= -8.868429:
                            if features["E(LEFT) - time_left"] <= -0.009403:
                                if features["E(UP) - T(LEFT)"] <= 0.022045:
                                    if features["T(RIGHT) - agent_row"] <= -3.500000:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(LEFT) - T(RIGHT)"] <= -0.221246:
                                        return 0
                                    else:
                                        if features["E(DOWN)"] <= 0.373426:
                                            if features["E(DOWN) - agent_row"] <= -3.146811:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 2
                            else:
                                if features["E(UP) - T(up)"] <= 0.306728:
                                    if features["T(up) - T(LEFT)"] <= 0.791591:
                                        if features["T(up) - time_left"] <= -0.120000:
                                            if features["E(DOWN) - E(RIGHT)"] <= 0.245388:
                                                if features["E(RIGHT) - T(RIGHT)"] <= -0.606530:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(LEFT) - time_left"] <= 0.363869:
                                                if features["E(RIGHT) - T(RIGHT)"] <= 0.017478:
                                                    if features["E(DOWN)"] <= 0.332289:
                                                        if features["E(DOWN) - T(RIGHT)"] <= 0.122546:
                                                            return 2
                                                        else:
                                                            if features["E(UP) - agent_row"] <= -4.897594:
                                                                return 2
                                                            else:
                                                                return 1
                                                    else:
                                                        return 2
                                                else:
                                                    if features["T(LEFT) - time_left"] <= 0.282586:
                                                        if features["E(LEFT) - T(DOWN)"] <= -0.386271:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 2
                                            else:
                                                if features["E(LEFT) - time_left"] <= 0.365669:
                                                    if features["E(DOWN) - T(LEFT)"] <= -0.049207:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 2
                                    else:
                                        if features["E(UP) - E(RIGHT)"] <= 0.133640:
                                            return 2
                                        else:
                                            return 0
                                else:
                                    return 0
                        else:
                            if features["E(DOWN)"] <= 0.371879:
                                if features["T(up) - agent_row"] <= -8.675020:
                                    if features["T(up) - T(LEFT)"] <= 0.234018:
                                        if features["E(UP) - E(RIGHT)"] <= -0.188041:
                                            return 3
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= 0.064657:
                                                if features["T(LEFT)"] <= 0.233588:
                                                    if features["T(LEFT) - time_left"] <= 0.058919:
                                                        if features["T(LEFT) - agent_row"] <= -8.846192:
                                                            if features["E(DOWN)"] <= 0.213635:
                                                                if features["E(LEFT) - E(RIGHT)"] <= -0.266996:
                                                                    if features["E(UP) - T(RIGHT)"] <= -0.204938:
                                                                        return 3
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["E(LEFT) - T(RIGHT)"] <= -0.449727:
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
                                                return 1
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -9.740565:
                                            if features["E(LEFT) - T(RIGHT)"] <= -0.337131:
                                                if features["E(LEFT) - E(RIGHT)"] <= -0.365816:
                                                    return 3
                                                else:
                                                    if features["E(UP) - T(up)"] <= -0.068004:
                                                        if features["E(LEFT) - E(RIGHT)"] <= -0.246158:
                                                            if features["E(RIGHT) - agent_row"] <= -12.658908:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["agent_row - agent_column"] <= 3.500000:
                                                                return 2
                                                            else:
                                                                return 0
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(RIGHT) - time_left"] <= 0.314487:
                                                    if features["E(UP) - T(up)"] <= -0.048546:
                                                        if features["E(RIGHT) - T(LEFT)"] <= 0.215466:
                                                            return 0
                                                        else:
                                                            if features["T(up) - T(RIGHT)"] <= 0.110098:
                                                                if features["E(DOWN) - E(RIGHT)"] <= -0.148666:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["E(LEFT) - agent_row"] <= -11.697881:
                                                            if features["E(RIGHT) - T(LEFT)"] <= 0.307725:
                                                                return 1
                                                            else:
                                                                return 0
                                                        else:
                                                            if features["E(DOWN) - time_left"] <= -0.131593:
                                                                return 3
                                                            else:
                                                                return 2
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.363545:
                                                        return 3
                                                    else:
                                                        return 1
                                        else:
                                            if features["E(LEFT) - T(up)"] <= -0.249434:
                                                if features["agent_row - time_left"] <= 9.840000:
                                                    return 3
                                                else:
                                                    return 2
                                            else:
                                                return 2
                                else:
                                    if features["E(UP)"] <= 0.171336:
                                        if features["E(RIGHT) - T(LEFT)"] <= 0.168856:
                                            return 1
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.016179:
                                                if features["E(UP) - T(LEFT)"] <= 0.050934:
                                                    if features["E(RIGHT) - agent_column"] <= -3.667711:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - time_left"] <= -0.320561:
                                                            return 0
                                                        else:
                                                            return 3
                                                else:
                                                    if features["T(RIGHT) - time_left"] <= 0.377489:
                                                        return 2
                                                    else:
                                                        return 3
                                            else:
                                                if features["E(DOWN) - time_left"] <= 0.195510:
                                                    if features["agent_column - time_left"] <= 0.560000:
                                                        if features["E(RIGHT) - T(DOWN)"] <= -0.001794:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["T(DOWN) - time_left"] <= 0.450874:
                                                            if features["E(LEFT) - T(DOWN)"] <= 0.067651:
                                                                return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            return 3
                                                else:
                                                    if features["T(DOWN) - time_left"] <= 0.363830:
                                                        if features["T(RIGHT) - agent_column"] <= -0.361575:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["E(UP) - E(LEFT)"] <= 0.016192:
                                                            return 1
                                                        else:
                                                            if features["E(LEFT) - T(RIGHT)"] <= -0.599318:
                                                                return 3
                                                            else:
                                                                return 1
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.300032:
                                            if features["T(up) - agent_row"] <= -8.670113:
                                                if features["T(RIGHT) - time_left"] <= 0.188803:
                                                    return 2
                                                else:
                                                    return 3
                                            else:
                                                if features["E(RIGHT) - T(DOWN)"] <= -0.089776:
                                                    if features["T(up) - T(RIGHT)"] <= -0.015654:
                                                        if features["E(LEFT)"] <= 0.307929:
                                                            if features["E(DOWN) - time_left"] <= 0.299684:
                                                                if features["E(LEFT) - T(DOWN)"] <= -0.496482:
                                                                    if features["E(LEFT) - E(RIGHT)"] <= -0.117575:
                                                                        if features["T(DOWN) - agent_column"] <= -0.315202:
                                                                            if features["E(RIGHT) - T(DOWN)"] <= -0.399475:
                                                                                return 3
                                                                            else:
                                                                                if features["E(RIGHT) - agent_row"] <= -7.591973:
                                                                                    return 0
                                                                                else:
                                                                                    return 3
                                                                        else:
                                                                            return 0
                                                                    else:
                                                                        if features["T(RIGHT) - agent_row"] <= -4.223281:
                                                                            if features["agent_row - time_left"] <= 6.390000:
                                                                                return 2
                                                                            else:
                                                                                return 0
                                                                        else:
                                                                            return 1
                                                                else:
                                                                    if features["E(LEFT) - time_left"] <= -0.023986:
                                                                        if features["E(LEFT) - T(LEFT)"] <= 0.047807:
                                                                            return 3
                                                                        else:
                                                                            if features["E(LEFT) - agent_row"] <= -7.805388:
                                                                                return 0
                                                                            else:
                                                                                return 2
                                                                    else:
                                                                        if features["E(UP) - T(RIGHT)"] <= -0.424128:
                                                                            if features["T(RIGHT) - agent_row"] <= -3.370242:
                                                                                if features["agent_row - agent_column"] <= -0.500000:
                                                                                    return 2
                                                                                else:
                                                                                    return 0
                                                                            else:
                                                                                return 1
                                                                        else:
                                                                            if features["E(UP) - E(RIGHT)"] <= -0.147651:
                                                                                if features["T(RIGHT) - agent_row"] <= -4.509837:
                                                                                    if features["T(RIGHT) - agent_column"] <= -1.502128:
                                                                                        return 2
                                                                                    else:
                                                                                        return 3
                                                                                else:
                                                                                    if features["T(DOWN) - time_left"] <= 0.352342:
                                                                                        return 0
                                                                                    else:
                                                                                        return 1
                                                                            else:
                                                                                if features["E(DOWN) - T(DOWN)"] <= -0.294581:
                                                                                    return 0
                                                                                else:
                                                                                    if features["E(DOWN) - T(RIGHT)"] <= -0.108970:
                                                                                        if features["T(RIGHT) - agent_row"] <= -6.501337:
                                                                                            return 2
                                                                                        else:
                                                                                            if features["E(RIGHT) - T(LEFT)"] <= 0.276544:
                                                                                                if features["E(LEFT) - T(RIGHT)"] <= -0.225925:
                                                                                                    return 2
                                                                                                else:
                                                                                                    return 0
                                                                                            else:
                                                                                                if features["E(RIGHT) - T(DOWN)"] <= -0.143239:
                                                                                                    return 0
                                                                                                else:
                                                                                                    return 2
                                                                                    else:
                                                                                        return 0
                                                            else:
                                                                if features["E(RIGHT) - T(LEFT)"] <= 0.240678:
                                                                    return 1
                                                                else:
                                                                    if features["E(LEFT) - T(RIGHT)"] <= -0.338150:
                                                                        return 1
                                                                    else:
                                                                        return 0
                                                        else:
                                                            if features["T(RIGHT)"] <= 0.657258:
                                                                return 2
                                                            else:
                                                                return 0
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.208681:
                                                        if features["T(RIGHT) - agent_row"] <= -4.677019:
                                                            if features["E(DOWN)"] <= 0.201200:
                                                                if features["E(DOWN) - T(RIGHT)"] <= -0.299161:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["E(DOWN) - time_left"] <= -0.096664:
                                                                    if features["T(up) - time_left"] <= 0.075754:
                                                                        if features["E(UP) - E(DOWN)"] <= 0.057191:
                                                                            return 0
                                                                        else:
                                                                            return 2
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    if features["agent_row - time_left"] <= 6.900000:
                                                                        if features["E(LEFT) - T(RIGHT)"] <= -0.604290:
                                                                            return 3
                                                                        else:
                                                                            if features["E(DOWN) - T(DOWN)"] <= 0.270620:
                                                                                if features["T(RIGHT) - agent_column"] <= -0.507849:
                                                                                    if features["T(RIGHT) - time_left"] <= 0.132978:
                                                                                        return 2
                                                                                    else:
                                                                                        if features["E(UP) - time_left"] <= 0.205934:
                                                                                            return 2
                                                                                        else:
                                                                                            return 0
                                                                                else:
                                                                                    return 2
                                                                            else:
                                                                                if features["E(RIGHT) - T(up)"] <= 0.368243:
                                                                                    return 2
                                                                                else:
                                                                                    if features["E(LEFT) - T(RIGHT)"] <= -0.293908:
                                                                                        return 1
                                                                                    else:
                                                                                        return 2
                                                                    else:
                                                                        if features["T(LEFT) - agent_row"] <= -6.931593:
                                                                            if features["E(RIGHT) - T(LEFT)"] <= 0.374257:
                                                                                if features["E(LEFT) - T(RIGHT)"] <= -0.526100:
                                                                                    return 0
                                                                                else:
                                                                                    return 2
                                                                            else:
                                                                                if features["T(up) - time_left"] <= 0.217508:
                                                                                    if features["E(LEFT) - T(DOWN)"] <= 0.070590:
                                                                                        if features["time_left"] <= 0.080000:
                                                                                            return 0
                                                                                        else:
                                                                                            return 2
                                                                                    else:
                                                                                        return 0
                                                                                else:
                                                                                    if features["T(up) - T(LEFT)"] <= 0.511428:
                                                                                        return 2
                                                                                    else:
                                                                                        if features["E(LEFT) - T(RIGHT)"] <= -0.588092:
                                                                                            return 3
                                                                                        else:
                                                                                            return 2
                                                                        else:
                                                                            return 0
                                                        else:
                                                            if features["T(LEFT) - time_left"] <= 0.090928:
                                                                if features["T(RIGHT) - time_left"] <= 0.385142:
                                                                    if features["agent_row - time_left"] <= 4.660000:
                                                                        return 0
                                                                    else:
                                                                        if features["T(DOWN) - T(RIGHT)"] <= -0.405447:
                                                                            return 1
                                                                        else:
                                                                            return 2
                                                                else:
                                                                    if features["T(up) - agent_column"] <= -1.234590:
                                                                        return 1
                                                                    else:
                                                                        return 3
                                                            else:
                                                                if features["T(DOWN) - T(RIGHT)"] <= 0.046456:
                                                                    return 3
                                                                else:
                                                                    if features["E(LEFT) - time_left"] <= 0.177712:
                                                                        return 0
                                                                    else:
                                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - agent_row"] <= -6.630088:
                                                            if features["T(RIGHT) - agent_column"] <= -3.588344:
                                                                if features["E(RIGHT) - T(up)"] <= 0.030325:
                                                                    if features["T(RIGHT) - agent_column"] <= -5.694950:
                                                                        if features["E(LEFT)"] <= 0.321807:
                                                                            if features["E(RIGHT) - time_left"] <= 0.271373:
                                                                                return 2
                                                                            else:
                                                                                return 3
                                                                        else:
                                                                            return 0
                                                                    else:
                                                                        if features["E(RIGHT) - T(LEFT)"] <= 0.060117:
                                                                            return 1
                                                                        else:
                                                                            if features["E(DOWN) - T(LEFT)"] <= 0.211556:
                                                                                return 0
                                                                            else:
                                                                                if features["agent_row - time_left"] <= 8.940000:
                                                                                    return 2
                                                                                else:
                                                                                    return 0
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["E(RIGHT) - time_left"] <= 0.366519:
                                                                    if features["T(DOWN) - T(RIGHT)"] <= -0.164846:
                                                                        if features["T(up) - agent_row"] <= -7.733930:
                                                                            return 0
                                                                        else:
                                                                            if features["E(DOWN) - T(up)"] <= -0.227789:
                                                                                return 3
                                                                            else:
                                                                                return 2
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    if features["T(LEFT) - time_left"] <= 0.003844:
                                                                        if features["E(LEFT) - T(RIGHT)"] <= -0.379012:
                                                                            return 3
                                                                        else:
                                                                            return 0
                                                                    else:
                                                                        return 2
                                                        else:
                                                            if features["T(LEFT)"] <= 0.136476:
                                                                if features["E(DOWN) - T(RIGHT)"] <= -0.135735:
                                                                    if features["E(UP) - time_left"] <= 0.220218:
                                                                        if features["T(RIGHT)"] <= 0.420041:
                                                                            return 0
                                                                        else:
                                                                            return 3
                                                                    else:
                                                                        return 3
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["T(up) - agent_row"] <= -5.759322:
                                                                    return 0
                                                                else:
                                                                    if features["T(RIGHT) - agent_column"] <= -7.237128:
                                                                        return 0
                                                                    else:
                                                                        if features["E(UP) - E(LEFT)"] <= 0.015264:
                                                                            return 1
                                                                        else:
                                                                            return 3
                                        else:
                                            if features["E(DOWN) - T(up)"] <= 0.324980:
                                                if features["E(LEFT) - T(RIGHT)"] <= -0.359271:
                                                    if features["T(up) - agent_column"] <= -7.333379:
                                                        return 2
                                                    else:
                                                        if features["E(DOWN) - time_left"] <= 0.119684:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.134228:
                                                        if features["T(RIGHT) - agent_column"] <= -2.572051:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                            else:
                                                return 1
                            else:
                                if features["E(LEFT) - T(RIGHT)"] <= -0.245643:
                                    if features["T(LEFT) - T(RIGHT)"] <= -0.331168:
                                        if features["E(DOWN) - time_left"] <= 0.230810:
                                            if features["E(UP) - T(up)"] <= 0.087884:
                                                if features["agent_column - time_left"] <= 3.780000:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["agent_column - time_left"] <= 7.720000:
                                                    return 0
                                                else:
                                                    return 2
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -6.340798:
                                                if features["E(RIGHT) - T(RIGHT)"] <= -0.300917:
                                                    if features["E(DOWN) - T(RIGHT)"] <= -0.430036:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.376208:
                                                    if features["T(DOWN) - agent_row"] <= -2.366832:
                                                        if features["T(RIGHT) - agent_column"] <= -4.554097:
                                                            return 0
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                                else:
                                                    return 2
                                    else:
                                        return 3
                                else:
                                    if features["T(RIGHT) - time_left"] <= 0.046621:
                                        if features["T(LEFT) - agent_column"] <= -8.560237:
                                            return 0
                                        else:
                                            if features["agent_column - time_left"] <= 8.880000:
                                                if features["T(RIGHT) - time_left"] <= -0.220000:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 1
                                    else:
                                        if features["E(LEFT) - T(up)"] <= 0.260157:
                                            if features["T(DOWN)"] <= 0.149850:
                                                return 1
                                            else:
                                                if features["E(DOWN) - E(LEFT)"] <= 0.178233:
                                                    return 0
                                                else:
                                                    if features["E(LEFT) - time_left"] <= 0.183684:
                                                        if features["T(RIGHT) - time_left"] <= 0.335750:
                                                            return 0
                                                        else:
                                                            return 1
                                                    else:
                                                        return 3
                                        else:
                                            return 2
                    else:
                        if features["E(LEFT) - T(LEFT)"] <= 0.281975:
                            if features["E(UP)"] <= 0.384758:
                                if features["E(LEFT) - T(up)"] <= 0.257678:
                                    if features["E(UP) - E(DOWN)"] <= 0.263242:
                                        if features["E(RIGHT) - T(up)"] <= -0.387392:
                                            if features["E(LEFT) - time_left"] <= 0.274487:
                                                if features["T(LEFT) - agent_column"] <= -5.298474:
                                                    if features["E(LEFT) - T(up)"] <= -0.118239:
                                                        if features["agent_row - time_left"] <= 10.860000:
                                                            if features["E(RIGHT) - T(LEFT)"] <= -0.589613:
                                                                return 2
                                                            else:
                                                                if features["E(LEFT) - agent_row"] <= -5.679686:
                                                                    if features["E(DOWN) - agent_column"] <= -7.707132:
                                                                        return 1
                                                                    else:
                                                                        if features["T(up) - agent_row"] <= -5.263995:
                                                                            return 3
                                                                        else:
                                                                            return 1
                                                                else:
                                                                    return 1
                                                        else:
                                                            return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(RIGHT) - T(LEFT)"] <= 0.414324:
                                                        if features["E(UP)"] <= 0.122934:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 2
                                            else:
                                                if features["agent_row - time_left"] <= 9.940000:
                                                    if features["E(DOWN) - T(LEFT)"] <= -0.282915:
                                                        if features["E(DOWN) - E(LEFT)"] <= -0.030918:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(up)"] <= 0.624733:
                                                        return 2
                                                    else:
                                                        return 0
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= 0.320126:
                                                if features["T(RIGHT) - time_left"] <= 0.106123:
                                                    if features["E(RIGHT) - T(up)"] <= 0.373426:
                                                        if features["E(DOWN) - T(DOWN)"] <= 0.334192:
                                                            if features["E(LEFT) - T(LEFT)"] <= 0.213716:
                                                                if features["E(LEFT) - T(DOWN)"] <= 0.278036:
                                                                    if features["E(DOWN) - T(RIGHT)"] <= 0.031845:
                                                                        if features["E(UP) - time_left"] <= 0.257535:
                                                                            return 0
                                                                        else:
                                                                            return 3
                                                                    else:
                                                                        if features["E(UP) - time_left"] <= -0.097963:
                                                                            return 0
                                                                        else:
                                                                            if features["E(UP) - T(up)"] <= 0.287134:
                                                                                return 3
                                                                            else:
                                                                                if features["T(DOWN) - agent_column"] <= -4.373931:
                                                                                    return 3
                                                                                else:
                                                                                    return 0
                                                                else:
                                                                    if features["T(LEFT)"] <= 0.501667:
                                                                        if features["agent_row - time_left"] <= 5.560000:
                                                                            return 1
                                                                        else:
                                                                            if features["E(UP) - time_left"] <= 0.209040:
                                                                                return 3
                                                                            else:
                                                                                if features["E(LEFT) - T(RIGHT)"] <= 0.346153:
                                                                                    return 3
                                                                                else:
                                                                                    return 0
                                                                    else:
                                                                        if features["agent_column - time_left"] <= 8.740000:
                                                                            return 3
                                                                        else:
                                                                            if features["E(DOWN) - T(LEFT)"] <= -0.230634:
                                                                                return 3
                                                                            else:
                                                                                return 1
                                                            else:
                                                                if features["E(LEFT) - T(DOWN)"] <= 0.228900:
                                                                    if features["E(DOWN) - T(DOWN)"] <= -0.234495:
                                                                        return 3
                                                                    else:
                                                                        if features["E(LEFT) - T(up)"] <= 0.240678:
                                                                            return 3
                                                                        else:
                                                                            return 0
                                                                else:
                                                                    return 3
                                                        else:
                                                            if features["E(UP) - T(LEFT)"] <= -0.493468:
                                                                return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["E(LEFT) - agent_row"] <= -5.929529:
                                                            return 0
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(RIGHT) - T(LEFT)"] <= -0.119556:
                                                        if features["T(LEFT) - time_left"] <= 0.318801:
                                                            if features["agent_row - time_left"] <= 9.960000:
                                                                if features["T(RIGHT) - agent_row"] <= -9.328664:
                                                                    return 3
                                                                else:
                                                                    if features["T(DOWN) - agent_row"] <= -7.759322:
                                                                        return 0
                                                                    else:
                                                                        return 1
                                                            else:
                                                                return 1
                                                        else:
                                                            if features["T(LEFT) - time_left"] <= 0.359818:
                                                                if features["E(LEFT) - T(RIGHT)"] <= 0.181615:
                                                                    if features["E(UP) - T(DOWN)"] <= 0.145783:
                                                                        if features["T(LEFT) - agent_column"] <= -9.154619:
                                                                            return 0
                                                                        else:
                                                                            return 1
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["agent_row - agent_column"] <= -4.500000:
                                                                    return 2
                                                                else:
                                                                    return 3
                                                    else:
                                                        if features["E(LEFT) - time_left"] <= 0.234148:
                                                            return 0
                                                        else:
                                                            if features["E(LEFT) - time_left"] <= 0.314980:
                                                                return 3
                                                            else:
                                                                return 0
                                            else:
                                                if features["T(DOWN) - time_left"] <= -0.060000:
                                                    if features["E(LEFT) - time_left"] <= 0.242638:
                                                        if features["E(LEFT) - T(LEFT)"] <= -0.301545:
                                                            if features["agent_row - time_left"] <= 8.840000:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["T(up) - agent_column"] <= -9.463992:
                                                                return 3
                                                            else:
                                                                if features["T(up) - agent_column"] <= -8.540618:
                                                                    if features["E(RIGHT) - time_left"] <= -0.058664:
                                                                        return 3
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    if features["T(up)"] <= 0.559898:
                                                                        return 3
                                                                    else:
                                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(DOWN) - T(up)"] <= 0.128352:
                                                        if features["T(LEFT) - agent_column"] <= -6.816975:
                                                            if features["E(LEFT) - T(LEFT)"] <= -0.245633:
                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            return 3
                                                    else:
                                                        return 0
                                    else:
                                        if features["E(DOWN)"] <= 0.016868:
                                            if features["agent_row - time_left"] <= 10.300000:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(LEFT) - time_left"] <= 0.311092:
                                                if features["E(DOWN) - agent_column"] <= -10.908845:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["E(LEFT) - T(up)"] <= -0.067765:
                                                    return 0
                                                else:
                                                    return 2
                                else:
                                    if features["E(DOWN) - time_left"] <= 0.238727:
                                        if features["E(LEFT) - T(LEFT)"] <= -0.091705:
                                            if features["E(RIGHT) - agent_column"] <= -7.759322:
                                                if features["E(UP) - time_left"] <= 0.183336:
                                                    if features["E(UP) - T(DOWN)"] <= -0.257255:
                                                        if features["E(LEFT) - agent_column"] <= -10.630182:
                                                            if features["T(DOWN) - agent_row"] <= -4.429535:
                                                                if features["E(DOWN) - time_left"] <= 0.116845:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["E(DOWN) - T(LEFT)"] <= -0.112008:
                                                                    return 2
                                                                else:
                                                                    return 3
                                                        else:
                                                            if features["E(DOWN) - T(DOWN)"] <= -0.143522:
                                                                if features["T(LEFT) - agent_row"] <= -4.410987:
                                                                    if features["E(LEFT) - time_left"] <= 0.222942:
                                                                        if features["E(DOWN) - T(LEFT)"] <= -0.174516:
                                                                            if features["E(UP) - E(LEFT)"] <= -0.132495:
                                                                                return 0
                                                                            else:
                                                                                if features["E(RIGHT) - T(DOWN)"] <= -0.450090:
                                                                                    return 0
                                                                                else:
                                                                                    if features["T(DOWN) - T(RIGHT)"] <= 0.522255:
                                                                                        return 0
                                                                                    else:
                                                                                        return 3
                                                                        else:
                                                                            return 3
                                                                    else:
                                                                        if features["E(UP) - agent_column"] <= -10.786629:
                                                                            return 2
                                                                        else:
                                                                            return 0
                                                                else:
                                                                    if features["E(LEFT) - T(LEFT)"] <= -0.317644:
                                                                        return 1
                                                                    else:
                                                                        if features["agent_column - time_left"] <= 9.740000:
                                                                            return 0
                                                                        else:
                                                                            return 2
                                                            else:
                                                                if features["T(DOWN) - time_left"] <= 0.262719:
                                                                    return 0
                                                                else:
                                                                    if features["T(DOWN) - agent_row"] <= -1.552835:
                                                                        return 0
                                                                    else:
                                                                        return 3
                                                    else:
                                                        if features["E(DOWN) - T(DOWN)"] <= 0.280189:
                                                            if features["E(DOWN) - T(DOWN)"] <= -0.175837:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            return 1
                                                else:
                                                    if features["E(LEFT) - agent_row"] <= -6.630088:
                                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.015400:
                                                            return 2
                                                        else:
                                                            if features["E(DOWN) - E(RIGHT)"] <= 0.062540:
                                                                return 0
                                                            else:
                                                                if features["E(RIGHT) - T(DOWN)"] <= 0.073987:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                    else:
                                                        if features["E(LEFT) - T(DOWN)"] <= -0.262020:
                                                            return 0
                                                        else:
                                                            return 2
                                            else:
                                                if features["E(DOWN) - E(LEFT)"] <= -0.030121:
                                                    if features["T(DOWN) - agent_column"] <= -7.457420:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(LEFT) - T(LEFT)"] <= -0.303655:
                                                        if features["E(UP) - T(LEFT)"] <= -0.570380:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(DOWN) - agent_row"] <= -5.776730:
                                                            return 3
                                                        else:
                                                            if features["T(up) - T(DOWN)"] <= -0.478356:
                                                                return 3
                                                            else:
                                                                if features["T(DOWN) - T(LEFT)"] <= -0.472957:
                                                                    return 1
                                                                else:
                                                                    return 0
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= 0.053067:
                                                if features["E(DOWN) - E(LEFT)"] <= 0.030714:
                                                    if features["E(RIGHT) - T(DOWN)"] <= -0.322954:
                                                        if features["T(LEFT) - T(RIGHT)"] <= 0.447717:
                                                            return 3
                                                        else:
                                                            if features["T(DOWN) - agent_row"] <= -4.505345:
                                                                return 3
                                                            else:
                                                                return 2
                                                    else:
                                                        if features["E(DOWN) - T(DOWN)"] <= 0.283524:
                                                            return 3
                                                        else:
                                                            return 1
                                                else:
                                                    if features["T(DOWN) - time_left"] <= 0.086562:
                                                        return 1
                                                    else:
                                                        if features["T(DOWN) - time_left"] <= 0.641784:
                                                            return 0
                                                        else:
                                                            return 1
                                            else:
                                                if features["E(RIGHT) - time_left"] <= -0.001751:
                                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.015400:
                                                        return 2
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= -0.217202:
                                            if features["E(DOWN) - T(DOWN)"] <= 0.309607:
                                                if features["agent_column - time_left"] <= 9.920000:
                                                    if features["E(UP) - agent_row"] <= -2.863524:
                                                        if features["T(DOWN) - agent_row"] <= -4.345659:
                                                            if features["T(LEFT) - agent_column"] <= -7.507703:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(UP) - T(LEFT)"] <= -0.368317:
                                                                if features["agent_column - time_left"] <= 8.920000:
                                                                    return 1
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["T(DOWN) - agent_row"] <= -2.509309:
                                                                    return 1
                                                                else:
                                                                    return 2
                                                    else:
                                                        if features["E(RIGHT) - T(LEFT)"] <= -0.449899:
                                                            if features["E(UP) - agent_row"] <= -1.907444:
                                                                return 1
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(RIGHT) - T(DOWN)"] <= -0.271374:
                                                                return 3
                                                            else:
                                                                return 1
                                                else:
                                                    if features["T(DOWN) - T(RIGHT)"] <= 0.598614:
                                                        if features["E(RIGHT) - time_left"] <= 0.034934:
                                                            if features["E(LEFT) - T(RIGHT)"] <= 0.365899:
                                                                return 3
                                                            else:
                                                                return 2
                                                        else:
                                                            return 2
                                                    else:
                                                        return 2
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.505008:
                                                    if features["E(LEFT) - T(RIGHT)"] <= 0.314830:
                                                        return 1
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -3.220225:
                                                            return 1
                                                        else:
                                                            return 2
                                                else:
                                                    return 1
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -8.850028:
                                                return 2
                                            else:
                                                if features["T(DOWN) - agent_column"] <= -6.361575:
                                                    return 0
                                                else:
                                                    return 1
                            else:
                                if features["T(LEFT) - time_left"] <= 0.313656:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.020420:
                                        if features["E(DOWN)"] <= 0.090692:
                                            return 1
                                        else:
                                            if features["E(LEFT) - T(RIGHT)"] <= 0.027140:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        if features["E(RIGHT) - T(up)"] <= -0.138604:
                                            if features["E(LEFT) - time_left"] <= 0.245219:
                                                if features["T(LEFT)"] <= 0.386721:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 2
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.157814:
                                        return 3
                                    else:
                                        if features["T(LEFT) - T(RIGHT)"] <= 0.405447:
                                            return 2
                                        else:
                                            return 0
                        else:
                            if features["E(UP) - T(up)"] <= 0.276544:
                                if features["E(DOWN) - agent_column"] <= -7.707132:
                                    if features["E(RIGHT) - time_left"] <= 0.028463:
                                        if features["E(DOWN) - time_left"] <= -0.097010:
                                            return 3
                                        else:
                                            if features["E(DOWN) - T(up)"] <= -0.510096:
                                                return 0
                                            else:
                                                return 2
                                    else:
                                        return 2
                                else:
                                    if features["T(DOWN) - agent_column"] <= -7.833565:
                                        return 1
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.495388:
                                            return 1
                                        else:
                                            if features["agent_row - time_left"] <= 3.800000:
                                                return 2
                                            else:
                                                return 0
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.221289:
                                    return 0
                                else:
                                    return 2
                else:
                    if features["E(LEFT) - time_left"] <= 0.336173:
                        if features["E(UP) - agent_column"] <= -13.747773:
                            if features["E(DOWN) - T(DOWN)"] <= -0.065551:
                                if features["E(UP) - T(LEFT)"] <= -0.162406:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(UP) - T(LEFT)"] <= -0.249868:
                                    return 2
                                else:
                                    if features["T(LEFT) - agent_column"] <= -13.698653:
                                        return 2
                                    else:
                                        return 1
                        else:
                            if features["E(UP) - T(up)"] <= 0.280923:
                                if features["E(UP)"] <= 0.377370:
                                    if features["T(up) - time_left"] <= -0.280000:
                                        if features["E(DOWN) - T(DOWN)"] <= -0.177786:
                                            if features["agent_row - time_left"] <= -0.500000:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["E(UP) - time_left"] <= -0.166778:
                                                if features["E(LEFT) - agent_row"] <= -5.388545:
                                                    if features["E(LEFT) - time_left"] <= 0.029566:
                                                        return 1
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -7.831368:
                                                            return 2
                                                        else:
                                                            return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["E(LEFT) - T(RIGHT)"] <= 0.450124:
                                                    return 2
                                                else:
                                                    return 1
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -13.655679:
                                            return 1
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.198884:
                                                return 2
                                            else:
                                                if features["T(LEFT) - agent_column"] <= -12.592049:
                                                    return 1
                                                else:
                                                    return 2
                                else:
                                    if features["T(LEFT) - agent_column"] <= -4.441678:
                                        if features["E(UP) - E(DOWN)"] <= 0.344074:
                                            if features["T(DOWN) - T(LEFT)"] <= -0.455983:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 0
                                    else:
                                        return 0
                            else:
                                if features["E(DOWN) - time_left"] <= -0.063346:
                                    return 0
                                else:
                                    return 2
                    else:
                        if features["E(UP) - T(DOWN)"] <= 0.377370:
                            if features["E(UP) - T(up)"] <= 0.290888:
                                if features["E(DOWN) - T(RIGHT)"] <= 0.286371:
                                    if features["E(LEFT) - T(up)"] <= -0.377530:
                                        if features["E(UP) - T(up)"] <= -0.576788:
                                            return 2
                                        else:
                                            if features["agent_row - agent_column"] <= -0.500000:
                                                return 0
                                            else:
                                                return 2
                                    else:
                                        if features["agent_row - agent_column"] <= -13.500000:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= -0.155837:
                                        if features["E(UP) - T(DOWN)"] <= -0.109508:
                                            return 1
                                        else:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.123742:
                                                return 2
                                            else:
                                                if features["T(LEFT) - agent_column"] <= -13.682967:
                                                    return 2
                                                else:
                                                    return 1
                                    else:
                                        return 2
                            else:
                                if features["E(LEFT) - T(LEFT)"] <= -0.470608:
                                    return 0
                                else:
                                    if features["E(LEFT) - T(RIGHT)"] <= -0.384071:
                                        return 0
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.323294:
                                            if features["E(UP) - E(RIGHT)"] <= 0.367845:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                        else:
                            if features["T(LEFT) - agent_column"] <= -4.834318:
                                return 2
                            else:
                                return 0
            else:
                if features["E(LEFT) - E(RIGHT)"] <= 0.360110:
                    if features["E(DOWN)"] <= 0.029922:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.013236:
                            if features["E(UP) - time_left"] <= 0.315623:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.227218:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.084562:
                                        if features["T(DOWN) - agent_row"] <= -9.427629:
                                            return 0
                                        else:
                                            if features["T(DOWN) - time_left"] <= -0.200000:
                                                return 0
                                            else:
                                                return 3
                                    else:
                                        return 0
                                else:
                                    if features["E(LEFT) - T(DOWN)"] <= 0.345676:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.232286:
                                            if features["T(up) - time_left"] <= -0.730000:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - T(DOWN)"] <= 0.335422:
                                                    return 0
                                                else:
                                                    if features["T(DOWN) - T(RIGHT)"] <= -0.340523:
                                                        return 0
                                                    else:
                                                        return 3
                                        else:
                                            if features["E(UP) - T(DOWN)"] <= 0.454875:
                                                return 0
                                            else:
                                                if features["E(UP) - T(RIGHT)"] <= -0.039381:
                                                    return 0
                                                else:
                                                    return 3
                                    else:
                                        if features["E(UP)"] <= 0.505575:
                                            if features["agent_column - time_left"] <= 10.780000:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 3
                            else:
                                if features["E(DOWN) - T(up)"] <= -0.510883:
                                    if features["E(UP) - E(LEFT)"] <= 0.261835:
                                        if features["T(up) - agent_row"] <= -8.480145:
                                            if features["E(UP) - T(LEFT)"] <= 0.455212:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -6.678193:
                                                if features["T(up) - agent_row"] <= -8.410987:
                                                    return 3
                                                else:
                                                    if features["E(RIGHT) - time_left"] <= -0.013049:
                                                        return 3
                                                    else:
                                                        if features["E(UP) - T(LEFT)"] <= 0.514507:
                                                            return 0
                                                        else:
                                                            return 3
                                            else:
                                                return 3
                                    else:
                                        if features["T(up)"] <= 0.511915:
                                            if features["E(RIGHT) - T(DOWN)"] <= 0.282867:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.390643:
                                                if features["T(up) - time_left"] <= 0.364329:
                                                    if features["T(up) - agent_column"] <= -3.398729:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.230707:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.397216:
                                            if features["E(LEFT) - E(RIGHT)"] <= -0.363116:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["T(up) - T(RIGHT)"] <= 0.070822:
                                                return 0
                                            else:
                                                return 3
                                    else:
                                        if features["E(RIGHT) - agent_row"] <= -7.715893:
                                            if features["E(UP) - T(DOWN)"] <= 0.417843:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 0
                        else:
                            if features["T(DOWN) - time_left"] <= -0.240000:
                                if features["agent_row - time_left"] <= 3.680000:
                                    return 3
                                else:
                                    if features["time_left"] <= 0.300000:
                                        return 0
                                    else:
                                        if features["E(UP) - agent_row"] <= -7.510800:
                                            if features["agent_row - agent_column"] <= 1.500000:
                                                return 2
                                            else:
                                                return 3
                                        else:
                                            return 3
                            else:
                                if features["E(LEFT) - T(DOWN)"] <= 0.286371:
                                    if features["T(LEFT) - agent_column"] <= -4.562741:
                                        if features["E(DOWN) - E(RIGHT)"] <= -0.118991:
                                            if features["E(UP) - T(DOWN)"] <= 0.479300:
                                                return 0
                                            else:
                                                if features["E(LEFT) - T(LEFT)"] <= 0.240914:
                                                    return 0
                                                else:
                                                    if features["T(up) - agent_column"] <= -6.361575:
                                                        return 2
                                                    else:
                                                        return 0
                                        else:
                                            return 2
                                    else:
                                        if features["E(RIGHT) - agent_row"] <= -11.651228:
                                            return 0
                                        else:
                                            if features["E(LEFT) - T(up)"] <= 0.020276:
                                                if features["E(LEFT) - T(LEFT)"] <= 0.134113:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                else:
                                    if features["time_left"] <= 0.140000:
                                        if features["E(UP) - T(up)"] <= 0.002382:
                                            return 0
                                        else:
                                            if features["E(RIGHT) - T(LEFT)"] <= -0.228060:
                                                return 0
                                            else:
                                                return 2
                                    else:
                                        return 0
                    else:
                        if features["T(DOWN)"] <= 0.016179:
                            if features["T(LEFT) - agent_column"] <= -8.864256:
                                if features["T(RIGHT) - agent_column"] <= -8.340798:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["T(RIGHT) - agent_row"] <= -12.507610:
                                    if features["T(up) - T(LEFT)"] <= 0.301281:
                                        if features["agent_column - time_left"] <= 8.860000:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 1
                                else:
                                    if features["agent_column - time_left"] <= 7.530000:
                                        return 0
                                    else:
                                        return 2
                        else:
                            if features["E(UP) - E(LEFT)"] <= 0.172119:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.099920:
                                    return 1
                                else:
                                    return 3
                            else:
                                return 1
                else:
                    if features["agent_row - time_left"] <= 1.120000:
                        if features["E(UP) - T(up)"] <= 0.829918:
                            if features["T(DOWN) - T(LEFT)"] <= -0.603543:
                                return 2
                            else:
                                if features["T(up) - agent_column"] <= -1.113520:
                                    return 2
                                else:
                                    return 0
                        else:
                            if features["T(LEFT) - agent_column"] <= -1.216522:
                                if features["T(LEFT) - T(RIGHT)"] <= 0.571663:
                                    if features["agent_column - time_left"] <= 12.780000:
                                        if features["T(RIGHT) - agent_column"] <= -3.593340:
                                            if features["agent_column - time_left"] <= 8.700000:
                                                if features["E(UP) - time_left"] <= 0.708123:
                                                    if features["T(DOWN) - time_left"] <= -0.120179:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["E(RIGHT) - time_left"] <= -0.440000:
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
                                return 0
                    else:
                        if features["T(LEFT) - agent_column"] <= -2.366057:
                            if features["E(UP) - agent_row"] <= -10.166124:
                                if features["E(UP) - time_left"] <= -0.028663:
                                    if features["T(LEFT) - agent_column"] <= -9.559701:
                                        return 0
                                    else:
                                        if features["agent_row - agent_column"] <= 3.500000:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT) - agent_row"] <= -11.239443:
                                        if features["E(LEFT) - agent_column"] <= -8.355776:
                                            if features["E(UP) - T(RIGHT)"] <= 0.657354:
                                                if features["E(UP) - time_left"] <= 0.321944:
                                                    return 2
                                                else:
                                                    if features["T(LEFT) - agent_column"] <= -12.574568:
                                                        return 0
                                                    else:
                                                        return 2
                                            else:
                                                if features["agent_column - time_left"] <= 12.430000:
                                                    if features["T(LEFT) - agent_column"] <= -10.589945:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    return 0
                                        else:
                                            if features["E(LEFT) - agent_column"] <= -2.280124:
                                                if features["E(LEFT)"] <= 0.436350:
                                                    return 0
                                                else:
                                                    if features["T(up) - agent_column"] <= -2.681663:
                                                        if features["agent_row - agent_column"] <= 8.500000:
                                                            if features["E(DOWN) - E(LEFT)"] <= -0.730042:
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
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.833876:
                                            if features["T(LEFT) - time_left"] <= 0.279725:
                                                if features["E(LEFT)"] <= 0.403884:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(up) - agent_row"] <= -11.464012:
                                                return 0
                                            else:
                                                return 2
                            else:
                                if features["E(UP) - T(RIGHT)"] <= 0.602901:
                                    if features["E(LEFT) - T(DOWN)"] <= 0.198077:
                                        if features["T(LEFT) - agent_row"] <= -3.921267:
                                            if features["T(up) - T(LEFT)"] <= -0.015061:
                                                if features["E(UP) - T(RIGHT)"] <= 0.522007:
                                                    if features["T(LEFT) - agent_row"] <= -8.314004:
                                                        return 0
                                                    else:
                                                        if features["E(LEFT) - time_left"] <= -0.293298:
                                                            return 0
                                                        else:
                                                            return 2
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= 0.724273:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        if features["E(RIGHT) - T(up)"] <= -0.135124:
                                            if features["T(DOWN) - T(LEFT)"] <= 0.184032:
                                                if features["E(LEFT) - T(DOWN)"] <= 0.386394:
                                                    return 0
                                                else:
                                                    if features["E(UP) - T(RIGHT)"] <= 0.552826:
                                                        if features["T(up) - agent_column"] <= -2.786475:
                                                            if features["E(LEFT) - time_left"] <= 0.469654:
                                                                if features["T(LEFT) - agent_row"] <= -4.554097:
                                                                    if features["E(RIGHT) - T(up)"] <= -0.410238:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    if features["E(DOWN) - T(RIGHT)"] <= -0.518386:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                            else:
                                                                if features["E(LEFT) - agent_row"] <= -3.275714:
                                                                    if features["E(LEFT) - T(up)"] <= 0.613261:
                                                                        if features["E(LEFT) - T(up)"] <= 0.256658:
                                                                            return 2
                                                                        else:
                                                                            return 0
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    return 0
                                                        else:
                                                            if features["E(LEFT)"] <= 0.724271:
                                                                return 0
                                                            else:
                                                                if features["E(DOWN) - E(LEFT)"] <= -0.833876:
                                                                    if features["T(RIGHT) - agent_row"] <= -5.499849:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    return 2
                                                    else:
                                                        if features["E(RIGHT) - T(RIGHT)"] <= -0.255809:
                                                            return 0
                                                        else:
                                                            if features["T(LEFT) - agent_row"] <= -7.606347:
                                                                return 0
                                                            else:
                                                                if features["T(LEFT) - agent_row"] <= -4.449871:
                                                                    return 0
                                                                else:
                                                                    return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(up) - T(LEFT)"] <= -0.016192:
                                                if features["E(LEFT) - T(DOWN)"] <= 0.365750:
                                                    return 2
                                                else:
                                                    if features["E(LEFT) - T(LEFT)"] <= -0.097266:
                                                        return 2
                                                    else:
                                                        if features["E(LEFT) - T(RIGHT)"] <= 0.444825:
                                                            return 2
                                                        else:
                                                            return 0
                                            else:
                                                if features["E(UP) - agent_row"] <= -1.208409:
                                                    if features["T(RIGHT) - agent_row"] <= -2.336697:
                                                        if features["E(UP) - agent_row"] <= -2.239443:
                                                            if features["T(RIGHT) - agent_row"] <= -3.361575:
                                                                if features["E(UP) - agent_row"] <= -3.303427:
                                                                    if features["E(LEFT) - T(up)"] <= 0.713313:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["E(UP)"] <= 0.728881:
                                                                    return 2
                                                                else:
                                                                    if features["E(LEFT) - agent_column"] <= -2.252390:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["E(UP) - T(up)"] <= 0.734280:
                                                            return 2
                                                        else:
                                                            if features["E(UP) - agent_column"] <= -3.166124:
                                                                return 0
                                                            else:
                                                                return 2
                                                else:
                                                    return 0
                                else:
                                    if features["agent_row - agent_column"] <= -1.500000:
                                        if features["T(up) - agent_row"] <= -2.156573:
                                            if features["T(LEFT) - agent_column"] <= -5.556233:
                                                if features["E(LEFT) - E(RIGHT)"] <= 0.833876:
                                                    return 0
                                                else:
                                                    if features["T(RIGHT) - agent_row"] <= -4.887016:
                                                        if features["T(RIGHT) - time_left"] <= -0.790000:
                                                            return 3
                                                        else:
                                                            if features["T(DOWN) - agent_column"] <= -12.758342:
                                                                return 0
                                                            else:
                                                                if features["T(LEFT) - agent_column"] <= -10.623407:
                                                                    if features["T(DOWN) - agent_column"] <= -11.746942:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    if features["T(LEFT) - agent_row"] <= -8.240346:
                                                                        return 2
                                                                    else:
                                                                        if features["T(up) - agent_row"] <= -4.275714:
                                                                            return 0
                                                                        else:
                                                                            return 2
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(UP) - T(DOWN)"] <= 0.664643:
                                                    if features["E(UP) - T(RIGHT)"] <= 0.760557:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    return 0
                                        else:
                                            if features["E(UP)"] <= 0.791591:
                                                if features["E(LEFT) - T(RIGHT)"] <= 0.730042:
                                                    return 2
                                                else:
                                                    if features["T(DOWN) - time_left"] <= -0.530000:
                                                        return 3
                                                    else:
                                                        if features["E(UP) - T(LEFT)"] <= 0.055224:
                                                            return 0
                                                        else:
                                                            return 2
                                            else:
                                                return 0
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -4.271122:
                                            if features["E(LEFT) - T(up)"] <= 0.833876:
                                                if features["T(LEFT) - time_left"] <= -0.175367:
                                                    return 0
                                                else:
                                                    if features["T(up) - time_left"] <= -0.163862:
                                                        return 2
                                                    else:
                                                        return 0
                                            else:
                                                return 0
                                        else:
                                            if features["T(DOWN) - agent_row"] <= -2.564745:
                                                return 0
                                            else:
                                                return 2
                        else:
                            if features["E(UP) - E(RIGHT)"] <= 0.799069:
                                return 0
                            else:
                                if features["T(LEFT) - agent_column"] <= -1.113520:
                                    if features["T(up) - T(RIGHT)"] <= -0.086514:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    if features["T(RIGHT) - agent_column"] <= -0.582027:
                                        return 0
                                    else:
                                        if features["T(RIGHT)"] <= 0.418981:
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
