import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbol_names = ['Evader(UP)', 'Evader(DOWN)', 'Evader(LEFT)', 'Evader(RIGHT)', 'Teammate(UP)', 'Teammate(DOWN)', 'Teammate(LEFT)', 'Teammate(RIGHT)', 'Teammate(Evader(UP))', 'Teammate(Evader(DOWN))', 'Teammate(Evader(LEFT))', 'Teammate(Evader(RIGHT))', 'Teammate(Teammate(UP))', 'Teammate(Teammate(DOWN))', 'Teammate(Teammate(LEFT))', 'Teammate(Teammate(RIGHT))', 'Agent_Row', 'Agent_Column', 'Time_Left', 'Evader(UP) - Evader(DOWN)', 'Evader(UP) - Evader(LEFT)', 'Evader(UP) - Evader(RIGHT)', 'Evader(UP) - Teammate(UP)', 'Evader(UP) - Teammate(DOWN)', 'Evader(UP) - Teammate(LEFT)', 'Evader(UP) - Teammate(RIGHT)', 'Evader(UP) - Teammate(Evader(UP))', 'Evader(UP) - Teammate(Evader(DOWN))', 'Evader(UP) - Teammate(Evader(LEFT))', 'Evader(UP) - Teammate(Evader(RIGHT))', 'Evader(UP) - Teammate(Teammate(UP))', 'Evader(UP) - Teammate(Teammate(DOWN))', 'Evader(UP) - Teammate(Teammate(LEFT))', 'Evader(UP) - Teammate(Teammate(RIGHT))', 'Evader(UP) - Agent_Row', 'Evader(UP) - Agent_Column', 'Evader(UP) - Time_Left', 'Evader(DOWN) - Evader(LEFT)', 'Evader(DOWN) - Evader(RIGHT)', 'Evader(DOWN) - Teammate(UP)', 'Evader(DOWN) - Teammate(DOWN)', 'Evader(DOWN) - Teammate(LEFT)', 'Evader(DOWN) - Teammate(RIGHT)', 'Evader(DOWN) - Teammate(Evader(UP))', 'Evader(DOWN) - Teammate(Evader(DOWN))', 'Evader(DOWN) - Teammate(Evader(LEFT))', 'Evader(DOWN) - Teammate(Evader(RIGHT))', 'Evader(DOWN) - Teammate(Teammate(UP))', 'Evader(DOWN) - Teammate(Teammate(DOWN))', 'Evader(DOWN) - Teammate(Teammate(LEFT))', 'Evader(DOWN) - Teammate(Teammate(RIGHT))', 'Evader(DOWN) - Agent_Row', 'Evader(DOWN) - Agent_Column', 'Evader(DOWN) - Time_Left', 'Evader(LEFT) - Evader(RIGHT)', 'Evader(LEFT) - Teammate(UP)', 'Evader(LEFT) - Teammate(DOWN)', 'Evader(LEFT) - Teammate(LEFT)', 'Evader(LEFT) - Teammate(RIGHT)', 'Evader(LEFT) - Teammate(Evader(UP))', 'Evader(LEFT) - Teammate(Evader(DOWN))', 'Evader(LEFT) - Teammate(Evader(LEFT))', 'Evader(LEFT) - Teammate(Evader(RIGHT))', 'Evader(LEFT) - Teammate(Teammate(UP))', 'Evader(LEFT) - Teammate(Teammate(DOWN))', 'Evader(LEFT) - Teammate(Teammate(LEFT))', 'Evader(LEFT) - Teammate(Teammate(RIGHT))', 'Evader(LEFT) - Agent_Row', 'Evader(LEFT) - Agent_Column', 'Evader(LEFT) - Time_Left', 'Evader(RIGHT) - Teammate(UP)', 'Evader(RIGHT) - Teammate(DOWN)', 'Evader(RIGHT) - Teammate(LEFT)', 'Evader(RIGHT) - Teammate(RIGHT)', 'Evader(RIGHT) - Teammate(Evader(UP))', 'Evader(RIGHT) - Teammate(Evader(DOWN))', 'Evader(RIGHT) - Teammate(Evader(LEFT))', 'Evader(RIGHT) - Teammate(Evader(RIGHT))', 'Evader(RIGHT) - Teammate(Teammate(UP))', 'Evader(RIGHT) - Teammate(Teammate(DOWN))', 'Evader(RIGHT) - Teammate(Teammate(LEFT))', 'Evader(RIGHT) - Teammate(Teammate(RIGHT))', 'Evader(RIGHT) - Agent_Row', 'Evader(RIGHT) - Agent_Column', 'Evader(RIGHT) - Time_Left', 'Teammate(UP) - Teammate(DOWN)', 'Teammate(UP) - Teammate(LEFT)', 'Teammate(UP) - Teammate(RIGHT)', 'Teammate(UP) - Teammate(Evader(UP))', 'Teammate(UP) - Teammate(Evader(DOWN))', 'Teammate(UP) - Teammate(Evader(LEFT))', 'Teammate(UP) - Teammate(Evader(RIGHT))', 'Teammate(UP) - Teammate(Teammate(UP))', 'Teammate(UP) - Teammate(Teammate(DOWN))', 'Teammate(UP) - Teammate(Teammate(LEFT))', 'Teammate(UP) - Teammate(Teammate(RIGHT))', 'Teammate(UP) - Agent_Row', 'Teammate(UP) - Agent_Column', 'Teammate(UP) - Time_Left', 'Teammate(DOWN) - Teammate(LEFT)', 'Teammate(DOWN) - Teammate(RIGHT)', 'Teammate(DOWN) - Teammate(Evader(UP))', 'Teammate(DOWN) - Teammate(Evader(DOWN))', 'Teammate(DOWN) - Teammate(Evader(LEFT))', 'Teammate(DOWN) - Teammate(Evader(RIGHT))', 'Teammate(DOWN) - Teammate(Teammate(UP))', 'Teammate(DOWN) - Teammate(Teammate(DOWN))', 'Teammate(DOWN) - Teammate(Teammate(LEFT))', 'Teammate(DOWN) - Teammate(Teammate(RIGHT))', 'Teammate(DOWN) - Agent_Row', 'Teammate(DOWN) - Agent_Column', 'Teammate(DOWN) - Time_Left', 'Teammate(LEFT) - Teammate(RIGHT)', 'Teammate(LEFT) - Teammate(Evader(UP))', 'Teammate(LEFT) - Teammate(Evader(DOWN))', 'Teammate(LEFT) - Teammate(Evader(LEFT))', 'Teammate(LEFT) - Teammate(Evader(RIGHT))', 'Teammate(LEFT) - Teammate(Teammate(UP))', 'Teammate(LEFT) - Teammate(Teammate(DOWN))', 'Teammate(LEFT) - Teammate(Teammate(LEFT))', 'Teammate(LEFT) - Teammate(Teammate(RIGHT))', 'Teammate(LEFT) - Agent_Row', 'Teammate(LEFT) - Agent_Column', 'Teammate(LEFT) - Time_Left', 'Teammate(RIGHT) - Teammate(Evader(UP))', 'Teammate(RIGHT) - Teammate(Evader(DOWN))', 'Teammate(RIGHT) - Teammate(Evader(LEFT))', 'Teammate(RIGHT) - Teammate(Evader(RIGHT))', 'Teammate(RIGHT) - Teammate(Teammate(UP))', 'Teammate(RIGHT) - Teammate(Teammate(DOWN))', 'Teammate(RIGHT) - Teammate(Teammate(LEFT))', 'Teammate(RIGHT) - Teammate(Teammate(RIGHT))', 'Teammate(RIGHT) - Agent_Row', 'Teammate(RIGHT) - Agent_Column', 'Teammate(RIGHT) - Time_Left', 'Teammate(Evader(UP)) - Teammate(Evader(DOWN))', 'Teammate(Evader(UP)) - Teammate(Evader(LEFT))', 'Teammate(Evader(UP)) - Teammate(Evader(RIGHT))', 'Teammate(Evader(UP)) - Teammate(Teammate(UP))', 'Teammate(Evader(UP)) - Teammate(Teammate(DOWN))', 'Teammate(Evader(UP)) - Teammate(Teammate(LEFT))', 'Teammate(Evader(UP)) - Teammate(Teammate(RIGHT))', 'Teammate(Evader(UP)) - Agent_Row', 'Teammate(Evader(UP)) - Agent_Column', 'Teammate(Evader(UP)) - Time_Left', 'Teammate(Evader(DOWN)) - Teammate(Evader(LEFT))', 'Teammate(Evader(DOWN)) - Teammate(Evader(RIGHT))', 'Teammate(Evader(DOWN)) - Teammate(Teammate(UP))', 'Teammate(Evader(DOWN)) - Teammate(Teammate(DOWN))', 'Teammate(Evader(DOWN)) - Teammate(Teammate(LEFT))', 'Teammate(Evader(DOWN)) - Teammate(Teammate(RIGHT))', 'Teammate(Evader(DOWN)) - Agent_Row', 'Teammate(Evader(DOWN)) - Agent_Column', 'Teammate(Evader(DOWN)) - Time_Left', 'Teammate(Evader(LEFT)) - Teammate(Evader(RIGHT))', 'Teammate(Evader(LEFT)) - Teammate(Teammate(UP))', 'Teammate(Evader(LEFT)) - Teammate(Teammate(DOWN))', 'Teammate(Evader(LEFT)) - Teammate(Teammate(LEFT))', 'Teammate(Evader(LEFT)) - Teammate(Teammate(RIGHT))', 'Teammate(Evader(LEFT)) - Agent_Row', 'Teammate(Evader(LEFT)) - Agent_Column', 'Teammate(Evader(LEFT)) - Time_Left', 'Teammate(Evader(RIGHT)) - Teammate(Teammate(UP))', 'Teammate(Evader(RIGHT)) - Teammate(Teammate(DOWN))', 'Teammate(Evader(RIGHT)) - Teammate(Teammate(LEFT))', 'Teammate(Evader(RIGHT)) - Teammate(Teammate(RIGHT))', 'Teammate(Evader(RIGHT)) - Agent_Row', 'Teammate(Evader(RIGHT)) - Agent_Column', 'Teammate(Evader(RIGHT)) - Time_Left', 'Teammate(Teammate(UP)) - Teammate(Teammate(DOWN))', 'Teammate(Teammate(UP)) - Teammate(Teammate(LEFT))', 'Teammate(Teammate(UP)) - Teammate(Teammate(RIGHT))', 'Teammate(Teammate(UP)) - Agent_Row', 'Teammate(Teammate(UP)) - Agent_Column', 'Teammate(Teammate(UP)) - Time_Left', 'Teammate(Teammate(DOWN)) - Teammate(Teammate(LEFT))', 'Teammate(Teammate(DOWN)) - Teammate(Teammate(RIGHT))', 'Teammate(Teammate(DOWN)) - Agent_Row', 'Teammate(Teammate(DOWN)) - Agent_Column', 'Teammate(Teammate(DOWN)) - Time_Left', 'Teammate(Teammate(LEFT)) - Teammate(Teammate(RIGHT))', 'Teammate(Teammate(LEFT)) - Agent_Row', 'Teammate(Teammate(LEFT)) - Agent_Column', 'Teammate(Teammate(LEFT)) - Time_Left', 'Teammate(Teammate(RIGHT)) - Agent_Row', 'Teammate(Teammate(RIGHT)) - Agent_Column', 'Teammate(Teammate(RIGHT)) - Time_Left', 'Agent_Row - Agent_Column', 'Agent_Row - Time_Left', 'Agent_Column - Time_Left']


