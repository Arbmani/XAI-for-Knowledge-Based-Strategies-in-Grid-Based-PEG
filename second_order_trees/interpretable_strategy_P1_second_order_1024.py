import random
from INTERPRETER_2ND import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'T(E(UP))', 'T(E(DOWN))', 'T(E(LEFT))', 'T(E(RIGHT))', 'T(T(up))', 'T(T(DOWN))', 'T(T(LEFT))', 'T(T(RIGHT))', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - T(E(UP))', 'E(UP) - T(E(DOWN))', 'E(UP) - T(E(LEFT))', 'E(UP) - T(E(RIGHT))', 'E(UP) - T(T(up))', 'E(UP) - T(T(DOWN))', 'E(UP) - T(T(LEFT))', 'E(UP) - T(T(RIGHT))', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - T(E(UP))', 'E(DOWN) - T(E(DOWN))', 'E(DOWN) - T(E(LEFT))', 'E(DOWN) - T(E(RIGHT))', 'E(DOWN) - T(T(up))', 'E(DOWN) - T(T(DOWN))', 'E(DOWN) - T(T(LEFT))', 'E(DOWN) - T(T(RIGHT))', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - T(E(UP))', 'E(LEFT) - T(E(DOWN))', 'E(LEFT) - T(E(LEFT))', 'E(LEFT) - T(E(RIGHT))', 'E(LEFT) - T(T(up))', 'E(LEFT) - T(T(DOWN))', 'E(LEFT) - T(T(LEFT))', 'E(LEFT) - T(T(RIGHT))', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - T(E(UP))', 'E(RIGHT) - T(E(DOWN))', 'E(RIGHT) - T(E(LEFT))', 'E(RIGHT) - T(E(RIGHT))', 'E(RIGHT) - T(T(up))', 'E(RIGHT) - T(T(DOWN))', 'E(RIGHT) - T(T(LEFT))', 'E(RIGHT) - T(T(RIGHT))', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - T(E(UP))', 'T(up) - T(E(DOWN))', 'T(up) - T(E(LEFT))', 'T(up) - T(E(RIGHT))', 'T(up) - T(T(up))', 'T(up) - T(T(DOWN))', 'T(up) - T(T(LEFT))', 'T(up) - T(T(RIGHT))', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - T(E(UP))', 'T(DOWN) - T(E(DOWN))', 'T(DOWN) - T(E(LEFT))', 'T(DOWN) - T(E(RIGHT))', 'T(DOWN) - T(T(up))', 'T(DOWN) - T(T(DOWN))', 'T(DOWN) - T(T(LEFT))', 'T(DOWN) - T(T(RIGHT))', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - T(E(UP))', 'T(LEFT) - T(E(DOWN))', 'T(LEFT) - T(E(LEFT))', 'T(LEFT) - T(E(RIGHT))', 'T(LEFT) - T(T(up))', 'T(LEFT) - T(T(DOWN))', 'T(LEFT) - T(T(LEFT))', 'T(LEFT) - T(T(RIGHT))', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - T(E(UP))', 'T(RIGHT) - T(E(DOWN))', 'T(RIGHT) - T(E(LEFT))', 'T(RIGHT) - T(E(RIGHT))', 'T(RIGHT) - T(T(up))', 'T(RIGHT) - T(T(DOWN))', 'T(RIGHT) - T(T(LEFT))', 'T(RIGHT) - T(T(RIGHT))', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'T(E(UP)) - T(E(DOWN))', 'T(E(UP)) - T(E(LEFT))', 'T(E(UP)) - T(E(RIGHT))', 'T(E(UP)) - T(T(up))', 'T(E(UP)) - T(T(DOWN))', 'T(E(UP)) - T(T(LEFT))', 'T(E(UP)) - T(T(RIGHT))', 'T(E(UP)) - agent_row', 'T(E(UP)) - agent_column', 'T(E(UP)) - time_left', 'T(E(DOWN)) - T(E(LEFT))', 'T(E(DOWN)) - T(E(RIGHT))', 'T(E(DOWN)) - T(T(up))', 'T(E(DOWN)) - T(T(DOWN))', 'T(E(DOWN)) - T(T(LEFT))', 'T(E(DOWN)) - T(T(RIGHT))', 'T(E(DOWN)) - agent_row', 'T(E(DOWN)) - agent_column', 'T(E(DOWN)) - time_left', 'T(E(LEFT)) - T(E(RIGHT))', 'T(E(LEFT)) - T(T(up))', 'T(E(LEFT)) - T(T(DOWN))', 'T(E(LEFT)) - T(T(LEFT))', 'T(E(LEFT)) - T(T(RIGHT))', 'T(E(LEFT)) - agent_row', 'T(E(LEFT)) - agent_column', 'T(E(LEFT)) - time_left', 'T(E(RIGHT)) - T(T(up))', 'T(E(RIGHT)) - T(T(DOWN))', 'T(E(RIGHT)) - T(T(LEFT))', 'T(E(RIGHT)) - T(T(RIGHT))', 'T(E(RIGHT)) - agent_row', 'T(E(RIGHT)) - agent_column', 'T(E(RIGHT)) - time_left', 'T(T(up)) - T(T(DOWN))', 'T(T(up)) - T(T(LEFT))', 'T(T(up)) - T(T(RIGHT))', 'T(T(up)) - agent_row', 'T(T(up)) - agent_column', 'T(T(up)) - time_left', 'T(T(DOWN)) - T(T(LEFT))', 'T(T(DOWN)) - T(T(RIGHT))', 'T(T(DOWN)) - agent_row', 'T(T(DOWN)) - agent_column', 'T(T(DOWN)) - time_left', 'T(T(LEFT)) - T(T(RIGHT))', 'T(T(LEFT)) - agent_row', 'T(T(LEFT)) - agent_column', 'T(T(LEFT)) - time_left', 'T(T(RIGHT)) - agent_row', 'T(T(RIGHT)) - agent_column', 'T(T(RIGHT)) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(RIGHT)"] <= -0.000048:
        if features["E(DOWN) - E(RIGHT)"] <= -0.000047:
            if features["E(LEFT)"] <= 0.060962:
                if features["E(RIGHT) - T(E(DOWN))"] <= 0.080374:
                    if features["E(UP) - agent_row"] <= -0.998701:
                        if features["E(LEFT)"] <= 0.000009:
                            if features["E(RIGHT)"] <= 0.800303:
                                if features["T(E(DOWN)) - agent_column"] <= 0.319612:
                                    return 3
                                else:
                                    return 1
                            else:
                                if features["T(RIGHT) - T(T(RIGHT))"] <= -0.009747:
                                    return 3
                                else:
                                    return 1
                        else:
                            if features["E(RIGHT) - agent_row"] <= -1.615522:
                                if features["E(UP) - T(RIGHT)"] <= -0.231343:
                                    if features["T(LEFT)"] <= 0.000138:
                                        if features["T(LEFT) - agent_column"] <= -0.999972:
                                            if features["E(UP) - time_left"] <= 0.028522:
                                                if features["E(RIGHT) - time_left"] <= -0.119139:
                                                    return 1
                                                else:
                                                    if features["T(up) - T(E(RIGHT))"] <= 0.016636:
                                                        if features["T(DOWN) - T(RIGHT)"] <= -0.000125:
                                                            if features["T(up) - agent_row"] <= -4.999764:
                                                                if features["E(DOWN) - agent_row"] <= -8.664185:
                                                                    return 1
                                                                else:
                                                                    if features["T(RIGHT) - T(E(DOWN))"] <= 0.062181:
                                                                        return 3
                                                                    else:
                                                                        return 1
                                                            else:
                                                                return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                            else:
                                                if features["E(RIGHT) - agent_row"] <= -7.547276:
                                                    if features["E(UP) - E(DOWN)"] <= 0.130701:
                                                        return 1
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(DOWN) - agent_column"] <= -7.720698:
                                                        return 1
                                                    else:
                                                        return 3
                                        else:
                                            return 3
                                    else:
                                        if features["T(T(up)) - agent_column"] <= -0.882060:
                                            if features["T(RIGHT) - T(T(LEFT))"] <= 0.143620:
                                                return 3
                                            else:
                                                if features["T(RIGHT) - T(T(up))"] <= 0.307811:
                                                    if features["E(LEFT) - T(E(LEFT))"] <= -0.005630:
                                                        return 1
                                                    else:
                                                        if features["T(E(UP)) - time_left"] <= -0.116477:
                                                            return 1
                                                        else:
                                                            return 3
                                                else:
                                                    if features["T(E(RIGHT)) - agent_column"] <= -4.709231:
                                                        return 1
                                                    else:
                                                        return 3
                                        else:
                                            return 3
                                else:
                                    if features["T(up) - time_left"] <= -0.139926:
                                        if features["E(DOWN) - T(E(DOWN))"] <= -0.263902:
                                            if features["T(DOWN) - T(RIGHT)"] <= -0.266624:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -10.590680:
                                                return 1
                                            else:
                                                if features["E(LEFT) - T(LEFT)"] <= 0.023565:
                                                    return 3
                                                else:
                                                    if features["T(E(UP)) - T(E(LEFT))"] <= 0.125596:
                                                        return 1
                                                    else:
                                                        return 2
                                    else:
                                        if features["agent_column - time_left"] <= 6.790000:
                                            return 3
                                        else:
                                            return 1
                            else:
                                if features["E(DOWN) - agent_column"] <= -3.640864:
                                    if features["T(up) - T(E(DOWN))"] <= -0.324105:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    if features["E(LEFT) - T(E(RIGHT))"] <= -0.307810:
                                        return 3
                                    else:
                                        return 1
                    else:
                        if features["T(E(LEFT)) - agent_column"] <= -1.971178:
                            return 3
                        else:
                            if features["E(DOWN) - T(T(up))"] <= -0.023404:
                                return 3
                            else:
                                return 1
                else:
                    if features["E(DOWN) - T(E(LEFT))"] <= 0.120956:
                        if features["E(UP) - T(T(up))"] <= 0.070395:
                            if features["E(RIGHT) - time_left"] <= 0.242787:
                                if features["E(LEFT)"] <= 0.001221:
                                    return 3
                                else:
                                    if features["E(LEFT) - agent_column"] <= -0.965489:
                                        if features["E(DOWN) - time_left"] <= -0.206010:
                                            if features["E(LEFT) - T(E(RIGHT))"] <= 0.032825:
                                                if features["T(up) - time_left"] <= -0.687239:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 1
                                        else:
                                            if features["E(LEFT)"] <= 0.028704:
                                                return 3
                                            else:
                                                if features["T(E(UP)) - agent_column"] <= -7.720172:
                                                    return 0
                                                else:
                                                    if features["E(RIGHT) - T(E(UP))"] <= 0.103139:
                                                        if features["T(RIGHT) - agent_column"] <= -3.445826:
                                                            if features["E(UP) - T(up)"] <= -0.023163:
                                                                return 1
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["T(T(RIGHT)) - agent_row"] <= -9.665350:
                                                                return 3
                                                            else:
                                                                return 2
                                                    else:
                                                        return 1
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -8.566965:
                                            return 0
                                        else:
                                            return 3
                            else:
                                if features["E(UP) - E(RIGHT)"] <= -0.000337:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.222051:
                                        if features["E(RIGHT) - agent_column"] <= 0.898022:
                                            return 3
                                        else:
                                            if features["T(E(DOWN)) - agent_row"] <= -1.989650:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        if features["E(DOWN) - time_left"] <= 0.070800:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(DOWN) - E(LEFT)"] <= -0.001601:
                                        return 0
                                    else:
                                        return 3
                        else:
                            if features["T(E(DOWN)) - time_left"] <= -0.043254:
                                if features["E(LEFT)"] <= 0.000140:
                                    if features["E(RIGHT) - T(T(LEFT))"] <= 0.780229:
                                        if features["E(RIGHT)"] <= 0.799750:
                                            if features["E(LEFT) - T(LEFT)"] <= -0.000001:
                                                if features["E(RIGHT) - agent_column"] <= -11.216107:
                                                    return 0
                                                else:
                                                    if features["T(E(LEFT)) - time_left"] <= -0.786229:
                                                        return 0
                                                    else:
                                                        return 3
                                            else:
                                                return 3
                                        else:
                                            if features["T(up) - T(RIGHT)"] <= -0.728480:
                                                return 0
                                            else:
                                                if features["T(E(LEFT)) - T(T(DOWN))"] <= 0.297797:
                                                    if features["E(LEFT) - agent_column"] <= -12.999999:
                                                        return 0
                                                    else:
                                                        if features["agent_row - agent_column"] <= 2.500000:
                                                            return 3
                                                        else:
                                                            if features["agent_row - agent_column"] <= 7.500000:
                                                                if features["E(DOWN) - E(RIGHT)"] <= -0.867804:
                                                                    return 3
                                                                else:
                                                                    if features["E(LEFT)"] <= 0.000002:
                                                                        if features["T(E(DOWN)) - T(E(RIGHT))"] <= -0.664921:
                                                                            return 3
                                                                        else:
                                                                            return 0
                                                                    else:
                                                                        return 3
                                                            else:
                                                                if features["T(T(LEFT)) - agent_column"] <= -1.806866:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                else:
                                                    return 0
                                    else:
                                        if features["E(DOWN) - T(LEFT)"] <= -0.000001:
                                            if features["E(UP) - T(T(LEFT))"] <= 0.854387:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 0
                                else:
                                    if features["E(UP) - E(RIGHT)"] <= -0.053368:
                                        if features["T(DOWN) - time_left"] <= -0.175847:
                                            if features["E(LEFT) - T(DOWN)"] <= 0.015976:
                                                return 3
                                            else:
                                                if features["T(E(UP)) - agent_column"] <= -3.580799:
                                                    if features["T(E(DOWN)) - time_left"] <= -0.218916:
                                                        if features["T(E(RIGHT)) - T(T(RIGHT))"] <= 0.007284:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                        else:
                                            return 3
                                    else:
                                        if features["E(UP) - time_left"] <= 0.198339:
                                            if features["E(RIGHT) - time_left"] <= -0.062027:
                                                if features["E(LEFT)"] <= 0.007387:
                                                    if features["T(RIGHT) - T(T(up))"] <= 0.210291:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    if features["T(DOWN) - T(T(DOWN))"] <= -0.422665:
                                                        return 2
                                                    else:
                                                        return 1
                                            else:
                                                if features["T(up) - T(E(DOWN))"] <= 0.297817:
                                                    if features["T(T(up)) - agent_row"] <= -7.885273:
                                                        if features["T(E(LEFT)) - time_left"] <= -0.278334:
                                                            return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                        else:
                                            if features["E(RIGHT) - T(E(LEFT))"] <= 0.284586:
                                                if features["T(LEFT) - agent_column"] <= -5.936038:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["E(RIGHT) - T(E(DOWN))"] <= 0.332219:
                                                    return 3
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -1.999801:
                                                        if features["T(DOWN) - T(T(LEFT))"] <= 0.135731:
                                                            if features["T(RIGHT) - T(E(RIGHT))"] <= -0.178602:
                                                                if features["agent_row - agent_column"] <= -2.500000:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                            else:
                                                                if features["T(LEFT) - T(T(LEFT))"] <= -0.191438:
                                                                    if features["T(E(UP)) - T(T(RIGHT))"] <= 0.113348:
                                                                        return 3
                                                                    else:
                                                                        if features["T(up) - T(T(RIGHT))"] <= 0.263919:
                                                                            return 0
                                                                        else:
                                                                            return 3
                                                                else:
                                                                    if features["E(DOWN) - T(LEFT)"] <= 0.015096:
                                                                        return 0
                                                                    else:
                                                                        return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        return 3
                            else:
                                if features["E(UP)"] <= 0.664854:
                                    if features["E(RIGHT) - time_left"] <= 0.353160:
                                        if features["T(up) - agent_column"] <= -7.463967:
                                            if features["T(RIGHT) - agent_column"] <= -7.555270:
                                                if features["E(DOWN)"] <= 0.089936:
                                                    return 0
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                        else:
                                            if features["E(RIGHT) - T(E(UP))"] <= 0.037149:
                                                if features["T(DOWN) - T(E(DOWN))"] <= -0.031462:
                                                    return 3
                                                else:
                                                    if features["T(RIGHT) - T(E(UP))"] <= -0.030402:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                return 3
                                    else:
                                        if features["T(LEFT) - T(E(DOWN))"] <= -0.412790:
                                            return 1
                                        else:
                                            if features["E(LEFT) - E(RIGHT)"] <= -0.391248:
                                                if features["T(T(up)) - agent_column"] <= -11.707233:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(DOWN) - agent_column"] <= 0.000115:
                                                    return 3
                                                else:
                                                    return 0
                                else:
                                    if features["E(LEFT)"] <= 0.000100:
                                        if features["E(DOWN) - agent_column"] <= -0.999990:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.816800:
                                                if features["T(T(RIGHT)) - agent_row"] <= -11.693524:
                                                    if features["T(T(RIGHT)) - agent_row"] <= -11.844622:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(DOWN)"] <= 0.000513:
                                                        if features["E(LEFT) - agent_row"] <= -9.999999:
                                                            if features["T(DOWN) - agent_row"] <= -11.999979:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(LEFT) - agent_row"] <= -8.000000:
                                                                if features["E(RIGHT) - agent_row"] <= -8.131950:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                return 3
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -11.215281:
                                                    return 0
                                                else:
                                                    return 3
                                        else:
                                            if features["T(T(DOWN)) - agent_row"] <= -8.787457:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -0.162172:
                                                    return 3
                                                else:
                                                    return 0
                                    else:
                                        if features["E(UP) - agent_column"] <= -11.192327:
                                            return 0
                                        else:
                                            if features["E(DOWN) - agent_row"] <= -1.999635:
                                                if features["T(T(up)) - T(T(RIGHT))"] <= 0.037460:
                                                    return 3
                                                else:
                                                    if features["E(DOWN) - E(LEFT)"] <= -0.002328:
                                                        return 0
                                                    else:
                                                        return 3
                                            else:
                                                return 3
                    else:
                        if features["E(RIGHT) - agent_column"] <= -11.200729:
                            if features["E(DOWN) - T(E(RIGHT))"] <= -0.064525:
                                return 3
                            else:
                                if features["E(RIGHT) - agent_row"] <= -6.168503:
                                    if features["E(DOWN) - agent_row"] <= -12.216045:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    if features["T(T(DOWN)) - agent_row"] <= -6.398274:
                                        return 3
                                    else:
                                        return 1
                        else:
                            if features["T(LEFT) - time_left"] <= -0.119993:
                                if features["E(RIGHT) - agent_row"] <= -11.259744:
                                    if features["E(UP) - agent_column"] <= -10.999998:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.800183:
                                        if features["E(LEFT)"] <= 0.000003:
                                            if features["E(RIGHT) - agent_column"] <= 0.434895:
                                                if features["E(DOWN) - time_left"] <= 0.666992:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["E(RIGHT) - T(E(LEFT))"] <= 0.793120:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            if features["E(DOWN) - T(E(UP))"] <= 0.079213:
                                                if features["E(LEFT)"] <= 0.032090:
                                                    if features["T(T(RIGHT)) - time_left"] <= -0.187904:
                                                        if features["E(RIGHT) - T(DOWN)"] <= 0.535423:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["E(DOWN) - E(LEFT)"] <= 0.399008:
                                                            if features["T(T(RIGHT)) - agent_row"] <= -8.521825:
                                                                if features["E(LEFT) - T(LEFT)"] <= -0.001150:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                            else:
                                                                return 3
                                                        else:
                                                            return 1
                                                else:
                                                    if features["T(E(UP)) - T(T(up))"] <= 0.160555:
                                                        if features["T(E(LEFT)) - agent_row"] <= -10.916331:
                                                            return 3
                                                        else:
                                                            if features["E(UP) - agent_row"] <= -7.859322:
                                                                return 1
                                                            else:
                                                                return 3
                                                    else:
                                                        return 3
                                            else:
                                                if features["T(RIGHT) - time_left"] <= 0.250210:
                                                    if features["E(UP) - agent_row"] <= -10.998689:
                                                        if features["E(DOWN) - agent_row"] <= -10.329314:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(LEFT) - T(LEFT)"] <= -0.000191:
                                                        if features["E(DOWN) - T(T(RIGHT))"] <= 0.073024:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["T(RIGHT) - T(T(up))"] <= 0.127313:
                                                            return 1
                                                        else:
                                                            if features["T(up) - T(T(DOWN))"] <= -0.078880:
                                                                return 3
                                                            else:
                                                                return 1
                                    else:
                                        return 1
                            else:
                                if features["E(DOWN) - E(LEFT)"] <= 0.838722:
                                    if features["E(LEFT) - time_left"] <= 0.045504:
                                        if features["E(RIGHT) - agent_column"] <= 0.431864:
                                            if features["E(LEFT)"] <= 0.024619:
                                                if features["E(UP) - E(LEFT)"] <= -0.000024:
                                                    if features["E(RIGHT) - agent_row"] <= -11.252814:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(RIGHT) - agent_column"] <= -10.223341:
                                                        if features["E(LEFT)"] <= 0.000003:
                                                            return 3
                                                        else:
                                                            if features["E(DOWN) - agent_row"] <= -11.257542:
                                                                return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["T(RIGHT) - T(E(UP))"] <= 0.351986:
                                                            return 3
                                                        else:
                                                            if features["E(RIGHT) - agent_column"] <= -5.494670:
                                                                if features["E(UP) - T(up)"] <= 0.001166:
                                                                    return 3
                                                                else:
                                                                    return 1
                                                            else:
                                                                return 3
                                            else:
                                                if features["E(DOWN) - T(E(RIGHT))"] <= -0.042928:
                                                    if features["T(DOWN) - T(RIGHT)"] <= -0.138271:
                                                        if features["T(DOWN) - T(T(up))"] <= 0.031902:
                                                            if features["T(DOWN) - T(T(DOWN))"] <= -0.025878:
                                                                return 3
                                                            else:
                                                                if features["E(RIGHT) - T(E(UP))"] <= 0.115669:
                                                                    return 3
                                                                else:
                                                                    if features["E(UP) - T(DOWN)"] <= 0.225860:
                                                                        return 1
                                                                    else:
                                                                        return 3
                                                        else:
                                                            return 2
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(up) - T(LEFT)"] <= -0.019242:
                                                        return 3
                                                    else:
                                                        return 1
                                        else:
                                            if features["T(E(RIGHT)) - time_left"] <= 0.406985:
                                                if features["T(up)"] <= 0.001583:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                    else:
                                        if features["T(E(LEFT)) - T(T(RIGHT))"] <= -0.348047:
                                            return 2
                                        else:
                                            if features["E(UP) - T(E(UP))"] <= -0.001288:
                                                return 3
                                            else:
                                                return 1
                                else:
                                    if features["T(LEFT) - agent_row"] <= -12.803212:
                                        return 3
                                    else:
                                        if features["E(UP) - agent_row"] <= -6.999960:
                                            if features["E(UP) - agent_row"] <= -12.999998:
                                                if features["T(DOWN) - agent_column"] <= -10.999998:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 1
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -2.999451:
                                                return 3
                                            else:
                                                return 1
            else:
                if features["T(E(UP)) - T(T(up))"] <= 0.006125:
                    if features["E(DOWN) - T(E(RIGHT))"] <= -0.175549:
                        if features["E(LEFT) - agent_column"] <= -1.922827:
                            if features["E(LEFT) - T(E(UP))"] <= -0.186727:
                                if features["T(E(UP)) - T(E(RIGHT))"] <= -0.012653:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.151716:
                                        if features["T(DOWN) - T(E(UP))"] <= -0.223292:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 1
                                else:
                                    if features["E(RIGHT)"] <= 0.331366:
                                        return 2
                                    else:
                                        return 1
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= -0.193170:
                                    if features["T(up) - T(LEFT)"] <= -0.000015:
                                        return 3
                                    else:
                                        return 2
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -11.603504:
                                        return 3
                                    else:
                                        return 1
                        else:
                            return 2
                    else:
                        if features["E(LEFT) - T(up)"] <= 0.045778:
                            if features["E(RIGHT) - T(DOWN)"] <= 0.224881:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.356693:
                                    return 3
                                else:
                                    return 1
                            else:
                                if features["E(DOWN) - time_left"] <= 0.074591:
                                    if features["T(up) - time_left"] <= 0.395512:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["T(LEFT)"] <= 0.000002:
                                        if features["E(UP) - T(RIGHT)"] <= -0.224838:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 1
                        else:
                            if features["E(UP) - T(RIGHT)"] <= 0.090650:
                                if features["E(RIGHT) - T(E(LEFT))"] <= 0.215331:
                                    return 2
                                else:
                                    return 1
                            else:
                                return 3
                else:
                    if features["T(LEFT)"] <= 0.000005:
                        if features["E(DOWN) - T(E(UP))"] <= -0.032146:
                            if features["E(LEFT) - agent_row"] <= -8.900907:
                                if features["E(LEFT) - agent_column"] <= -2.874078:
                                    if features["E(DOWN) - T(E(LEFT))"] <= 0.106295:
                                        if features["E(LEFT) - T(up)"] <= -0.559395:
                                            return 3
                                        else:
                                            if features["E(UP) - agent_column"] <= -2.696000:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        return 1
                                else:
                                    if features["E(LEFT) - T(E(UP))"] <= -0.290649:
                                        return 0
                                    else:
                                        if features["T(RIGHT) - agent_column"] <= -1.404425:
                                            return 2
                                        else:
                                            return 0
                            else:
                                if features["E(LEFT) - T(RIGHT)"] <= -0.534681:
                                    return 3
                                else:
                                    if features["E(UP) - agent_column"] <= -0.795572:
                                        if features["T(up) - T(RIGHT)"] <= -0.000002:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        return 0
                        else:
                            if features["E(RIGHT) - agent_row"] <= -5.670410:
                                if features["T(up) - T(E(LEFT))"] <= 0.336140:
                                    if features["E(RIGHT) - T(E(LEFT))"] <= 0.217438:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                return 1
                    else:
                        if features["T(DOWN) - T(RIGHT)"] <= -0.000001:
                            if features["E(UP) - E(DOWN)"] <= 0.087249:
                                if features["E(DOWN) - time_left"] <= -0.077107:
                                    return 2
                                else:
                                    if features["E(LEFT) - T(up)"] <= -0.457998:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.120835:
                                            if features["T(LEFT) - agent_column"] <= -5.999412:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["E(LEFT) - agent_column"] <= -8.821633:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        if features["E(LEFT) - agent_column"] <= -1.935815:
                                            return 1
                                        else:
                                            if features["E(LEFT) - agent_column"] <= -1.912362:
                                                return 3
                                            else:
                                                return 1
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.247681:
                                    if features["E(RIGHT) - agent_column"] <= -1.667241:
                                        if features["E(LEFT) - T(RIGHT)"] <= -0.266127:
                                            return 1
                                        else:
                                            if features["T(up) - T(E(LEFT))"] <= 0.239094:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.112412:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    if features["time_left"] <= 0.150000:
                                        if features["E(RIGHT) - T(E(LEFT))"] <= 0.172125:
                                            if features["T(up) - T(E(DOWN))"] <= 0.546847:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["E(LEFT) - T(DOWN)"] <= 0.138191:
                                                if features["T(DOWN) - agent_column"] <= -6.907442:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                    else:
                                        if features["agent_column - time_left"] <= 7.790000:
                                            if features["T(DOWN) - time_left"] <= -0.199923:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 1
                        else:
                            if features["E(LEFT) - agent_row"] <= -6.840897:
                                if features["T(DOWN) - T(E(LEFT))"] <= -0.026161:
                                    if features["T(T(RIGHT)) - agent_row"] <= -7.984571:
                                        return 3
                                    else:
                                        if features["E(RIGHT) - T(T(up))"] <= 0.208849:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["T(E(LEFT)) - T(E(RIGHT))"] <= -0.256061:
                                        return 3
                                    else:
                                        return 0
                            else:
                                if features["E(RIGHT) - time_left"] <= 0.285080:
                                    if features["E(DOWN) - T(DOWN)"] <= -0.066949:
                                        if features["E(LEFT) - time_left"] <= 0.207859:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 1
                                else:
                                    return 3
        else:
            if features["E(LEFT) - T(E(RIGHT))"] <= 0.139961:
                if features["E(DOWN) - agent_row"] <= -12.128042:
                    if features["E(RIGHT) - T(up)"] <= 0.005215:
                        return 1
                    else:
                        if features["T(RIGHT) - T(E(UP))"] <= 0.546075:
                            if features["E(LEFT) - agent_column"] <= -10.999984:
                                if features["T(up) - agent_column"] <= -10.664907:
                                    return 3
                                else:
                                    return 1
                            else:
                                return 3
                        else:
                            return 1
                else:
                    if features["E(UP) - T(LEFT)"] <= 0.077781:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.208641:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.331429:
                                if features["E(LEFT) - T(LEFT)"] <= 0.023470:
                                    if features["T(T(up)) - time_left"] <= -0.674509:
                                        return 3
                                    else:
                                        if features["E(DOWN) - T(E(UP))"] <= -0.038178:
                                            return 3
                                        else:
                                            if features["T(LEFT) - time_left"] <= -0.949570:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - T(T(DOWN))"] <= 0.107054:
                                                    return 1
                                                else:
                                                    if features["T(RIGHT) - T(E(RIGHT))"] <= 0.014257:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - T(T(RIGHT))"] <= 0.052397:
                                                            if features["E(UP) - E(LEFT)"] <= -0.028569:
                                                                return 2
                                                            else:
                                                                if features["E(UP)"] <= 0.030308:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                        else:
                                                            return 1
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.023977:
                                        return 2
                                    else:
                                        if features["T(E(DOWN)) - time_left"] <= -0.019849:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.215649:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["agent_row - agent_column"] <= -5.500000:
                                                if features["E(RIGHT) - T(T(DOWN))"] <= 0.104387:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["E(UP) - T(up)"] <= 0.047356:
                                                    if features["E(LEFT) - E(RIGHT)"] <= -0.283153:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                            else:
                                if features["E(UP)"] <= 0.000016:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.000010:
                                        if features["E(UP) - E(DOWN)"] <= -0.832830:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        if features["T(DOWN) - time_left"] <= -0.689922:
                                            return 2
                                        else:
                                            if features["agent_row - agent_column"] <= -7.500000:
                                                return 3
                                            else:
                                                return 1
                                else:
                                    if features["T(DOWN) - agent_column"] <= -0.614062:
                                        if features["E(DOWN) - agent_row"] <= -11.351963:
                                            return 3
                                        else:
                                            if features["E(DOWN) - T(E(LEFT))"] <= 0.341893:
                                                return 1
                                            else:
                                                if features["T(LEFT)"] <= 0.000004:
                                                    if features["T(RIGHT) - T(T(DOWN))"] <= 0.423364:
                                                        if features["E(UP)"] <= 0.006736:
                                                            return 1
                                                        else:
                                                            if features["E(UP) - T(DOWN)"] <= 0.041949:
                                                                return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                                    else:
                                        if features["T(DOWN) - T(RIGHT)"] <= -0.000135:
                                            return 1
                                        else:
                                            return 3
                        else:
                            if features["T(E(RIGHT)) - agent_row"] <= -2.678298:
                                if features["E(UP)"] <= 0.000012:
                                    if features["E(DOWN) - agent_row"] <= -11.202065:
                                        if features["T(up) - T(RIGHT)"] <= 0.002415:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -5.229429:
                                            return 1
                                        else:
                                            if features["E(DOWN)"] <= 0.749126:
                                                return 1
                                            else:
                                                if features["T(RIGHT) - time_left"] <= 0.193058:
                                                    if features["E(RIGHT) - agent_column"] <= -0.132062:
                                                        if features["T(E(RIGHT)) - agent_column"] <= -11.528615:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 1
                                                else:
                                                    if features["T(E(LEFT)) - T(E(RIGHT))"] <= -0.189176:
                                                        return 1
                                                    else:
                                                        return 3
                                else:
                                    if features["E(DOWN) - E(RIGHT)"] <= 0.091998:
                                        if features["E(UP) - agent_column"] <= -11.984856:
                                            return 1
                                        else:
                                            if features["T(E(UP))"] <= 0.390011:
                                                if features["E(LEFT) - time_left"] <= 0.142200:
                                                    if features["T(E(LEFT)) - agent_column"] <= -1.932758:
                                                        if features["E(DOWN) - agent_row"] <= -11.226230:
                                                            return 3
                                                        else:
                                                            if features["E(UP) - E(LEFT)"] <= 0.000004:
                                                                if features["E(UP) - T(up)"] <= 0.000028:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                            else:
                                                                if features["T(RIGHT) - time_left"] <= -0.119883:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                    else:
                                                        return 1
                                                else:
                                                    if features["T(RIGHT) - agent_row"] <= -9.999984:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                return 3
                                    else:
                                        if features["T(RIGHT) - T(E(UP))"] <= -0.341481:
                                            return 3
                                        else:
                                            return 1
                            else:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.297040:
                                    if features["T(E(DOWN)) - T(E(RIGHT))"] <= 0.056020:
                                        if features["T(RIGHT) - agent_column"] <= -4.999975:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.627989:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        return 1
                                else:
                                    if features["T(T(DOWN)) - agent_column"] <= -0.892347:
                                        if features["E(DOWN) - agent_column"] <= -11.197094:
                                            return 1
                                        else:
                                            if features["T(DOWN) - T(E(UP))"] <= 0.510845:
                                                if features["E(DOWN) - agent_row"] <= -0.280273:
                                                    if features["T(RIGHT) - T(E(UP))"] <= -0.064289:
                                                        return 3
                                                    else:
                                                        if features["E(UP) - E(DOWN)"] <= -0.867687:
                                                            return 3
                                                        else:
                                                            return 1
                                                else:
                                                    return 3
                                            else:
                                                return 1
                                    else:
                                        if features["T(T(RIGHT)) - time_left"] <= -0.055104:
                                            return 3
                                        else:
                                            return 1
                    else:
                        if features["T(up) - T(RIGHT)"] <= 0.000038:
                            if features["T(E(DOWN)) - T(T(RIGHT))"] <= -0.105026:
                                if features["T(RIGHT) - T(T(up))"] <= -0.025095:
                                    return 1
                                else:
                                    if features["E(LEFT)"] <= 0.154247:
                                        return 1
                                    else:
                                        return 2
                            else:
                                if features["T(up) - T(E(UP))"] <= -0.210272:
                                    if features["E(RIGHT) - time_left"] <= 0.231684:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.254633:
                                        if features["T(DOWN) - T(E(RIGHT))"] <= 0.046236:
                                            if features["T(up) - agent_row"] <= -5.998917:
                                                if features["T(E(UP)) - T(T(up))"] <= 0.030645:
                                                    if features["T(RIGHT) - T(E(LEFT))"] <= 0.185667:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                        else:
                                            if features["T(DOWN) - T(E(RIGHT))"] <= 0.398517:
                                                if features["E(UP) - E(RIGHT)"] <= -0.174240:
                                                    return 1
                                                else:
                                                    if features["T(E(LEFT)) - agent_row"] <= -8.981891:
                                                        return 1
                                                    else:
                                                        return 2
                                            else:
                                                return 1
                                    else:
                                        if features["T(E(LEFT)) - agent_column"] <= -4.962767:
                                            return 0
                                        else:
                                            if features["T(DOWN) - T(E(UP))"] <= 0.568209:
                                                return 3
                                            else:
                                                return 1
                        else:
                            if features["T(E(LEFT)) - agent_column"] <= -8.945071:
                                if features["T(up) - T(E(UP))"] <= 0.110004:
                                    return 0
                                else:
                                    return 2
                            else:
                                if features["E(RIGHT) - time_left"] <= 0.279491:
                                    if features["T(up) - agent_row"] <= -11.650702:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 1
            else:
                if features["T(up) - agent_row"] <= -12.329738:
                    if features["T(LEFT) - agent_column"] <= -0.999996:
                        if features["E(LEFT) - time_left"] <= 0.168827:
                            return 1
                        else:
                            return 2
                    else:
                        return 1
                else:
                    if features["agent_row - agent_column"] <= -6.500000:
                        if features["E(DOWN) - time_left"] <= 0.365213:
                            if features["T(DOWN) - T(T(LEFT))"] <= 0.031582:
                                if features["E(LEFT) - T(LEFT)"] <= 0.320486:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.002719:
                                        return 1
                                    else:
                                        if features["agent_row - agent_column"] <= -8.500000:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    return 2
                            else:
                                if features["T(E(RIGHT)) - agent_column"] <= -8.968766:
                                    if features["E(DOWN) - T(E(DOWN))"] <= 0.056901:
                                        if features["E(LEFT) - time_left"] <= 0.256696:
                                            if features["E(UP) - agent_row"] <= -0.999676:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["E(RIGHT) - T(up)"] <= -0.001974:
                                                return 1
                                            else:
                                                if features["E(DOWN) - T(RIGHT)"] <= 0.425093:
                                                    return 2
                                                else:
                                                    return 1
                                    else:
                                        if features["T(up)"] <= 0.000003:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    if features["T(LEFT) - T(E(LEFT))"] <= 0.009581:
                                        if features["T(T(RIGHT)) - agent_row"] <= -1.931973:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - T(T(up))"] <= 0.074541:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= -0.002580:
                                            return 1
                                        else:
                                            if features["E(LEFT) - time_left"] <= 0.274587:
                                                return 1
                                            else:
                                                return 2
                        else:
                            if features["E(UP) - T(LEFT)"] <= -0.290360:
                                if features["E(LEFT) - T(T(DOWN))"] <= -0.028052:
                                    return 1
                                else:
                                    if features["E(UP) - agent_row"] <= -1.997913:
                                        if features["E(LEFT) - T(E(DOWN))"] <= 0.449306:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["T(E(DOWN))"] <= 0.374154:
                                            return 2
                                        else:
                                            return 1
                            else:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.004429:
                                    if features["T(LEFT) - T(E(DOWN))"] <= -0.068654:
                                        return 2
                                    else:
                                        return 3
                                else:
                                    if features["T(LEFT) - agent_column"] <= -8.999790:
                                        return 2
                                    else:
                                        return 1
                    else:
                        if features["E(UP) - T(LEFT)"] <= 0.000054:
                            if features["T(up) - agent_row"] <= -11.327065:
                                if features["E(LEFT) - agent_row"] <= -11.156870:
                                    if features["E(LEFT) - agent_row"] <= -11.206534:
                                        if features["E(LEFT) - T(up)"] <= 0.139088:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 1
                                else:
                                    return 2
                            else:
                                if features["E(UP) - T(E(UP))"] <= 0.076638:
                                    if features["E(DOWN)"] <= 0.167344:
                                        return 2
                                    else:
                                        if features["T(up) - time_left"] <= -0.159988:
                                            if features["T(RIGHT) - time_left"] <= -0.689999:
                                                return 0
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - E(LEFT)"] <= -0.000065:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - time_left"] <= -0.060131:
                                                    if features["E(UP)"] <= 0.000053:
                                                        return 1
                                                    else:
                                                        if features["T(up) - agent_column"] <= -8.994796:
                                                            if features["E(UP) - agent_column"] <= -11.999591:
                                                                return 1
                                                            else:
                                                                if features["T(RIGHT) - T(E(DOWN))"] <= -0.345586:
                                                                    return 1
                                                                else:
                                                                    return 2
                                                        else:
                                                            return 1
                                                else:
                                                    return 1
                                else:
                                    return 2
                        else:
                            if features["T(up) - agent_row"] <= -6.999994:
                                if features["E(RIGHT) - agent_column"] <= -1.888730:
                                    if features["T(up) - T(RIGHT)"] <= 0.002005:
                                        if features["E(RIGHT) - agent_row"] <= -11.994367:
                                            return 2
                                        else:
                                            if features["E(DOWN) - time_left"] <= 0.300614:
                                                if features["E(LEFT) - time_left"] <= 0.075770:
                                                    if features["T(DOWN) - T(E(LEFT))"] <= -0.420258:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 2
                                            else:
                                                return 2
                                    else:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.091734:
                                            if features["E(RIGHT) - T(E(UP))"] <= -0.011059:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 1
                                else:
                                    return 1
                            else:
                                if features["E(LEFT) - time_left"] <= 0.294300:
                                    if features["E(UP) - T(up)"] <= 0.048899:
                                        if features["E(RIGHT) - agent_column"] <= -9.902564:
                                            return 2
                                        else:
                                            if features["E(DOWN) - T(T(RIGHT))"] <= -0.252772:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        if features["T(DOWN) - time_left"] <= 0.325490:
                                            return 1
                                        else:
                                            if features["T(DOWN) - T(E(LEFT))"] <= 0.228315:
                                                if features["T(LEFT) - T(E(UP))"] <= -0.004729:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                else:
                                    if features["E(LEFT) - agent_row"] <= -5.268929:
                                        return 1
                                    else:
                                        if features["E(DOWN) - E(LEFT)"] <= 0.001739:
                                            return 2
                                        else:
                                            return 1
    else:
        if features["E(UP) - E(LEFT)"] <= -0.000009:
            if features["E(DOWN) - E(LEFT)"] <= -0.151107:
                if features["E(UP)"] <= 0.662760:
                    if features["E(RIGHT) - T(DOWN)"] <= 0.000175:
                        if features["E(LEFT) - time_left"] <= 0.144287:
                            if features["T(LEFT) - agent_column"] <= -13.639629:
                                return 0
                            else:
                                if features["E(DOWN) - T(E(UP))"] <= 0.105753:
                                    if features["T(T(LEFT)) - time_left"] <= -0.753925:
                                        if features["T(DOWN) - T(RIGHT)"] <= 0.000503:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["T(E(DOWN)) - T(T(LEFT))"] <= -0.449663:
                                            return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(RIGHT) - time_left"] <= -0.411459:
                                        return 1
                                    else:
                                        return 2
                        else:
                            if features["E(RIGHT) - T(up)"] <= 0.000118:
                                if features["E(UP) - agent_column"] <= -0.458824:
                                    if features["E(DOWN) - T(E(LEFT))"] <= -0.075655:
                                        if features["T(up) - agent_column"] <= -13.980393:
                                            if features["T(up) - agent_column"] <= -13.995390:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                                    else:
                                        if features["E(LEFT) - T(E(DOWN))"] <= 0.141646:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    return 0
                            else:
                                if features["E(UP) - time_left"] <= 0.260748:
                                    return 2
                                else:
                                    if features["T(up) - time_left"] <= -0.006273:
                                        return 2
                                    else:
                                        return 0
                    else:
                        if features["T(DOWN) - time_left"] <= -0.119985:
                            if features["E(DOWN) - T(T(DOWN))"] <= 0.053572:
                                if features["E(DOWN) - T(T(LEFT))"] <= -0.361166:
                                    if features["E(RIGHT) - T(up)"] <= -0.315116:
                                        if features["E(UP) - E(LEFT)"] <= -0.006099:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["T(E(RIGHT)) - T(T(DOWN))"] <= -0.259086:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    if features["E(UP) - E(RIGHT)"] <= 0.351356:
                                        if features["T(up) - T(RIGHT)"] <= -0.000348:
                                            if features["E(UP) - T(E(RIGHT))"] <= 0.236054:
                                                return 2
                                            else:
                                                if features["E(DOWN) - agent_row"] <= -8.851324:
                                                    return 0
                                                else:
                                                    return 2
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -8.559210:
                                                return 2
                                            else:
                                                if features["E(RIGHT) - T(E(UP))"] <= -0.291424:
                                                    return 2
                                                else:
                                                    if features["E(DOWN) - E(LEFT)"] <= -0.196019:
                                                        if features["E(LEFT) - T(E(UP))"] <= 0.403879:
                                                            if features["T(LEFT) - T(T(up))"] <= -0.326760:
                                                                return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        return 1
                                    else:
                                        if features["E(LEFT) - time_left"] <= -0.106475:
                                            if features["E(DOWN)"] <= 0.016189:
                                                return 0
                                            else:
                                                return 1
                                        else:
                                            if features["T(LEFT) - time_left"] <= -0.411694:
                                                return 2
                                            else:
                                                if features["agent_row - agent_column"] <= 4.500000:
                                                    if features["E(DOWN) - E(RIGHT)"] <= -0.001199:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                            else:
                                if features["T(up) - T(LEFT)"] <= 0.005885:
                                    return 2
                                else:
                                    if features["E(RIGHT) - T(DOWN)"] <= 0.007987:
                                        return 2
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= 0.000927:
                                            return 2
                                        else:
                                            return 1
                        else:
                            if features["T(E(UP)) - T(E(RIGHT))"] <= 0.135671:
                                if features["E(DOWN) - agent_column"] <= -8.809744:
                                    return 2
                                else:
                                    if features["T(RIGHT) - time_left"] <= 0.485653:
                                        if features["T(DOWN)"] <= 0.000001:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(UP) - agent_row"] <= -5.775845:
                                            return 2
                                        else:
                                            return 1
                            else:
                                if features["T(up) - T(T(LEFT))"] <= 0.038865:
                                    if features["E(LEFT) - agent_row"] <= -9.659523:
                                        if features["E(LEFT) - T(T(up))"] <= 0.172773:
                                            return 3
                                        else:
                                            if features["E(DOWN) - T(up)"] <= 0.098757:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(E(LEFT)) - agent_column"] <= -12.651834:
                                        return 0
                                    else:
                                        return 2
                else:
                    if features["E(RIGHT) - agent_column"] <= -1.999893:
                        if features["E(RIGHT)"] <= 0.000056:
                            if features["E(LEFT)"] <= 0.806438:
                                if features["E(RIGHT) - agent_column"] <= -2.999998:
                                    return 2
                                else:
                                    if features["T(DOWN) - agent_row"] <= -5.328608:
                                        return 2
                                    else:
                                        if features["T(E(UP)) - agent_row"] <= -3.332271:
                                            return 0
                                        else:
                                            return 2
                            else:
                                if features["agent_row - agent_column"] <= 8.500000:
                                    if features["agent_row - agent_column"] <= -2.500000:
                                        if features["E(DOWN)"] <= 0.000057:
                                            if features["T(E(LEFT)) - agent_row"] <= -4.644675:
                                                if features["E(LEFT) - agent_row"] <= -7.134309:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["T(T(LEFT)) - agent_column"] <= -13.470341:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["T(up) - agent_row"] <= -2.930170:
                                                return 0
                                            else:
                                                return 2
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -1.952312:
                                            if features["T(up) - T(E(LEFT))"] <= -0.366185:
                                                return 2
                                            else:
                                                if features["T(T(up)) - agent_column"] <= -13.639747:
                                                    return 0
                                                else:
                                                    return 2
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= 0.542541:
                                                return 0
                                            else:
                                                return 2
                                else:
                                    return 0
                        else:
                            if features["E(DOWN) - agent_row"] <= -11.999979:
                                return 0
                            else:
                                if features["E(DOWN) - E(LEFT)"] <= -0.752718:
                                    return 2
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.000369:
                                        if features["T(E(DOWN)) - time_left"] <= -0.814798:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 2
                    else:
                        if features["T(RIGHT) - agent_column"] <= -0.993281:
                            if features["E(LEFT) - T(T(up))"] <= 0.684204:
                                if features["E(UP) - E(LEFT)"] <= -0.049707:
                                    return 2
                                else:
                                    if features["T(LEFT) - T(E(LEFT))"] <= -0.774382:
                                        return 2
                                    else:
                                        return 0
                            else:
                                return 0
                        else:
                            return 0
            else:
                if features["E(DOWN) - E(LEFT)"] <= 0.000006:
                    if features["E(RIGHT)"] <= 0.000130:
                        if features["E(LEFT)"] <= 0.819603:
                            if features["T(E(DOWN)) - agent_column"] <= -13.779222:
                                if features["T(E(UP)) - time_left"] <= -0.464703:
                                    return 1
                                else:
                                    return 2
                            else:
                                if features["E(RIGHT)"] <= 0.000028:
                                    if features["T(RIGHT) - T(E(LEFT))"] <= -0.663667:
                                        return 2
                                    else:
                                        if features["T(RIGHT) - time_left"] <= -0.795201:
                                            if features["T(E(DOWN)) - T(T(DOWN))"] <= 0.133916:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(LEFT) - T(E(UP))"] <= 0.507734:
                                                if features["time_left"] <= 0.970000:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["E(LEFT) - agent_column"] <= -1.200289:
                                                    if features["T(T(DOWN)) - agent_column"] <= -13.734083:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    return 2
                                else:
                                    if features["T(up) - agent_column"] <= -0.810613:
                                        if features["T(E(UP)) - time_left"] <= -0.497861:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 1
                        else:
                            if features["E(RIGHT) - agent_column"] <= -1.999952:
                                if features["agent_row - agent_column"] <= -0.500000:
                                    return 1
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -11.999973:
                                        return 2
                                    else:
                                        if features["T(E(DOWN)) - agent_column"] <= -4.143435:
                                            if features["E(UP) - agent_column"] <= -7.999999:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(UP) - agent_row"] <= -10.999998:
                                                return 1
                                            else:
                                                return 2
                            else:
                                return 1
                    else:
                        if features["E(LEFT) - T(T(LEFT))"] <= 0.029333:
                            if features["T(E(DOWN)) - T(T(LEFT))"] <= -0.088695:
                                if features["E(UP) - time_left"] <= 0.210684:
                                    if features["T(RIGHT)"] <= 0.000027:
                                        if features["E(DOWN) - T(E(RIGHT))"] <= 0.145529:
                                            if features["T(up) - agent_row"] <= -8.476484:
                                                if features["E(UP) - T(LEFT)"] <= -0.109527:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.351972:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            if features["T(T(DOWN)) - T(T(RIGHT))"] <= -0.053605:
                                                return 1
                                            else:
                                                return 2
                                    else:
                                        if features["E(LEFT) - T(T(up))"] <= 0.236210:
                                            if features["E(RIGHT) - T(E(UP))"] <= -0.137197:
                                                if features["T(DOWN)"] <= 0.000447:
                                                    if features["E(RIGHT) - T(up)"] <= -0.454317:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["T(up) - T(E(RIGHT))"] <= 0.049051:
                                                    return 2
                                                else:
                                                    if features["E(RIGHT) - agent_row"] <= -11.798869:
                                                        return 2
                                                    else:
                                                        return 1
                                        else:
                                            return 2
                                else:
                                    if features["E(RIGHT) - T(E(LEFT))"] <= -0.124918:
                                        return 2
                                    else:
                                        if features["E(UP) - time_left"] <= 0.286688:
                                            return 1
                                        else:
                                            return 0
                            else:
                                if features["T(E(DOWN)) - T(T(up))"] <= 0.249933:
                                    if features["E(UP) - T(E(RIGHT))"] <= 0.117102:
                                        if features["T(DOWN) - time_left"] <= 0.337427:
                                            if features["T(E(LEFT)) - agent_column"] <= -6.670467:
                                                if features["E(DOWN) - agent_column"] <= -12.708410:
                                                    return 2
                                                else:
                                                    if features["E(LEFT) - T(T(DOWN))"] <= 0.109598:
                                                        return 1
                                                    else:
                                                        if features["E(DOWN) - T(T(DOWN))"] <= 0.039588:
                                                            if features["T(E(DOWN)) - T(T(LEFT))"] <= -0.061033:
                                                                return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(DOWN) - T(LEFT)"] <= -0.006334:
                                                return 3
                                            else:
                                                if features["T(E(DOWN)) - time_left"] <= 0.332789:
                                                    return 2
                                                else:
                                                    return 1
                                    else:
                                        if features["T(DOWN) - T(T(up))"] <= -0.098575:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    if features["T(E(LEFT)) - T(T(RIGHT))"] <= 0.179530:
                                        return 1
                                    else:
                                        return 2
                        else:
                            if features["T(up) - T(RIGHT)"] <= 0.000011:
                                if features["T(E(UP)) - time_left"] <= 0.031302:
                                    if features["T(up) - T(RIGHT)"] <= -0.005084:
                                        return 1
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -1.999947:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    return 2
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.105034:
                                    if features["T(E(DOWN)) - T(T(DOWN))"] <= 0.002465:
                                        if features["T(RIGHT) - T(E(UP))"] <= -0.150489:
                                            if features["T(E(UP)) - T(E(LEFT))"] <= -0.204284:
                                                return 1
                                            else:
                                                if features["E(LEFT) - T(E(RIGHT))"] <= 0.399045:
                                                    if features["T(E(DOWN)) - agent_column"] <= -9.797835:
                                                        return 2
                                                    else:
                                                        if features["T(T(up)) - agent_column"] <= -5.901440:
                                                            return 1
                                                        else:
                                                            return 2
                                                else:
                                                    if features["T(T(up)) - agent_column"] <= -9.568645:
                                                        if features["T(T(up)) - agent_row"] <= -5.922869:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -6.780006:
                                                return 2
                                            else:
                                                if features["T(RIGHT) - agent_column"] <= -6.300555:
                                                    return 1
                                                else:
                                                    return 2
                                    else:
                                        if features["T(T(LEFT)) - time_left"] <= 0.217195:
                                            if features["T(LEFT) - agent_column"] <= -9.514722:
                                                if features["T(LEFT) - T(RIGHT)"] <= 0.411301:
                                                    return 2
                                                else:
                                                    if features["E(RIGHT) - T(LEFT)"] <= -0.693406:
                                                        return 2
                                                    else:
                                                        if features["T(E(RIGHT)) - T(T(RIGHT))"] <= -0.163787:
                                                            return 2
                                                        else:
                                                            if features["E(RIGHT) - T(E(UP))"] <= -0.215397:
                                                                return 2
                                                            else:
                                                                return 1
                                            else:
                                                if features["T(DOWN) - agent_column"] <= -7.788356:
                                                    if features["T(LEFT) - T(T(LEFT))"] <= 0.080376:
                                                        return 1
                                                    else:
                                                        if features["T(LEFT) - T(T(LEFT))"] <= 0.095929:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    if features["T(DOWN) - agent_column"] <= -7.514635:
                                                        return 2
                                                    else:
                                                        if features["E(RIGHT) - T(LEFT)"] <= -0.477905:
                                                            return 1
                                                        else:
                                                            if features["E(LEFT) - T(up)"] <= 0.132906:
                                                                if features["T(T(LEFT)) - agent_column"] <= -6.744643:
                                                                    return 1
                                                                else:
                                                                    return 2
                                                            else:
                                                                return 2
                                        else:
                                            if features["E(RIGHT) - T(E(UP))"] <= -0.128936:
                                                if features["T(E(LEFT)) - time_left"] <= 0.301030:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["E(LEFT)"] <= 0.429674:
                                                    if features["T(LEFT) - T(E(DOWN))"] <= 0.027066:
                                                        return 3
                                                    else:
                                                        if features["E(DOWN) - T(E(LEFT))"] <= -0.129211:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    if features["T(T(LEFT)) - agent_column"] <= -11.643058:
                                                        return 3
                                                    else:
                                                        return 2
                                else:
                                    if features["E(DOWN) - agent_column"] <= -8.736138:
                                        if features["T(up) - T(LEFT)"] <= 0.548660:
                                            if features["T(LEFT) - T(E(DOWN))"] <= 0.513755:
                                                if features["T(up) - T(E(UP))"] <= -0.296949:
                                                    if features["T(DOWN) - T(LEFT)"] <= -0.494776:
                                                        if features["E(LEFT) - agent_row"] <= -7.629695:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 2
                                                else:
                                                    if features["T(E(RIGHT))"] <= 0.100643:
                                                        if features["E(DOWN) - agent_column"] <= -9.740573:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["T(RIGHT) - agent_row"] <= -8.999998:
                                                            if features["T(up) - T(LEFT)"] <= 0.000026:
                                                                return 3
                                                            else:
                                                                return 1
                                                        else:
                                                            return 1
                                            else:
                                                if features["E(DOWN) - agent_column"] <= -9.750466:
                                                    return 2
                                                else:
                                                    if features["T(T(LEFT)) - agent_row"] <= -8.911872:
                                                        if features["T(E(LEFT))"] <= 0.277648:
                                                            return 3
                                                        else:
                                                            return 2
                                                    else:
                                                        return 1
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -8.786712:
                                                if features["T(RIGHT) - agent_row"] <= -4.936757:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["T(RIGHT) - T(E(RIGHT))"] <= -0.038933:
                                                    return 1
                                                else:
                                                    return 2
                                    else:
                                        if features["E(DOWN) - T(E(UP))"] <= -0.150376:
                                            if features["E(RIGHT) - T(E(LEFT))"] <= -0.110037:
                                                return 1
                                            else:
                                                if features["T(RIGHT)"] <= 0.000013:
                                                    return 3
                                                else:
                                                    if features["E(UP) - T(RIGHT)"] <= -0.357326:
                                                        return 2
                                                    else:
                                                        if features["E(UP) - T(up)"] <= -0.176902:
                                                            return 1
                                                        else:
                                                            return 3
                                        else:
                                            if features["T(RIGHT)"] <= 0.000008:
                                                if features["T(E(UP)) - T(E(LEFT))"] <= 0.035091:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 1
                else:
                    if features["E(DOWN) - agent_row"] <= -12.123451:
                        return 2
                    else:
                        if features["E(RIGHT) - T(T(up))"] <= -0.000046:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.861534:
                                if features["E(UP) - T(LEFT)"] <= 0.000028:
                                    if features["E(RIGHT) - T(up)"] <= 0.000354:
                                        return 1
                                    else:
                                        if features["T(E(UP)) - agent_column"] <= -9.969525:
                                            if features["E(LEFT) - T(T(DOWN))"] <= 0.014361:
                                                return 3
                                            else:
                                                return 2
                                        else:
                                            return 1
                                else:
                                    if features["T(LEFT) - agent_column"] <= -1.999929:
                                        return 2
                                    else:
                                        return 1
                            else:
                                if features["T(E(UP)) - agent_column"] <= -0.999538:
                                    if features["T(DOWN) - agent_column"] <= -4.417139:
                                        if features["T(up) - agent_column"] <= -5.998277:
                                            if features["T(up) - agent_row"] <= -11.277675:
                                                return 2
                                            else:
                                                if features["T(DOWN) - T(LEFT)"] <= 0.482254:
                                                    return 1
                                                else:
                                                    return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -3.132363:
                                            return 2
                                        else:
                                            if features["E(RIGHT)"] <= 0.000003:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    return 1
                        else:
                            if features["T(RIGHT) - T(E(DOWN))"] <= -0.357813:
                                return 1
                            else:
                                if features["E(LEFT) - T(E(DOWN))"] <= -0.013786:
                                    return 1
                                else:
                                    return 2
        else:
            if features["E(UP) - E(DOWN)"] <= 0.385064:
                if features["E(RIGHT) - T(T(RIGHT))"] <= 0.007249:
                    if features["E(DOWN)"] <= 0.003386:
                        if features["T(T(DOWN)) - time_left"] <= -0.000313:
                            if features["T(RIGHT) - agent_row"] <= -12.996086:
                                if features["E(UP) - E(RIGHT)"] <= 0.368104:
                                    if features["E(RIGHT) - T(DOWN)"] <= 0.028189:
                                        if features["T(E(RIGHT)) - time_left"] <= -0.537598:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -3.668347:
                                            if features["T(E(LEFT)) - T(T(LEFT))"] <= 0.005096:
                                                if features["E(UP) - T(E(UP))"] <= 0.044546:
                                                    return 2
                                                else:
                                                    return 3
                                            else:
                                                if features["T(up) - agent_column"] <= -5.665323:
                                                    return 2
                                                else:
                                                    if features["E(RIGHT) - T(up)"] <= -0.239497:
                                                        return 0
                                                    else:
                                                        return 2
                                        else:
                                            if features["T(E(RIGHT)) - agent_row"] <= -13.981053:
                                                return 3
                                            else:
                                                return 0
                                else:
                                    return 2
                            else:
                                if features["E(DOWN)"] <= 0.000104:
                                    return 0
                                else:
                                    if features["E(LEFT) - T(T(up))"] <= 0.071970:
                                        if features["T(DOWN)"] <= 0.001059:
                                            if features["T(T(DOWN)) - time_left"] <= -0.387077:
                                                return 2
                                            else:
                                                if features["T(RIGHT)"] <= 0.000201:
                                                    return 0
                                                else:
                                                    if features["E(DOWN) - E(RIGHT)"] <= -0.073853:
                                                        return 0
                                                    else:
                                                        return 2
                                        else:
                                            return 0
                                    else:
                                        return 2
                        else:
                            if features["E(DOWN) - T(DOWN)"] <= 0.000425:
                                if features["T(RIGHT)"] <= 0.000398:
                                    if features["E(UP) - T(E(LEFT))"] <= -0.044465:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 0
                            else:
                                if features["T(RIGHT) - T(T(LEFT))"] <= -0.165141:
                                    return 0
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= 0.103081:
                                        return 2
                                    else:
                                        return 0
                    else:
                        if features["E(LEFT) - T(T(up))"] <= -0.051433:
                            if features["T(T(LEFT)) - time_left"] <= 0.163545:
                                if features["T(T(DOWN)) - time_left"] <= 0.065294:
                                    if features["E(RIGHT) - time_left"] <= 0.294781:
                                        if features["E(DOWN) - T(E(UP))"] <= -0.297577:
                                            if features["T(E(DOWN)) - time_left"] <= -0.030486:
                                                if features["T(E(LEFT)) - T(T(up))"] <= -0.345722:
                                                    return 3
                                                else:
                                                    if features["T(up) - agent_row"] <= -12.549830:
                                                        if features["E(LEFT) - T(LEFT)"] <= 0.020730:
                                                            if features["T(RIGHT) - T(E(RIGHT))"] <= -0.073005:
                                                                return 3
                                                            else:
                                                                return 2
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["T(T(DOWN)) - agent_column"] <= -1.769083:
                                                            if features["T(E(DOWN)) - time_left"] <= -0.319344:
                                                                if features["T(LEFT) - T(E(UP))"] <= -0.127709:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                            else:
                                                                if features["T(DOWN)"] <= 0.000258:
                                                                    if features["T(LEFT) - agent_column"] <= -3.549381:
                                                                        return 2
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    return 2
                                                        else:
                                                            return 0
                                            else:
                                                return 0
                                        else:
                                            if features["T(E(UP)) - T(E(LEFT))"] <= 0.175061:
                                                if features["T(LEFT) - agent_row"] <= -12.573802:
                                                    return 2
                                                else:
                                                    if features["T(T(DOWN)) - agent_row"] <= -10.851623:
                                                        if features["E(DOWN) - T(E(LEFT))"] <= -0.191663:
                                                            return 1
                                                        else:
                                                            if features["T(DOWN) - T(RIGHT)"] <= -0.000024:
                                                                return 1
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["E(UP) - E(RIGHT)"] <= 0.030743:
                                                            return 1
                                                        else:
                                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.155403:
                                                                return 2
                                                            else:
                                                                return 1
                                            else:
                                                if features["E(RIGHT) - T(DOWN)"] <= 0.092375:
                                                    return 2
                                                else:
                                                    if features["T(E(LEFT)) - agent_column"] <= -1.957542:
                                                        return 3
                                                    else:
                                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(UP) - T(up)"] <= -0.023624:
                                        if features["T(DOWN) - T(T(DOWN))"] <= -0.047234:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.236742:
                                                if features["T(RIGHT) - agent_column"] <= -1.468823:
                                                    if features["T(DOWN)"] <= 0.000107:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                                            else:
                                                return 3
                                        else:
                                            return 1
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -4.855107:
                                            if features["E(UP) - time_left"] <= 0.341924:
                                                if features["T(E(UP)) - agent_column"] <= -5.717188:
                                                    return 3
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(UP) - E(RIGHT)"] <= 0.006373:
                                                return 1
                                            else:
                                                if features["T(T(up)) - T(T(RIGHT))"] <= -0.183854:
                                                    return 0
                                                else:
                                                    if features["T(E(RIGHT)) - agent_row"] <= -11.691475:
                                                        return 3
                                                    else:
                                                        return 2
                            else:
                                if features["E(UP) - time_left"] <= 0.280913:
                                    if features["T(DOWN)"] <= 0.000469:
                                        return 3
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= 0.070930:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.161732:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 2
                                else:
                                    if features["T(RIGHT) - T(E(LEFT))"] <= -0.139023:
                                        if features["E(UP) - T(T(up))"] <= 0.011761:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        if features["E(LEFT) - T(E(LEFT))"] <= 0.019023:
                                            if features["E(DOWN) - T(T(LEFT))"] <= -0.010791:
                                                if features["E(UP) - time_left"] <= 0.413547:
                                                    return 0
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                        else:
                                            if features["T(T(LEFT))"] <= 0.230103:
                                                return 0
                                            else:
                                                return 2
                        else:
                            if features["T(RIGHT) - time_left"] <= -0.009832:
                                if features["T(RIGHT) - T(E(RIGHT))"] <= -0.150883:
                                    if features["T(LEFT) - T(E(LEFT))"] <= -0.143663:
                                        return 1
                                    else:
                                        if features["T(E(UP)) - agent_column"] <= -7.642977:
                                            if features["T(up) - agent_row"] <= -8.394235:
                                                if features["E(RIGHT) - T(DOWN)"] <= 0.153621:
                                                    return 2
                                                else:
                                                    return 3
                                            else:
                                                return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT) - T(T(DOWN))"] <= 0.329137:
                                        if features["agent_column - time_left"] <= 9.890000:
                                            if features["T(LEFT) - agent_column"] <= -2.999973:
                                                if features["T(LEFT) - T(E(LEFT))"] <= 0.201190:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["T(up) - T(RIGHT)"] <= -0.008335:
                                                    return 1
                                                else:
                                                    if features["E(RIGHT) - T(E(RIGHT))"] <= -0.050137:
                                                        return 0
                                                    else:
                                                        return 3
                                        else:
                                            if features["T(E(RIGHT)) - agent_row"] <= -10.942146:
                                                if features["T(E(UP)) - agent_row"] <= -12.662027:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 2
                                    else:
                                        return 2
                            else:
                                if features["E(DOWN) - time_left"] <= 0.210449:
                                    if features["E(UP) - T(LEFT)"] <= 0.347585:
                                        if features["T(E(LEFT)) - time_left"] <= -0.092202:
                                            if features["E(UP) - agent_column"] <= -0.751966:
                                                if features["T(up) - T(RIGHT)"] <= -0.000281:
                                                    return 2
                                                else:
                                                    if features["E(DOWN) - T(up)"] <= -0.307385:
                                                        return 2
                                                    else:
                                                        return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(LEFT) - T(T(LEFT))"] <= 0.013293:
                                                if features["T(LEFT) - T(E(LEFT))"] <= 0.010147:
                                                    if features["T(E(DOWN)) - time_left"] <= 0.154204:
                                                        if features["E(RIGHT) - time_left"] <= 0.204168:
                                                            if features["T(T(DOWN)) - T(T(LEFT))"] <= 0.321402:
                                                                return 2
                                                            else:
                                                                return 0
                                                        else:
                                                            if features["T(T(LEFT)) - agent_row"] <= -9.599207:
                                                                return 0
                                                            else:
                                                                return 2
                                                    else:
                                                        if features["E(RIGHT) - T(T(RIGHT))"] <= -0.002968:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    if features["T(DOWN) - T(T(LEFT))"] <= -0.171026:
                                                        return 1
                                                    else:
                                                        if features["T(E(UP)) - T(T(DOWN))"] <= 0.133288:
                                                            return 2
                                                        else:
                                                            return 0
                                            else:
                                                if features["T(up) - agent_column"] <= -1.394509:
                                                    if features["T(E(RIGHT))"] <= 0.031886:
                                                        return 0
                                                    else:
                                                        if features["T(E(UP))"] <= 0.224168:
                                                            return 1
                                                        else:
                                                            return 2
                                                else:
                                                    return 0
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= -0.000001:
                                            if features["E(DOWN) - T(LEFT)"] <= 0.073123:
                                                if features["T(LEFT)"] <= 0.000027:
                                                    if features["T(T(LEFT)) - agent_row"] <= -5.861673:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 2
                                            else:
                                                if features["T(E(UP)) - T(E(RIGHT))"] <= 0.437055:
                                                    return 2
                                                else:
                                                    if features["T(DOWN)"] <= 0.007659:
                                                        return 0
                                                    else:
                                                        return 2
                                        else:
                                            if features["E(RIGHT) - T(E(LEFT))"] <= 0.055881:
                                                if features["T(E(RIGHT)) - agent_column"] <= -5.792108:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                else:
                                    return 1
                else:
                    if features["T(LEFT) - T(E(LEFT))"] <= -0.141139:
                        if features["T(up) - T(RIGHT)"] <= 0.000081:
                            if features["E(LEFT) - agent_row"] <= -9.803335:
                                if features["E(DOWN) - T(E(UP))"] <= -0.241385:
                                    return 0
                                else:
                                    return 2
                            else:
                                if features["E(LEFT) - T(DOWN)"] <= 0.216960:
                                    if features["T(RIGHT) - T(E(RIGHT))"] <= -0.230240:
                                        if features["E(RIGHT) - agent_column"] <= -5.242047:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        if features["E(DOWN) - T(E(UP))"] <= -0.348832:
                                            return 0
                                        else:
                                            if features["T(T(RIGHT)) - agent_row"] <= -4.791360:
                                                return 2
                                            else:
                                                return 0
                                else:
                                    return 2
                        else:
                            if features["E(UP) - E(DOWN)"] <= 0.226876:
                                if features["T(up) - T(E(RIGHT))"] <= 0.542361:
                                    if features["E(DOWN) - T(E(UP))"] <= -0.149149:
                                        if features["T(up) - T(T(up))"] <= -0.245368:
                                            return 3
                                        else:
                                            if features["E(LEFT) - T(T(LEFT))"] <= -0.305751:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        return 1
                                else:
                                    if features["T(E(DOWN)) - agent_column"] <= -4.998657:
                                        return 2
                                    else:
                                        return 1
                            else:
                                if features["T(E(DOWN)) - agent_column"] <= -7.964834:
                                    if features["E(DOWN) - T(LEFT)"] <= -0.000282:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["E(LEFT) - T(E(RIGHT))"] <= 0.107529:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.003875:
                                            if features["T(T(up)) - time_left"] <= 0.420504:
                                                if features["T(up) - T(T(LEFT))"] <= 0.087570:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 3
                                        else:
                                            if features["T(E(UP)) - time_left"] <= 0.292445:
                                                return 1
                                            else:
                                                return 2
                                    else:
                                        if features["T(E(UP)) - agent_column"] <= -2.334976:
                                            return 2
                                        else:
                                            return 3
                    else:
                        if features["E(DOWN) - T(RIGHT)"] <= 0.066291:
                            if features["T(T(DOWN)) - T(T(RIGHT))"] <= -0.301535:
                                return 3
                            else:
                                if features["T(DOWN) - time_left"] <= -0.059408:
                                    if features["E(DOWN) - time_left"] <= -0.195183:
                                        if features["E(LEFT) - T(E(UP))"] <= -0.242641:
                                            if features["E(DOWN) - T(DOWN)"] <= 0.016964:
                                                if features["T(up) - time_left"] <= -0.214447:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 3
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= -0.225678:
                                                if features["T(RIGHT) - T(E(UP))"] <= 0.545866:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["E(RIGHT) - T(RIGHT)"] <= 0.084655:
                                                    if features["T(RIGHT) - T(T(LEFT))"] <= -0.538076:
                                                        return 0
                                                    else:
                                                        if features["T(T(up)) - time_left"] <= -0.263763:
                                                            return 2
                                                        else:
                                                            return 0
                                                else:
                                                    if features["E(RIGHT) - agent_column"] <= -3.755146:
                                                        if features["T(up) - T(LEFT)"] <= 0.000056:
                                                            if features["E(LEFT) - time_left"] <= -0.212597:
                                                                return 2
                                                            else:
                                                                return 3
                                                        else:
                                                            return 2
                                                    else:
                                                        return 3
                                    else:
                                        if features["T(T(up)) - agent_row"] <= -10.419625:
                                            if features["E(DOWN) - E(LEFT)"] <= -0.000343:
                                                if features["E(RIGHT) - T(E(UP))"] <= -0.196382:
                                                    if features["E(LEFT) - T(LEFT)"] <= 0.244501:
                                                        return 3
                                                    else:
                                                        if features["T(T(LEFT)) - agent_column"] <= -8.644824:
                                                            return 2
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(RIGHT) - time_left"] <= 0.220169:
                                                        if features["T(DOWN)"] <= 0.002267:
                                                            if features["T(up) - T(E(LEFT))"] <= 0.044554:
                                                                return 2
                                                            else:
                                                                if features["T(RIGHT)"] <= 0.433315:
                                                                    return 3
                                                                else:
                                                                    if features["E(RIGHT) - agent_column"] <= -7.804400:
                                                                        return 2
                                                                    else:
                                                                        if features["E(UP) - E(LEFT)"] <= 0.126959:
                                                                            return 1
                                                                        else:
                                                                            return 3
                                                        else:
                                                            if features["T(RIGHT) - T(E(LEFT))"] <= 0.203919:
                                                                return 2
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["T(RIGHT) - agent_row"] <= -13.999663:
                                                            return 0
                                                        else:
                                                            return 3
                                            else:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.018058:
                                                    return 0
                                                else:
                                                    return 3
                                        else:
                                            if features["E(DOWN) - T(E(UP))"] <= -0.229102:
                                                if features["T(E(UP)) - T(T(up))"] <= 0.352636:
                                                    if features["E(LEFT) - T(E(UP))"] <= -0.309941:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(LEFT)"] <= 0.114656:
                                                        return 0
                                                    else:
                                                        return 2
                                            else:
                                                if features["T(up) - T(RIGHT)"] <= -0.000562:
                                                    return 2
                                                else:
                                                    if features["E(UP) - T(LEFT)"] <= 0.311429:
                                                        return 1
                                                    else:
                                                        return 3
                                else:
                                    if features["T(E(RIGHT)) - agent_row"] <= -8.711866:
                                        if features["T(RIGHT) - T(E(RIGHT))"] <= -0.267286:
                                            if features["T(up) - agent_column"] <= -4.508504:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["E(DOWN) - T(E(RIGHT))"] <= -0.020938:
                                                if features["T(T(LEFT)) - T(T(RIGHT))"] <= -0.257186:
                                                    return 2
                                                else:
                                                    if features["T(E(RIGHT)) - T(T(RIGHT))"] <= 0.001831:
                                                        if features["T(LEFT) - T(E(LEFT))"] <= -0.098971:
                                                            return 1
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["E(DOWN) - time_left"] <= 0.111282:
                                                            if features["T(DOWN) - T(E(RIGHT))"] <= -0.342009:
                                                                return 3
                                                            else:
                                                                if features["T(up) - agent_column"] <= -12.998303:
                                                                    return 2
                                                                else:
                                                                    if features["E(DOWN) - T(LEFT)"] <= 0.022573:
                                                                        if features["T(RIGHT) - T(T(up))"] <= 0.580236:
                                                                            if features["T(LEFT) - T(T(LEFT))"] <= 0.895573:
                                                                                return 0
                                                                            else:
                                                                                return 2
                                                                        else:
                                                                            return 3
                                                                    else:
                                                                        if features["T(LEFT) - T(RIGHT)"] <= -0.591069:
                                                                            return 0
                                                                        else:
                                                                            return 2
                                                        else:
                                                            return 2
                                            else:
                                                return 2
                                    else:
                                        if features["E(UP) - T(E(LEFT))"] <= 0.123896:
                                            return 1
                                        else:
                                            return 2
                        else:
                            if features["T(up) - T(LEFT)"] <= 0.000014:
                                if features["E(UP) - E(RIGHT)"] <= 0.172325:
                                    if features["T(T(up)) - agent_row"] <= -8.744489:
                                        return 3
                                    else:
                                        if features["T(up) - T(E(UP))"] <= 0.248915:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["T(up) - time_left"] <= 0.000525:
                                        if features["T(LEFT) - agent_column"] <= -8.415002:
                                            return 2
                                        else:
                                            return 3
                                    else:
                                        if features["T(LEFT) - T(E(RIGHT))"] <= 0.451057:
                                            return 3
                                        else:
                                            return 0
                            else:
                                if features["E(UP) - E(LEFT)"] <= 0.175860:
                                    if features["T(E(UP)) - T(E(DOWN))"] <= 0.418789:
                                        if features["E(UP) - T(T(LEFT))"] <= 0.312253:
                                            if features["E(DOWN) - T(up)"] <= -0.435355:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 3
                                    else:
                                        return 2
                                else:
                                    if features["T(up) - agent_column"] <= -7.417331:
                                        return 1
                                    else:
                                        return 3
            else:
                if features["E(LEFT) - T(T(up))"] <= 0.001339:
                    if features["E(RIGHT) - T(T(RIGHT))"] <= 0.058114:
                        if features["E(LEFT) - T(T(LEFT))"] <= 0.047269:
                            if features["E(DOWN) - T(RIGHT)"] <= 0.000947:
                                if features["E(UP) - time_left"] <= 0.286549:
                                    if features["E(LEFT)"] <= 0.010565:
                                        if features["E(DOWN) - T(DOWN)"] <= -0.000003:
                                            if features["T(T(up)) - agent_row"] <= -2.478607:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 0
                                    else:
                                        if features["E(RIGHT) - T(up)"] <= -0.126514:
                                            return 0
                                        else:
                                            return 2
                                else:
                                    if features["E(DOWN)"] <= 0.045330:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.293088:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        if features["E(UP) - time_left"] <= 0.368703:
                                            return 2
                                        else:
                                            return 0
                            else:
                                if features["T(DOWN) - T(E(RIGHT))"] <= -0.254689:
                                    return 3
                                else:
                                    return 0
                        else:
                            if features["E(RIGHT) - T(DOWN)"] <= 0.055870:
                                if features["E(LEFT) - T(E(DOWN))"] <= 0.083186:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(RIGHT) - T(E(LEFT))"] <= 0.145717:
                                    if features["T(up) - T(RIGHT)"] <= 0.004744:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 3
                    else:
                        if features["E(UP) - E(DOWN)"] <= 0.800657:
                            if features["E(DOWN)"] <= 0.000132:
                                if features["T(up) - agent_row"] <= -1.999794:
                                    if features["T(RIGHT) - agent_row"] <= -13.622476:
                                        if features["E(RIGHT) - T(E(LEFT))"] <= 0.390463:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.000008:
                                            if features["E(UP) - E(RIGHT)"] <= -0.000029:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 0
                                else:
                                    if features["T(E(UP)) - agent_row"] <= -0.968188:
                                        return 0
                                    else:
                                        return 3
                            else:
                                if features["E(UP) - T(LEFT)"] <= 0.021419:
                                    if features["E(UP) - T(RIGHT)"] <= 0.495288:
                                        if features["T(DOWN) - time_left"] <= -0.199989:
                                            if features["T(DOWN) - T(RIGHT)"] <= 0.000002:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        return 0
                                else:
                                    if features["E(UP) - E(RIGHT)"] <= 0.021581:
                                        if features["E(RIGHT) - T(T(RIGHT))"] <= 0.127953:
                                            return 3
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -10.999788:
                                                return 0
                                            else:
                                                if features["agent_row - time_left"] <= 1.930000:
                                                    return 3
                                                else:
                                                    if features["T(up)"] <= 0.444727:
                                                        if features["T(RIGHT) - T(E(RIGHT))"] <= 0.057576:
                                                            if features["T(up) - agent_row"] <= -4.796768:
                                                                return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            if features["E(LEFT) - T(up)"] <= 0.032248:
                                                                return 0
                                                            else:
                                                                return 2
                                                    else:
                                                        if features["agent_row - time_left"] <= 8.770000:
                                                            if features["E(LEFT) - E(RIGHT)"] <= -0.534940:
                                                                return 0
                                                            else:
                                                                if features["E(LEFT) - T(RIGHT)"] <= -0.409786:
                                                                    if features["T(E(UP)) - time_left"] <= 0.199534:
                                                                        return 1
                                                                    else:
                                                                        return 3
                                                                else:
                                                                    return 0
                                                        else:
                                                            if features["E(DOWN) - T(LEFT)"] <= -0.005348:
                                                                return 3
                                                            else:
                                                                if features["T(LEFT)"] <= 0.005463:
                                                                    return 3
                                                                else:
                                                                    return 1
                                    else:
                                        if features["T(up) - T(T(LEFT))"] <= 0.153231:
                                            if features["T(T(up)) - agent_row"] <= -1.951292:
                                                if features["E(DOWN) - T(T(LEFT))"] <= -0.384784:
                                                    if features["T(DOWN) - agent_column"] <= -11.999848:
                                                        return 0
                                                    else:
                                                        if features["T(DOWN) - T(LEFT)"] <= -0.003188:
                                                            return 3
                                                        else:
                                                            return 0
                                                else:
                                                    if features["E(RIGHT) - time_left"] <= -0.063262:
                                                        return 2
                                                    else:
                                                        return 0
                                            else:
                                                return 3
                                        else:
                                            if features["E(DOWN) - T(E(LEFT))"] <= -0.126495:
                                                if features["agent_column - time_left"] <= 4.890000:
                                                    if features["T(up) - agent_row"] <= -6.516448:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 0
                                            else:
                                                if features["E(UP) - time_left"] <= 0.303258:
                                                    return 3
                                                else:
                                                    return 0
                        else:
                            if features["T(E(LEFT)) - agent_row"] <= -0.998738:
                                if features["E(UP) - agent_column"] <= -11.133071:
                                    if features["T(E(DOWN)) - agent_row"] <= -9.912861:
                                        if features["E(UP) - E(RIGHT)"] <= 0.041247:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 0
                                else:
                                    if features["E(UP) - T(T(LEFT))"] <= 0.740224:
                                        if features["E(RIGHT) - T(E(LEFT))"] <= 0.374305:
                                            return 0
                                        else:
                                            if features["T(up) - T(RIGHT)"] <= -0.668683:
                                                return 0
                                            else:
                                                return 3
                                    else:
                                        if features["T(T(DOWN)) - agent_column"] <= -0.673670:
                                            return 3
                                        else:
                                            return 0
                            else:
                                if features["T(E(DOWN)) - time_left"] <= -0.731572:
                                    return 1
                                else:
                                    if features["T(DOWN) - T(E(LEFT))"] <= 0.647183:
                                        return 3
                                    else:
                                        return 0
                else:
                    if features["E(DOWN) - agent_row"] <= -1.999994:
                        if features["E(DOWN) - T(DOWN)"] <= 0.000008:
                            if features["E(LEFT)"] <= 0.799538:
                                if features["E(DOWN)"] <= 0.000038:
                                    if features["E(DOWN) - T(DOWN)"] <= -0.000004:
                                        if features["E(UP)"] <= 0.730461:
                                            if features["T(LEFT) - time_left"] <= -0.719871:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 0
                                    else:
                                        if features["T(up) - T(E(LEFT))"] <= 0.211605:
                                            if features["E(RIGHT) - agent_row"] <= -13.895640:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(RIGHT) - T(T(RIGHT))"] <= 0.309557:
                                                return 0
                                            else:
                                                return 3
                                else:
                                    if features["agent_row - time_left"] <= 10.910000:
                                        if features["E(UP) - T(T(up))"] <= 0.144739:
                                            if features["T(E(DOWN)) - T(T(RIGHT))"] <= -0.155762:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            if features["T(up) - T(DOWN)"] <= 0.476148:
                                                if features["E(RIGHT) - T(E(UP))"] <= -0.192066:
                                                    if features["E(LEFT)"] <= 0.631382:
                                                        if features["E(RIGHT) - T(T(up))"] <= -0.044180:
                                                            if features["T(DOWN) - T(T(up))"] <= -0.285504:
                                                                return 2
                                                            else:
                                                                return 0
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["T(T(DOWN)) - agent_column"] <= -2.477509:
                                                            if features["E(DOWN)"] <= 0.000599:
                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            return 0
                                                else:
                                                    if features["T(up) - T(E(UP))"] <= -0.092844:
                                                        if features["E(UP) - time_left"] <= -0.023089:
                                                            return 2
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -9.584842:
                                                            return 0
                                                        else:
                                                            return 2
                                            else:
                                                if features["E(DOWN) - T(T(DOWN))"] <= -0.421280:
                                                    if features["E(RIGHT) - time_left"] <= 0.198872:
                                                        return 2
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(UP) - time_left"] <= 0.388407:
                                                        return 2
                                                    else:
                                                        return 0
                                    else:
                                        if features["E(UP) - T(E(RIGHT))"] <= 0.463519:
                                            return 0
                                        else:
                                            return 2
                            else:
                                if features["E(UP) - agent_column"] <= -1.132198:
                                    if features["E(RIGHT) - agent_row"] <= -4.999992:
                                        if features["E(UP) - agent_column"] <= -5.132518:
                                            if features["agent_row - agent_column"] <= 2.500000:
                                                if features["E(DOWN) - E(RIGHT)"] <= 0.000005:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                if features["E(UP) - agent_column"] <= -6.136690:
                                                    return 2
                                                else:
                                                    if features["T(up) - agent_column"] <= -5.596082:
                                                        return 0
                                                    else:
                                                        return 2
                                        else:
                                            if features["T(T(up)) - agent_column"] <= -1.928885:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        if features["T(DOWN) - T(E(DOWN))"] <= 0.229682:
                                            if features["T(DOWN) - agent_row"] <= -4.693484:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 0
                                else:
                                    if features["agent_row - time_left"] <= 1.770000:
                                        return 2
                                    else:
                                        if features["T(E(DOWN)) - agent_column"] <= -1.999028:
                                            return 2
                                        else:
                                            return 0
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.122571:
                                if features["T(T(up)) - time_left"] <= 0.156408:
                                    if features["agent_row - agent_column"] <= 2.500000:
                                        if features["T(RIGHT)"] <= 0.000005:
                                            if features["T(E(RIGHT)) - time_left"] <= -0.021718:
                                                if features["E(UP)"] <= 0.520523:
                                                    if features["E(LEFT)"] <= 0.211189:
                                                        return 3
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                        else:
                                            if features["T(up) - T(T(LEFT))"] <= 0.142693:
                                                if features["T(T(up)) - time_left"] <= 0.101455:
                                                    if features["E(LEFT) - T(LEFT)"] <= 0.310750:
                                                        if features["T(RIGHT) - T(T(DOWN))"] <= -0.203581:
                                                            return 2
                                                        else:
                                                            if features["E(DOWN) - T(T(up))"] <= -0.002863:
                                                                return 0
                                                            else:
                                                                return 2
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                                            else:
                                                if features["T(E(UP)) - T(E(DOWN))"] <= 0.435238:
                                                    return 2
                                                else:
                                                    if features["T(RIGHT) - time_left"] <= -0.457270:
                                                        return 3
                                                    else:
                                                        return 2
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= 0.192888:
                                            if features["T(RIGHT) - T(E(UP))"] <= 0.127074:
                                                return 0
                                            else:
                                                if features["T(up) - agent_row"] <= -8.419713:
                                                    return 0
                                                else:
                                                    if features["T(E(DOWN)) - agent_column"] <= -1.946469:
                                                        return 2
                                                    else:
                                                        return 0
                                        else:
                                            if features["E(LEFT) - T(RIGHT)"] <= 0.096161:
                                                return 2
                                            else:
                                                if features["T(T(LEFT)) - time_left"] <= -0.299307:
                                                    if features["E(UP) - T(LEFT)"] <= -0.022691:
                                                        return 3
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(RIGHT) - T(up)"] <= -0.447118:
                                                        if features["E(DOWN) - E(RIGHT)"] <= -0.002643:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["E(UP) - T(up)"] <= 0.008581:
                                                            return 2
                                                        else:
                                                            if features["agent_column - time_left"] <= 5.750000:
                                                                return 2
                                                            else:
                                                                return 0
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= -0.310678:
                                        if features["E(UP) - agent_column"] <= -6.556705:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["T(RIGHT) - T(E(RIGHT))"] <= -0.000897:
                                            return 0
                                        else:
                                            if features["agent_row - agent_column"] <= 3.500000:
                                                return 2
                                            else:
                                                return 0
                            else:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.311095:
                                    if features["T(E(UP)) - time_left"] <= 0.330963:
                                        if features["T(up) - T(E(DOWN))"] <= 0.370257:
                                            return 0
                                        else:
                                            if features["E(UP) - E(RIGHT)"] <= 0.198872:
                                                if features["T(DOWN) - time_left"] <= -0.172358:
                                                    return 1
                                                else:
                                                    if features["T(LEFT) - T(T(RIGHT))"] <= -0.239236:
                                                        return 0
                                                    else:
                                                        return 3
                                            else:
                                                return 0
                                    else:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.217619:
                                            return 0
                                        else:
                                            if features["T(RIGHT) - T(E(UP))"] <= -0.383910:
                                                return 0
                                            else:
                                                return 3
                                else:
                                    if features["E(UP) - time_left"] <= 0.410955:
                                        if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.410594:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        return 0
                    else:
                        if features["T(E(RIGHT)) - agent_row"] <= -0.995672:
                            if features["E(DOWN) - E(LEFT)"] <= -0.257235:
                                if features["T(LEFT) - T(E(DOWN))"] <= 0.518950:
                                    if features["T(E(LEFT)) - agent_column"] <= -0.945722:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 0
                            else:
                                return 0
                        else:
                            if features["E(LEFT) - time_left"] <= 0.067931:
                                return 3
                            else:
                                if features["E(UP) - agent_column"] <= -0.132035:
                                    return 2
                                else:
                                    return 0


def interpretable_action(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability,agent_position, time_left, gamma, size, valid_actions):
    input_representation = symbolic_representation(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability, agent_position, time_left, gamma, size)
    input_combinations   = get_feature_vector(input_representation)
    symbole_to_value     = {name: input_combinations[i] for i, name in enumerate(symbole_names)}
    action               = Index_to_Action[interpretable_strategy(symbole_to_value)]
    if action in valid_actions:
        return action
    else:
        return random.choice(valid_actions)
