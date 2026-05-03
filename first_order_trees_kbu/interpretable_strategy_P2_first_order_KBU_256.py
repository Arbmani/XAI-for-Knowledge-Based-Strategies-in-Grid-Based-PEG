import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(DOWN)"] <= -0.364744:
        if features["E(LEFT) - E(RIGHT)"] <= 0.329779:
            if features["E(RIGHT)"] <= 0.334643:
                if features["E(UP)"] <= 0.008222:
                    if features["E(LEFT) - T(LEFT)"] <= 0.004412:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.018016:
                            if features["E(UP) - T(DOWN)"] <= -0.510883:
                                if features["E(DOWN) - E(RIGHT)"] <= 0.265298:
                                    if features["agent_row - time_left"] <= 4.820000:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(LEFT)"] <= 0.325931:
                                        if features["E(RIGHT) - T(up)"] <= 0.294813:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        if features["agent_row - time_left"] <= 7.280000:
                                            return 1
                                        else:
                                            return 2
                            else:
                                return 1
                        else:
                            if features["T(LEFT) - agent_column"] <= -6.281099:
                                if features["agent_row - agent_column"] <= -7.500000:
                                    if features["T(LEFT) - agent_column"] <= -8.592926:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN) - T(up)"] <= 0.553953:
                                        return 1
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.382381:
                                            return 2
                                        else:
                                            return 1
                            else:
                                return 1
                    else:
                        if features["agent_row - agent_column"] <= -6.500000:
                            return 2
                        else:
                            return 1
                else:
                    if features["E(RIGHT) - T(DOWN)"] <= -0.261845:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.176830:
                            return 2
                        else:
                            return 3
                    else:
                        return 0
            else:
                if features["E(RIGHT) - agent_column"] <= -11.208409:
                    if features["E(DOWN) - T(up)"] <= 0.850646:
                        return 1
                    else:
                        return 3
                else:
                    if features["E(RIGHT) - agent_row"] <= -11.208409:
                        if features["E(DOWN) - E(RIGHT)"] <= 0.189213:
                            return 3
                        else:
                            return 1
                    else:
                        if features["T(up) - agent_column"] <= -1.458671:
                            if features["E(DOWN) - agent_column"] <= -7.442202:
                                if features["E(UP) - E(DOWN)"] <= -0.611864:
                                    if features["T(up) - T(LEFT)"] <= -0.310582:
                                        return 3
                                    else:
                                        if features["E(LEFT) - E(RIGHT)"] <= -0.802442:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    return 1
                            else:
                                if features["E(UP) - E(RIGHT)"] <= -0.345676:
                                    if features["E(DOWN) - agent_row"] <= -9.338459:
                                        if features["E(LEFT) - E(RIGHT)"] <= -0.728881:
                                            return 3
                                        else:
                                            if features["E(RIGHT) - time_left"] <= 0.165074:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -7.790336:
                                            return 1
                                        else:
                                            if features["E(DOWN) - agent_row"] <= -0.548621:
                                                if features["E(LEFT) - agent_row"] <= -4.893734:
                                                    return 3
                                                else:
                                                    if features["E(LEFT) - E(RIGHT)"] <= -0.791591:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT)"] <= 0.452069:
                                                            return 1
                                                        else:
                                                            return 3
                                            else:
                                                return 3
                                else:
                                    if features["E(DOWN) - T(up)"] <= 0.524348:
                                        if features["E(LEFT) - T(RIGHT)"] <= -0.578451:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 3
                        else:
                            if features["E(DOWN) - agent_row"] <= -8.487992:
                                return 3
                            else:
                                if features["E(LEFT) - T(up)"] <= 0.039755:
                                    return 1
                                else:
                                    return 3
        else:
            if features["E(LEFT) - agent_row"] <= -11.208409:
                return 2
            else:
                if features["E(RIGHT) - agent_column"] <= -12.978880:
                    return 1
                else:
                    if features["agent_row - time_left"] <= 2.840000:
                        if features["T(DOWN) - agent_column"] <= -1.675289:
                            if features["agent_row - time_left"] <= -0.100000:
                                return 1
                            else:
                                return 2
                        else:
                            return 1
                    else:
                        if features["E(DOWN)"] <= 0.805255:
                            if features["E(LEFT) - agent_row"] <= -9.338459:
                                if features["E(UP) - E(LEFT)"] <= -0.708946:
                                    return 1
                                else:
                                    return 2
                            else:
                                if features["T(RIGHT) - agent_column"] <= -1.600205:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.005833:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 1
                        else:
                            if features["T(RIGHT) - agent_row"] <= -11.431408:
                                return 1
                            else:
                                if features["T(up) - agent_column"] <= -0.754147:
                                    return 2
                                else:
                                    return 1
    else:
        if features["E(LEFT) - E(RIGHT)"] <= -0.370323:
            if features["E(UP) - E(DOWN)"] <= 0.338461:
                if features["E(UP) - T(up)"] <= 0.041449:
                    if features["E(LEFT) - T(LEFT)"] <= 0.011180:
                        return 3
                    else:
                        return 2
                else:
                    if features["E(RIGHT) - T(LEFT)"] <= 0.573767:
                        if features["E(LEFT) - E(RIGHT)"] <= -0.375548:
                            return 3
                        else:
                            return 2
                    else:
                        return 3
            else:
                if features["T(LEFT) - agent_row"] <= -1.902892:
                    if features["E(RIGHT) - agent_column"] <= -11.225466:
                        if features["T(up) - T(LEFT)"] <= 0.095719:
                            if features["T(up) - agent_row"] <= -8.863810:
                                if features["E(RIGHT) - agent_row"] <= -10.217988:
                                    return 0
                                else:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.833876:
                                        return 3
                                    else:
                                        return 0
                            else:
                                return 0
                        else:
                            return 3
                    else:
                        if features["E(UP) - agent_column"] <= -4.166123:
                            if features["T(RIGHT) - agent_row"] <= -12.841552:
                                return 3
                            else:
                                if features["E(RIGHT) - agent_column"] <= -10.275532:
                                    return 0
                                else:
                                    if features["T(LEFT) - agent_column"] <= -9.848379:
                                        return 3
                                    else:
                                        if features["E(UP) - E(LEFT)"] <= 0.747987:
                                            if features["E(UP) - agent_column"] <= -9.383451:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 0
                        else:
                            if features["E(RIGHT) - agent_column"] <= -1.446323:
                                if features["E(RIGHT) - agent_row"] <= -6.507849:
                                    return 3
                                else:
                                    if features["E(RIGHT)"] <= 0.498877:
                                        return 3
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -1.829699:
                                            return 0
                                        else:
                                            return 3
                            else:
                                if features["E(UP) - E(DOWN)"] <= 0.371944:
                                    return 3
                                else:
                                    if features["T(up) - agent_row"] <= -4.521748:
                                        return 0
                                    else:
                                        if features["E(UP) - agent_column"] <= 0.839502:
                                            if features["E(UP) - E(LEFT)"] <= 0.631714:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 3
                else:
                    if features["E(UP) - agent_column"] <= -12.166124:
                        return 0
                    else:
                        return 3
        else:
            if features["E(UP) - E(DOWN)"] <= 0.364744:
                if features["E(LEFT) - E(RIGHT)"] <= 0.380634:
                    if features["E(UP) - T(RIGHT)"] <= 0.089651:
                        if features["E(UP) - agent_column"] <= -9.721687:
                            if features["E(DOWN) - E(LEFT)"] <= 0.120781:
                                if features["E(DOWN) - T(RIGHT)"] <= -0.634281:
                                    return 0
                                else:
                                    if features["E(UP) - T(RIGHT)"] <= 0.028927:
                                        return 2
                                    else:
                                        if features["T(LEFT)"] <= 0.373426:
                                            if features["E(UP) - T(RIGHT)"] <= 0.031832:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -12.597573:
                                                return 3
                                            else:
                                                return 2
                            else:
                                return 1
                        else:
                            if features["T(up) - T(LEFT)"] <= -0.060404:
                                if features["E(DOWN) - T(DOWN)"] <= -0.001587:
                                    if features["E(RIGHT) - T(up)"] <= 0.276357:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["T(up) - T(DOWN)"] <= -0.210964:
                                        return 0
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -8.669916:
                                            return 0
                                        else:
                                            if features["T(DOWN) - agent_row"] <= -3.645097:
                                                return 2
                                            else:
                                                if features["time_left"] <= 0.060000:
                                                    return 1
                                                else:
                                                    return 0
                            else:
                                if features["T(up) - agent_row"] <= -8.675020:
                                    if features["E(UP) - time_left"] <= 0.002699:
                                        return 3
                                    else:
                                        if features["T(up) - T(LEFT)"] <= 0.234018:
                                            if features["E(UP) - T(RIGHT)"] <= 0.064657:
                                                if features["T(RIGHT) - time_left"] <= 0.183252:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 1
                                        else:
                                            if features["E(LEFT)"] <= 0.046376:
                                                if features["T(LEFT) - agent_column"] <= -0.956835:
                                                    if features["T(RIGHT) - agent_column"] <= -0.642845:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                            else:
                                                if features["E(RIGHT) - T(DOWN)"] <= 0.238921:
                                                    if features["E(LEFT) - E(RIGHT)"] <= 0.166920:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    if features["T(RIGHT) - time_left"] <= 0.315682:
                                                        if features["E(RIGHT) - T(LEFT)"] <= 0.290779:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["E(RIGHT) - T(up)"] <= -0.034291:
                                                            if features["T(RIGHT) - time_left"] <= 0.363027:
                                                                return 1
                                                            else:
                                                                return 0
                                                        else:
                                                            return 3
                                else:
                                    if features["E(UP)"] <= 0.175643:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.016179:
                                            if features["E(RIGHT)"] <= 0.246158:
                                                return 1
                                            else:
                                                if features["E(UP) - T(LEFT)"] <= 0.050387:
                                                    if features["E(DOWN) - agent_column"] <= -4.650525:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(RIGHT) - time_left"] <= 0.377489:
                                                        return 2
                                                    else:
                                                        return 3
                                        else:
                                            if features["E(RIGHT) - time_left"] <= 0.180014:
                                                if features["E(RIGHT) - agent_row"] <= -2.765203:
                                                    return 2
                                                else:
                                                    if features["E(LEFT) - agent_row"] <= -1.739745:
                                                        if features["T(RIGHT) - time_left"] <= 0.391808:
                                                            return 0
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["E(DOWN) - T(LEFT)"] <= 0.332181:
                                                            return 1
                                                        else:
                                                            return 2
                                            else:
                                                return 1
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.305050:
                                            if features["T(up) - agent_row"] <= -8.669916:
                                                if features["T(RIGHT) - time_left"] <= 0.188803:
                                                    return 2
                                                else:
                                                    return 3
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.285583:
                                                    if features["E(UP) - E(LEFT)"] <= 0.120824:
                                                        if features["T(LEFT) - agent_row"] <= -4.808249:
                                                            if features["T(DOWN) - T(LEFT)"] <= 0.060198:
                                                                if features["E(RIGHT) - time_left"] <= 0.251373:
                                                                    return 2
                                                                else:
                                                                    if features["T(up) - agent_row"] <= -8.665808:
                                                                        return 3
                                                                    else:
                                                                        return 2
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["E(UP) - T(DOWN)"] <= -0.119556:
                                                                return 2
                                                            else:
                                                                if features["agent_column - time_left"] <= 4.880000:
                                                                    return 2
                                                                else:
                                                                    return 3
                                                    else:
                                                        if features["T(LEFT)"] <= 0.093486:
                                                            if features["E(DOWN)"] <= 0.201200:
                                                                if features["E(DOWN) - T(RIGHT)"] <= -0.356817:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                if features["T(LEFT)"] <= 0.047331:
                                                                    if features["T(RIGHT) - time_left"] <= 0.401445:
                                                                        if features["E(DOWN) - time_left"] <= -0.084371:
                                                                            return 0
                                                                        else:
                                                                            return 2
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    return 2
                                                        else:
                                                            if features["T(DOWN) - time_left"] <= 0.144148:
                                                                return 2
                                                            else:
                                                                if features["E(RIGHT) - time_left"] <= 0.380810:
                                                                    if features["E(UP) - time_left"] <= 0.265819:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                                else:
                                                                    return 3
                                                else:
                                                    if features["E(RIGHT) - agent_row"] <= -5.631757:
                                                        return 0
                                                    else:
                                                        if features["E(RIGHT) - time_left"] <= 0.293955:
                                                            if features["E(LEFT) - T(RIGHT)"] <= -0.482757:
                                                                return 3
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["E(DOWN) - T(LEFT)"] <= 0.190884:
                                                                return 3
                                                            else:
                                                                if features["E(UP) - T(RIGHT)"] <= -0.215871:
                                                                    return 3
                                                                else:
                                                                    return 2
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -7.333379:
                                                return 2
                                            else:
                                                return 1
                    else:
                        if features["E(LEFT) - T(LEFT)"] <= 0.280541:
                            if features["E(UP) - E(DOWN)"] <= 0.263242:
                                if features["E(LEFT) - T(up)"] <= 0.257678:
                                    if features["E(UP) - T(RIGHT)"] <= 0.309607:
                                        if features["E(RIGHT) - T(up)"] <= -0.412549:
                                            if features["E(UP) - agent_column"] <= -6.735868:
                                                if features["E(LEFT) - time_left"] <= 0.287200:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 3
                                        else:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.243522:
                                                if features["E(LEFT) - time_left"] <= 0.301514:
                                                    if features["E(LEFT) - T(DOWN)"] <= 0.182680:
                                                        return 3
                                                    else:
                                                        if features["E(LEFT) - T(RIGHT)"] <= 0.192985:
                                                            return 1
                                                        else:
                                                            if features["E(LEFT) - agent_row"] <= -4.740898:
                                                                return 3
                                                            else:
                                                                return 1
                                                else:
                                                    return 2
                                            else:
                                                return 3
                                    else:
                                        if features["E(LEFT) - time_left"] <= 0.254661:
                                            if features["E(LEFT) - T(up)"] <= 0.063079:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.283524:
                                        if features["T(DOWN) - agent_row"] <= -4.282117:
                                            if features["E(UP) - time_left"] <= 0.159730:
                                                if features["T(DOWN)"] <= 0.455398:
                                                    return 3
                                                else:
                                                    if features["T(DOWN) - agent_column"] <= -7.450926:
                                                        if features["E(UP) - T(DOWN)"] <= -0.314539:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                            else:
                                                if features["E(UP) - agent_row"] <= -7.692071:
                                                    return 0
                                                else:
                                                    if features["T(LEFT) - agent_row"] <= -6.503272:
                                                        return 3
                                                    else:
                                                        if features["E(LEFT) - time_left"] <= 0.326153:
                                                            return 0
                                                        else:
                                                            return 2
                                        else:
                                            if features["agent_column - time_left"] <= 9.760000:
                                                if features["T(LEFT) - time_left"] <= 0.363294:
                                                    return 0
                                                else:
                                                    if features["E(LEFT)"] <= 0.280189:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                return 2
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.245430:
                                            if features["E(RIGHT) - T(LEFT)"] <= -0.609414:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 3
                            else:
                                if features["E(UP) - T(LEFT)"] <= 0.064494:
                                    if features["T(DOWN) - time_left"] <= 0.002231:
                                        return 0
                                    else:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.185489:
                                            return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(UP)"] <= 0.384758:
                                        if features["E(DOWN) - T(LEFT)"] <= 0.016868:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        if features["E(UP) - T(DOWN)"] <= 0.364184:
                                            return 1
                                        else:
                                            if features["E(LEFT) - T(up)"] <= -0.189064:
                                                return 1
                                            else:
                                                return 3
                        else:
                            if features["E(UP) - T(up)"] <= 0.276544:
                                if features["E(RIGHT) - T(up)"] <= 0.233588:
                                    if features["E(DOWN) - T(up)"] <= -0.627311:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 0
                            else:
                                return 0
                else:
                    if features["E(LEFT) - time_left"] <= 0.336173:
                        if features["T(LEFT) - agent_column"] <= -13.595424:
                            if features["E(LEFT) - time_left"] <= 0.001525:
                                return 0
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.178445:
                                    if features["E(LEFT) - T(up)"] <= 0.433371:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 1
                        else:
                            if features["E(UP) - T(up)"] <= 0.288227:
                                if features["E(UP)"] <= 0.377370:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.191662:
                                        return 2
                                    else:
                                        if features["E(RIGHT) - time_left"] <= -0.667199:
                                            return 3
                                        else:
                                            return 2
                                else:
                                    if features["T(LEFT) - agent_column"] <= -4.418228:
                                        return 2
                                    else:
                                        return 0
                            else:
                                return 0
                    else:
                        if features["E(UP)"] <= 0.377370:
                            return 2
                        else:
                            if features["T(LEFT) - agent_column"] <= -4.418228:
                                return 2
                            else:
                                return 0
            else:
                if features["E(LEFT) - E(RIGHT)"] <= 0.311758:
                    if features["E(DOWN)"] <= 0.011180:
                        if features["T(up) - T(DOWN)"] <= 0.483031:
                            if features["E(LEFT) - T(LEFT)"] <= 0.230707:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.365750:
                                    return 3
                                else:
                                    return 0
                            else:
                                return 0
                        else:
                            if features["E(RIGHT)"] <= 0.036742:
                                return 0
                            else:
                                if features["T(up) - time_left"] <= 0.345561:
                                    if features["T(LEFT) - agent_column"] <= -2.936875:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 0
                    else:
                        return 1
                else:
                    if features["T(DOWN) - agent_row"] <= -0.863734:
                        if features["T(up) - agent_column"] <= -1.902892:
                            if features["E(UP) - agent_row"] <= -10.194745:
                                if features["E(UP)"] <= 0.839502:
                                    if features["E(LEFT) - E(RIGHT)"] <= 0.368961:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 0
                            else:
                                if features["E(LEFT) - T(RIGHT)"] <= 0.545367:
                                    if features["T(up) - T(LEFT)"] <= -0.150598:
                                        if features["T(DOWN) - agent_row"] <= -5.482959:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        if features["T(LEFT) - agent_row"] <= -3.813010:
                                            return 0
                                        else:
                                            if features["E(UP) - E(RIGHT)"] <= 0.724468:
                                                return 2
                                            else:
                                                return 0
                                else:
                                    if features["agent_row - agent_column"] <= -2.500000:
                                        if features["agent_row - time_left"] <= 2.540000:
                                            if features["E(DOWN) - E(LEFT)"] <= -0.791030:
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
