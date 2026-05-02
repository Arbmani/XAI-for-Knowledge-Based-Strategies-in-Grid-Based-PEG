import random
from INTERPRETER_2ND import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'T(E(UP))', 'T(E(DOWN))', 'T(E(LEFT))', 'T(E(RIGHT))', 'T(T(up))', 'T(T(DOWN))', 'T(T(LEFT))', 'T(T(RIGHT))', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - T(E(UP))', 'E(UP) - T(E(DOWN))', 'E(UP) - T(E(LEFT))', 'E(UP) - T(E(RIGHT))', 'E(UP) - T(T(up))', 'E(UP) - T(T(DOWN))', 'E(UP) - T(T(LEFT))', 'E(UP) - T(T(RIGHT))', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - T(E(UP))', 'E(DOWN) - T(E(DOWN))', 'E(DOWN) - T(E(LEFT))', 'E(DOWN) - T(E(RIGHT))', 'E(DOWN) - T(T(up))', 'E(DOWN) - T(T(DOWN))', 'E(DOWN) - T(T(LEFT))', 'E(DOWN) - T(T(RIGHT))', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - T(E(UP))', 'E(LEFT) - T(E(DOWN))', 'E(LEFT) - T(E(LEFT))', 'E(LEFT) - T(E(RIGHT))', 'E(LEFT) - T(T(up))', 'E(LEFT) - T(T(DOWN))', 'E(LEFT) - T(T(LEFT))', 'E(LEFT) - T(T(RIGHT))', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - T(E(UP))', 'E(RIGHT) - T(E(DOWN))', 'E(RIGHT) - T(E(LEFT))', 'E(RIGHT) - T(E(RIGHT))', 'E(RIGHT) - T(T(up))', 'E(RIGHT) - T(T(DOWN))', 'E(RIGHT) - T(T(LEFT))', 'E(RIGHT) - T(T(RIGHT))', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - T(E(UP))', 'T(up) - T(E(DOWN))', 'T(up) - T(E(LEFT))', 'T(up) - T(E(RIGHT))', 'T(up) - T(T(up))', 'T(up) - T(T(DOWN))', 'T(up) - T(T(LEFT))', 'T(up) - T(T(RIGHT))', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - T(E(UP))', 'T(DOWN) - T(E(DOWN))', 'T(DOWN) - T(E(LEFT))', 'T(DOWN) - T(E(RIGHT))', 'T(DOWN) - T(T(up))', 'T(DOWN) - T(T(DOWN))', 'T(DOWN) - T(T(LEFT))', 'T(DOWN) - T(T(RIGHT))', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - T(E(UP))', 'T(LEFT) - T(E(DOWN))', 'T(LEFT) - T(E(LEFT))', 'T(LEFT) - T(E(RIGHT))', 'T(LEFT) - T(T(up))', 'T(LEFT) - T(T(DOWN))', 'T(LEFT) - T(T(LEFT))', 'T(LEFT) - T(T(RIGHT))', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - T(E(UP))', 'T(RIGHT) - T(E(DOWN))', 'T(RIGHT) - T(E(LEFT))', 'T(RIGHT) - T(E(RIGHT))', 'T(RIGHT) - T(T(up))', 'T(RIGHT) - T(T(DOWN))', 'T(RIGHT) - T(T(LEFT))', 'T(RIGHT) - T(T(RIGHT))', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'T(E(UP)) - T(E(DOWN))', 'T(E(UP)) - T(E(LEFT))', 'T(E(UP)) - T(E(RIGHT))', 'T(E(UP)) - T(T(up))', 'T(E(UP)) - T(T(DOWN))', 'T(E(UP)) - T(T(LEFT))', 'T(E(UP)) - T(T(RIGHT))', 'T(E(UP)) - agent_row', 'T(E(UP)) - agent_column', 'T(E(UP)) - time_left', 'T(E(DOWN)) - T(E(LEFT))', 'T(E(DOWN)) - T(E(RIGHT))', 'T(E(DOWN)) - T(T(up))', 'T(E(DOWN)) - T(T(DOWN))', 'T(E(DOWN)) - T(T(LEFT))', 'T(E(DOWN)) - T(T(RIGHT))', 'T(E(DOWN)) - agent_row', 'T(E(DOWN)) - agent_column', 'T(E(DOWN)) - time_left', 'T(E(LEFT)) - T(E(RIGHT))', 'T(E(LEFT)) - T(T(up))', 'T(E(LEFT)) - T(T(DOWN))', 'T(E(LEFT)) - T(T(LEFT))', 'T(E(LEFT)) - T(T(RIGHT))', 'T(E(LEFT)) - agent_row', 'T(E(LEFT)) - agent_column', 'T(E(LEFT)) - time_left', 'T(E(RIGHT)) - T(T(up))', 'T(E(RIGHT)) - T(T(DOWN))', 'T(E(RIGHT)) - T(T(LEFT))', 'T(E(RIGHT)) - T(T(RIGHT))', 'T(E(RIGHT)) - agent_row', 'T(E(RIGHT)) - agent_column', 'T(E(RIGHT)) - time_left', 'T(T(up)) - T(T(DOWN))', 'T(T(up)) - T(T(LEFT))', 'T(T(up)) - T(T(RIGHT))', 'T(T(up)) - agent_row', 'T(T(up)) - agent_column', 'T(T(up)) - time_left', 'T(T(DOWN)) - T(T(LEFT))', 'T(T(DOWN)) - T(T(RIGHT))', 'T(T(DOWN)) - agent_row', 'T(T(DOWN)) - agent_column', 'T(T(DOWN)) - time_left', 'T(T(LEFT)) - T(T(RIGHT))', 'T(T(LEFT)) - agent_row', 'T(T(LEFT)) - agent_column', 'T(T(LEFT)) - time_left', 'T(T(RIGHT)) - agent_row', 'T(T(RIGHT)) - agent_column', 'T(T(RIGHT)) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(LEFT) - E(RIGHT)"] <= 0.328143:
        if features["E(UP) - E(RIGHT)"] <= 0.000003:
            if features["E(DOWN) - E(RIGHT)"] <= -0.000020:
                if features["E(UP) - T(T(up))"] <= 0.031269:
                    if features["E(UP) - E(DOWN)"] <= -0.799738:
                        if features["T(DOWN) - agent_column"] <= -12.411637:
                            return 1
                        else:
                            if features["T(E(DOWN)) - agent_column"] <= -5.690614:
                                return 3
                            else:
                                if features["T(DOWN) - T(E(DOWN))"] <= -0.017480:
                                    return 1
                                else:
                                    return 3
                    else:
                        if features["E(UP) - T(T(DOWN))"] <= 0.083381:
                            if features["E(LEFT) - T(up)"] <= 0.059033:
                                if features["E(DOWN) - T(E(UP))"] <= 0.251270:
                                    if features["E(LEFT) - T(T(LEFT))"] <= 0.013462:
                                        if features["E(RIGHT)"] <= 0.273870:
                                            if features["E(UP) - agent_row"] <= -10.999970:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        if features["E(DOWN) - T(E(UP))"] <= -0.058373:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT)"] <= 0.000026:
                                        if features["T(DOWN) - agent_column"] <= -12.181350:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        if features["T(up) - agent_column"] <= -0.982358:
                                            if features["E(RIGHT) - agent_column"] <= -11.244479:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(T(up)) - T(T(RIGHT))"] <= -0.182016:
                                                return 1
                                            else:
                                                return 3
                            else:
                                if features["T(LEFT) - T(E(LEFT))"] <= 0.254472:
                                    if features["T(up) - agent_column"] <= -4.999999:
                                        if features["T(up)"] <= 0.000006:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        if features["T(DOWN) - T(E(DOWN))"] <= 0.115377:
                                            return 1
                                        else:
                                            if features["E(UP) - T(LEFT)"] <= 0.231066:
                                                return 3
                                            else:
                                                return 0
                                else:
                                    return 3
                        else:
                            if features["E(RIGHT) - T(T(RIGHT))"] <= 0.019928:
                                if features["T(LEFT) - T(E(LEFT))"] <= -0.010791:
                                    if features["E(RIGHT) - T(RIGHT)"] <= -0.012734:
                                        if features["E(LEFT) - time_left"] <= 0.045267:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                                else:
                                    if features["T(E(RIGHT)) - T(T(RIGHT))"] <= -0.005659:
                                        return 3
                                    else:
                                        if features["E(UP) - T(E(UP))"] <= 0.026159:
                                            return 0
                                        else:
                                            return 3
                            else:
                                if features["E(DOWN) - T(RIGHT)"] <= -0.351490:
                                    if features["E(LEFT) - E(RIGHT)"] <= -0.376129:
                                        return 3
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= 0.000017:
                                            if features["T(RIGHT) - agent_row"] <= -5.200413:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 3
                                else:
                                    if features["E(RIGHT) - time_left"] <= 0.301544:
                                        if features["E(UP) - T(E(DOWN))"] <= 0.191038:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        if features["E(LEFT) - T(E(LEFT))"] <= -0.365698:
                                            return 1
                                        else:
                                            return 3
                else:
                    if features["E(LEFT) - T(up)"] <= 0.066862:
                        if features["E(DOWN) - E(RIGHT)"] <= -0.800900:
                            if features["E(DOWN) - E(LEFT)"] <= 0.000022:
                                if features["T(T(DOWN)) - agent_column"] <= -0.915752:
                                    if features["T(up) - T(RIGHT)"] <= -0.580698:
                                        return 0
                                    else:
                                        if features["E(RIGHT) - agent_column"] <= -1.132048:
                                            if features["T(T(RIGHT)) - time_left"] <= 0.109064:
                                                if features["T(LEFT) - agent_column"] <= -12.533249:
                                                    if features["T(RIGHT) - agent_row"] <= -6.000000:
                                                        return 3
                                                    else:
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
                                return 0
                        else:
                            if features["agent_row - agent_column"] <= 7.500000:
                                if features["E(LEFT)"] <= 0.000016:
                                    if features["E(UP) - agent_column"] <= 0.543749:
                                        if features["E(UP) - agent_column"] <= -11.236829:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 0
                                else:
                                    if features["E(DOWN) - T(E(LEFT))"] <= 0.008928:
                                        if features["T(E(RIGHT)) - T(T(RIGHT))"] <= 0.039175:
                                            return 0
                                        else:
                                            if features["E(LEFT) - T(up)"] <= 0.030694:
                                                if features["E(RIGHT) - agent_column"] <= -11.233420:
                                                    return 0
                                                else:
                                                    if features["T(RIGHT) - time_left"] <= 0.590814:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                return 0
                                    else:
                                        if features["T(up) - time_left"] <= -0.129995:
                                            if features["E(LEFT) - T(up)"] <= 0.033838:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -2.996630:
                                                if features["E(RIGHT) - T(E(UP))"] <= 0.042217:
                                                    if features["agent_row - agent_column"] <= 1.500000:
                                                        return 3
                                                    else:
                                                        if features["E(LEFT) - T(LEFT)"] <= 0.019339:
                                                            return 3
                                                        else:
                                                            return 0
                                                else:
                                                    return 3
                                            else:
                                                return 3
                            else:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.006961:
                                    if features["T(E(RIGHT)) - T(T(up))"] <= 0.022351:
                                        return 3
                                    else:
                                        if features["E(RIGHT) - T(E(LEFT))"] <= 0.400094:
                                            if features["E(UP)"] <= 0.338207:
                                                return 0
                                            else:
                                                if features["E(LEFT) - agent_column"] <= -1.998666:
                                                    return 3
                                                else:
                                                    return 0
                                        else:
                                            return 3
                                else:
                                    if features["E(RIGHT) - T(E(UP))"] <= 0.065591:
                                        if features["T(E(UP)) - agent_row"] <= -10.644170:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        if features["agent_column - time_left"] <= -0.060000:
                                            return 0
                                        else:
                                            return 3
                    else:
                        if features["T(DOWN) - T(LEFT)"] <= 0.000045:
                            if features["T(E(UP)) - T(E(RIGHT))"] <= 0.077627:
                                return 3
                            else:
                                return 0
                        else:
                            if features["E(DOWN) - agent_column"] <= -3.758017:
                                if features["E(UP) - E(RIGHT)"] <= -0.203894:
                                    return 0
                                else:
                                    if features["T(DOWN) - T(T(LEFT))"] <= 0.070970:
                                        if features["T(E(DOWN)) - time_left"] <= -0.124181:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 0
                            else:
                                if features["E(DOWN) - T(RIGHT)"] <= 0.170911:
                                    if features["E(UP) - time_left"] <= 0.254541:
                                        if features["T(LEFT) - agent_column"] <= -2.999835:
                                            if features["E(UP) - E(DOWN)"] <= -0.167731:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 3
                                    else:
                                        return 0
                                else:
                                    return 3
            else:
                if features["E(UP)"] <= 0.010496:
                    if features["E(RIGHT) - T(T(RIGHT))"] <= 0.032250:
                        if features["E(DOWN) - time_left"] <= 0.175839:
                            if features["E(RIGHT)"] <= 0.006145:
                                return 1
                            else:
                                if features["agent_row - time_left"] <= -0.420000:
                                    return 3
                                else:
                                    if features["E(DOWN) - T(DOWN)"] <= -0.118448:
                                        return 1
                                    else:
                                        if features["T(DOWN) - T(RIGHT)"] <= 0.006842:
                                            return 3
                                        else:
                                            if features["T(DOWN) - T(T(up))"] <= 0.304065:
                                                if features["T(LEFT) - T(E(RIGHT))"] <= 0.208380:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                        else:
                            if features["E(RIGHT) - T(RIGHT)"] <= 0.041754:
                                if features["E(LEFT) - T(E(LEFT))"] <= 0.148033:
                                    if features["E(RIGHT) - T(T(LEFT))"] <= 0.185385:
                                        if features["E(LEFT) - T(E(DOWN))"] <= 0.033898:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        if features["T(up) - T(T(LEFT))"] <= -0.095583:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["E(DOWN) - E(LEFT)"] <= 0.225340:
                                        return 1
                                    else:
                                        return 3
                            else:
                                if features["E(RIGHT) - T(E(LEFT))"] <= 0.117598:
                                    if features["T(up) - time_left"] <= -0.049999:
                                        if features["T(LEFT) - agent_column"] <= -9.392274:
                                            return 1
                                        else:
                                            if features["T(E(RIGHT)) - agent_row"] <= -8.996709:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        return 1
                                else:
                                    if features["T(E(LEFT)) - agent_row"] <= 0.010098:
                                        return 1
                                    else:
                                        return 3
                    else:
                        if features["E(DOWN) - agent_row"] <= -11.200427:
                            return 3
                        else:
                            if features["E(RIGHT) - agent_row"] <= -1.336978:
                                if features["T(DOWN) - T(E(LEFT))"] <= 0.463420:
                                    if features["E(UP) - E(DOWN)"] <= -0.800617:
                                        if features["T(T(RIGHT)) - agent_column"] <= -4.775303:
                                            if features["T(E(UP)) - agent_column"] <= -12.551663:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(UP)"] <= 0.000019:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - T(LEFT)"] <= 0.408935:
                                                if features["E(DOWN) - T(up)"] <= 0.431676:
                                                    if features["T(up) - T(E(UP))"] <= -0.073583:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(RIGHT) - T(up)"] <= 0.698767:
                                                        return 1
                                                    else:
                                                        if features["E(DOWN) - agent_column"] <= -11.251000:
                                                            return 1
                                                        else:
                                                            return 3
                                            else:
                                                return 3
                                else:
                                    if features["T(E(DOWN)) - T(E(RIGHT))"] <= 0.011007:
                                        if features["E(UP) - E(RIGHT)"] <= -0.333484:
                                            if features["E(UP)"] <= 0.000003:
                                                if features["E(DOWN) - T(up)"] <= 0.729084:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(LEFT) - T(E(RIGHT))"] <= -0.590600:
                                            return 3
                                        else:
                                            if features["E(UP)"] <= 0.000001:
                                                return 1
                                            else:
                                                if features["T(E(RIGHT)) - time_left"] <= -0.238765:
                                                    return 0
                                                else:
                                                    return 1
                            else:
                                if features["E(LEFT) - time_left"] <= 0.026944:
                                    if features["agent_column - time_left"] <= 12.430000:
                                        if features["E(DOWN) - time_left"] <= 0.259751:
                                            if features["agent_row - time_left"] <= -0.420000:
                                                return 3
                                            else:
                                                if features["E(UP) - E(LEFT)"] <= -0.012179:
                                                    if features["E(RIGHT) - agent_column"] <= -7.619984:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                                        else:
                                            if features["E(RIGHT) - T(T(LEFT))"] <= 0.565413:
                                                if features["T(T(up)) - time_left"] <= -0.006605:
                                                    return 3
                                                else:
                                                    if features["T(up) - agent_row"] <= -0.999776:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                return 3
                                    else:
                                        return 1
                                else:
                                    if features["T(E(RIGHT)) - time_left"] <= 0.302664:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.299069:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        if features["T(E(UP)) - agent_row"] <= -0.981388:
                                            return 1
                                        else:
                                            return 3
                else:
                    if features["E(LEFT) - T(E(RIGHT))"] <= 0.070573:
                        if features["E(UP) - T(LEFT)"] <= 0.064305:
                            if features["E(UP)"] <= 0.101565:
                                if features["E(LEFT) - time_left"] <= 0.138447:
                                    if features["E(RIGHT) - T(T(RIGHT))"] <= -0.035770:
                                        if features["E(UP)"] <= 0.049646:
                                            if features["E(LEFT) - time_left"] <= 0.012045:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 3
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.018916:
                                            if features["T(up)"] <= 0.007094:
                                                if features["E(DOWN) - time_left"] <= 0.356787:
                                                    return 3
                                                else:
                                                    if features["T(RIGHT) - T(T(up))"] <= 0.160668:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                if features["T(up) - T(T(DOWN))"] <= -0.365810:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - T(T(DOWN))"] <= 0.017526:
                                                        return 1
                                                    else:
                                                        if features["E(LEFT)"] <= 0.276140:
                                                            return 3
                                                        else:
                                                            return 2
                                        else:
                                            if features["T(RIGHT) - T(T(up))"] <= 0.306567:
                                                if features["agent_row - time_left"] <= 0.920000:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 1
                                else:
                                    if features["T(E(DOWN)) - T(T(DOWN))"] <= 0.001149:
                                        if features["T(E(UP)) - time_left"] <= 0.030339:
                                            if features["E(LEFT) - T(E(UP))"] <= 0.163655:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["T(up) - T(LEFT)"] <= -0.059695:
                                                return 0
                                            else:
                                                return 3
                                    else:
                                        if features["T(E(DOWN)) - T(T(DOWN))"] <= 0.016113:
                                            return 3
                                        else:
                                            if features["T(E(DOWN)) - agent_row"] <= -5.588451:
                                                if features["T(T(DOWN)) - agent_row"] <= -5.841138:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                            else:
                                if features["T(RIGHT) - time_left"] <= 0.067271:
                                    if features["T(DOWN)"] <= 0.000003:
                                        return 1
                                    else:
                                        if features["T(E(DOWN)) - T(E(LEFT))"] <= 0.027433:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    return 3
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= 0.000037:
                                if features["E(DOWN) - time_left"] <= 0.270020:
                                    if features["T(DOWN) - time_left"] <= 0.274262:
                                        return 3
                                    else:
                                        if features["T(E(RIGHT)) - T(T(RIGHT))"] <= -0.183922:
                                            return 2
                                        else:
                                            return 0
                                else:
                                    if features["E(UP) - T(E(DOWN))"] <= -0.254533:
                                        return 1
                                    else:
                                        return 3
                            else:
                                if features["E(DOWN)"] <= 0.356514:
                                    if features["T(E(LEFT)) - time_left"] <= -0.143411:
                                        return 0
                                    else:
                                        if features["T(T(LEFT)) - agent_column"] <= -4.603525:
                                            if features["T(DOWN) - agent_column"] <= -8.550719:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 3
                                else:
                                    if features["T(DOWN) - agent_column"] <= -5.503407:
                                        return 0
                                    else:
                                        return 3
                    else:
                        if features["E(UP) - T(E(DOWN))"] <= -0.265283:
                            if features["E(DOWN) - time_left"] <= 0.310171:
                                if features["T(E(RIGHT)) - time_left"] <= -0.363590:
                                    return 3
                                else:
                                    if features["T(LEFT) - agent_row"] <= -5.455750:
                                        if features["T(E(UP)) - agent_row"] <= -5.914910:
                                            if features["E(UP)"] <= 0.041781:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - T(DOWN)"] <= -0.210833:
                                                    return 3
                                                else:
                                                    return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(UP) - T(E(DOWN))"] <= -0.367199:
                                            return 1
                                        else:
                                            if features["T(LEFT) - T(T(RIGHT))"] <= 0.113782:
                                                if features["T(DOWN) - T(T(up))"] <= 0.319304:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                if features["T(RIGHT) - T(E(UP))"] <= 0.020474:
                                                    return 1
                                                else:
                                                    return 3
                            else:
                                if features["E(UP) - T(LEFT)"] <= -0.248122:
                                    if features["T(RIGHT) - T(T(up))"] <= -0.109611:
                                        if features["T(up) - T(E(UP))"] <= -0.047291:
                                            if features["T(LEFT) - T(E(DOWN))"] <= 0.005320:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 1
                                    else:
                                        return 1
                                else:
                                    if features["T(LEFT) - T(T(up))"] <= 0.168408:
                                        if features["E(DOWN) - agent_column"] <= -8.562810:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        return 0
                        else:
                            if features["T(E(LEFT)) - T(T(LEFT))"] <= -0.006225:
                                if features["E(DOWN) - time_left"] <= 0.307227:
                                    if features["T(T(up)) - time_left"] <= 0.064671:
                                        if features["E(LEFT) - T(LEFT)"] <= -0.075977:
                                            if features["T(T(RIGHT)) - time_left"] <= -0.687409:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 0
                                    else:
                                        if features["T(T(RIGHT)) - time_left"] <= 0.165028:
                                            if features["E(RIGHT) - T(DOWN)"] <= -0.363487:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - T(up)"] <= 0.014692:
                                                    return 2
                                                else:
                                                    return 3
                                        else:
                                            return 1
                                else:
                                    return 2
                            else:
                                if features["T(DOWN) - T(E(DOWN))"] <= -0.103006:
                                    if features["T(RIGHT) - agent_row"] <= -5.999965:
                                        return 3
                                    else:
                                        return 2
                                else:
                                    if features["E(UP) - T(RIGHT)"] <= 0.077289:
                                        if features["T(E(UP)) - T(T(LEFT))"] <= -0.203833:
                                            return 0
                                        else:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.023398:
                                                return 0
                                            else:
                                                return 2
                                    else:
                                        if features["T(LEFT) - T(E(UP))"] <= 0.431632:
                                            return 0
                                        else:
                                            if features["T(DOWN) - T(LEFT)"] <= -0.000003:
                                                return 3
                                            else:
                                                return 0
        else:
            if features["E(UP) - E(RIGHT)"] <= 0.151992:
                if features["E(UP) - E(DOWN)"] <= 0.007352:
                    if features["E(LEFT) - time_left"] <= 0.319461:
                        if features["E(UP)"] <= 0.066444:
                            if features["E(DOWN) - T(E(RIGHT))"] <= 0.367618:
                                if features["T(T(RIGHT)) - time_left"] <= -0.577523:
                                    return 0
                                else:
                                    if features["T(up)"] <= 0.001233:
                                        if features["T(LEFT) - agent_row"] <= -1.565607:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(DOWN)"] <= 0.344554:
                                            return 2
                                        else:
                                            return 3
                            else:
                                return 1
                        else:
                            if features["T(E(DOWN)) - T(T(DOWN))"] <= -0.005062:
                                if features["T(RIGHT)"] <= 0.000027:
                                    if features["T(E(UP))"] <= 0.216356:
                                        if features["T(E(UP)) - agent_column"] <= -11.985804:
                                            return 0
                                        else:
                                            if features["T(DOWN) - T(LEFT)"] <= 0.000007:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        return 0
                                else:
                                    return 0
                            else:
                                if features["T(DOWN) - agent_row"] <= -5.399482:
                                    if features["E(LEFT) - time_left"] <= 0.315030:
                                        if features["T(E(UP)) - T(E(RIGHT))"] <= 0.111594:
                                            if features["T(T(DOWN)) - agent_row"] <= -5.736546:
                                                if features["E(RIGHT) - T(E(LEFT))"] <= -0.239091:
                                                    return 3
                                                else:
                                                    if features["E(RIGHT) - T(LEFT)"] <= 0.135322:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                return 2
                                        else:
                                            return 0
                                    else:
                                        return 1
                                else:
                                    if features["T(LEFT) - T(T(DOWN))"] <= 0.156241:
                                        if features["E(DOWN) - time_left"] <= 0.270390:
                                            return 0
                                        else:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.282970:
                                                if features["E(LEFT) - T(T(DOWN))"] <= 0.033127:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                    else:
                                        if features["T(E(DOWN)) - T(E(LEFT))"] <= 0.008356:
                                            return 0
                                        else:
                                            if features["E(UP)"] <= 0.149021:
                                                return 1
                                            else:
                                                return 3
                    else:
                        if features["E(UP) - T(E(UP))"] <= -0.008855:
                            if features["T(DOWN) - agent_column"] <= -9.530197:
                                return 2
                            else:
                                return 0
                        else:
                            if features["E(LEFT) - T(T(up))"] <= 0.160025:
                                if features["E(RIGHT) - T(E(RIGHT))"] <= 0.005210:
                                    return 1
                                else:
                                    return 2
                            else:
                                if features["T(up) - T(LEFT)"] <= -0.215046:
                                    if features["T(LEFT) - T(RIGHT)"] <= 0.283732:
                                        return 0
                                    else:
                                        return 1
                                else:
                                    return 2
                else:
                    if features["T(E(UP)) - T(E(RIGHT))"] <= 0.087051:
                        if features["T(RIGHT) - T(T(LEFT))"] <= 0.188354:
                            if features["E(UP) - T(T(up))"] <= 0.025223:
                                if features["T(T(DOWN)) - time_left"] <= 0.152882:
                                    if features["T(T(DOWN)) - time_left"] <= 0.149269:
                                        if features["T(E(UP))"] <= 0.365557:
                                            if features["T(DOWN) - T(E(DOWN))"] <= 0.017668:
                                                if features["T(DOWN) - T(LEFT)"] <= -0.089351:
                                                    if features["E(DOWN) - T(DOWN)"] <= 0.026566:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                            else:
                                                if features["T(E(DOWN)) - T(T(RIGHT))"] <= -0.077475:
                                                    return 0
                                                else:
                                                    if features["T(DOWN) - T(LEFT)"] <= -0.000008:
                                                        return 3
                                                    else:
                                                        return 0
                                        else:
                                            if features["E(DOWN) - T(E(LEFT))"] <= -0.009906:
                                                return 0
                                            else:
                                                return 3
                                    else:
                                        return 0
                                else:
                                    return 3
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.029310:
                                    if features["E(DOWN) - agent_row"] <= -1.999998:
                                        if features["T(DOWN) - T(T(LEFT))"] <= 0.030029:
                                            if features["E(RIGHT) - time_left"] <= 0.201510:
                                                if features["E(UP) - E(RIGHT)"] <= 0.108042:
                                                    if features["E(RIGHT) - T(LEFT)"] <= 0.126450:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    if features["T(E(DOWN)) - T(T(LEFT))"] <= -0.078452:
                                                        if features["T(up) - T(T(LEFT))"] <= 0.021457:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(RIGHT) - time_left"] <= 0.255714:
                                                    if features["T(DOWN) - time_left"] <= -0.118879:
                                                        return 3
                                                    else:
                                                        if features["T(T(RIGHT)) - time_left"] <= 0.247654:
                                                            return 0
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(UP) - E(DOWN)"] <= 0.354867:
                                                        if features["E(UP) - T(up)"] <= -0.003582:
                                                            if features["T(E(UP)) - T(E(RIGHT))"] <= 0.000979:
                                                                return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["E(UP) - E(DOWN)"] <= 0.865475:
                                                            if features["E(DOWN)"] <= 0.000007:
                                                                return 0
                                                            else:
                                                                if features["T(DOWN) - T(T(up))"] <= -0.304268:
                                                                    return 0
                                                                else:
                                                                    if features["E(UP) - T(T(up))"] <= 0.099980:
                                                                        return 3
                                                                    else:
                                                                        return 0
                                                        else:
                                                            return 3
                                        else:
                                            if features["T(DOWN) - T(LEFT)"] <= -0.000112:
                                                if features["E(DOWN)"] <= 0.065063:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                    else:
                                        if features["E(DOWN) - E(RIGHT)"] <= -0.589806:
                                            if features["T(T(LEFT)) - agent_column"] <= -12.455503:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 0
                                else:
                                    if features["T(LEFT) - agent_row"] <= -7.998755:
                                        if features["T(up) - T(RIGHT)"] <= 0.005625:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 3
                        else:
                            if features["T(DOWN) - time_left"] <= -0.109983:
                                if features["E(UP) - time_left"] <= 0.272941:
                                    return 3
                                else:
                                    return 0
                            else:
                                if features["T(LEFT)"] <= 0.097847:
                                    if features["E(LEFT) - agent_row"] <= -1.999998:
                                        if features["T(DOWN) - agent_column"] <= -5.414322:
                                            return 0
                                        else:
                                            if features["E(RIGHT) - T(T(RIGHT))"] <= -0.082329:
                                                if features["E(LEFT) - T(RIGHT)"] <= -0.335841:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= -0.099708:
                                        return 0
                                    else:
                                        return 3
                    else:
                        if features["T(T(RIGHT)) - time_left"] <= -0.099053:
                            if features["E(UP) - T(up)"] <= 0.282772:
                                if features["E(RIGHT) - time_left"] <= 0.116524:
                                    return 3
                                else:
                                    return 0
                            else:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.839377:
                                    return 3
                                else:
                                    return 0
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.212334:
                                if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.105672:
                                    if features["T(up) - T(E(RIGHT))"] <= 0.147461:
                                        if features["T(up) - T(E(DOWN))"] <= 0.240361:
                                            if features["T(LEFT) - agent_column"] <= -10.683790:
                                                if features["T(RIGHT) - T(T(RIGHT))"] <= -0.000346:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                        else:
                                            if features["T(DOWN) - T(T(up))"] <= -0.146352:
                                                return 0
                                            else:
                                                return 3
                                    else:
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.054079:
                                            if features["T(E(DOWN)) - T(E(RIGHT))"] <= -0.128681:
                                                return 3
                                            else:
                                                if features["T(E(RIGHT)) - time_left"] <= -0.169508:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["T(DOWN) - time_left"] <= 0.190227:
                                                if features["E(LEFT) - T(up)"] <= -0.402066:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 3
                                else:
                                    if features["T(T(up)) - T(T(RIGHT))"] <= 0.083923:
                                        if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.105597:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["E(LEFT) - T(up)"] <= 0.057844:
                                            return 3
                                        else:
                                            if features["T(up) - time_left"] <= 0.170695:
                                                return 0
                                            else:
                                                return 2
                            else:
                                if features["E(UP) - T(E(DOWN))"] <= 0.614226:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.025159:
                                        return 0
                                    else:
                                        if features["T(E(DOWN)) - agent_column"] <= -3.934784:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    return 0
            else:
                if features["E(UP) - T(E(LEFT))"] <= 0.010816:
                    if features["E(LEFT) - time_left"] <= 0.320866:
                        if features["T(DOWN) - agent_column"] <= -10.999997:
                            if features["E(LEFT) - time_left"] <= 0.261035:
                                if features["T(LEFT) - agent_row"] <= -4.506936:
                                    return 0
                                else:
                                    return 2
                            else:
                                return 2
                        else:
                            if features["T(up) - T(RIGHT)"] <= 0.281589:
                                return 0
                            else:
                                if features["T(up) - T(E(DOWN))"] <= 0.317670:
                                    if features["T(DOWN)"] <= 0.000001:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    if features["T(T(DOWN)) - agent_row"] <= -4.754781:
                                        return 0
                                    else:
                                        return 2
                    else:
                        if features["T(up) - time_left"] <= -0.004825:
                            return 0
                        else:
                            if features["T(T(up)) - T(T(RIGHT))"] <= 0.258484:
                                if features["E(LEFT) - T(T(LEFT))"] <= -0.005331:
                                    return 1
                                else:
                                    return 2
                            else:
                                return 3
                else:
                    if features["E(UP) - time_left"] <= 0.269894:
                        if features["T(LEFT) - time_left"] <= -0.589144:
                            if features["E(RIGHT) - agent_row"] <= -11.999952:
                                if features["E(LEFT)"] <= 0.285952:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["T(E(UP)) - T(E(RIGHT))"] <= 0.135778:
                                    return 3
                                else:
                                    return 1
                        else:
                            if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.072353:
                                return 0
                            else:
                                if features["T(DOWN) - T(LEFT)"] <= 0.000121:
                                    if features["E(RIGHT)"] <= 0.123740:
                                        if features["T(E(LEFT)) - time_left"] <= -0.684533:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                                else:
                                    return 0
                    else:
                        if features["E(LEFT) - T(T(up))"] <= 0.027371:
                            return 0
                        else:
                            if features["E(RIGHT) - agent_row"] <= -11.814783:
                                if features["E(RIGHT) - T(E(UP))"] <= -0.246749:
                                    if features["T(DOWN) - time_left"] <= -0.029962:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 0
                            else:
                                return 0
    else:
        if features["E(DOWN) - E(LEFT)"] <= 0.000002:
            if features["E(UP) - E(LEFT)"] <= 0.000000:
                if features["E(RIGHT) - T(up)"] <= 0.000391:
                    if features["E(DOWN)"] <= 0.663394:
                        if features["E(UP) - E(DOWN)"] <= 0.809231:
                            if features["E(LEFT) - time_left"] <= 0.132164:
                                if features["E(UP)"] <= 0.015394:
                                    if features["E(UP) - E(LEFT)"] <= -0.548963:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    if features["E(LEFT) - T(RIGHT)"] <= 0.650397:
                                        if features["E(UP) - T(RIGHT)"] <= 0.305015:
                                            if features["T(RIGHT) - T(T(up))"] <= -0.337299:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                                    else:
                                        if features["T(up) - agent_row"] <= -5.969847:
                                            return 0
                                        else:
                                            return 1
                            else:
                                if features["E(LEFT) - agent_column"] <= -13.615106:
                                    if features["E(UP) - T(DOWN)"] <= 0.347413:
                                        if features["E(LEFT) - agent_row"] <= -1.618378:
                                            if features["T(E(LEFT)) - time_left"] <= 0.321113:
                                                if features["E(DOWN) - T(up)"] <= 0.363828:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(RIGHT) - T(T(up))"] <= -0.035913:
                                                return 1
                                            else:
                                                return 2
                                    else:
                                        return 0
                                else:
                                    if features["E(RIGHT) - T(DOWN)"] <= 0.000144:
                                        if features["E(RIGHT)"] <= 0.067381:
                                            if features["E(UP) - E(RIGHT)"] <= 0.664182:
                                                if features["T(DOWN) - T(LEFT)"] <= -0.404141:
                                                    if features["E(RIGHT)"] <= 0.000550:
                                                        return 2
                                                    else:
                                                        if features["T(E(RIGHT)) - T(T(up))"] <= -0.236112:
                                                            return 0
                                                        else:
                                                            return 2
                                                else:
                                                    if features["E(LEFT) - T(E(DOWN))"] <= 0.087044:
                                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.001267:
                                                            if features["T(E(DOWN)) - agent_column"] <= -13.684914:
                                                                return 1
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["T(DOWN) - time_left"] <= 0.313712:
                                                                if features["E(RIGHT) - T(E(RIGHT))"] <= -0.114890:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                            else:
                                                                return 0
                                                    else:
                                                        if features["E(DOWN) - E(RIGHT)"] <= -0.003745:
                                                            return 0
                                                        else:
                                                            return 2
                                            else:
                                                if features["E(RIGHT)"] <= 0.000007:
                                                    if features["T(E(DOWN)) - agent_column"] <= -13.759989:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    if features["T(E(UP)) - T(E(LEFT))"] <= 0.077065:
                                                        if features["T(up) - agent_column"] <= -9.999813:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["T(T(LEFT)) - agent_column"] <= -2.852184:
                                                            if features["E(DOWN) - agent_column"] <= -9.999687:
                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            return 0
                                        else:
                                            if features["E(LEFT) - T(E(DOWN))"] <= 0.248471:
                                                return 0
                                            else:
                                                if features["T(E(LEFT)) - time_left"] <= 0.211493:
                                                    return 3
                                                else:
                                                    return 2
                                    else:
                                        if features["T(E(DOWN)) - time_left"] <= -0.030686:
                                            if features["E(RIGHT) - T(DOWN)"] <= 0.023703:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(E(LEFT)) - time_left"] <= 0.266427:
                                                if features["E(UP) - time_left"] <= 0.181993:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 2
                        else:
                            if features["E(RIGHT) - agent_column"] <= -11.999998:
                                return 0
                            else:
                                return 2
                    else:
                        if features["E(UP) - E(LEFT)"] <= -0.800238:
                            if features["T(up) - T(LEFT)"] <= -0.006215:
                                if features["E(UP) - E(RIGHT)"] <= -0.000012:
                                    return 2
                                else:
                                    if features["T(LEFT) - agent_column"] <= -8.697640:
                                        if features["T(E(DOWN)) - agent_row"] <= -11.455562:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["T(E(LEFT)) - agent_row"] <= -4.598880:
                                            return 1
                                        else:
                                            return 2
                            else:
                                if features["E(DOWN) - agent_row"] <= -0.132271:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["E(RIGHT)"] <= 0.000007:
                                if features["E(LEFT) - time_left"] <= 0.257767:
                                    return 1
                                else:
                                    return 2
                            else:
                                if features["T(up) - agent_row"] <= -9.999844:
                                    return 2
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -4.587491:
                                        return 1
                                    else:
                                        if features["T(E(DOWN)) - agent_column"] <= -1.645171:
                                            return 2
                                        else:
                                            return 1
                else:
                    if features["E(DOWN) - time_left"] <= 0.212129:
                        if features["E(RIGHT) - T(up)"] <= 0.026897:
                            if features["E(DOWN) - E(LEFT)"] <= -0.148689:
                                return 2
                            else:
                                if features["T(T(DOWN)) - agent_column"] <= -3.911979:
                                    if features["E(UP) - T(RIGHT)"] <= 0.011101:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 1
                        else:
                            if features["E(DOWN) - T(E(UP))"] <= 0.152496:
                                if features["agent_row - agent_column"] <= -3.500000:
                                    if features["E(DOWN) - T(E(RIGHT))"] <= 0.026590:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 0
                            else:
                                if features["T(LEFT) - agent_column"] <= -4.999664:
                                    if features["agent_row - time_left"] <= 3.720000:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 3
                    else:
                        if features["E(DOWN) - time_left"] <= 0.292929:
                            return 2
                        else:
                            if features["E(RIGHT) - T(E(LEFT))"] <= -0.323815:
                                return 2
                            else:
                                return 1
            else:
                if features["E(UP)"] <= 0.865541:
                    if features["E(DOWN)"] <= 0.000035:
                        if features["T(DOWN) - T(T(up))"] <= -0.360121:
                            if features["T(RIGHT) - time_left"] <= -0.789908:
                                if features["E(UP) - T(LEFT)"] <= 0.019738:
                                    return 1
                                else:
                                    return 0
                            else:
                                if features["E(DOWN) - T(T(DOWN))"] <= -0.009555:
                                    return 0
                                else:
                                    return 2
                        else:
                            if features["E(DOWN) - agent_row"] <= -1.999967:
                                if features["T(up) - T(E(RIGHT))"] <= 0.358116:
                                    if features["T(E(RIGHT)) - time_left"] <= -0.907118:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 0
                            else:
                                return 2
                    else:
                        if features["E(RIGHT)"] <= 0.026954:
                            if features["E(RIGHT) - agent_column"] <= -11.991783:
                                return 0
                            else:
                                if features["T(E(DOWN)) - time_left"] <= -0.681314:
                                    return 1
                                else:
                                    if features["T(DOWN) - agent_row"] <= -1.705045:
                                        if features["T(E(RIGHT)) - agent_column"] <= -1.877953:
                                            if features["E(LEFT) - agent_column"] <= -4.390965:
                                                if features["E(LEFT) - agent_column"] <= -10.519958:
                                                    return 2
                                                else:
                                                    if features["T(T(DOWN)) - agent_column"] <= -9.812962:
                                                        return 0
                                                    else:
                                                        if features["T(LEFT) - agent_column"] <= -7.349773:
                                                            return 2
                                                        else:
                                                            return 0
                                            else:
                                                return 2
                                        else:
                                            return 0
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -5.999940:
                                            if features["E(UP) - E(DOWN)"] <= 0.773002:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                        else:
                            if features["E(UP)"] <= 0.387420:
                                return 2
                            else:
                                if features["T(up) - agent_column"] <= -11.999959:
                                    return 2
                                else:
                                    return 0
                else:
                    if features["T(RIGHT) - agent_column"] <= -7.999974:
                        if features["T(LEFT) - time_left"] <= 0.301862:
                            if features["E(DOWN) - E(RIGHT)"] <= -0.000121:
                                return 2
                            else:
                                if features["E(UP) - agent_row"] <= -1.132766:
                                    if features["E(RIGHT) - agent_row"] <= -2.999968:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(E(LEFT)) - agent_row"] <= -0.708482:
                                        return 0
                                    else:
                                        return 2
                        else:
                            return 0
                    else:
                        if features["E(DOWN) - agent_column"] <= -5.999999:
                            if features["T(DOWN) - T(RIGHT)"] <= 0.670400:
                                return 2
                            else:
                                return 0
                        else:
                            if features["T(up) - agent_column"] <= -3.675005:
                                if features["T(RIGHT) - agent_row"] <= -9.999078:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["T(DOWN) - agent_column"] <= -1.876744:
                                    return 2
                                else:
                                    if features["T(E(DOWN)) - time_left"] <= 0.096013:
                                        return 2
                                    else:
                                        return 0
        else:
            if features["E(DOWN)"] <= 0.729487:
                if features["E(UP)"] <= 0.000019:
                    if features["E(UP) - T(up)"] <= -0.000004:
                        return 1
                    else:
                        if features["T(E(DOWN)) - agent_row"] <= 0.349992:
                            if features["agent_row - agent_column"] <= 4.500000:
                                return 1
                            else:
                                return 2
                        else:
                            if features["E(DOWN) - T(T(DOWN))"] <= 0.075606:
                                return 1
                            else:
                                return 2
                else:
                    if features["E(RIGHT) - agent_row"] <= -1.989844:
                        if features["E(LEFT) - time_left"] <= 0.179668:
                            if features["E(UP) - T(DOWN)"] <= 0.003720:
                                if features["T(DOWN) - T(RIGHT)"] <= 0.326172:
                                    return 1
                                else:
                                    if features["T(DOWN) - agent_row"] <= -6.458469:
                                        return 2
                                    else:
                                        if features["T(E(DOWN)) - time_left"] <= -0.224312:
                                            if features["T(LEFT) - T(E(LEFT))"] <= 0.208961:
                                                return 0
                                            else:
                                                return 1
                                        else:
                                            return 1
                            else:
                                return 3
                        else:
                            if features["T(DOWN)"] <= 0.367514:
                                if features["T(LEFT) - agent_row"] <= -9.999999:
                                    return 2
                                else:
                                    return 1
                            else:
                                if features["T(E(DOWN)) - T(E(LEFT))"] <= 0.028060:
                                    return 2
                                else:
                                    return 1
                    else:
                        if features["T(LEFT) - agent_column"] <= -12.393507:
                            return 1
                        else:
                            if features["E(RIGHT) - T(DOWN)"] <= -0.366936:
                                if features["E(RIGHT)"] <= 0.000499:
                                    return 2
                                else:
                                    return 1
                            else:
                                if features["E(RIGHT) - agent_column"] <= -11.988045:
                                    return 2
                                else:
                                    return 1
            else:
                if features["E(DOWN) - agent_column"] <= -9.131965:
                    if features["T(LEFT) - agent_row"] <= -10.992695:
                        if features["E(UP) - agent_column"] <= -13.000000:
                            return 1
                        else:
                            return 2
                    else:
                        return 1
                else:
                    if features["E(DOWN)"] <= 0.867661:
                        if features["E(DOWN) - agent_row"] <= -10.224233:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.796594:
                                return 2
                            else:
                                return 1
                        else:
                            if features["E(UP) - T(up)"] <= -0.000001:
                                if features["E(DOWN)"] <= 0.867320:
                                    return 1
                                else:
                                    return 2
                            else:
                                if features["T(E(UP)) - agent_column"] <= -1.969785:
                                    if features["T(T(up)) - T(T(RIGHT))"] <= -0.151722:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 1
                    else:
                        if features["T(RIGHT) - agent_row"] <= -4.653781:
                            if features["T(LEFT) - agent_row"] <= -10.699068:
                                return 2
                            else:
                                return 1
                        else:
                            if features["E(RIGHT) - agent_column"] <= -0.999965:
                                if features["agent_row - time_left"] <= 1.540000:
                                    if features["E(UP) - agent_row"] <= -0.999999:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    return 2
                            else:
                                return 1


def interpretable_action(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability,agent_position, time_left, gamma, size, valid_actions):
    input_representation = symbolic_representation(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability, agent_position, time_left, gamma, size)
    input_combinations   = get_feature_vector(input_representation)
    symbole_to_value     = {name: input_combinations[i] for i, name in enumerate(symbole_names)}
    action               = Index_to_Action[interpretable_strategy(symbole_to_value)]
    if action in valid_actions:
        return action
    else:
        return random.choice(valid_actions)
