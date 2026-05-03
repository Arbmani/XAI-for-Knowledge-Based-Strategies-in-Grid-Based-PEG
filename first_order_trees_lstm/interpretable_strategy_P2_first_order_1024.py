import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(DOWN) - E(LEFT)"] <= 0.000000:
        if features["E(UP) - E(LEFT)"] <= -0.261030:
            if features["E(DOWN)"] <= 0.157217:
                if features["E(UP) - T(RIGHT)"] <= 0.000001:
                    if features["time_left"] <= 0.840000:
                        return 2
                    else:
                        return 1
                else:
                    if features["E(LEFT) - time_left"] <= 0.231277:
                        if features["E(LEFT) - time_left"] <= -0.413385:
                            return 1
                        else:
                            return 2
                    else:
                        if features["E(LEFT) - T(LEFT)"] <= 0.269930:
                            return 2
                        else:
                            if features["E(UP) - E(LEFT)"] <= -0.904711:
                                return 0
                            else:
                                return 2
            else:
                if features["E(RIGHT)"] <= 0.000023:
                    if features["E(LEFT) - E(RIGHT)"] <= 0.800400:
                        if features["E(RIGHT) - T(RIGHT)"] <= -0.000000:
                            if features["E(UP) - agent_column"] <= -1.999963:
                                return 2
                            else:
                                if features["T(up) - T(LEFT)"] <= 0.000089:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["T(up) - agent_column"] <= -13.994606:
                                if features["T(LEFT) - agent_row"] <= -1.395844:
                                    if features["E(UP)"] <= 0.000113:
                                        return 2
                                    else:
                                        if features["E(DOWN) - T(LEFT)"] <= -0.149524:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - T(up)"] <= -0.000000:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    return 2
                            else:
                                if features["T(up) - agent_column"] <= -13.845011:
                                    if features["E(UP) - T(up)"] <= 0.026091:
                                        if features["agent_column - time_left"] <= 13.920000:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(LEFT) - T(DOWN)"] <= 0.083988:
                                            return 2
                                        else:
                                            return 0
                                else:
                                    if features["E(UP) - T(LEFT)"] <= -0.271926:
                                        if features["E(DOWN) - T(LEFT)"] <= -0.139904:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.431482:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 2
                                    else:
                                        if features["E(LEFT) - T(DOWN)"] <= 0.368452:
                                            if features["T(LEFT) - time_left"] <= -0.350059:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 1
                    else:
                        if features["E(UP) - E(RIGHT)"] <= -0.000001:
                            if features["T(DOWN) - agent_column"] <= -0.821425:
                                if features["T(DOWN) - agent_row"] <= -2.650005:
                                    if features["E(LEFT) - agent_row"] <= -4.131923:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 2
                            else:
                                return 1
                        else:
                            if features["T(RIGHT) - agent_row"] <= -11.919503:
                                return 2
                            else:
                                if features["E(RIGHT) - agent_column"] <= -12.000000:
                                    if features["E(RIGHT) - agent_row"] <= -2.000000:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    if features["E(DOWN) - agent_row"] <= -6.133825:
                                        if features["agent_row - agent_column"] <= 10.500000:
                                            if features["E(UP) - E(RIGHT)"] <= 0.000350:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 2
                                    else:
                                        if features["T(up) - agent_column"] <= -1.999928:
                                            if features["E(UP) - agent_column"] <= -4.999994:
                                                if features["E(DOWN) - T(RIGHT)"] <= 0.866105:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 2
                                        else:
                                            return 1
                else:
                    if features["E(DOWN)"] <= 0.386858:
                        if features["E(RIGHT)"] <= 0.015779:
                            if features["T(up) - time_left"] <= -0.166477:
                                if features["T(LEFT) - agent_column"] <= -12.599187:
                                    if features["T(up) - T(LEFT)"] <= -0.000579:
                                        return 1
                                    else:
                                        return 0
                                else:
                                    if features["E(LEFT) - T(RIGHT)"] <= 0.453216:
                                        if features["E(UP) - time_left"] <= -0.717628:
                                            return 3
                                        else:
                                            if features["T(LEFT) - time_left"] <= -0.370685:
                                                return 2
                                            else:
                                                if features["T(RIGHT) - agent_column"] <= -8.999337:
                                                    return 2
                                                else:
                                                    return 0
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= -0.144345:
                                            return 2
                                        else:
                                            return 1
                            else:
                                if features["T(RIGHT) - time_left"] <= -0.027207:
                                    if features["E(UP) - T(LEFT)"] <= -0.284425:
                                        if features["E(RIGHT) - time_left"] <= -0.283879:
                                            if features["agent_row - agent_column"] <= -3.500000:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(UP) - T(up)"] <= 0.042839:
                                                return 2
                                            else:
                                                if features["E(RIGHT) - T(RIGHT)"] <= 0.010370:
                                                    if features["E(DOWN) - agent_column"] <= -12.715255:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(UP) - agent_row"] <= -3.909202:
                                                        return 2
                                                    else:
                                                        return 0
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -12.700617:
                                            if features["E(DOWN) - T(DOWN)"] <= -0.003507:
                                                return 2
                                            else:
                                                if features["E(DOWN) - time_left"] <= 0.225733:
                                                    if features["E(RIGHT) - T(up)"] <= -0.033497:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 1
                                        else:
                                            if features["T(DOWN) - agent_row"] <= -2.633823:
                                                return 2
                                            else:
                                                return 0
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.334959:
                                        if features["E(LEFT) - agent_row"] <= -7.510930:
                                            return 3
                                        else:
                                            return 2
                                    else:
                                        return 0
                        else:
                            if features["E(RIGHT) - agent_column"] <= -12.982530:
                                return 0
                            else:
                                if features["T(up) - time_left"] <= -0.529942:
                                    return 3
                                else:
                                    if features["E(LEFT) - agent_row"] <= -5.564953:
                                        if features["agent_row - time_left"] <= 8.700000:
                                            if features["T(LEFT) - time_left"] <= -0.439714:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 3
                                    else:
                                        if features["E(LEFT) - T(up)"] <= 0.297327:
                                            if features["T(DOWN) - agent_column"] <= -6.999914:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(up) - agent_column"] <= -11.997629:
                                                return 1
                                            else:
                                                if features["E(LEFT) - agent_column"] <= -7.554593:
                                                    if features["T(up) - T(RIGHT)"] <= 0.000002:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 1
                    else:
                        if features["E(LEFT) - E(RIGHT)"] <= 0.497204:
                            if features["T(LEFT) - time_left"] <= 0.287680:
                                if features["E(UP) - T(LEFT)"] <= -0.394264:
                                    if features["E(RIGHT) - agent_row"] <= -9.981908:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["T(LEFT) - time_left"] <= 0.271616:
                                        if features["E(LEFT) - time_left"] <= -0.075529:
                                            return 0
                                        else:
                                            if features["E(DOWN) - agent_row"] <= -8.562392:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        return 2
                            else:
                                if features["agent_row - agent_column"] <= -6.500000:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["E(DOWN) - agent_column"] <= -1.319423:
                                if features["E(LEFT) - agent_row"] <= -7.262754:
                                    if features["E(DOWN) - agent_row"] <= -10.309041:
                                        if features["E(UP) - E(LEFT)"] <= -0.829597:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(DOWN) - E(LEFT)"] <= -0.008013:
                                            if features["E(UP) - time_left"] <= -0.187551:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 1
                                else:
                                    return 2
                            else:
                                if features["T(RIGHT) - agent_row"] <= -10.848037:
                                    return 2
                                else:
                                    if features["E(UP) - agent_column"] <= -1.999986:
                                        return 2
                                    else:
                                        return 1
        else:
            if features["E(UP) - E(LEFT)"] <= 0.000090:
                if features["E(LEFT)"] <= 0.442258:
                    if features["E(RIGHT) - T(DOWN)"] <= 0.054508:
                        if features["E(RIGHT)"] <= 0.014579:
                            if features["T(LEFT) - agent_column"] <= -11.550614:
                                if features["E(DOWN) - T(up)"] <= 0.136522:
                                    if features["E(LEFT)"] <= 0.420597:
                                        if features["T(LEFT) - time_left"] <= 0.342872:
                                            if features["E(UP) - time_left"] <= 0.278223:
                                                if features["E(DOWN)"] <= 0.053903:
                                                    return 2
                                                else:
                                                    if features["T(DOWN) - agent_row"] <= -6.710385:
                                                        if features["E(LEFT) - T(LEFT)"] <= -0.266554:
                                                            return 2
                                                        else:
                                                            if features["E(UP) - T(DOWN)"] <= 0.183451:
                                                                if features["E(DOWN) - T(up)"] <= -0.318837:
                                                                    return 2
                                                                else:
                                                                    if features["T(DOWN) - time_left"] <= -0.188986:
                                                                        return 0
                                                                    else:
                                                                        if features["E(DOWN) - agent_row"] <= -8.859062:
                                                                            return 0
                                                                        else:
                                                                            return 1
                                                            else:
                                                                return 0
                                                    else:
                                                        if features["T(RIGHT) - agent_column"] <= -11.999873:
                                                            if features["E(UP) - T(up)"] <= -0.029381:
                                                                if features["E(LEFT) - agent_row"] <= -5.629389:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["T(up) - T(RIGHT)"] <= 0.000012:
                                                                    if features["E(DOWN) - T(DOWN)"] <= -0.317920:
                                                                        return 2
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    if features["E(DOWN) - agent_row"] <= -2.774026:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                        else:
                                                            return 0
                                            else:
                                                if features["T(RIGHT) - agent_row"] <= -8.999576:
                                                    if features["E(RIGHT) - T(RIGHT)"] <= -0.000000:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    return 2
                                        else:
                                            if features["T(LEFT) - T(RIGHT)"] <= 0.399174:
                                                return 2
                                            else:
                                                if features["E(UP) - T(RIGHT)"] <= 0.318757:
                                                    if features["E(DOWN) - T(up)"] <= 0.075630:
                                                        if features["T(RIGHT)"] <= 0.005720:
                                                            if features["E(RIGHT) - T(DOWN)"] <= 0.003430:
                                                                return 2
                                                            else:
                                                                if features["T(DOWN) - agent_row"] <= -5.999996:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["E(DOWN) - time_left"] <= -0.070971:
                                                            return 2
                                                        else:
                                                            return 0
                                                else:
                                                    if features["T(up) - agent_row"] <= -8.999948:
                                                        return 0
                                                    else:
                                                        return 2
                                    else:
                                        if features["T(RIGHT)"] <= 0.000194:
                                            if features["T(DOWN) - agent_column"] <= -13.818888:
                                                return 2
                                            else:
                                                if features["E(RIGHT) - agent_row"] <= -5.999630:
                                                    if features["T(DOWN) - T(LEFT)"] <= -0.529101:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(UP) - T(LEFT)"] <= -0.076149:
                                                        return 2
                                                    else:
                                                        return 0
                                        else:
                                            if features["E(UP) - time_left"] <= 0.105146:
                                                if features["T(RIGHT) - time_left"] <= -0.099417:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                else:
                                    if features["T(LEFT) - T(RIGHT)"] <= 0.367847:
                                        if features["E(DOWN) - agent_row"] <= -8.831492:
                                            if features["T(DOWN) - time_left"] <= -0.199739:
                                                return 0
                                            else:
                                                if features["E(RIGHT)"] <= 0.000567:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["E(LEFT) - agent_column"] <= -12.577060:
                                                if features["agent_row - time_left"] <= 2.780000:
                                                    if features["E(DOWN) - E(LEFT)"] <= -0.025915:
                                                        if features["E(UP) - T(LEFT)"] <= -0.205322:
                                                            return 0
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(DOWN) - time_left"] <= -0.276563:
                                                        if features["T(DOWN) - time_left"] <= -0.141029:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["E(UP) - T(DOWN)"] <= 0.193895:
                                                            return 1
                                                        else:
                                                            return 0
                                            else:
                                                if features["E(LEFT) - T(LEFT)"] <= 0.045841:
                                                    return 0
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -5.855236:
                                                        return 0
                                                    else:
                                                        return 2
                                    else:
                                        if features["T(DOWN) - agent_row"] <= -2.815325:
                                            if features["E(DOWN) - T(DOWN)"] <= 0.232698:
                                                if features["E(RIGHT) - T(DOWN)"] <= 0.002699:
                                                    if features["T(LEFT) - time_left"] <= 0.258798:
                                                        if features["E(RIGHT) - agent_row"] <= -8.999557:
                                                            return 2
                                                        else:
                                                            if features["T(up) - T(LEFT)"] <= -0.405243:
                                                                if features["T(up) - time_left"] <= -0.449810:
                                                                    return 2
                                                                else:
                                                                    return 0
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["E(UP) - T(up)"] <= 0.265481:
                                                            return 2
                                                        else:
                                                            if features["T(LEFT) - agent_row"] <= -6.270525:
                                                                return 0
                                                            else:
                                                                return 2
                                                else:
                                                    return 0
                                            else:
                                                if features["E(UP) - agent_column"] <= -12.850800:
                                                    return 1
                                                else:
                                                    return 2
                                        else:
                                            return 0
                            else:
                                if features["E(DOWN) - agent_column"] <= -11.858046:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.002436:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    if features["E(UP) - time_left"] <= 0.016705:
                                        if features["T(DOWN) - agent_row"] <= -5.443661:
                                            if features["E(UP) - T(DOWN)"] <= -0.261707:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(RIGHT)"] <= 0.010879:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        if features["E(UP) - E(LEFT)"] <= 0.000031:
                                            return 2
                                        else:
                                            return 0
                        else:
                            if features["E(DOWN) - T(up)"] <= 0.162330:
                                if features["E(UP) - time_left"] <= 0.037236:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.575349:
                                        if features["T(DOWN)"] <= 0.000000:
                                            return 3
                                        else:
                                            return 2
                                    else:
                                        if features["T(LEFT)"] <= 0.289749:
                                            if features["T(up) - agent_column"] <= -11.526841:
                                                return 3
                                            else:
                                                if features["T(LEFT) - agent_row"] <= -9.999890:
                                                    return 3
                                                else:
                                                    return 2
                                        else:
                                            if features["E(UP) - agent_column"] <= -12.812583:
                                                if features["E(UP) - agent_row"] <= -8.905821:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["E(RIGHT) - T(RIGHT)"] <= 0.056072:
                                                    return 0
                                                else:
                                                    return 3
                                else:
                                    if features["T(RIGHT) - time_left"] <= 0.189051:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.164572:
                                            if features["agent_row - agent_column"] <= 0.500000:
                                                if features["T(RIGHT) - time_left"] <= -0.150000:
                                                    return 0
                                                else:
                                                    if features["E(DOWN) - time_left"] <= 0.302106:
                                                        if features["T(DOWN)"] <= 0.000000:
                                                            return 2
                                                        else:
                                                            if features["E(UP) - time_left"] <= 0.319457:
                                                                if features["E(LEFT)"] <= 0.261759:
                                                                    if features["T(up) - T(RIGHT)"] <= 0.003307:
                                                                        return 0
                                                                    else:
                                                                        return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["E(UP) - time_left"] <= 0.320658:
                                                                    return 1
                                                                else:
                                                                    return 0
                                                    else:
                                                        if features["E(UP) - E(RIGHT)"] <= 0.019430:
                                                            return 0
                                                        else:
                                                            return 3
                                            else:
                                                return 2
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -11.633579:
                                                return 0
                                            else:
                                                return 2
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= 0.006139:
                                            return 0
                                        else:
                                            return 3
                            else:
                                if features["agent_row - time_left"] <= 3.940000:
                                    if features["T(LEFT) - time_left"] <= 0.198012:
                                        if features["T(DOWN) - T(LEFT)"] <= -0.000350:
                                            return 3
                                        else:
                                            if features["E(UP) - T(DOWN)"] <= -0.300171:
                                                if features["agent_row - time_left"] <= 3.800000:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                    else:
                                        if features["T(RIGHT)"] <= 0.000000:
                                            return 1
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.281113:
                                                return 0
                                            else:
                                                if features["agent_row - agent_column"] <= -8.500000:
                                                    return 2
                                                else:
                                                    return 0
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= 0.000008:
                                        if features["E(UP) - time_left"] <= 0.146246:
                                            if features["T(up) - T(DOWN)"] <= -0.246253:
                                                if features["E(RIGHT) - T(DOWN)"] <= -0.348573:
                                                    if features["agent_row - time_left"] <= 8.720000:
                                                        if features["agent_row - agent_column"] <= -6.500000:
                                                            if features["E(RIGHT) - T(DOWN)"] <= -0.436822:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["agent_row - agent_column"] <= -2.500000:
                                                        return 1
                                                    else:
                                                        if features["T(up) - agent_column"] <= -11.999496:
                                                            return 0
                                                        else:
                                                            return 3
                                            else:
                                                return 3
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.188913:
                                                return 0
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.414823:
                                                    return 0
                                                else:
                                                    return 1
                                    else:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.125549:
                                            if features["E(UP) - T(up)"] <= 0.086733:
                                                return 3
                                            else:
                                                if features["E(LEFT) - agent_row"] <= -9.637494:
                                                    return 3
                                                else:
                                                    if features["E(UP) - T(RIGHT)"] <= -0.575410:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - T(DOWN)"] <= -0.359739:
                                                            if features["E(UP) - T(RIGHT)"] <= 0.264171:
                                                                return 2
                                                            else:
                                                                return 0
                                                        else:
                                                            return 0
                                        else:
                                            if features["E(UP) - agent_column"] <= -9.731498:
                                                if features["E(UP) - T(LEFT)"] <= 0.211623:
                                                    if features["T(DOWN) - time_left"] <= 0.569224:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 2
                                            else:
                                                return 0
                    else:
                        if features["E(DOWN) - T(DOWN)"] <= 0.246793:
                            if features["E(UP) - T(LEFT)"] <= 0.249084:
                                if features["E(UP) - E(RIGHT)"] <= 0.154545:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.486255:
                                        if features["E(LEFT) - time_left"] <= 0.299151:
                                            if features["T(DOWN) - T(RIGHT)"] <= -0.000000:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 2
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -6.999981:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.287970:
                                        if features["T(RIGHT)"] <= 0.000025:
                                            return 3
                                        else:
                                            if features["E(UP) - T(up)"] <= -0.306071:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= 0.544089:
                                            if features["T(LEFT) - agent_row"] <= -6.329748:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 2
                            else:
                                if features["agent_row - time_left"] <= 8.540000:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.165696:
                                        if features["T(RIGHT) - agent_row"] <= -5.098238:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        return 1
                                else:
                                    return 3
                        else:
                            if features["T(up) - agent_row"] <= -8.479749:
                                return 3
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.285041:
                                    if features["E(UP) - T(LEFT)"] <= 0.166397:
                                        if features["E(UP) - E(LEFT)"] <= -0.068845:
                                            if features["T(LEFT) - T(RIGHT)"] <= 0.606597:
                                                if features["T(up) - agent_row"] <= -5.999321:
                                                    if features["T(up) - T(LEFT)"] <= 0.000053:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(RIGHT) - T(up)"] <= -0.431239:
                                                        return 2
                                                    else:
                                                        return 1
                                            else:
                                                if features["E(LEFT) - time_left"] <= 0.323751:
                                                    if features["E(UP) - time_left"] <= -0.013406:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 2
                                        else:
                                            return 3
                                    else:
                                        if features["E(UP) - time_left"] <= 0.173001:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    if features["E(LEFT)"] <= 0.402617:
                                        return 1
                                    else:
                                        return 2
                else:
                    if features["T(RIGHT) - agent_column"] <= -11.999687:
                        if features["E(RIGHT) - T(RIGHT)"] <= -0.000000:
                            if features["E(UP) - agent_column"] <= -11.200566:
                                if features["E(DOWN) - E(RIGHT)"] <= 0.000000:
                                    return 0
                                else:
                                    if features["E(UP) - agent_row"] <= -0.166799:
                                        return 2
                                    else:
                                        return 0
                            else:
                                if features["E(RIGHT) - agent_row"] <= -2.999999:
                                    return 0
                                else:
                                    return 2
                        else:
                            if features["E(DOWN) - agent_row"] <= -0.999999:
                                if features["E(UP) - E(LEFT)"] <= -0.074387:
                                    return 2
                                else:
                                    if features["E(UP) - E(LEFT)"] <= -0.000205:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.000000:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.799903:
                                                if features["T(DOWN) - time_left"] <= -0.499686:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(DOWN) - T(LEFT)"] <= 0.000098:
                                                return 0
                                            else:
                                                if features["E(DOWN) - E(LEFT)"] <= -0.407117:
                                                    return 0
                                                else:
                                                    return 2
                                    else:
                                        return 0
                            else:
                                return 2
                    else:
                        if features["E(RIGHT)"] <= 0.000000:
                            if features["E(UP) - E(DOWN)"] <= 0.799610:
                                return 2
                            else:
                                return 0
                        else:
                            if features["E(DOWN) - E(RIGHT)"] <= -0.000001:
                                if features["E(DOWN) - agent_row"] <= -2.000000:
                                    if features["T(DOWN)"] <= 0.000000:
                                        return 2
                                    else:
                                        if features["E(UP) - T(LEFT)"] <= 0.800432:
                                            if features["E(UP) - time_left"] <= -0.107768:
                                                return 1
                                            else:
                                                return 0
                                        else:
                                            if features["agent_row - agent_column"] <= 2.500000:
                                                return 0
                                            else:
                                                return 2
                                else:
                                    if features["T(up) - T(LEFT)"] <= -0.442130:
                                        return 0
                                    else:
                                        return 2
                            else:
                                if features["E(LEFT) - T(up)"] <= 0.799784:
                                    if features["E(UP) - agent_row"] <= -0.565521:
                                        if features["E(RIGHT)"] <= 0.000007:
                                            if features["T(LEFT) - agent_column"] <= -1.000000:
                                                if features["E(DOWN) - agent_column"] <= -10.999992:
                                                    return 0
                                                else:
                                                    if features["T(LEFT) - agent_row"] <= -8.999070:
                                                        return 2
                                                    else:
                                                        if features["E(UP) - E(LEFT)"] <= 0.000022:
                                                            return 2
                                                        else:
                                                            return 0
                                            else:
                                                return 0
                                        else:
                                            if features["E(UP) - time_left"] <= 0.154450:
                                                if features["agent_column - time_left"] <= 8.820000:
                                                    if features["agent_row - agent_column"] <= 3.500000:
                                                        if features["E(RIGHT) - T(DOWN)"] <= -0.438735:
                                                            if features["E(DOWN) - time_left"] <= -0.105270:
                                                                if features["E(DOWN) - E(LEFT)"] <= -0.205445:
                                                                    if features["E(LEFT)"] <= 0.615421:
                                                                        return 2
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    return 3
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["T(up) - time_left"] <= -0.649991:
                                                                return 2
                                                            else:
                                                                if features["E(LEFT) - T(up)"] <= -0.238621:
                                                                    return 2
                                                                else:
                                                                    return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 2
                                            else:
                                                if features["E(UP) - T(up)"] <= 0.739509:
                                                    if features["T(RIGHT) - time_left"] <= -0.130000:
                                                        if features["E(RIGHT)"] <= 0.000369:
                                                            return 2
                                                        else:
                                                            return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                                    else:
                                        return 2
                                else:
                                    if features["agent_row - agent_column"] <= -0.500000:
                                        return 0
                                    else:
                                        return 2
            else:
                if features["E(UP) - E(RIGHT)"] <= 0.115772:
                    if features["E(DOWN) - T(DOWN)"] <= 0.054438:
                        if features["E(DOWN) - agent_row"] <= -2.000000:
                            if features["E(UP) - E(RIGHT)"] <= 0.000001:
                                if features["E(LEFT)"] <= 0.093395:
                                    if features["T(up) - T(RIGHT)"] <= 0.003753:
                                        if features["E(LEFT) - agent_column"] <= -0.999404:
                                            if features["T(LEFT) - agent_column"] <= -1.999536:
                                                if features["E(LEFT)"] <= 0.000000:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 3
                                        else:
                                            return 0
                                    else:
                                        if features["E(DOWN)"] <= 0.000000:
                                            return 3
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -5.999998:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -3.115792:
                                                    return 0
                                                else:
                                                    return 3
                                else:
                                    return 0
                            else:
                                if features["E(RIGHT)"] <= 0.799727:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.000001:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.000141:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.018693:
                                                if features["T(up) - T(LEFT)"] <= 0.375895:
                                                    if features["E(LEFT)"] <= 0.285898:
                                                        if features["E(DOWN) - E(RIGHT)"] <= -0.662896:
                                                            if features["E(DOWN)"] <= 0.000176:
                                                                if features["T(DOWN) - agent_row"] <= -12.999543:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                return 0
                                                        else:
                                                            if features["E(LEFT) - time_left"] <= -0.699910:
                                                                if features["E(UP) - T(RIGHT)"] <= 0.398628:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["E(UP) - T(RIGHT)"] <= 0.039607:
                                                                    if features["E(UP) - T(RIGHT)"] <= 0.034823:
                                                                        if features["E(UP) - T(up)"] <= -0.013477:
                                                                            if features["E(UP) - T(up)"] <= -0.018653:
                                                                                return 0
                                                                            else:
                                                                                return 3
                                                                        else:
                                                                            return 0
                                                                    else:
                                                                        if features["E(DOWN) - T(LEFT)"] <= -0.035970:
                                                                            return 0
                                                                        else:
                                                                            return 3
                                                                else:
                                                                    return 0
                                                    else:
                                                        if features["E(UP) - time_left"] <= 0.275789:
                                                            return 0
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(DOWN) - T(DOWN)"] <= -0.000000:
                                                        return 0
                                                    else:
                                                        if features["E(LEFT) - T(up)"] <= -0.383855:
                                                            if features["E(UP) - agent_row"] <= -13.648249:
                                                                return 3
                                                            else:
                                                                if features["E(RIGHT) - T(up)"] <= -0.006400:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                        else:
                                                            return 3
                                            else:
                                                return 3
                                        else:
                                            if features["T(RIGHT) - time_left"] <= -0.109947:
                                                if features["E(DOWN) - agent_column"] <= -11.999362:
                                                    return 0
                                                else:
                                                    if features["T(RIGHT)"] <= 0.000044:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                return 0
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.165777:
                                            if features["agent_row - agent_column"] <= 5.500000:
                                                if features["E(RIGHT) - T(LEFT)"] <= 0.289512:
                                                    return 3
                                                else:
                                                    if features["E(RIGHT) - agent_column"] <= -4.563299:
                                                        return 0
                                                    else:
                                                        if features["E(UP) - time_left"] <= 0.340202:
                                                            if features["E(UP) - E(LEFT)"] <= 0.301690:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(DOWN) - T(RIGHT)"] <= -0.586074:
                                                                return 0
                                                            else:
                                                                return 3
                                            else:
                                                if features["T(DOWN) - T(RIGHT)"] <= -0.257866:
                                                    return 0
                                                else:
                                                    if features["T(LEFT) - agent_column"] <= -2.999611:
                                                        return 0
                                                    else:
                                                        return 3
                                        else:
                                            if features["T(LEFT)"] <= 0.000010:
                                                if features["E(DOWN) - agent_row"] <= -6.816914:
                                                    return 0
                                                else:
                                                    if features["E(UP) - T(RIGHT)"] <= -0.208764:
                                                        return 2
                                                    else:
                                                        if features["E(LEFT) - agent_column"] <= -3.818037:
                                                            return 0
                                                        else:
                                                            return 2
                                            else:
                                                return 0
                                else:
                                    if features["T(up) - agent_column"] <= -4.725786:
                                        if features["T(DOWN) - agent_column"] <= -7.999917:
                                            return 3
                                        else:
                                            if features["T(up) - agent_column"] <= -7.720516:
                                                return 0
                                            else:
                                                return 3
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -13.999982:
                                            return 3
                                        else:
                                            return 0
                        else:
                            if features["E(UP) - E(RIGHT)"] <= 0.027631:
                                if features["E(LEFT) - T(DOWN)"] <= -0.197623:
                                    if features["T(up) - agent_column"] <= -11.999994:
                                        return 0
                                    else:
                                        if features["E(UP) - agent_column"] <= -5.217580:
                                            if features["T(DOWN) - agent_row"] <= -0.381621:
                                                if features["E(DOWN) - agent_row"] <= -2.000000:
                                                    return 0
                                                else:
                                                    if features["E(UP) - agent_column"] <= -5.232158:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                return 0
                                        else:
                                            return 3
                                else:
                                    return 3
                            else:
                                if features["E(RIGHT) - agent_row"] <= -0.500745:
                                    return 0
                                else:
                                    return 3
                    else:
                        if features["T(DOWN) - T(LEFT)"] <= -0.000000:
                            if features["E(UP) - time_left"] <= 0.301164:
                                if features["E(DOWN) - T(RIGHT)"] <= 0.110917:
                                    if features["T(RIGHT) - agent_column"] <= -11.999653:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["T(up) - agent_row"] <= -5.703038:
                                        if features["E(RIGHT) - time_left"] <= -0.199596:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 0
                            else:
                                if features["T(LEFT) - time_left"] <= 0.538653:
                                    if features["E(RIGHT) - T(RIGHT)"] <= -0.185285:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT) - agent_column"] <= -3.589732:
                                        return 0
                                    else:
                                        return 3
                        else:
                            if features["T(up) - agent_row"] <= -8.582454:
                                if features["E(UP) - agent_column"] <= -6.693365:
                                    return 3
                                else:
                                    return 0
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.312263:
                                    if features["E(DOWN) - time_left"] <= 0.000610:
                                        if features["T(up) - agent_column"] <= -5.999787:
                                            return 3
                                        else:
                                            return 2
                                    else:
                                        return 2
                                else:
                                    if features["T(up) - agent_row"] <= -7.516390:
                                        return 0
                                    else:
                                        if features["T(DOWN) - T(RIGHT)"] <= -0.670184:
                                            return 3
                                        else:
                                            return 1
                else:
                    if features["E(LEFT)"] <= 0.676399:
                        if features["E(DOWN) - T(DOWN)"] <= 0.056191:
                            if features["E(RIGHT)"] <= 0.338158:
                                if features["E(UP) - time_left"] <= -0.034700:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.000537:
                                        return 0
                                    else:
                                        if features["E(DOWN) - E(RIGHT)"] <= -0.001166:
                                            if features["E(RIGHT) - time_left"] <= -0.650635:
                                                return 1
                                            else:
                                                return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(DOWN) - E(RIGHT)"] <= 0.001594:
                                        if features["E(LEFT) - agent_row"] <= -0.410534:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.056754:
                                                if features["E(LEFT) - T(LEFT)"] <= 0.017424:
                                                    return 0
                                                else:
                                                    if features["E(DOWN) - time_left"] <= -0.000340:
                                                        return 0
                                                    else:
                                                        if features["T(up) - T(RIGHT)"] <= 0.174647:
                                                            if features["E(LEFT) - T(LEFT)"] <= 0.040954:
                                                                return 1
                                                            else:
                                                                return 0
                                                        else:
                                                            return 3
                                            else:
                                                if features["T(DOWN) - time_left"] <= -0.129952:
                                                    if features["E(DOWN) - T(DOWN)"] <= 0.019682:
                                                        return 0
                                                    else:
                                                        if features["E(UP) - T(up)"] <= -0.119918:
                                                            return 0
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.111921:
                                                        return 3
                                                    else:
                                                        if features["T(up) - agent_row"] <= -13.497162:
                                                            if features["T(up) - agent_column"] <= -7.683859:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(UP) - agent_column"] <= -11.643247:
                                                                return 2
                                                            else:
                                                                return 0
                                        else:
                                            return 2
                                    else:
                                        if features["time_left"] <= 0.020000:
                                            return 1
                                        else:
                                            return 0
                            else:
                                if features["E(DOWN) - agent_row"] <= -1.991980:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.008404:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT) - time_left"] <= 0.147243:
                                        return 0
                                    else:
                                        return 3
                        else:
                            if features["E(UP) - time_left"] <= 0.299889:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.119774:
                                    return 0
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.280777:
                                        if features["T(up) - agent_row"] <= -8.566946:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.494882:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        return 0
                            else:
                                if features["T(DOWN)"] <= 0.000000:
                                    if features["agent_column - time_left"] <= 9.980000:
                                        if features["T(up) - T(DOWN)"] <= 0.548944:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(RIGHT) - time_left"] <= -0.110000:
                                        return 3
                                    else:
                                        return 0
                    else:
                        if features["E(DOWN) - agent_row"] <= -0.999999:
                            if features["E(UP) - T(LEFT)"] <= 0.799954:
                                if features["E(DOWN)"] <= 0.000103:
                                    if features["E(UP)"] <= 0.800092:
                                        if features["E(DOWN) - T(DOWN)"] <= -0.000000:
                                            if features["T(up) - agent_row"] <= -1.095352:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -12.216773:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -3.999999:
                                            if features["T(RIGHT) - agent_column"] <= -9.000000:
                                                if features["T(up) - agent_column"] <= -11.774897:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                if features["E(UP) - agent_column"] <= -6.132444:
                                                    return 2
                                                else:
                                                    if features["E(RIGHT) - agent_row"] <= -4.999978:
                                                        if features["E(RIGHT) - agent_column"] <= -4.999996:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 0
                                        else:
                                            if features["agent_row - agent_column"] <= -10.500000:
                                                return 2
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -1.999936:
                                                    return 0
                                                else:
                                                    return 2
                                else:
                                    if features["agent_row - agent_column"] <= -9.500000:
                                        return 2
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -1.999960:
                                            if features["T(LEFT) - agent_row"] <= -10.999995:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(LEFT) - agent_column"] <= -7.249392:
                                                return 2
                                            else:
                                                if features["T(RIGHT) - agent_column"] <= -4.999871:
                                                    return 0
                                                else:
                                                    if features["T(DOWN) - agent_column"] <= -3.551042:
                                                        return 2
                                                    else:
                                                        if features["E(LEFT) - T(LEFT)"] <= 0.788228:
                                                            return 0
                                                        else:
                                                            return 2
                            else:
                                if features["E(UP) - T(DOWN)"] <= 0.471379:
                                    if features["E(RIGHT) - agent_column"] <= -1.999863:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(RIGHT) - agent_column"] <= -4.427027:
                                        return 0
                                    else:
                                        return 2
                        else:
                            if features["T(DOWN) - agent_column"] <= -1.482095:
                                return 2
                            else:
                                return 0
    else:
        if features["E(DOWN) - E(RIGHT)"] <= 0.000010:
            if features["E(UP) - E(RIGHT)"] <= -0.136325:
                if features["E(DOWN) - E(RIGHT)"] <= -0.172396:
                    if features["T(LEFT)"] <= 0.000403:
                        if features["E(RIGHT) - time_left"] <= -0.108401:
                            if features["T(LEFT) - agent_row"] <= -8.999817:
                                return 3
                            else:
                                return 2
                        else:
                            return 3
                    else:
                        if features["E(LEFT) - agent_column"] <= -0.950240:
                            return 3
                        else:
                            if features["E(LEFT) - T(up)"] <= -0.183580:
                                return 3
                            else:
                                return 1
                else:
                    if features["E(LEFT) - agent_column"] <= -1.940597:
                        if features["E(DOWN) - agent_column"] <= -11.215523:
                            if features["T(RIGHT) - agent_row"] <= -3.095287:
                                if features["E(LEFT) - agent_row"] <= -8.999996:
                                    if features["E(UP) - T(up)"] <= 0.000040:
                                        if features["E(LEFT) - agent_row"] <= -11.999882:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(UP)"] <= 0.000032:
                                        return 1
                                    else:
                                        return 3
                            else:
                                return 1
                        else:
                            if features["E(RIGHT)"] <= 0.364221:
                                if features["E(UP) - time_left"] <= 0.143167:
                                    if features["E(DOWN)"] <= 0.306675:
                                        if features["T(LEFT)"] <= 0.121340:
                                            if features["T(LEFT)"] <= 0.000005:
                                                if features["E(UP) - time_left"] <= 0.072649:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["T(DOWN) - T(RIGHT)"] <= 0.011167:
                                                    return 3
                                                else:
                                                    return 0
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -5.826486:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        if features["E(UP) - T(LEFT)"] <= 0.030955:
                                            return 3
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -3.629363:
                                                return 3
                                            else:
                                                return 1
                                else:
                                    if features["T(up) - T(LEFT)"] <= 0.025948:
                                        if features["T(up) - agent_column"] <= -4.999626:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= -0.029700:
                                            return 2
                                        else:
                                            return 1
                            else:
                                if features["T(LEFT)"] <= 0.000005:
                                    if features["T(up) - agent_column"] <= -2.000000:
                                        if features["T(up) - T(LEFT)"] <= 0.000000:
                                            return 3
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= -0.000000:
                                                return 3
                                            else:
                                                if features["E(DOWN) - E(RIGHT)"] <= -0.099386:
                                                    return 3
                                                else:
                                                    if features["E(RIGHT) - agent_row"] <= -10.301950:
                                                        return 3
                                                    else:
                                                        if features["E(LEFT) - T(LEFT)"] <= 0.000000:
                                                            return 3
                                                        else:
                                                            if features["E(DOWN) - T(RIGHT)"] <= -0.415454:
                                                                return 3
                                                            else:
                                                                return 1
                                    else:
                                        if features["E(LEFT)"] <= 0.000000:
                                            return 3
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= -0.438120:
                                                return 3
                                            else:
                                                if features["E(DOWN) - E(RIGHT)"] <= -0.108690:
                                                    return 3
                                                else:
                                                    return 1
                                else:
                                    if features["E(LEFT) - time_left"] <= -0.171876:
                                        if features["E(LEFT)"] <= 0.000001:
                                            if features["E(UP) - E(DOWN)"] <= -0.865385:
                                                if features["T(DOWN) - agent_row"] <= -4.550527:
                                                    if features["E(RIGHT) - agent_column"] <= -9.132766:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                        else:
                                            if features["T(up) - agent_row"] <= -10.971850:
                                                if features["E(UP) - agent_column"] <= -11.999643:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["E(UP) - agent_column"] <= -7.999886:
                                                    if features["E(LEFT) - time_left"] <= -0.214543:
                                                        if features["E(LEFT) - T(up)"] <= 0.002023:
                                                            if features["T(RIGHT) - agent_column"] <= -8.441762:
                                                                return 3
                                                            else:
                                                                return 1
                                                        else:
                                                            if features["E(DOWN) - E(LEFT)"] <= 0.415166:
                                                                if features["E(DOWN) - time_left"] <= -0.113580:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(DOWN) - T(LEFT)"] <= 0.562235:
                                                        return 3
                                                    else:
                                                        if features["E(LEFT) - agent_column"] <= -5.999998:
                                                            return 3
                                                        else:
                                                            return 1
                                    else:
                                        if features["E(UP) - E(LEFT)"] <= -0.000001:
                                            return 3
                                        else:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.169403:
                                                if features["E(UP) - T(up)"] <= 0.122505:
                                                    if features["agent_row - time_left"] <= 5.880000:
                                                        if features["T(up)"] <= 0.000005:
                                                            return 3
                                                        else:
                                                            if features["T(LEFT) - time_left"] <= 0.639731:
                                                                if features["E(LEFT) - T(up)"] <= 0.023916:
                                                                    if features["T(up) - T(LEFT)"] <= 0.003311:
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
                                                    if features["E(UP) - agent_row"] <= -3.798023:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(UP) - E(RIGHT)"] <= -0.867109:
                                                    if features["E(UP) - agent_column"] <= -2.999997:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 3
                    else:
                        if features["E(RIGHT) - agent_row"] <= -3.593284:
                            if features["E(LEFT) - agent_row"] <= -5.897837:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.153023:
                                    if features["T(LEFT)"] <= 0.000001:
                                        if features["E(DOWN) - agent_row"] <= -5.743108:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 3
                                else:
                                    if features["T(DOWN) - agent_row"] <= -6.999948:
                                        if features["E(UP) - E(RIGHT)"] <= -0.663547:
                                            if features["E(RIGHT) - agent_row"] <= -11.211952:
                                                return 3
                                            else:
                                                if features["E(UP) - time_left"] <= -0.909907:
                                                    return 2
                                                else:
                                                    if features["E(UP) - agent_column"] <= -0.999997:
                                                        return 3
                                                    else:
                                                        return 1
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -1.999999:
                                                return 1
                                            else:
                                                if features["T(DOWN) - time_left"] <= -0.289937:
                                                    return 1
                                                else:
                                                    return 3
                                    else:
                                        if features["E(RIGHT) - T(up)"] <= -0.292445:
                                            return 3
                                        else:
                                            return 1
                            else:
                                if features["T(LEFT) - agent_row"] <= -3.970291:
                                    if features["T(up) - T(LEFT)"] <= 0.000000:
                                        return 3
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= -0.000000:
                                            return 3
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= -0.398825:
                                                if features["E(LEFT) - agent_row"] <= -4.934748:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["T(RIGHT) - time_left"] <= -0.029900:
                                                    return 3
                                                else:
                                                    return 1
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.067370:
                                        return 3
                                    else:
                                        return 2
                        else:
                            if features["E(LEFT) - T(up)"] <= -0.001545:
                                if features["E(DOWN) - agent_column"] <= 0.803034:
                                    return 3
                                else:
                                    return 1
                            else:
                                if features["E(UP) - E(LEFT)"] <= 0.016856:
                                    if features["E(LEFT) - T(LEFT)"] <= -0.000000:
                                        return 3
                                    else:
                                        if features["T(LEFT)"] <= 0.000055:
                                            if features["T(up) - time_left"] <= -0.027493:
                                                if features["E(RIGHT) - T(up)"] <= 0.799641:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                        else:
                                            return 1
                                else:
                                    if features["T(LEFT) - agent_column"] <= -1.000000:
                                        if features["T(LEFT)"] <= 0.000000:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        return 3
            else:
                if features["E(LEFT) - E(RIGHT)"] <= -0.206708:
                    if features["E(RIGHT) - agent_column"] <= -11.200384:
                        if features["E(UP) - agent_row"] <= -6.376558:
                            if features["E(DOWN) - agent_row"] <= -11.998516:
                                return 0
                            else:
                                if features["E(DOWN) - agent_row"] <= -9.999895:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.743428:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(DOWN)"] <= 0.032238:
                                        return 0
                                    else:
                                        if features["E(RIGHT) - time_left"] <= 0.073885:
                                            return 0
                                        else:
                                            return 3
                        else:
                            if features["T(LEFT) - agent_row"] <= -1.163435:
                                if features["agent_row - agent_column"] <= -8.500000:
                                    return 0
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -3.208891:
                                        if features["T(DOWN)"] <= 0.000084:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                            else:
                                return 3
                    else:
                        if features["T(LEFT)"] <= 0.000000:
                            if features["E(UP) - agent_column"] <= 0.356869:
                                if features["T(up) - agent_column"] <= 0.273060:
                                    if features["E(LEFT) - time_left"] <= -0.010005:
                                        if features["E(UP) - time_left"] <= 0.216111:
                                            if features["E(LEFT) - T(RIGHT)"] <= -0.423847:
                                                return 3
                                            else:
                                                if features["E(LEFT) - E(RIGHT)"] <= -0.313691:
                                                    return 3
                                                else:
                                                    if features["T(LEFT)"] <= 0.000000:
                                                        return 1
                                                    else:
                                                        if features["T(RIGHT) - agent_column"] <= -3.566278:
                                                            return 0
                                                        else:
                                                            if features["agent_row - agent_column"] <= 7.500000:
                                                                return 2
                                                            else:
                                                                return 0
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -9.999997:
                                                return 3
                                            else:
                                                if features["E(DOWN) - agent_row"] <= -6.989254:
                                                    if features["T(RIGHT) - agent_column"] <= -0.259384:
                                                        if features["T(RIGHT)"] <= 0.492988:
                                                            if features["E(RIGHT)"] <= 0.407460:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(LEFT) - T(LEFT)"] <= 0.000000:
                                                                if features["E(RIGHT) - T(RIGHT)"] <= -0.198289:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                    else:
                                        if features["T(up) - agent_row"] <= -8.655852:
                                            if features["T(DOWN) - agent_row"] <= -9.999997:
                                                return 0
                                            else:
                                                if features["T(DOWN) - T(RIGHT)"] <= -0.016471:
                                                    if features["T(up) - agent_column"] <= -5.999589:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    return 0
                                        else:
                                            if features["E(LEFT) - T(RIGHT)"] <= -0.484320:
                                                if features["E(LEFT) - T(up)"] <= 0.082891:
                                                    return 3
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.189546:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(UP) - E(DOWN)"] <= 0.052650:
                                                    return 1
                                                else:
                                                    return 2
                                else:
                                    return 3
                            else:
                                if features["E(UP) - time_left"] <= 0.273147:
                                    return 3
                                else:
                                    if features["E(DOWN) - T(up)"] <= 0.000983:
                                        return 0
                                    else:
                                        return 3
                        else:
                            if features["E(DOWN) - time_left"] <= 0.194463:
                                if features["T(LEFT) - agent_column"] <= -0.998837:
                                    if features["E(LEFT) - T(up)"] <= 0.000001:
                                        if features["E(DOWN) - E(LEFT)"] <= 0.061791:
                                            if features["E(LEFT)"] <= 0.000001:
                                                if features["E(UP) - E(DOWN)"] <= 0.798996:
                                                    if features["T(DOWN) - time_left"] <= -0.569926:
                                                        if features["E(UP) - T(up)"] <= 0.029998:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["T(LEFT) - agent_column"] <= -9.785982:
                                                            if features["T(DOWN) - agent_row"] <= -9.714290:
                                                                return 3
                                                            else:
                                                                if features["T(LEFT)"] <= 0.207916:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                        else:
                                                            return 3
                                                else:
                                                    if features["T(DOWN) - agent_row"] <= -1.999522:
                                                        if features["E(DOWN) - agent_row"] <= -2.999996:
                                                            if features["E(UP) - T(LEFT)"] <= 0.801830:
                                                                if features["E(DOWN) - T(LEFT)"] <= -0.776581:
                                                                    return 0
                                                                else:
                                                                    if features["E(UP) - E(RIGHT)"] <= 0.000324:
                                                                        return 3
                                                                    else:
                                                                        return 0
                                                            else:
                                                                if features["E(LEFT)"] <= 0.000000:
                                                                    return 3
                                                                else:
                                                                    if features["T(RIGHT) - agent_row"] <= -10.996996:
                                                                        return 3
                                                                    else:
                                                                        return 0
                                                        else:
                                                            return 0
                                                    else:
                                                        return 3
                                            else:
                                                if features["E(LEFT) - T(LEFT)"] <= 0.006971:
                                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.009791:
                                                        if features["T(DOWN) - agent_column"] <= -2.875307:
                                                            if features["E(LEFT) - agent_column"] <= -4.992757:
                                                                if features["E(UP) - T(LEFT)"] <= 0.657162:
                                                                    if features["E(LEFT) - T(LEFT)"] <= 0.004273:
                                                                        return 3
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["T(LEFT)"] <= 0.001204:
                                                                    if features["T(DOWN) - agent_row"] <= -7.999917:
                                                                        return 0
                                                                    else:
                                                                        return 3
                                                                else:
                                                                    return 0
                                                        else:
                                                            if features["E(UP) - T(up)"] <= -0.016952:
                                                                return 0
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["E(LEFT)"] <= 0.148905:
                                                            if features["E(UP) - E(LEFT)"] <= 0.729210:
                                                                if features["E(UP) - T(RIGHT)"] <= -0.008750:
                                                                    if features["T(DOWN) - agent_row"] <= -6.999748:
                                                                        return 3
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    if features["E(UP) - T(RIGHT)"] <= -0.001942:
                                                                        return 0
                                                                    else:
                                                                        if features["T(up) - agent_column"] <= -5.748521:
                                                                            if features["E(DOWN) - agent_column"] <= -9.995385:
                                                                                if features["T(DOWN) - agent_row"] <= -4.999915:
                                                                                    return 3
                                                                                else:
                                                                                    return 0
                                                                            else:
                                                                                if features["E(LEFT) - time_left"] <= -0.779971:
                                                                                    return 2
                                                                                else:
                                                                                    return 3
                                                                        else:
                                                                            if features["T(LEFT) - agent_row"] <= -7.999815:
                                                                                if features["T(LEFT) - agent_column"] <= -2.263023:
                                                                                    if features["E(LEFT) - T(LEFT)"] <= -0.583801:
                                                                                        return 0
                                                                                    else:
                                                                                        if features["E(UP) - agent_row"] <= -8.570300:
                                                                                            return 3
                                                                                        else:
                                                                                            return 0
                                                                                else:
                                                                                    return 3
                                                                            else:
                                                                                return 3
                                                            else:
                                                                if features["T(DOWN) - agent_row"] <= -1.999647:
                                                                    if features["E(UP) - agent_row"] <= -2.215456:
                                                                        if features["E(LEFT) - agent_column"] <= -9.999980:
                                                                            if features["E(DOWN) - T(DOWN)"] <= 0.000533:
                                                                                return 3
                                                                            else:
                                                                                return 0
                                                                        else:
                                                                            if features["E(DOWN) - agent_column"] <= -8.999833:
                                                                                return 0
                                                                            else:
                                                                                return 3
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    return 3
                                                        else:
                                                            if features["T(up) - T(DOWN)"] <= 0.501781:
                                                                return 0
                                                            else:
                                                                return 3
                                                else:
                                                    if features["E(UP)"] <= 0.361551:
                                                        return 3
                                                    else:
                                                        if features["E(DOWN) - T(DOWN)"] <= 0.003955:
                                                            return 0
                                                        else:
                                                            return 3
                                        else:
                                            if features["E(RIGHT)"] <= 0.355042:
                                                if features["E(DOWN) - agent_row"] <= -8.758823:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -3.808404:
                                            if features["E(LEFT) - agent_column"] <= -4.996491:
                                                if features["E(UP) - E(DOWN)"] <= 0.656622:
                                                    if features["E(UP) - time_left"] <= -0.033443:
                                                        if features["E(UP) - T(LEFT)"] <= -0.400620:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -1.999992:
                                                        if features["E(UP) - agent_row"] <= -2.214742:
                                                            if features["E(RIGHT) - agent_row"] <= -3.246316:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        return 3
                                            else:
                                                if features["agent_column - time_left"] <= 4.760000:
                                                    if features["T(up) - agent_row"] <= -8.999650:
                                                        if features["T(DOWN) - agent_row"] <= -8.264455:
                                                            return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["E(RIGHT) - time_left"] <= 0.244612:
                                                            if features["T(LEFT) - agent_row"] <= -1.999897:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(LEFT) - T(DOWN)"] <= 0.120482:
                                                        if features["E(RIGHT) - T(LEFT)"] <= 0.435453:
                                                            if features["E(UP) - E(DOWN)"] <= 0.135370:
                                                                if features["T(up)"] <= 0.000016:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -7.659988:
                                                            return 0
                                                        else:
                                                            return 3
                                        else:
                                            return 3
                                else:
                                    if features["E(UP) - agent_column"] <= -0.696571:
                                        return 3
                                    else:
                                        if features["E(LEFT) - time_left"] <= 0.045940:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.001750:
                                                if features["E(RIGHT) - agent_column"] <= -0.200424:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                        else:
                                            return 1
                            else:
                                if features["T(up) - T(LEFT)"] <= 0.122864:
                                    if features["E(LEFT) - E(RIGHT)"] <= -0.212931:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 1
                else:
                    if features["T(DOWN) - agent_column"] <= -5.997186:
                        if features["T(RIGHT) - agent_row"] <= -4.999981:
                            if features["E(LEFT) - T(LEFT)"] <= 0.234239:
                                if features["E(DOWN) - agent_column"] <= -11.806419:
                                    return 0
                                else:
                                    return 3
                            else:
                                return 2
                        else:
                            return 0
                    else:
                        if features["E(RIGHT) - T(LEFT)"] <= 0.202648:
                            if features["T(LEFT) - time_left"] <= 0.230319:
                                if features["E(RIGHT) - time_left"] <= 0.343280:
                                    if features["E(DOWN)"] <= 0.310994:
                                        if features["E(RIGHT) - agent_row"] <= -0.726997:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                if features["E(DOWN) - agent_row"] <= -3.815941:
                                    if features["T(up) - agent_row"] <= -7.479085:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 0
                        else:
                            if features["E(LEFT) - agent_column"] <= -4.803014:
                                if features["T(LEFT) - agent_row"] <= -1.999765:
                                    if features["E(LEFT) - T(DOWN)"] <= 0.153945:
                                        if features["E(DOWN) - T(LEFT)"] <= 0.270211:
                                            if features["T(up) - time_left"] <= -0.289996:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 3
                                    else:
                                        if features["T(DOWN)"] <= 0.000001:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    return 3
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.306866:
                                    if features["T(DOWN) - T(RIGHT)"] <= -0.000671:
                                        if features["E(UP) - T(LEFT)"] <= 0.081224:
                                            return 3
                                        else:
                                            return 2
                                    else:
                                        return 0
                                else:
                                    if features["E(DOWN) - T(up)"] <= -0.158923:
                                        if features["T(LEFT)"] <= 0.000002:
                                            return 2
                                        else:
                                            return 3
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -8.773183:
                                            return 0
                                        else:
                                            return 1
        else:
            if features["E(DOWN) - E(RIGHT)"] <= 0.189302:
                if features["E(UP) - E(DOWN)"] <= -0.330230:
                    if features["E(UP) - E(DOWN)"] <= -0.800711:
                        if features["E(UP) - T(LEFT)"] <= -0.000001:
                            if features["T(up) - agent_column"] <= -11.999895:
                                if features["T(DOWN) - time_left"] <= 0.522562:
                                    if features["E(LEFT) - agent_row"] <= 0.000048:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    return 3
                            else:
                                if features["T(DOWN) - agent_column"] <= -8.000000:
                                    if features["T(up) - time_left"] <= -0.329869:
                                        return 3
                                    else:
                                        if features["E(LEFT) - agent_column"] <= -9.999959:
                                            if features["E(UP) - agent_column"] <= -10.000000:
                                                return 3
                                            else:
                                                if features["T(DOWN) - agent_row"] <= -7.589098:
                                                    return 1
                                                else:
                                                    if features["E(UP)"] <= 0.000002:
                                                        return 1
                                                    else:
                                                        return 3
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT) - agent_column"] <= -7.999914:
                                        if features["T(up) - T(LEFT)"] <= -0.506159:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -5.999902:
                                            return 3
                                        else:
                                            if features["T(up) - agent_column"] <= -0.998704:
                                                if features["T(RIGHT) - agent_column"] <= -0.993010:
                                                    if features["E(LEFT) - agent_column"] <= -2.000000:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 3
                                            else:
                                                return 1
                        else:
                            if features["T(up) - agent_column"] <= -5.999892:
                                return 3
                            else:
                                return 1
                    else:
                        if features["E(UP)"] <= 0.000001:
                            if features["T(DOWN) - T(LEFT)"] <= 0.363219:
                                if features["agent_row - time_left"] <= -0.020000:
                                    if features["E(RIGHT) - T(LEFT)"] <= 0.046705:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -11.221480:
                                        return 3
                                    else:
                                        if features["E(LEFT) - time_left"] <= -0.900000:
                                            return 2
                                        else:
                                            return 1
                            else:
                                if features["T(DOWN) - agent_column"] <= -4.509103:
                                    return 1
                                else:
                                    if features["T(RIGHT) - time_left"] <= -0.669665:
                                        return 3
                                    else:
                                        return 1
                        else:
                            if features["E(UP) - E(LEFT)"] <= -0.058009:
                                if features["E(DOWN) - agent_column"] <= -5.569753:
                                    if features["E(RIGHT) - time_left"] <= 0.241366:
                                        if features["T(RIGHT) - agent_row"] <= -8.998810:
                                            if features["T(LEFT) - time_left"] <= -0.124336:
                                                return 1
                                            else:
                                                if features["E(DOWN) - time_left"] <= -0.023305:
                                                    return 2
                                                else:
                                                    return 3
                                        else:
                                            if features["E(UP) - E(LEFT)"] <= -0.112717:
                                                if features["T(up)"] <= 0.000000:
                                                    if features["E(UP) - T(DOWN)"] <= -0.477969:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - agent_column"] <= -8.778512:
                                                            return 1
                                                        else:
                                                            return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["T(DOWN) - T(LEFT)"] <= 0.252731:
                                                    if features["E(RIGHT) - agent_column"] <= -7.703577:
                                                        return 1
                                                    else:
                                                        if features["agent_row - time_left"] <= 4.820000:
                                                            if features["T(DOWN) - T(LEFT)"] <= 0.008110:
                                                                return 1
                                                            else:
                                                                return 3
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(UP) - T(DOWN)"] <= -0.470176:
                                                        return 1
                                                    else:
                                                        if features["T(DOWN) - time_left"] <= 0.080911:
                                                            return 1
                                                        else:
                                                            return 3
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -5.497590:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["T(LEFT) - agent_row"] <= -0.843169:
                                        if features["T(up) - time_left"] <= -0.129961:
                                            if features["T(up) - agent_column"] <= -3.994688:
                                                if features["T(RIGHT) - agent_row"] <= -6.784017:
                                                    if features["E(LEFT) - T(LEFT)"] <= -0.461961:
                                                        return 3
                                                    else:
                                                        if features["agent_row - time_left"] <= 9.760000:
                                                            return 1
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(UP) - T(LEFT)"] <= 0.027320:
                                                        return 1
                                                    else:
                                                        return 2
                                            else:
                                                if features["E(UP) - E(RIGHT)"] <= -0.334436:
                                                    return 3
                                                else:
                                                    return 1
                                        else:
                                            if features["T(up)"] <= 0.000000:
                                                if features["E(RIGHT) - T(DOWN)"] <= -0.184430:
                                                    return 1
                                                else:
                                                    if features["E(DOWN)"] <= 0.450981:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                if features["T(up) - T(DOWN)"] <= -0.379100:
                                                    if features["T(up) - T(LEFT)"] <= -0.001274:
                                                        return 1
                                                    else:
                                                        if features["T(DOWN) - agent_row"] <= -4.273539:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    if features["T(DOWN)"] <= 0.367789:
                                                        if features["T(RIGHT) - agent_row"] <= -9.998964:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 3
                                    else:
                                        if features["E(DOWN) - time_left"] <= 0.362719:
                                            return 1
                                        else:
                                            return 3
                            else:
                                if features["E(DOWN) - agent_column"] <= -10.317395:
                                    if features["agent_row - agent_column"] <= -0.500000:
                                        if features["E(LEFT) - T(DOWN)"] <= -0.653359:
                                            return 1
                                        else:
                                            if features["E(LEFT)"] <= 0.050646:
                                                return 1
                                            else:
                                                if features["T(up)"] <= 0.000414:
                                                    return 1
                                                else:
                                                    return 3
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -11.219597:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["T(LEFT) - agent_column"] <= -1.974769:
                                        if features["T(RIGHT) - agent_row"] <= -1.999949:
                                            if features["T(RIGHT) - agent_row"] <= -11.260824:
                                                return 3
                                            else:
                                                if features["E(LEFT) - T(DOWN)"] <= -0.312370:
                                                    if features["T(DOWN) - T(LEFT)"] <= -0.000200:
                                                        if features["agent_row - agent_column"] <= 0.500000:
                                                            if features["E(DOWN) - T(up)"] <= 0.711726:
                                                                if features["E(UP)"] <= 0.069070:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(DOWN) - time_left"] <= 0.302436:
                                                                return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["E(UP) - T(RIGHT)"] <= -0.398430:
                                                            if features["T(RIGHT)"] <= 0.441995:
                                                                return 1
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(UP) - agent_column"] <= -2.996158:
                                                                if features["E(UP) - T(DOWN)"] <= -0.656144:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                            else:
                                                                return 3
                                                else:
                                                    if features["E(UP)"] <= 0.000037:
                                                        return 1
                                                    else:
                                                        if features["T(up) - agent_column"] <= -10.608665:
                                                            return 3
                                                        else:
                                                            if features["E(RIGHT) - time_left"] <= 0.176678:
                                                                return 3
                                                            else:
                                                                return 1
                                        else:
                                            if features["T(RIGHT) - time_left"] <= -0.129877:
                                                if features["agent_row - agent_column"] <= -8.500000:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["E(LEFT) - T(DOWN)"] <= -0.466381:
                                                    return 3
                                                else:
                                                    if features["E(DOWN) - agent_column"] <= -1.602543:
                                                        return 3
                                                    else:
                                                        return 1
                                    else:
                                        return 1
                else:
                    if features["E(UP) - agent_row"] <= -3.852823:
                        if features["T(LEFT)"] <= 0.000035:
                            if features["E(DOWN) - agent_row"] <= -8.739563:
                                return 3
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.283963:
                                    if features["E(LEFT) - agent_column"] <= -4.770670:
                                        if features["T(up)"] <= 0.000000:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -2.000000:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    if features["T(LEFT)"] <= 0.000001:
                                        if features["agent_row - agent_column"] <= 0.500000:
                                            return 1
                                        else:
                                            if features["E(RIGHT)"] <= 0.322972:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        return 1
                        else:
                            if features["E(LEFT) - T(RIGHT)"] <= 0.235463:
                                if features["E(LEFT) - time_left"] <= 0.245991:
                                    if features["E(UP) - T(up)"] <= 0.006398:
                                        if features["T(up) - time_left"] <= 0.267744:
                                            if features["E(UP) - time_left"] <= -0.308647:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -8.484006:
                                                if features["T(DOWN) - agent_column"] <= -7.999900:
                                                    return 3
                                                else:
                                                    if features["E(DOWN) - T(LEFT)"] <= 0.308502:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                return 1
                                    else:
                                        if features["E(DOWN) - T(up)"] <= 0.133602:
                                            return 0
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= -0.329155:
                                                if features["T(LEFT) - agent_column"] <= -5.095414:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["T(up)"] <= 0.000000:
                                                    if features["agent_row - agent_column"] <= -2.500000:
                                                        if features["E(UP) - agent_column"] <= -8.886703:
                                                            return 3
                                                        else:
                                                            if features["T(up) - T(DOWN)"] <= -0.670282:
                                                                return 3
                                                            else:
                                                                return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(RIGHT) - agent_row"] <= -8.855176:
                                                        return 3
                                                    else:
                                                        if features["T(up) - agent_row"] <= -3.999758:
                                                            if features["E(UP) - agent_row"] <= -5.831514:
                                                                if features["T(DOWN) - T(RIGHT)"] <= 0.091195:
                                                                    return 3
                                                                else:
                                                                    return 1
                                                            else:
                                                                return 3
                                                        else:
                                                            return 1
                                else:
                                    if features["T(DOWN) - agent_row"] <= -4.666681:
                                        return 0
                                    else:
                                        if features["E(DOWN)"] <= 0.333824:
                                            return 3
                                        else:
                                            return 1
                            else:
                                if features["T(up)"] <= 0.000000:
                                    return 0
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -8.999713:
                                        return 3
                                    else:
                                        if features["E(UP) - E(LEFT)"] <= -0.109366:
                                            if features["T(up) - T(RIGHT)"] <= 0.474111:
                                                if features["agent_column - time_left"] <= 8.880000:
                                                    return 3
                                                else:
                                                    if features["agent_column - time_left"] <= 10.800000:
                                                        return 1
                                                    else:
                                                        return 3
                                            else:
                                                return 1
                                        else:
                                            if features["T(RIGHT)"] <= 0.000001:
                                                if features["T(DOWN) - agent_column"] <= -7.999785:
                                                    if features["E(LEFT) - agent_row"] <= -4.739273:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["T(DOWN) - agent_row"] <= -4.514408:
                                                    if features["E(UP) - E(DOWN)"] <= -0.086679:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                    else:
                        if features["E(UP) - E(RIGHT)"] <= -0.141235:
                            if features["T(DOWN) - T(LEFT)"] <= 0.207910:
                                if features["agent_row - agent_column"] <= -6.500000:
                                    return 1
                                else:
                                    if features["T(RIGHT)"] <= 0.305175:
                                        if features["E(RIGHT) - time_left"] <= 0.267506:
                                            if features["T(up)"] <= 0.060872:
                                                if features["E(UP) - E(DOWN)"] <= -0.298409:
                                                    return 1
                                                else:
                                                    if features["E(LEFT) - T(LEFT)"] <= -0.332219:
                                                        return 3
                                                    else:
                                                        if features["T(DOWN) - agent_column"] <= -5.556397:
                                                            return 0
                                                        else:
                                                            return 3
                                            else:
                                                return 0
                                        else:
                                            return 3
                                    else:
                                        if features["E(DOWN) - time_left"] <= 0.315829:
                                            return 3
                                        else:
                                            return 1
                            else:
                                if features["T(LEFT)"] <= 0.000000:
                                    return 1
                                else:
                                    if features["E(RIGHT) - time_left"] <= 0.270307:
                                        if features["T(LEFT) - agent_column"] <= -3.999978:
                                            if features["E(LEFT)"] <= 0.173400:
                                                if features["E(LEFT) - T(DOWN)"] <= -0.526287:
                                                    return 1
                                                else:
                                                    if features["agent_row - agent_column"] <= -8.500000:
                                                        return 1
                                                    else:
                                                        if features["T(LEFT)"] <= 0.152924:
                                                            return 3
                                                        else:
                                                            return 1
                                            else:
                                                return 0
                                        else:
                                            if features["agent_row - time_left"] <= -0.360000:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        if features["T(RIGHT)"] <= 0.404728:
                                            return 3
                                        else:
                                            return 1
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= 0.005715:
                                if features["E(LEFT) - time_left"] <= 0.179199:
                                    if features["E(DOWN) - agent_row"] <= -1.707331:
                                        if features["T(LEFT)"] <= 0.000000:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -1.402732:
                                        if features["T(up)"] <= 0.000000:
                                            return 0
                                        else:
                                            return 1
                                    else:
                                        return 2
                            else:
                                if features["E(RIGHT) - time_left"] <= 0.240336:
                                    if features["E(UP) - time_left"] <= -0.099597:
                                        if features["E(LEFT) - agent_column"] <= -8.786274:
                                            return 1
                                        else:
                                            return 0
                                    else:
                                        if features["T(LEFT) - time_left"] <= 0.510565:
                                            if features["E(LEFT) - agent_row"] <= -0.780735:
                                                if features["T(DOWN) - time_left"] <= 0.694651:
                                                    return 0
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(DOWN) - T(LEFT)"] <= -0.000060:
                                                return 1
                                            else:
                                                return 0
                                else:
                                    if features["E(DOWN) - time_left"] <= 0.326740:
                                        return 3
                                    else:
                                        return 1
            else:
                if features["E(LEFT)"] <= 0.729001:
                    if features["E(UP) - time_left"] <= -0.002634:
                        if features["E(UP) - T(RIGHT)"] <= 0.000106:
                            if features["E(DOWN) - E(LEFT)"] <= 0.097317:
                                if features["T(LEFT) - agent_row"] <= -1.618659:
                                    if features["E(DOWN) - agent_row"] <= -10.271745:
                                        if features["E(UP) - E(DOWN)"] <= -0.416105:
                                            return 2
                                        else:
                                            return 3
                                    else:
                                        if features["E(UP)"] <= 0.066452:
                                            if features["E(DOWN) - time_left"] <= -0.103508:
                                                if features["E(UP) - T(RIGHT)"] <= -0.000006:
                                                    if features["E(UP) - E(RIGHT)"] <= -0.042709:
                                                        return 0
                                                    else:
                                                        if features["E(LEFT) - agent_row"] <= -3.462555:
                                                            return 2
                                                        else:
                                                            return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["E(UP) - agent_row"] <= -1.977312:
                                                    if features["E(RIGHT) - T(DOWN)"] <= -0.381676:
                                                        if features["E(RIGHT) - T(DOWN)"] <= -0.381766:
                                                            if features["E(UP) - E(DOWN)"] <= -0.729925:
                                                                return 1
                                                            else:
                                                                if features["E(UP) - T(up)"] <= -0.000000:
                                                                    return 1
                                                                else:
                                                                    if features["E(RIGHT) - T(DOWN)"] <= -0.390297:
                                                                        return 1
                                                                    else:
                                                                        return 3
                                                        else:
                                                            return 3
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(RIGHT) - time_left"] <= 0.005432:
                                                        return 1
                                                    else:
                                                        return 2
                                        else:
                                            if features["T(LEFT) - time_left"] <= 0.148205:
                                                if features["T(RIGHT) - agent_row"] <= -9.386381:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                else:
                                    if features["E(RIGHT) - T(DOWN)"] <= -0.375657:
                                        if features["E(UP) - agent_row"] <= -1.998595:
                                            return 1
                                        else:
                                            if features["T(DOWN) - time_left"] <= 0.343796:
                                                if features["E(UP) - time_left"] <= -0.129851:
                                                    if features["E(LEFT) - agent_row"] <= -0.668129:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    return 2
                                            else:
                                                if features["E(RIGHT) - T(DOWN)"] <= -0.731214:
                                                    return 2
                                                else:
                                                    return 1
                                    else:
                                        if features["E(UP)"] <= 0.015287:
                                            if features["E(DOWN) - T(DOWN)"] <= 0.304587:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(LEFT) - time_left"] <= 0.181741:
                                                return 1
                                            else:
                                                return 2
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= -0.013950:
                                    if features["E(UP) - T(LEFT)"] <= 0.019380:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.604851:
                                            if features["T(LEFT) - time_left"] <= -0.769915:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -9.998999:
                                                if features["E(DOWN) - agent_row"] <= -9.329678:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                    else:
                                        if features["E(RIGHT) - agent_column"] <= -5.773815:
                                            if features["T(up) - time_left"] <= -0.069987:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 2
                                else:
                                    if features["E(DOWN) - agent_row"] <= -12.130104:
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.393349:
                                            return 3
                                        else:
                                            return 2
                                    else:
                                        if features["agent_column - time_left"] <= -0.620000:
                                            return 0
                                        else:
                                            if features["T(LEFT) - time_left"] <= -0.629910:
                                                if features["T(up) - agent_column"] <= -1.546321:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                        else:
                            if features["agent_row - agent_column"] <= -9.500000:
                                if features["E(DOWN) - T(LEFT)"] <= 0.007173:
                                    if features["E(LEFT) - E(RIGHT)"] <= 0.319814:
                                        if features["T(RIGHT) - agent_column"] <= -11.999964:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(DOWN) - time_left"] <= 0.328148:
                                            return 2
                                        else:
                                            if features["T(LEFT) - agent_row"] <= -0.341382:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    if features["T(up)"] <= 0.000000:
                                        if features["T(DOWN) - T(LEFT)"] <= 0.332476:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        return 1
                            else:
                                if features["E(DOWN) - agent_row"] <= -8.517826:
                                    if features["E(DOWN) - E(RIGHT)"] <= 0.336944:
                                        if features["T(up) - T(LEFT)"] <= -0.000663:
                                            return 3
                                        else:
                                            if features["T(RIGHT) - time_left"] <= -0.249967:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        if features["agent_row - time_left"] <= 10.150000:
                                            if features["T(DOWN) - time_left"] <= -0.609898:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.316089:
                                                if features["E(UP) - agent_column"] <= -10.993930:
                                                    return 2
                                                else:
                                                    if features["T(DOWN) - T(LEFT)"] <= -0.027922:
                                                        return 1
                                                    else:
                                                        return 2
                                            else:
                                                return 1
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= 0.000006:
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.409544:
                                            if features["E(UP) - T(up)"] <= 0.031230:
                                                if features["E(LEFT) - agent_row"] <= -0.658320:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -6.287227:
                                                if features["T(DOWN)"] <= 0.000001:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                return 2
                                    else:
                                        if features["E(UP) - E(DOWN)"] <= -0.333087:
                                            if features["agent_row - agent_column"] <= -3.500000:
                                                if features["E(LEFT) - time_left"] <= 0.218712:
                                                    if features["E(UP) - T(up)"] <= 0.008404:
                                                        return 1
                                                    else:
                                                        if features["E(UP) - agent_row"] <= -1.983810:
                                                            return 1
                                                        else:
                                                            return 0
                                                else:
                                                    if features["T(DOWN) - agent_row"] <= -1.594926:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - agent_column"] <= -8.986360:
                                                            return 2
                                                        else:
                                                            return 1
                                            else:
                                                if features["E(RIGHT) - agent_row"] <= -6.786707:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -3.555468:
                                                        return 2
                                                    else:
                                                        return 1
                                        else:
                                            return 0
                    else:
                        if features["T(DOWN) - T(RIGHT)"] <= 0.188414:
                            if features["T(RIGHT) - agent_row"] <= -2.000000:
                                return 1
                            else:
                                if features["agent_column - time_left"] <= 6.980000:
                                    return 1
                                else:
                                    return 2
                        else:
                            if features["T(up) - time_left"] <= -0.002796:
                                if features["T(LEFT) - agent_column"] <= -9.845306:
                                    if features["T(up)"] <= 0.040118:
                                        if features["T(DOWN) - agent_row"] <= -2.536318:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 3
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= 0.000003:
                                        return 1
                                    else:
                                        return 0
                            else:
                                if features["E(RIGHT) - T(RIGHT)"] <= -0.006760:
                                    return 3
                                else:
                                    return 0
                else:
                    if features["T(LEFT) - agent_row"] <= -1.793520:
                        if features["E(DOWN) - agent_row"] <= -11.200801:
                            return 2
                        else:
                            if features["E(RIGHT) - agent_row"] <= -6.999994:
                                if features["T(up) - agent_row"] <= -11.609453:
                                    if features["E(DOWN)"] <= 0.799634:
                                        return 1
                                    else:
                                        if features["agent_column - time_left"] <= 9.610000:
                                            if features["E(RIGHT)"] <= 0.000287:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 2
                                else:
                                    if features["E(UP) - T(DOWN)"] <= -0.728807:
                                        return 1
                                    else:
                                        if features["agent_row - agent_column"] <= 2.500000:
                                            if features["E(DOWN) - agent_row"] <= -10.222363:
                                                if features["E(DOWN) - agent_row"] <= -11.200369:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -9.999958:
                                                    return 1
                                                else:
                                                    if features["agent_row - agent_column"] <= -1.500000:
                                                        return 2
                                                    else:
                                                        return 1
                                        else:
                                            return 1
                            else:
                                if features["E(RIGHT) - agent_column"] <= -1.999929:
                                    if features["E(UP)"] <= 0.000000:
                                        if features["E(UP) - T(up)"] <= -0.000000:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(RIGHT) - agent_column"] <= -10.999999:
                                            return 1
                                        else:
                                            if features["E(LEFT)"] <= 0.864041:
                                                return 2
                                            else:
                                                if features["E(UP) - agent_column"] <= -5.000000:
                                                    if features["T(up) - agent_column"] <= -8.771278:
                                                        return 2
                                                    else:
                                                        if features["T(RIGHT) - agent_row"] <= -4.702730:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    if features["agent_row - agent_column"] <= 3.500000:
                                                        if features["agent_row - time_left"] <= 1.680000:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        return 1
                                else:
                                    if features["T(up) - time_left"] <= -0.669642:
                                        return 3
                                    else:
                                        return 1
                    else:
                        if features["E(RIGHT) - agent_row"] <= 0.000009:
                            if features["E(UP) - agent_row"] <= -1.999203:
                                return 2
                            else:
                                if features["E(UP) - agent_column"] <= -1.997162:
                                    if features["E(LEFT) - time_left"] <= 0.154970:
                                        return 3
                                    else:
                                        return 2
                                else:
                                    return 1
                        else:
                            if features["E(RIGHT) - agent_column"] <= -6.999935:
                                if features["E(DOWN) - T(up)"] <= 0.868108:
                                    if features["E(LEFT)"] <= 0.867889:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 2
                            else:
                                if features["T(RIGHT) - agent_column"] <= -1.998296:
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