def interpretable_strategy(features):
    if features["Evader(LEFT) - Evader(RIGHT)"] <= 0.328143:
        if features["Evader(UP) - Evader(RIGHT)"] <= 0.000003:
            if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.000020:
                if features["Evader(UP) - Teammate(Teammate(UP))"] <= 0.031269:
                    if features["Evader(UP) - Evader(DOWN)"] <= -0.799738:
                        if features["Teammate(DOWN) - Agent_Column"] <= -12.411637:
                            return 1 # WALK DOWN
                        else:
                            if features["Teammate(Evader(DOWN)) - Agent_Column"] <= -5.690614:
                                return 3 # WALK RIGHT
                            else:
                                if features["Teammate(DOWN) - Teammate(Evader(DOWN))"] <= -0.017480:
                                    return 1 # WALK DOWN
                                else:
                                    return 3 # WALK RIGHT
                    else:
                        if features["Evader(UP) - Teammate(Teammate(DOWN))"] <= 0.083381:
                            if features["Evader(LEFT) - Teammate(UP)"] <= 0.059033:
                                if features["Evader(DOWN) - Teammate(Evader(UP))"] <= 0.251270:
                                    if features["Evader(LEFT) - Teammate(Teammate(LEFT))"] <= 0.013462:
                                        if features["Evader(RIGHT)"] <= 0.273870:
                                            if features["Evader(UP) - Agent_Row"] <= -10.999970:
                                                return 0 # WALK UP
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            return 3 # WALK RIGHT
                                    else:
                                        if features["Evader(DOWN) - Teammate(Evader(UP))"] <= -0.058373:
                                            return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                else:
                                    if features["Evader(LEFT)"] <= 0.000026:
                                        if features["Teammate(DOWN) - Agent_Column"] <= -12.181350:
                                            return 1 # WALK DOWN
                                        else:
                                            return 3 # WALK RIGHT
                                    else:
                                        if features["Teammate(UP) - Agent_Column"] <= -0.982358:
                                            if features["Evader(RIGHT) - Agent_Column"] <= -11.244479:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(Teammate(UP)) - Teammate(Teammate(RIGHT))"] <= -0.182016:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                            else:
                                if features["Teammate(LEFT) - Teammate(Evader(LEFT))"] <= 0.254472:
                                    if features["Teammate(UP) - Agent_Column"] <= -4.999999:
                                        if features["Teammate(UP)"] <= 0.000006:
                                            return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                    else:
                                        if features["Teammate(DOWN) - Teammate(Evader(DOWN))"] <= 0.115377:
                                            return 1 # WALK DOWN
                                        else:
                                            if features["Evader(UP) - Teammate(LEFT)"] <= 0.231066:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                else:
                                    return 3 # WALK RIGHT
                        else:
                            if features["Evader(RIGHT) - Teammate(Teammate(RIGHT))"] <= 0.019928:
                                if features["Teammate(LEFT) - Teammate(Evader(LEFT))"] <= -0.010791:
                                    if features["Evader(RIGHT) - Teammate(RIGHT)"] <= -0.012734:
                                        if features["Evader(LEFT) - Time_Left"] <= 0.045267:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                                else:
                                    if features["Teammate(Evader(RIGHT)) - Teammate(Teammate(RIGHT))"] <= -0.005659:
                                        return 3 # WALK RIGHT
                                    else:
                                        if features["Evader(UP) - Teammate(Evader(UP))"] <= 0.026159:
                                            return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                            else:
                                if features["Evader(DOWN) - Teammate(RIGHT)"] <= -0.351490:
                                    if features["Evader(LEFT) - Evader(RIGHT)"] <= -0.376129:
                                        return 3 # WALK RIGHT
                                    else:
                                        if features["Teammate(UP) - Teammate(RIGHT)"] <= 0.000017:
                                            if features["Teammate(RIGHT) - Agent_Row"] <= -5.200413:
                                                return 0 # WALK UP
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            return 3 # WALK RIGHT
                                else:
                                    if features["Evader(RIGHT) - Time_Left"] <= 0.301544:
                                        if features["Evader(UP) - Teammate(Evader(DOWN))"] <= 0.191038:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        if features["Evader(LEFT) - Teammate(Evader(LEFT))"] <= -0.365698:
                                            return 1 # WALK DOWN
                                        else:
                                            return 3 # WALK RIGHT
                else:
                    if features["Evader(LEFT) - Teammate(UP)"] <= 0.066862:
                        if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.800900:
                            if features["Evader(DOWN) - Evader(LEFT)"] <= 0.000022:
                                if features["Teammate(Teammate(DOWN)) - Agent_Column"] <= -0.915752:
                                    if features["Teammate(UP) - Teammate(RIGHT)"] <= -0.580698:
                                        return 0 # WALK UP
                                    else:
                                        if features["Evader(RIGHT) - Agent_Column"] <= -1.132048:
                                            if features["Teammate(Teammate(RIGHT)) - Time_Left"] <= 0.109064:
                                                if features["Teammate(LEFT) - Agent_Column"] <= -12.533249:
                                                    if features["Teammate(RIGHT) - Agent_Row"] <= -6.000000:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        return 0 # WALK UP
                                                else:
                                                    return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                else:
                                    return 0 # WALK UP
                            else:
                                return 0 # WALK UP
                        else:
                            if features["Agent_Row - Agent_Column"] <= 7.500000:
                                if features["Evader(LEFT)"] <= 0.000016:
                                    if features["Evader(UP) - Agent_Column"] <= 0.543749:
                                        if features["Evader(UP) - Agent_Column"] <= -11.236829:
                                            return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                    else:
                                        return 0 # WALK UP
                                else:
                                    if features["Evader(DOWN) - Teammate(Evader(LEFT))"] <= 0.008928:
                                        if features["Teammate(Evader(RIGHT)) - Teammate(Teammate(RIGHT))"] <= 0.039175:
                                            return 0 # WALK UP
                                        else:
                                            if features["Evader(LEFT) - Teammate(UP)"] <= 0.030694:
                                                if features["Evader(RIGHT) - Agent_Column"] <= -11.233420:
                                                    return 0 # WALK UP
                                                else:
                                                    if features["Teammate(RIGHT) - Time_Left"] <= 0.590814:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        return 0 # WALK UP
                                            else:
                                                return 0 # WALK UP
                                    else:
                                        if features["Teammate(UP) - Time_Left"] <= -0.129995:
                                            if features["Evader(LEFT) - Teammate(UP)"] <= 0.033838:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            if features["Teammate(RIGHT) - Agent_Row"] <= -2.996630:
                                                if features["Evader(RIGHT) - Teammate(Evader(UP))"] <= 0.042217:
                                                    if features["Agent_Row - Agent_Column"] <= 1.500000:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        if features["Evader(LEFT) - Teammate(LEFT)"] <= 0.019339:
                                                            return 3 # WALK RIGHT
                                                        else:
                                                            return 0 # WALK UP
                                                else:
                                                    return 3 # WALK RIGHT
                                            else:
                                                return 3 # WALK RIGHT
                            else:
                                if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.006961:
                                    if features["Teammate(Evader(RIGHT)) - Teammate(Teammate(UP))"] <= 0.022351:
                                        return 3 # WALK RIGHT
                                    else:
                                        if features["Evader(RIGHT) - Teammate(Evader(LEFT))"] <= 0.400094:
                                            if features["Evader(UP)"] <= 0.338207:
                                                return 0 # WALK UP
                                            else:
                                                if features["Evader(LEFT) - Agent_Column"] <= -1.998666:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                else:
                                    if features["Evader(RIGHT) - Teammate(Evader(UP))"] <= 0.065591:
                                        if features["Teammate(Evader(UP)) - Agent_Row"] <= -10.644170:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        if features["Agent_Column - Time_Left"] <= -0.060000:
                                            return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                    else:
                        if features["Teammate(DOWN) - Teammate(LEFT)"] <= 0.000045:
                            if features["Teammate(Evader(UP)) - Teammate(Evader(RIGHT))"] <= 0.077627:
                                return 3 # WALK RIGHT
                            else:
                                return 0 # WALK UP
                        else:
                            if features["Evader(DOWN) - Agent_Column"] <= -3.758017:
                                if features["Evader(UP) - Evader(RIGHT)"] <= -0.203894:
                                    return 0 # WALK UP
                                else:
                                    if features["Teammate(DOWN) - Teammate(Teammate(LEFT))"] <= 0.070970:
                                        if features["Teammate(Evader(DOWN)) - Time_Left"] <= -0.124181:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 0 # WALK UP
                            else:
                                if features["Evader(DOWN) - Teammate(RIGHT)"] <= 0.170911:
                                    if features["Evader(UP) - Time_Left"] <= 0.254541:
                                        if features["Teammate(LEFT) - Agent_Column"] <= -2.999835:
                                            if features["Evader(UP) - Evader(DOWN)"] <= -0.167731:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                    else:
                                        return 0 # WALK UP
                                else:
                                    return 3 # WALK RIGHT
            else:
                if features["Evader(UP)"] <= 0.010496:
                    if features["Evader(RIGHT) - Teammate(Teammate(RIGHT))"] <= 0.032250:
                        if features["Evader(DOWN) - Time_Left"] <= 0.175839:
                            if features["Evader(RIGHT)"] <= 0.006145:
                                return 1 # WALK DOWN
                            else:
                                if features["Agent_Row - Time_Left"] <= -0.420000:
                                    return 3 # WALK RIGHT
                                else:
                                    if features["Evader(DOWN) - Teammate(DOWN)"] <= -0.118448:
                                        return 1 # WALK DOWN
                                    else:
                                        if features["Teammate(DOWN) - Teammate(RIGHT)"] <= 0.006842:
                                            return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(DOWN) - Teammate(Teammate(UP))"] <= 0.304065:
                                                if features["Teammate(LEFT) - Teammate(Evader(RIGHT))"] <= 0.208380:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 2 # WALK LEFT
                                            else:
                                                return 1 # WALK DOWN
                        else:
                            if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.041754:
                                if features["Evader(LEFT) - Teammate(Evader(LEFT))"] <= 0.148033:
                                    if features["Evader(RIGHT) - Teammate(Teammate(LEFT))"] <= 0.185385:
                                        if features["Evader(LEFT) - Teammate(Evader(DOWN))"] <= 0.033898:
                                            return 1 # WALK DOWN
                                        else:
                                            return 3 # WALK RIGHT
                                    else:
                                        if features["Teammate(UP) - Teammate(Teammate(LEFT))"] <= -0.095583:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 1 # WALK DOWN
                                else:
                                    if features["Evader(DOWN) - Evader(LEFT)"] <= 0.225340:
                                        return 1 # WALK DOWN
                                    else:
                                        return 3 # WALK RIGHT
                            else:
                                if features["Evader(RIGHT) - Teammate(Evader(LEFT))"] <= 0.117598:
                                    if features["Teammate(UP) - Time_Left"] <= -0.049999:
                                        if features["Teammate(LEFT) - Agent_Column"] <= -9.392274:
                                            return 1 # WALK DOWN
                                        else:
                                            if features["Teammate(Evader(RIGHT)) - Agent_Row"] <= -8.996709:
                                                return 2 # WALK LEFT
                                            else:
                                                return 1 # WALK DOWN
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    if features["Teammate(Evader(LEFT)) - Agent_Row"] <= 0.010098:
                                        return 1 # WALK DOWN
                                    else:
                                        return 3 # WALK RIGHT
                    else:
                        if features["Evader(DOWN) - Agent_Row"] <= -11.200427:
                            return 3 # WALK RIGHT
                        else:
                            if features["Evader(RIGHT) - Agent_Row"] <= -1.336978:
                                if features["Teammate(DOWN) - Teammate(Evader(LEFT))"] <= 0.463420:
                                    if features["Evader(UP) - Evader(DOWN)"] <= -0.800617:
                                        if features["Teammate(Teammate(RIGHT)) - Agent_Column"] <= -4.775303:
                                            if features["Teammate(Evader(UP)) - Agent_Column"] <= -12.551663:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        if features["Evader(UP)"] <= 0.000019:
                                            return 1 # WALK DOWN
                                        else:
                                            if features["Evader(RIGHT) - Teammate(LEFT)"] <= 0.408935:
                                                if features["Evader(DOWN) - Teammate(UP)"] <= 0.431676:
                                                    if features["Teammate(UP) - Teammate(Evader(UP))"] <= -0.073583:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        return 1 # WALK DOWN
                                                else:
                                                    if features["Evader(RIGHT) - Teammate(UP)"] <= 0.698767:
                                                        return 1 # WALK DOWN
                                                    else:
                                                        if features["Evader(DOWN) - Agent_Column"] <= -11.251000:
                                                            return 1 # WALK DOWN
                                                        else:
                                                            return 3 # WALK RIGHT
                                            else:
                                                return 3 # WALK RIGHT
                                else:
                                    if features["Teammate(Evader(DOWN)) - Teammate(Evader(RIGHT))"] <= 0.011007:
                                        if features["Evader(UP) - Evader(RIGHT)"] <= -0.333484:
                                            if features["Evader(UP)"] <= 0.000003:
                                                if features["Evader(DOWN) - Teammate(UP)"] <= 0.729084:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 3 # WALK RIGHT
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        if features["Evader(LEFT) - Teammate(Evader(RIGHT))"] <= -0.590600:
                                            return 3 # WALK RIGHT
                                        else:
                                            if features["Evader(UP)"] <= 0.000001:
                                                return 1 # WALK DOWN
                                            else:
                                                if features["Teammate(Evader(RIGHT)) - Time_Left"] <= -0.238765:
                                                    return 0 # WALK UP
                                                else:
                                                    return 1 # WALK DOWN
                            else:
                                if features["Evader(LEFT) - Time_Left"] <= 0.026944:
                                    if features["Agent_Column - Time_Left"] <= 12.430000:
                                        if features["Evader(DOWN) - Time_Left"] <= 0.259751:
                                            if features["Agent_Row - Time_Left"] <= -0.420000:
                                                return 3 # WALK RIGHT
                                            else:
                                                if features["Evader(UP) - Evader(LEFT)"] <= -0.012179:
                                                    if features["Evader(RIGHT) - Agent_Column"] <= -7.619984:
                                                        return 1 # WALK DOWN
                                                    else:
                                                        return 3 # WALK RIGHT
                                                else:
                                                    return 1 # WALK DOWN
                                        else:
                                            if features["Evader(RIGHT) - Teammate(Teammate(LEFT))"] <= 0.565413:
                                                if features["Teammate(Teammate(UP)) - Time_Left"] <= -0.006605:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    if features["Teammate(UP) - Agent_Row"] <= -0.999776:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    if features["Teammate(Evader(RIGHT)) - Time_Left"] <= 0.302664:
                                        if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.299069:
                                            return 1 # WALK DOWN
                                        else:
                                            return 3 # WALK RIGHT
                                    else:
                                        if features["Teammate(Evader(UP)) - Agent_Row"] <= -0.981388:
                                            return 1 # WALK DOWN
                                        else:
                                            return 3 # WALK RIGHT
                else:
                    if features["Evader(LEFT) - Teammate(Evader(RIGHT))"] <= 0.070573:
                        if features["Evader(UP) - Teammate(LEFT)"] <= 0.064305:
                            if features["Evader(UP)"] <= 0.101565:
                                if features["Evader(LEFT) - Time_Left"] <= 0.138447:
                                    if features["Evader(RIGHT) - Teammate(Teammate(RIGHT))"] <= -0.035770:
                                        if features["Evader(UP)"] <= 0.049646:
                                            if features["Evader(LEFT) - Time_Left"] <= 0.012045:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            return 3 # WALK RIGHT
                                    else:
                                        if features["Evader(DOWN) - Teammate(DOWN)"] <= 0.018916:
                                            if features["Teammate(UP)"] <= 0.007094:
                                                if features["Evader(DOWN) - Time_Left"] <= 0.356787:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    if features["Teammate(RIGHT) - Teammate(Teammate(UP))"] <= 0.160668:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        return 1 # WALK DOWN
                                            else:
                                                if features["Teammate(UP) - Teammate(Teammate(DOWN))"] <= -0.365810:
                                                    return 1 # WALK DOWN
                                                else:
                                                    if features["Evader(DOWN) - Teammate(Teammate(DOWN))"] <= 0.017526:
                                                        return 1 # WALK DOWN
                                                    else:
                                                        if features["Evader(LEFT)"] <= 0.276140:
                                                            return 3 # WALK RIGHT
                                                        else:
                                                            return 2 # WALK LEFT
                                        else:
                                            if features["Teammate(RIGHT) - Teammate(Teammate(UP))"] <= 0.306567:
                                                if features["Agent_Row - Time_Left"] <= 0.920000:
                                                    return 0 # WALK UP
                                                else:
                                                    return 3 # WALK RIGHT
                                            else:
                                                return 1 # WALK DOWN
                                else:
                                    if features["Teammate(Evader(DOWN)) - Teammate(Teammate(DOWN))"] <= 0.001149:
                                        if features["Teammate(Evader(UP)) - Time_Left"] <= 0.030339:
                                            if features["Evader(LEFT) - Teammate(Evader(UP))"] <= 0.163655:
                                                return 2 # WALK LEFT
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            if features["Teammate(UP) - Teammate(LEFT)"] <= -0.059695:
                                                return 0 # WALK UP
                                            else:
                                                return 3 # WALK RIGHT
                                    else:
                                        if features["Teammate(Evader(DOWN)) - Teammate(Teammate(DOWN))"] <= 0.016113:
                                            return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(Evader(DOWN)) - Agent_Row"] <= -5.588451:
                                                if features["Teammate(Teammate(DOWN)) - Agent_Row"] <= -5.841138:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 2 # WALK LEFT
                                            else:
                                                return 1 # WALK DOWN
                            else:
                                if features["Teammate(RIGHT) - Time_Left"] <= 0.067271:
                                    if features["Teammate(DOWN)"] <= 0.000003:
                                        return 1 # WALK DOWN
                                    else:
                                        if features["Teammate(Evader(DOWN)) - Teammate(Evader(LEFT))"] <= 0.027433:
                                            return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                else:
                                    return 3 # WALK RIGHT
                        else:
                            if features["Teammate(DOWN) - Teammate(RIGHT)"] <= 0.000037:
                                if features["Evader(DOWN) - Time_Left"] <= 0.270020:
                                    if features["Teammate(DOWN) - Time_Left"] <= 0.274262:
                                        return 3 # WALK RIGHT
                                    else:
                                        if features["Teammate(Evader(RIGHT)) - Teammate(Teammate(RIGHT))"] <= -0.183922:
                                            return 2 # WALK LEFT
                                        else:
                                            return 0 # WALK UP
                                else:
                                    if features["Evader(UP) - Teammate(Evader(DOWN))"] <= -0.254533:
                                        return 1 # WALK DOWN
                                    else:
                                        return 3 # WALK RIGHT
                            else:
                                if features["Evader(DOWN)"] <= 0.356514:
                                    if features["Teammate(Evader(LEFT)) - Time_Left"] <= -0.143411:
                                        return 0 # WALK UP
                                    else:
                                        if features["Teammate(Teammate(LEFT)) - Agent_Column"] <= -4.603525:
                                            if features["Teammate(DOWN) - Agent_Column"] <= -8.550719:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                else:
                                    if features["Teammate(DOWN) - Agent_Column"] <= -5.503407:
                                        return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                    else:
                        if features["Evader(UP) - Teammate(Evader(DOWN))"] <= -0.265283:
                            if features["Evader(DOWN) - Time_Left"] <= 0.310171:
                                if features["Teammate(Evader(RIGHT)) - Time_Left"] <= -0.363590:
                                    return 3 # WALK RIGHT
                                else:
                                    if features["Teammate(LEFT) - Agent_Row"] <= -5.455750:
                                        if features["Teammate(Evader(UP)) - Agent_Row"] <= -5.914910:
                                            if features["Evader(UP)"] <= 0.041781:
                                                return 1 # WALK DOWN
                                            else:
                                                if features["Evader(RIGHT) - Teammate(DOWN)"] <= -0.210833:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    return 1 # WALK DOWN
                                        else:
                                            return 2 # WALK LEFT
                                    else:
                                        if features["Evader(UP) - Teammate(Evader(DOWN))"] <= -0.367199:
                                            return 1 # WALK DOWN
                                        else:
                                            if features["Teammate(LEFT) - Teammate(Teammate(RIGHT))"] <= 0.113782:
                                                if features["Teammate(DOWN) - Teammate(Teammate(UP))"] <= 0.319304:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 0 # WALK UP
                                            else:
                                                if features["Teammate(RIGHT) - Teammate(Evader(UP))"] <= 0.020474:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 3 # WALK RIGHT
                            else:
                                if features["Evader(UP) - Teammate(LEFT)"] <= -0.248122:
                                    if features["Teammate(RIGHT) - Teammate(Teammate(UP))"] <= -0.109611:
                                        if features["Teammate(UP) - Teammate(Evader(UP))"] <= -0.047291:
                                            if features["Teammate(LEFT) - Teammate(Evader(DOWN))"] <= 0.005320:
                                                return 2 # WALK LEFT
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    if features["Teammate(LEFT) - Teammate(Teammate(UP))"] <= 0.168408:
                                        if features["Evader(DOWN) - Agent_Column"] <= -8.562810:
                                            return 2 # WALK LEFT
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        return 0 # WALK UP
                        else:
                            if features["Teammate(Evader(LEFT)) - Teammate(Teammate(LEFT))"] <= -0.006225:
                                if features["Evader(DOWN) - Time_Left"] <= 0.307227:
                                    if features["Teammate(Teammate(UP)) - Time_Left"] <= 0.064671:
                                        if features["Evader(LEFT) - Teammate(LEFT)"] <= -0.075977:
                                            if features["Teammate(Teammate(RIGHT)) - Time_Left"] <= -0.687409:
                                                return 0 # WALK UP
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        if features["Teammate(Teammate(RIGHT)) - Time_Left"] <= 0.165028:
                                            if features["Evader(RIGHT) - Teammate(DOWN)"] <= -0.363487:
                                                return 1 # WALK DOWN
                                            else:
                                                if features["Evader(RIGHT) - Teammate(UP)"] <= 0.014692:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 3 # WALK RIGHT
                                        else:
                                            return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                            else:
                                if features["Teammate(DOWN) - Teammate(Evader(DOWN))"] <= -0.103006:
                                    if features["Teammate(RIGHT) - Agent_Row"] <= -5.999965:
                                        return 3 # WALK RIGHT
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    if features["Evader(UP) - Teammate(RIGHT)"] <= 0.077289:
                                        if features["Teammate(Evader(UP)) - Teammate(Teammate(LEFT))"] <= -0.203833:
                                            return 0 # WALK UP
                                        else:
                                            if features["Evader(DOWN) - Teammate(LEFT)"] <= -0.023398:
                                                return 0 # WALK UP
                                            else:
                                                return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(LEFT) - Teammate(Evader(UP))"] <= 0.431632:
                                            return 0 # WALK UP
                                        else:
                                            if features["Teammate(DOWN) - Teammate(LEFT)"] <= -0.000003:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
        else:
            if features["Evader(UP) - Evader(RIGHT)"] <= 0.151992:
                if features["Evader(UP) - Evader(DOWN)"] <= 0.007352:
                    if features["Evader(LEFT) - Time_Left"] <= 0.319461:
                        if features["Evader(UP)"] <= 0.066444:
                            if features["Evader(DOWN) - Teammate(Evader(RIGHT))"] <= 0.367618:
                                if features["Teammate(Teammate(RIGHT)) - Time_Left"] <= -0.577523:
                                    return 0 # WALK UP
                                else:
                                    if features["Teammate(UP)"] <= 0.001233:
                                        if features["Teammate(LEFT) - Agent_Row"] <= -1.565607:
                                            return 2 # WALK LEFT
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        if features["Evader(DOWN)"] <= 0.344554:
                                            return 2 # WALK LEFT
                                        else:
                                            return 3 # WALK RIGHT
                            else:
                                return 1 # WALK DOWN
                        else:
                            if features["Teammate(Evader(DOWN)) - Teammate(Teammate(DOWN))"] <= -0.005062:
                                if features["Teammate(RIGHT)"] <= 0.000027:
                                    if features["Teammate(Evader(UP))"] <= 0.216356:
                                        if features["Teammate(Evader(UP)) - Agent_Column"] <= -11.985804:
                                            return 0 # WALK UP
                                        else:
                                            if features["Teammate(DOWN) - Teammate(LEFT)"] <= 0.000007:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                    else:
                                        return 0 # WALK UP
                                else:
                                    return 0 # WALK UP
                            else:
                                if features["Teammate(DOWN) - Agent_Row"] <= -5.399482:
                                    if features["Evader(LEFT) - Time_Left"] <= 0.315030:
                                        if features["Teammate(Evader(UP)) - Teammate(Evader(RIGHT))"] <= 0.111594:
                                            if features["Teammate(Teammate(DOWN)) - Agent_Row"] <= -5.736546:
                                                if features["Evader(RIGHT) - Teammate(Evader(LEFT))"] <= -0.239091:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    if features["Evader(RIGHT) - Teammate(LEFT)"] <= 0.135322:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        return 0 # WALK UP
                                            else:
                                                return 2 # WALK LEFT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    if features["Teammate(LEFT) - Teammate(Teammate(DOWN))"] <= 0.156241:
                                        if features["Evader(DOWN) - Time_Left"] <= 0.270390:
                                            return 0 # WALK UP
                                        else:
                                            if features["Evader(LEFT) - Evader(RIGHT)"] <= 0.282970:
                                                if features["Evader(LEFT) - Teammate(Teammate(DOWN))"] <= 0.033127:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 2 # WALK LEFT
                                            else:
                                                return 0 # WALK UP
                                    else:
                                        if features["Teammate(Evader(DOWN)) - Teammate(Evader(LEFT))"] <= 0.008356:
                                            return 0 # WALK UP
                                        else:
                                            if features["Evader(UP)"] <= 0.149021:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                    else:
                        if features["Evader(UP) - Teammate(Evader(UP))"] <= -0.008855:
                            if features["Teammate(DOWN) - Agent_Column"] <= -9.530197:
                                return 2 # WALK LEFT
                            else:
                                return 0 # WALK UP
                        else:
                            if features["Evader(LEFT) - Teammate(Teammate(UP))"] <= 0.160025:
                                if features["Evader(RIGHT) - Teammate(Evader(RIGHT))"] <= 0.005210:
                                    return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                            else:
                                if features["Teammate(UP) - Teammate(LEFT)"] <= -0.215046:
                                    if features["Teammate(LEFT) - Teammate(RIGHT)"] <= 0.283732:
                                        return 0 # WALK UP
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                else:
                    if features["Teammate(Evader(UP)) - Teammate(Evader(RIGHT))"] <= 0.087051:
                        if features["Teammate(RIGHT) - Teammate(Teammate(LEFT))"] <= 0.188354:
                            if features["Evader(UP) - Teammate(Teammate(UP))"] <= 0.025223:
                                if features["Teammate(Teammate(DOWN)) - Time_Left"] <= 0.152882:
                                    if features["Teammate(Teammate(DOWN)) - Time_Left"] <= 0.149269:
                                        if features["Teammate(Evader(UP))"] <= 0.365557:
                                            if features["Teammate(DOWN) - Teammate(Evader(DOWN))"] <= 0.017668:
                                                if features["Teammate(DOWN) - Teammate(LEFT)"] <= -0.089351:
                                                    if features["Evader(DOWN) - Teammate(DOWN)"] <= 0.026566:
                                                        return 0 # WALK UP
                                                    else:
                                                        return 3 # WALK RIGHT
                                                else:
                                                    return 3 # WALK RIGHT
                                            else:
                                                if features["Teammate(Evader(DOWN)) - Teammate(Teammate(RIGHT))"] <= -0.077475:
                                                    return 0 # WALK UP
                                                else:
                                                    if features["Teammate(DOWN) - Teammate(LEFT)"] <= -0.000008:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        return 0 # WALK UP
                                        else:
                                            if features["Evader(DOWN) - Teammate(Evader(LEFT))"] <= -0.009906:
                                                return 0 # WALK UP
                                            else:
                                                return 3 # WALK RIGHT
                                    else:
                                        return 0 # WALK UP
                                else:
                                    return 3 # WALK RIGHT
                            else:
                                if features["Evader(DOWN) - Teammate(DOWN)"] <= 0.029310:
                                    if features["Evader(DOWN) - Agent_Row"] <= -1.999998:
                                        if features["Teammate(DOWN) - Teammate(Teammate(LEFT))"] <= 0.030029:
                                            if features["Evader(RIGHT) - Time_Left"] <= 0.201510:
                                                if features["Evader(UP) - Evader(RIGHT)"] <= 0.108042:
                                                    if features["Evader(RIGHT) - Teammate(LEFT)"] <= 0.126450:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        return 0 # WALK UP
                                                else:
                                                    if features["Teammate(Evader(DOWN)) - Teammate(Teammate(LEFT))"] <= -0.078452:
                                                        if features["Teammate(UP) - Teammate(Teammate(LEFT))"] <= 0.021457:
                                                            return 0 # WALK UP
                                                        else:
                                                            return 3 # WALK RIGHT
                                                    else:
                                                        return 0 # WALK UP
                                            else:
                                                if features["Evader(RIGHT) - Time_Left"] <= 0.255714:
                                                    if features["Teammate(DOWN) - Time_Left"] <= -0.118879:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        if features["Teammate(Teammate(RIGHT)) - Time_Left"] <= 0.247654:
                                                            return 0 # WALK UP
                                                        else:
                                                            return 3 # WALK RIGHT
                                                else:
                                                    if features["Evader(UP) - Evader(DOWN)"] <= 0.354867:
                                                        if features["Evader(UP) - Teammate(UP)"] <= -0.003582:
                                                            if features["Teammate(Evader(UP)) - Teammate(Evader(RIGHT))"] <= 0.000979:
                                                                return 3 # WALK RIGHT
                                                            else:
                                                                return 0 # WALK UP
                                                        else:
                                                            return 3 # WALK RIGHT
                                                    else:
                                                        if features["Evader(UP) - Evader(DOWN)"] <= 0.865475:
                                                            if features["Evader(DOWN)"] <= 0.000007:
                                                                return 0 # WALK UP
                                                            else:
                                                                if features["Teammate(DOWN) - Teammate(Teammate(UP))"] <= -0.304268:
                                                                    return 0 # WALK UP
                                                                else:
                                                                    if features["Evader(UP) - Teammate(Teammate(UP))"] <= 0.099980:
                                                                        return 3 # WALK RIGHT
                                                                    else:
                                                                        return 0 # WALK UP
                                                        else:
                                                            return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(DOWN) - Teammate(LEFT)"] <= -0.000112:
                                                if features["Evader(DOWN)"] <= 0.065063:
                                                    return 0 # WALK UP
                                                else:
                                                    return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                    else:
                                        if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.589806:
                                            if features["Teammate(Teammate(LEFT)) - Agent_Column"] <= -12.455503:
                                                return 0 # WALK UP
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                else:
                                    if features["Teammate(LEFT) - Agent_Row"] <= -7.998755:
                                        if features["Teammate(UP) - Teammate(RIGHT)"] <= 0.005625:
                                            return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                    else:
                                        return 3 # WALK RIGHT
                        else:
                            if features["Teammate(DOWN) - Time_Left"] <= -0.109983:
                                if features["Evader(UP) - Time_Left"] <= 0.272941:
                                    return 3 # WALK RIGHT
                                else:
                                    return 0 # WALK UP
                            else:
                                if features["Teammate(LEFT)"] <= 0.097847:
                                    if features["Evader(LEFT) - Agent_Row"] <= -1.999998:
                                        if features["Teammate(DOWN) - Agent_Column"] <= -5.414322:
                                            return 0 # WALK UP
                                        else:
                                            if features["Evader(RIGHT) - Teammate(Teammate(RIGHT))"] <= -0.082329:
                                                if features["Evader(LEFT) - Teammate(RIGHT)"] <= -0.335841:
                                                    return 0 # WALK UP
                                                else:
                                                    return 2 # WALK LEFT
                                            else:
                                                return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                                else:
                                    if features["Evader(LEFT) - Teammate(LEFT)"] <= -0.099708:
                                        return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                    else:
                        if features["Teammate(Teammate(RIGHT)) - Time_Left"] <= -0.099053:
                            if features["Evader(UP) - Teammate(UP)"] <= 0.282772:
                                if features["Evader(RIGHT) - Time_Left"] <= 0.116524:
                                    return 3 # WALK RIGHT
                                else:
                                    return 0 # WALK UP
                            else:
                                if features["Evader(LEFT) - Evader(RIGHT)"] <= -0.839377:
                                    return 3 # WALK RIGHT
                                else:
                                    return 0 # WALK UP
                        else:
                            if features["Evader(RIGHT) - Time_Left"] <= 0.212334:
                                if features["Teammate(Evader(DOWN)) - Teammate(Evader(LEFT))"] <= -0.105672:
                                    if features["Teammate(UP) - Teammate(Evader(RIGHT))"] <= 0.147461:
                                        if features["Teammate(UP) - Teammate(Evader(DOWN))"] <= 0.240361:
                                            if features["Teammate(LEFT) - Agent_Column"] <= -10.683790:
                                                if features["Teammate(RIGHT) - Teammate(Teammate(RIGHT))"] <= -0.000346:
                                                    return 0 # WALK UP
                                                else:
                                                    return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            if features["Teammate(DOWN) - Teammate(Teammate(UP))"] <= -0.146352:
                                                return 0 # WALK UP
                                            else:
                                                return 3 # WALK RIGHT
                                    else:
                                        if features["Evader(LEFT) - Evader(RIGHT)"] <= 0.054079:
                                            if features["Teammate(Evader(DOWN)) - Teammate(Evader(RIGHT))"] <= -0.128681:
                                                return 3 # WALK RIGHT
                                            else:
                                                if features["Teammate(Evader(RIGHT)) - Time_Left"] <= -0.169508:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 0 # WALK UP
                                        else:
                                            if features["Teammate(DOWN) - Time_Left"] <= 0.190227:
                                                if features["Evader(LEFT) - Teammate(UP)"] <= -0.402066:
                                                    return 0 # WALK UP
                                                else:
                                                    return 2 # WALK LEFT
                                            else:
                                                return 3 # WALK RIGHT
                                else:
                                    if features["Teammate(Teammate(UP)) - Teammate(Teammate(RIGHT))"] <= 0.083923:
                                        if features["Teammate(Evader(DOWN)) - Teammate(Evader(LEFT))"] <= -0.105597:
                                            return 2 # WALK LEFT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        if features["Evader(LEFT) - Teammate(UP)"] <= 0.057844:
                                            return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(UP) - Time_Left"] <= 0.170695:
                                                return 0 # WALK UP
                                            else:
                                                return 2 # WALK LEFT
                            else:
                                if features["Evader(UP) - Teammate(Evader(DOWN))"] <= 0.614226:
                                    if features["Evader(DOWN) - Teammate(RIGHT)"] <= 0.025159:
                                        return 0 # WALK UP
                                    else:
                                        if features["Teammate(Evader(DOWN)) - Agent_Column"] <= -3.934784:
                                            return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                else:
                                    return 0 # WALK UP
            else:
                if features["Evader(UP) - Teammate(Evader(LEFT))"] <= 0.010816:
                    if features["Evader(LEFT) - Time_Left"] <= 0.320866:
                        if features["Teammate(DOWN) - Agent_Column"] <= -10.999997:
                            if features["Evader(LEFT) - Time_Left"] <= 0.261035:
                                if features["Teammate(LEFT) - Agent_Row"] <= -4.506936:
                                    return 0 # WALK UP
                                else:
                                    return 2 # WALK LEFT
                            else:
                                return 2 # WALK LEFT
                        else:
                            if features["Teammate(UP) - Teammate(RIGHT)"] <= 0.281589:
                                return 0 # WALK UP
                            else:
                                if features["Teammate(UP) - Teammate(Evader(DOWN))"] <= 0.317670:
                                    if features["Teammate(DOWN)"] <= 0.000001:
                                        return 2 # WALK LEFT
                                    else:
                                        return 0 # WALK UP
                                else:
                                    if features["Teammate(Teammate(DOWN)) - Agent_Row"] <= -4.754781:
                                        return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                    else:
                        if features["Teammate(UP) - Time_Left"] <= -0.004825:
                            return 0 # WALK UP
                        else:
                            if features["Teammate(Teammate(UP)) - Teammate(Teammate(RIGHT))"] <= 0.258484:
                                if features["Evader(LEFT) - Teammate(Teammate(LEFT))"] <= -0.005331:
                                    return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                            else:
                                return 3 # WALK RIGHT
                else:
                    if features["Evader(UP) - Time_Left"] <= 0.269894:
                        if features["Teammate(LEFT) - Time_Left"] <= -0.589144:
                            if features["Evader(RIGHT) - Agent_Row"] <= -11.999952:
                                if features["Evader(LEFT)"] <= 0.285952:
                                    return 2 # WALK LEFT
                                else:
                                    return 0 # WALK UP
                            else:
                                if features["Teammate(Evader(UP)) - Teammate(Evader(RIGHT))"] <= 0.135778:
                                    return 3 # WALK RIGHT
                                else:
                                    return 1 # WALK DOWN
                        else:
                            if features["Teammate(Evader(DOWN)) - Teammate(Evader(LEFT))"] <= -0.072353:
                                return 0 # WALK UP
                            else:
                                if features["Teammate(DOWN) - Teammate(LEFT)"] <= 0.000121:
                                    if features["Evader(RIGHT)"] <= 0.123740:
                                        if features["Teammate(Evader(LEFT)) - Time_Left"] <= -0.684533:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                                else:
                                    return 0 # WALK UP
                    else:
                        if features["Evader(LEFT) - Teammate(Teammate(UP))"] <= 0.027371:
                            return 0 # WALK UP
                        else:
                            if features["Evader(RIGHT) - Agent_Row"] <= -11.814783:
                                if features["Evader(RIGHT) - Teammate(Evader(UP))"] <= -0.246749:
                                    if features["Teammate(DOWN) - Time_Left"] <= -0.029962:
                                        return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 0 # WALK UP
                            else:
                                return 0 # WALK UP
    else:
        if features["Evader(DOWN) - Evader(LEFT)"] <= 0.000002:
            if features["Evader(UP) - Evader(LEFT)"] <= 0.000000:
                if features["Evader(RIGHT) - Teammate(UP)"] <= 0.000391:
                    if features["Evader(DOWN)"] <= 0.663394:
                        if features["Evader(UP) - Evader(DOWN)"] <= 0.809231:
                            if features["Evader(LEFT) - Time_Left"] <= 0.132164:
                                if features["Evader(UP)"] <= 0.015394:
                                    if features["Evader(UP) - Evader(LEFT)"] <= -0.548963:
                                        return 1 # WALK DOWN
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    if features["Evader(LEFT) - Teammate(RIGHT)"] <= 0.650397:
                                        if features["Evader(UP) - Teammate(RIGHT)"] <= 0.305015:
                                            if features["Teammate(RIGHT) - Teammate(Teammate(UP))"] <= -0.337299:
                                                return 2 # WALK LEFT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(UP) - Agent_Row"] <= -5.969847:
                                            return 0 # WALK UP
                                        else:
                                            return 1 # WALK DOWN
                            else:
                                if features["Evader(LEFT) - Agent_Column"] <= -13.615106:
                                    if features["Evader(UP) - Teammate(DOWN)"] <= 0.347413:
                                        if features["Evader(LEFT) - Agent_Row"] <= -1.618378:
                                            if features["Teammate(Evader(LEFT)) - Time_Left"] <= 0.321113:
                                                if features["Evader(DOWN) - Teammate(UP)"] <= 0.363828:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 1 # WALK DOWN
                                            else:
                                                return 2 # WALK LEFT
                                        else:
                                            if features["Teammate(RIGHT) - Teammate(Teammate(UP))"] <= -0.035913:
                                                return 1 # WALK DOWN
                                            else:
                                                return 2 # WALK LEFT
                                    else:
                                        return 0 # WALK UP
                                else:
                                    if features["Evader(RIGHT) - Teammate(DOWN)"] <= 0.000144:
                                        if features["Evader(RIGHT)"] <= 0.067381:
                                            if features["Evader(UP) - Evader(RIGHT)"] <= 0.664182:
                                                if features["Teammate(DOWN) - Teammate(LEFT)"] <= -0.404141:
                                                    if features["Evader(RIGHT)"] <= 0.000550:
                                                        return 2 # WALK LEFT
                                                    else:
                                                        if features["Teammate(Evader(RIGHT)) - Teammate(Teammate(UP))"] <= -0.236112:
                                                            return 0 # WALK UP
                                                        else:
                                                            return 2 # WALK LEFT
                                                else:
                                                    if features["Evader(LEFT) - Teammate(Evader(DOWN))"] <= 0.087044:
                                                        if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.001267:
                                                            if features["Teammate(Evader(DOWN)) - Agent_Column"] <= -13.684914:
                                                                return 1 # WALK DOWN
                                                            else:
                                                                return 2 # WALK LEFT
                                                        else:
                                                            if features["Teammate(DOWN) - Time_Left"] <= 0.313712:
                                                                if features["Evader(RIGHT) - Teammate(Evader(RIGHT))"] <= -0.114890:
                                                                    return 0 # WALK UP
                                                                else:
                                                                    return 2 # WALK LEFT
                                                            else:
                                                                return 0 # WALK UP
                                                    else:
                                                        if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.003745:
                                                            return 0 # WALK UP
                                                        else:
                                                            return 2 # WALK LEFT
                                            else:
                                                if features["Evader(RIGHT)"] <= 0.000007:
                                                    if features["Teammate(Evader(DOWN)) - Agent_Column"] <= -13.759989:
                                                        return 0 # WALK UP
                                                    else:
                                                        return 2 # WALK LEFT
                                                else:
                                                    if features["Teammate(Evader(UP)) - Teammate(Evader(LEFT))"] <= 0.077065:
                                                        if features["Teammate(UP) - Agent_Column"] <= -9.999813:
                                                            return 0 # WALK UP
                                                        else:
                                                            return 2 # WALK LEFT
                                                    else:
                                                        if features["Teammate(Teammate(LEFT)) - Agent_Column"] <= -2.852184:
                                                            if features["Evader(DOWN) - Agent_Column"] <= -9.999687:
                                                                return 0 # WALK UP
                                                            else:
                                                                return 2 # WALK LEFT
                                                        else:
                                                            return 0 # WALK UP
                                        else:
                                            if features["Evader(LEFT) - Teammate(Evader(DOWN))"] <= 0.248471:
                                                return 0 # WALK UP
                                            else:
                                                if features["Teammate(Evader(LEFT)) - Time_Left"] <= 0.211493:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(Evader(DOWN)) - Time_Left"] <= -0.030686:
                                            if features["Evader(RIGHT) - Teammate(DOWN)"] <= 0.023703:
                                                return 2 # WALK LEFT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            if features["Teammate(Evader(LEFT)) - Time_Left"] <= 0.266427:
                                                if features["Evader(UP) - Time_Left"] <= 0.181993:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 0 # WALK UP
                                            else:
                                                return 2 # WALK LEFT
                        else:
                            if features["Evader(RIGHT) - Agent_Column"] <= -11.999998:
                                return 0 # WALK UP
                            else:
                                return 2 # WALK LEFT
                    else:
                        if features["Evader(UP) - Evader(LEFT)"] <= -0.800238:
                            if features["Teammate(UP) - Teammate(LEFT)"] <= -0.006215:
                                if features["Evader(UP) - Evader(RIGHT)"] <= -0.000012:
                                    return 2 # WALK LEFT
                                else:
                                    if features["Teammate(LEFT) - Agent_Column"] <= -8.697640:
                                        if features["Teammate(Evader(DOWN)) - Agent_Row"] <= -11.455562:
                                            return 2 # WALK LEFT
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        if features["Teammate(Evader(LEFT)) - Agent_Row"] <= -4.598880:
                                            return 1 # WALK DOWN
                                        else:
                                            return 2 # WALK LEFT
                            else:
                                if features["Evader(DOWN) - Agent_Row"] <= -0.132271:
                                    return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
                        else:
                            if features["Evader(RIGHT)"] <= 0.000007:
                                if features["Evader(LEFT) - Time_Left"] <= 0.257767:
                                    return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                            else:
                                if features["Teammate(UP) - Agent_Row"] <= -9.999844:
                                    return 2 # WALK LEFT
                                else:
                                    if features["Teammate(RIGHT) - Agent_Row"] <= -4.587491:
                                        return 1 # WALK DOWN
                                    else:
                                        if features["Teammate(Evader(DOWN)) - Agent_Column"] <= -1.645171:
                                            return 2 # WALK LEFT
                                        else:
                                            return 1 # WALK DOWN
                else:
                    if features["Evader(DOWN) - Time_Left"] <= 0.212129:
                        if features["Evader(RIGHT) - Teammate(UP)"] <= 0.026897:
                            if features["Evader(DOWN) - Evader(LEFT)"] <= -0.148689:
                                return 2 # WALK LEFT
                            else:
                                if features["Teammate(Teammate(DOWN)) - Agent_Column"] <= -3.911979:
                                    if features["Evader(UP) - Teammate(RIGHT)"] <= 0.011101:
                                        return 2 # WALK LEFT
                                    else:
                                        return 0 # WALK UP
                                else:
                                    return 1 # WALK DOWN
                        else:
                            if features["Evader(DOWN) - Teammate(Evader(UP))"] <= 0.152496:
                                if features["Agent_Row - Agent_Column"] <= -3.500000:
                                    if features["Evader(DOWN) - Teammate(Evader(RIGHT))"] <= 0.026590:
                                        return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 0 # WALK UP
                            else:
                                if features["Teammate(LEFT) - Agent_Column"] <= -4.999664:
                                    if features["Agent_Row - Time_Left"] <= 3.720000:
                                        return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 3 # WALK RIGHT
                    else:
                        if features["Evader(DOWN) - Time_Left"] <= 0.292929:
                            return 2 # WALK LEFT
                        else:
                            if features["Evader(RIGHT) - Teammate(Evader(LEFT))"] <= -0.323815:
                                return 2 # WALK LEFT
                            else:
                                return 1 # WALK DOWN
            else:
                if features["Evader(UP)"] <= 0.865541:
                    if features["Evader(DOWN)"] <= 0.000035:
                        if features["Teammate(DOWN) - Teammate(Teammate(UP))"] <= -0.360121:
                            if features["Teammate(RIGHT) - Time_Left"] <= -0.789908:
                                if features["Evader(UP) - Teammate(LEFT)"] <= 0.019738:
                                    return 1 # WALK DOWN
                                else:
                                    return 0 # WALK UP
                            else:
                                if features["Evader(DOWN) - Teammate(Teammate(DOWN))"] <= -0.009555:
                                    return 0 # WALK UP
                                else:
                                    return 2 # WALK LEFT
                        else:
                            if features["Evader(DOWN) - Agent_Row"] <= -1.999967:
                                if features["Teammate(UP) - Teammate(Evader(RIGHT))"] <= 0.358116:
                                    if features["Teammate(Evader(RIGHT)) - Time_Left"] <= -0.907118:
                                        return 2 # WALK LEFT
                                    else:
                                        return 0 # WALK UP
                                else:
                                    return 0 # WALK UP
                            else:
                                return 2 # WALK LEFT
                    else:
                        if features["Evader(RIGHT)"] <= 0.026954:
                            if features["Evader(RIGHT) - Agent_Column"] <= -11.991783:
                                return 0 # WALK UP
                            else:
                                if features["Teammate(Evader(DOWN)) - Time_Left"] <= -0.681314:
                                    return 1 # WALK DOWN
                                else:
                                    if features["Teammate(DOWN) - Agent_Row"] <= -1.705045:
                                        if features["Teammate(Evader(RIGHT)) - Agent_Column"] <= -1.877953:
                                            if features["Evader(LEFT) - Agent_Column"] <= -4.390965:
                                                if features["Evader(LEFT) - Agent_Column"] <= -10.519958:
                                                    return 2 # WALK LEFT
                                                else:
                                                    if features["Teammate(Teammate(DOWN)) - Agent_Column"] <= -9.812962:
                                                        return 0 # WALK UP
                                                    else:
                                                        if features["Teammate(LEFT) - Agent_Column"] <= -7.349773:
                                                            return 2 # WALK LEFT
                                                        else:
                                                            return 0 # WALK UP
                                            else:
                                                return 2 # WALK LEFT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        if features["Evader(DOWN) - Agent_Column"] <= -5.999940:
                                            if features["Evader(UP) - Evader(DOWN)"] <= 0.773002:
                                                return 2 # WALK LEFT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            return 2 # WALK LEFT
                        else:
                            if features["Evader(UP)"] <= 0.387420:
                                return 2 # WALK LEFT
                            else:
                                if features["Teammate(UP) - Agent_Column"] <= -11.999959:
                                    return 2 # WALK LEFT
                                else:
                                    return 0 # WALK UP
                else:
                    if features["Teammate(RIGHT) - Agent_Column"] <= -7.999974:
                        if features["Teammate(LEFT) - Time_Left"] <= 0.301862:
                            if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.000121:
                                return 2 # WALK LEFT
                            else:
                                if features["Evader(UP) - Agent_Row"] <= -1.132766:
                                    if features["Evader(RIGHT) - Agent_Row"] <= -2.999968:
                                        return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    if features["Teammate(Evader(LEFT)) - Agent_Row"] <= -0.708482:
                                        return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                        else:
                            return 0 # WALK UP
                    else:
                        if features["Evader(DOWN) - Agent_Column"] <= -5.999999:
                            if features["Teammate(DOWN) - Teammate(RIGHT)"] <= 0.670400:
                                return 2 # WALK LEFT
                            else:
                                return 0 # WALK UP
                        else:
                            if features["Teammate(UP) - Agent_Column"] <= -3.675005:
                                if features["Teammate(RIGHT) - Agent_Row"] <= -9.999078:
                                    return 2 # WALK LEFT
                                else:
                                    return 0 # WALK UP
                            else:
                                if features["Teammate(DOWN) - Agent_Column"] <= -1.876744:
                                    return 2 # WALK LEFT
                                else:
                                    if features["Teammate(Evader(DOWN)) - Time_Left"] <= 0.096013:
                                        return 2 # WALK LEFT
                                    else:
                                        return 0 # WALK UP
        else:
            if features["Evader(DOWN)"] <= 0.729487:
                if features["Evader(UP)"] <= 0.000019:
                    if features["Evader(UP) - Teammate(UP)"] <= -0.000004:
                        return 1 # WALK DOWN
                    else:
                        if features["Teammate(Evader(DOWN)) - Agent_Row"] <= 0.349992:
                            if features["Agent_Row - Agent_Column"] <= 4.500000:
                                return 1 # WALK DOWN
                            else:
                                return 2 # WALK LEFT
                        else:
                            if features["Evader(DOWN) - Teammate(Teammate(DOWN))"] <= 0.075606:
                                return 1 # WALK DOWN
                            else:
                                return 2 # WALK LEFT
                else:
                    if features["Evader(RIGHT) - Agent_Row"] <= -1.989844:
                        if features["Evader(LEFT) - Time_Left"] <= 0.179668:
                            if features["Evader(UP) - Teammate(DOWN)"] <= 0.003720:
                                if features["Teammate(DOWN) - Teammate(RIGHT)"] <= 0.326172:
                                    return 1 # WALK DOWN
                                else:
                                    if features["Teammate(DOWN) - Agent_Row"] <= -6.458469:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(Evader(DOWN)) - Time_Left"] <= -0.224312:
                                            if features["Teammate(LEFT) - Teammate(Evader(LEFT))"] <= 0.208961:
                                                return 0 # WALK UP
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            return 1 # WALK DOWN
                            else:
                                return 3 # WALK RIGHT
                        else:
                            if features["Teammate(DOWN)"] <= 0.367514:
                                if features["Teammate(LEFT) - Agent_Row"] <= -9.999999:
                                    return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
                            else:
                                if features["Teammate(Evader(DOWN)) - Teammate(Evader(LEFT))"] <= 0.028060:
                                    return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
                    else:
                        if features["Teammate(LEFT) - Agent_Column"] <= -12.393507:
                            return 1 # WALK DOWN
                        else:
                            if features["Evader(RIGHT) - Teammate(DOWN)"] <= -0.366936:
                                if features["Evader(RIGHT)"] <= 0.000499:
                                    return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
                            else:
                                if features["Evader(RIGHT) - Agent_Column"] <= -11.988045:
                                    return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
            else:
                if features["Evader(DOWN) - Agent_Column"] <= -9.131965:
                    if features["Teammate(LEFT) - Agent_Row"] <= -10.992695:
                        if features["Evader(UP) - Agent_Column"] <= -13.000000:
                            return 1 # WALK DOWN
                        else:
                            return 2 # WALK LEFT
                    else:
                        return 1 # WALK DOWN
                else:
                    if features["Evader(DOWN)"] <= 0.867661:
                        if features["Evader(DOWN) - Agent_Row"] <= -10.224233:
                            if features["Evader(LEFT) - Evader(RIGHT)"] <= 0.796594:
                                return 2 # WALK LEFT
                            else:
                                return 1 # WALK DOWN
                        else:
                            if features["Evader(UP) - Teammate(UP)"] <= -0.000001:
                                if features["Evader(DOWN)"] <= 0.867320:
                                    return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                            else:
                                if features["Teammate(Evader(UP)) - Agent_Column"] <= -1.969785:
                                    if features["Teammate(Teammate(UP)) - Teammate(Teammate(RIGHT))"] <= -0.151722:
                                        return 2 # WALK LEFT
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    return 1 # WALK DOWN
                    else:
                        if features["Teammate(RIGHT) - Agent_Row"] <= -4.653781:
                            if features["Teammate(LEFT) - Agent_Row"] <= -10.699068:
                                return 2 # WALK LEFT
                            else:
                                return 1 # WALK DOWN
                        else:
                            if features["Evader(RIGHT) - Agent_Column"] <= -0.999965:
                                if features["Agent_Row - Time_Left"] <= 1.540000:
                                    if features["Evader(UP) - Agent_Row"] <= -0.999999:
                                        return 1 # WALK DOWN
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 2 # WALK LEFT
                            else:
                                return 1 # WALK DOWN


def interpretable_action(Evader_Probability_Grid, Teammate_Probability_Grid, Teammate_Evader_Probability_Grid, Teammate_Teammate_Probability_Grid, Main_Agent_Position, Time_Left, Gamma, Size, Valid_Actions):
    input_representation = symbolic_representation(Evader_Probability_Grid, Teammate_Probability_Grid, Teammate_Evader_Probability_Grid, Teammate_Teammate_Probability_Grid, Main_Agent_Position, Time_Left, Gamma, Size)
    input_combinations   = get_feature_vector(input_representation)
    symbol_to_value     = {name: input_combinations[i] for i, name in enumerate(symbol_names)}
    action               = Index_to_Action[interpretable_strategy(symbol_to_value)]
    if action in Valid_Actions:
        return action
    else:
        return random.choice(Valid_Actions)
