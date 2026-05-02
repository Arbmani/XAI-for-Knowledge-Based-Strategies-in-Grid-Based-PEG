import random
from INTERPRETER_2ND import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'T(E(UP))', 'T(E(DOWN))', 'T(E(LEFT))', 'T(E(RIGHT))', 'T(T(up))', 'T(T(DOWN))', 'T(T(LEFT))', 'T(T(RIGHT))', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - T(E(UP))', 'E(UP) - T(E(DOWN))', 'E(UP) - T(E(LEFT))', 'E(UP) - T(E(RIGHT))', 'E(UP) - T(T(up))', 'E(UP) - T(T(DOWN))', 'E(UP) - T(T(LEFT))', 'E(UP) - T(T(RIGHT))', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - T(E(UP))', 'E(DOWN) - T(E(DOWN))', 'E(DOWN) - T(E(LEFT))', 'E(DOWN) - T(E(RIGHT))', 'E(DOWN) - T(T(up))', 'E(DOWN) - T(T(DOWN))', 'E(DOWN) - T(T(LEFT))', 'E(DOWN) - T(T(RIGHT))', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - T(E(UP))', 'E(LEFT) - T(E(DOWN))', 'E(LEFT) - T(E(LEFT))', 'E(LEFT) - T(E(RIGHT))', 'E(LEFT) - T(T(up))', 'E(LEFT) - T(T(DOWN))', 'E(LEFT) - T(T(LEFT))', 'E(LEFT) - T(T(RIGHT))', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - T(E(UP))', 'E(RIGHT) - T(E(DOWN))', 'E(RIGHT) - T(E(LEFT))', 'E(RIGHT) - T(E(RIGHT))', 'E(RIGHT) - T(T(up))', 'E(RIGHT) - T(T(DOWN))', 'E(RIGHT) - T(T(LEFT))', 'E(RIGHT) - T(T(RIGHT))', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - T(E(UP))', 'T(up) - T(E(DOWN))', 'T(up) - T(E(LEFT))', 'T(up) - T(E(RIGHT))', 'T(up) - T(T(up))', 'T(up) - T(T(DOWN))', 'T(up) - T(T(LEFT))', 'T(up) - T(T(RIGHT))', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - T(E(UP))', 'T(DOWN) - T(E(DOWN))', 'T(DOWN) - T(E(LEFT))', 'T(DOWN) - T(E(RIGHT))', 'T(DOWN) - T(T(up))', 'T(DOWN) - T(T(DOWN))', 'T(DOWN) - T(T(LEFT))', 'T(DOWN) - T(T(RIGHT))', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - T(E(UP))', 'T(LEFT) - T(E(DOWN))', 'T(LEFT) - T(E(LEFT))', 'T(LEFT) - T(E(RIGHT))', 'T(LEFT) - T(T(up))', 'T(LEFT) - T(T(DOWN))', 'T(LEFT) - T(T(LEFT))', 'T(LEFT) - T(T(RIGHT))', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - T(E(UP))', 'T(RIGHT) - T(E(DOWN))', 'T(RIGHT) - T(E(LEFT))', 'T(RIGHT) - T(E(RIGHT))', 'T(RIGHT) - T(T(up))', 'T(RIGHT) - T(T(DOWN))', 'T(RIGHT) - T(T(LEFT))', 'T(RIGHT) - T(T(RIGHT))', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'T(E(UP)) - T(E(DOWN))', 'T(E(UP)) - T(E(LEFT))', 'T(E(UP)) - T(E(RIGHT))', 'T(E(UP)) - T(T(up))', 'T(E(UP)) - T(T(DOWN))', 'T(E(UP)) - T(T(LEFT))', 'T(E(UP)) - T(T(RIGHT))', 'T(E(UP)) - agent_row', 'T(E(UP)) - agent_column', 'T(E(UP)) - time_left', 'T(E(DOWN)) - T(E(LEFT))', 'T(E(DOWN)) - T(E(RIGHT))', 'T(E(DOWN)) - T(T(up))', 'T(E(DOWN)) - T(T(DOWN))', 'T(E(DOWN)) - T(T(LEFT))', 'T(E(DOWN)) - T(T(RIGHT))', 'T(E(DOWN)) - agent_row', 'T(E(DOWN)) - agent_column', 'T(E(DOWN)) - time_left', 'T(E(LEFT)) - T(E(RIGHT))', 'T(E(LEFT)) - T(T(up))', 'T(E(LEFT)) - T(T(DOWN))', 'T(E(LEFT)) - T(T(LEFT))', 'T(E(LEFT)) - T(T(RIGHT))', 'T(E(LEFT)) - agent_row', 'T(E(LEFT)) - agent_column', 'T(E(LEFT)) - time_left', 'T(E(RIGHT)) - T(T(up))', 'T(E(RIGHT)) - T(T(DOWN))', 'T(E(RIGHT)) - T(T(LEFT))', 'T(E(RIGHT)) - T(T(RIGHT))', 'T(E(RIGHT)) - agent_row', 'T(E(RIGHT)) - agent_column', 'T(E(RIGHT)) - time_left', 'T(T(up)) - T(T(DOWN))', 'T(T(up)) - T(T(LEFT))', 'T(T(up)) - T(T(RIGHT))', 'T(T(up)) - agent_row', 'T(T(up)) - agent_column', 'T(T(up)) - time_left', 'T(T(DOWN)) - T(T(LEFT))', 'T(T(DOWN)) - T(T(RIGHT))', 'T(T(DOWN)) - agent_row', 'T(T(DOWN)) - agent_column', 'T(T(DOWN)) - time_left', 'T(T(LEFT)) - T(T(RIGHT))', 'T(T(LEFT)) - agent_row', 'T(T(LEFT)) - agent_column', 'T(T(LEFT)) - time_left', 'T(T(RIGHT)) - agent_row', 'T(T(RIGHT)) - agent_column', 'T(T(RIGHT)) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(LEFT) - E(RIGHT)"] <= 0.299659:
        if features["E(UP) - E(RIGHT)"] <= 0.000002:
            if features["E(DOWN) - E(RIGHT)"] <= -0.000018:
                if features["E(UP) - T(T(up))"] <= 0.030960:
                    if features["E(DOWN) - E(LEFT)"] <= 0.799831:
                        if features["E(UP) - T(T(DOWN))"] <= 0.083358:
                            if features["E(LEFT) - T(up)"] <= 0.048207:
                                if features["E(DOWN) - T(E(UP))"] <= 0.252884:
                                    if features["E(LEFT) - T(T(LEFT))"] <= 0.013462:
                                        if features["E(RIGHT)"] <= 0.273870:
                                            if features["E(UP) - agent_row"] <= -10.999970:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["E(UP) - T(up)"] <= 0.252159:
                                                if features["T(E(RIGHT))"] <= 0.032148:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["E(RIGHT) - T(RIGHT)"] <= -0.223046:
                                                    if features["E(DOWN) - agent_column"] <= -3.766002:
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
                                        if features["T(E(RIGHT)) - agent_column"] <= -12.245032:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        if features["T(up) - agent_column"] <= -0.982473:
                                            if features["E(DOWN) - T(DOWN)"] <= 0.013571:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -11.267652:
                                                    return 1
                                                else:
                                                    if features["E(RIGHT) - agent_row"] <= -10.336100:
                                                        return 3
                                                    else:
                                                        if features["E(RIGHT) - agent_column"] <= -4.300370:
                                                            if features["E(RIGHT) - agent_column"] <= -10.268885:
                                                                if features["E(RIGHT) - agent_row"] <= -9.276387:
                                                                    return 1
                                                                else:
                                                                    if features["E(RIGHT) - time_left"] <= 0.543754:
                                                                        return 1
                                                                    else:
                                                                        return 3
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(DOWN) - E(RIGHT)"] <= -0.010566:
                                                                return 3
                                                            else:
                                                                return 1
                                        else:
                                            if features["T(T(up)) - time_left"] <= 0.170019:
                                                return 1
                                            else:
                                                return 3
                            else:
                                if features["T(LEFT) - T(E(LEFT))"] <= 0.254472:
                                    if features["E(UP) - T(T(LEFT))"] <= -0.112082:
                                        if features["T(RIGHT) - agent_column"] <= -4.455975:
                                            if features["T(DOWN) - T(LEFT)"] <= -0.000204:
                                                if features["T(up) - agent_column"] <= -11.999909:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["E(RIGHT)"] <= 0.381048:
                                                    return 0
                                                else:
                                                    if features["T(E(RIGHT)) - T(T(RIGHT))"] <= 0.104693:
                                                        return 1
                                                    else:
                                                        return 3
                                        else:
                                            return 3
                                    else:
                                        if features["T(T(RIGHT)) - agent_column"] <= -4.913851:
                                            return 0
                                        else:
                                            if features["E(UP) - time_left"] <= 0.149317:
                                                return 3
                                            else:
                                                return 0
                                else:
                                    return 3
                        else:
                            if features["E(RIGHT) - T(T(RIGHT))"] <= 0.019928:
                                if features["T(LEFT) - agent_column"] <= -0.975631:
                                    if features["E(LEFT) - T(T(LEFT))"] <= 0.018154:
                                        if features["E(UP) - T(T(DOWN))"] <= 0.121671:
                                            if features["E(LEFT) - time_left"] <= 0.082482:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["T(LEFT)"] <= 0.000125:
                                                return 0
                                            else:
                                                return 3
                                    else:
                                        if features["T(E(UP)) - T(T(up))"] <= -0.012998:
                                            return 3
                                        else:
                                            return 0
                                else:
                                    if features["E(RIGHT) - T(T(RIGHT))"] <= 0.005546:
                                        return 3
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -8.972006:
                                            return 0
                                        else:
                                            return 3
                            else:
                                if features["E(DOWN) - T(RIGHT)"] <= -0.351490:
                                    if features["E(LEFT) - E(RIGHT)"] <= -0.416486:
                                        if features["E(LEFT) - T(T(RIGHT))"] <= 0.008041:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= 0.000015:
                                            if features["T(E(UP)) - time_left"] <= 0.281400:
                                                if features["E(LEFT) - time_left"] <= -0.008331:
                                                    return 3
                                                else:
                                                    if features["E(UP)"] <= 0.217615:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                return 0
                                        else:
                                            return 3
                                else:
                                    if features["E(RIGHT) - time_left"] <= 0.308120:
                                        if features["E(UP) - T(E(DOWN))"] <= 0.189920:
                                            if features["T(E(UP)) - T(E(LEFT))"] <= -0.518061:
                                                return 1
                                            else:
                                                if features["T(up) - T(T(DOWN))"] <= -0.034185:
                                                    if features["T(E(LEFT)) - T(T(LEFT))"] <= 0.184771:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    return 3
                                        else:
                                            if features["E(LEFT) - T(E(RIGHT))"] <= -0.226121:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        if features["E(LEFT) - T(E(LEFT))"] <= -0.365698:
                                            return 1
                                        else:
                                            if features["E(UP) - T(up)"] <= 0.183437:
                                                return 3
                                            else:
                                                if features["T(up) - agent_row"] <= -8.999928:
                                                    return 0
                                                else:
                                                    return 3
                    else:
                        if features["T(DOWN) - agent_column"] <= -12.411637:
                            if features["T(T(LEFT)) - agent_row"] <= -7.562373:
                                if features["T(LEFT) - agent_row"] <= -8.550730:
                                    return 1
                                else:
                                    return 3
                            else:
                                return 1
                        else:
                            if features["T(E(DOWN)) - agent_column"] <= -5.690139:
                                if features["T(DOWN) - agent_row"] <= -10.117905:
                                    if features["E(DOWN) - E(LEFT)"] <= 0.867255:
                                        if features["T(T(RIGHT)) - agent_column"] <= -9.979618:
                                            return 3
                                        else:
                                            if features["T(E(DOWN)) - T(E(RIGHT))"] <= -0.100006:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        return 3
                                else:
                                    return 3
                            else:
                                if features["T(E(LEFT)) - agent_row"] <= -2.989450:
                                    if features["T(E(DOWN)) - agent_row"] <= -11.510059:
                                        return 3
                                    else:
                                        if features["T(DOWN) - T(T(RIGHT))"] <= 0.167348:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["T(T(DOWN)) - agent_row"] <= -0.922300:
                                        return 3
                                    else:
                                        return 1
                else:
                    if features["E(LEFT) - T(up)"] <= 0.036760:
                        if features["E(DOWN) - E(RIGHT)"] <= -0.801018:
                            if features["E(DOWN) - E(LEFT)"] <= 0.000084:
                                if features["E(UP) - agent_column"] <= -0.132486:
                                    if features["E(RIGHT) - agent_column"] <= -12.131904:
                                        return 0
                                    else:
                                        if features["E(UP) - E(LEFT)"] <= 0.867951:
                                            if features["T(T(RIGHT)) - agent_row"] <= -4.910449:
                                                if features["E(UP) - T(RIGHT)"] <= 0.289363:
                                                    return 0
                                                else:
                                                    if features["T(T(LEFT)) - agent_column"] <= -10.589769:
                                                        if features["T(E(DOWN)) - agent_row"] <= -7.990185:
                                                            return 3
                                                        else:
                                                            if features["T(T(LEFT)) - agent_row"] <= -6.618095:
                                                                return 0
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["T(LEFT) - T(T(RIGHT))"] <= 0.244172:
                                                            if features["T(T(RIGHT)) - agent_row"] <= -11.847041:
                                                                return 3
                                                            else:
                                                                if features["agent_row - agent_column"] <= 3.500000:
                                                                    return 3
                                                                else:
                                                                    if features["E(RIGHT)"] <= 0.867955:
                                                                        return 0
                                                                    else:
                                                                        return 3
                                                        else:
                                                            return 3
                                            else:
                                                if features["agent_row - agent_column"] <= -8.500000:
                                                    if features["T(LEFT) - T(E(UP))"] <= -0.513470:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["agent_column - time_left"] <= 2.780000:
                                                        if features["E(LEFT) - E(RIGHT)"] <= -0.867887:
                                                            return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["E(UP) - E(RIGHT)"] <= -0.001274:
                                                            return 3
                                                        else:
                                                            if features["T(E(UP)) - agent_column"] <= -11.600541:
                                                                return 3
                                                            else:
                                                                return 0
                                        else:
                                            return 3
                                else:
                                    if features["T(T(DOWN)) - time_left"] <= -0.365945:
                                        return 3
                                    else:
                                        return 0
                            else:
                                if features["T(T(RIGHT)) - agent_row"] <= -2.545255:
                                    return 0
                                else:
                                    return 3
                        else:
                            if features["agent_row - agent_column"] <= 7.500000:
                                if features["E(UP) - agent_column"] <= -11.234131:
                                    return 0
                                else:
                                    if features["T(E(LEFT)) - T(E(RIGHT))"] <= 0.345097:
                                        if features["E(LEFT)"] <= 0.000015:
                                            if features["E(UP) - agent_column"] <= 0.544076:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(DOWN) - T(E(LEFT))"] <= 0.008928:
                                                if features["T(RIGHT) - time_left"] <= 0.501024:
                                                    if features["T(T(RIGHT)) - time_left"] <= 0.222215:
                                                        if features["T(E(RIGHT)) - T(T(DOWN))"] <= -0.309521:
                                                            return 3
                                                        else:
                                                            if features["T(LEFT) - T(T(up))"] <= -0.213839:
                                                                return 3
                                                            else:
                                                                if features["T(E(UP)) - T(E(RIGHT))"] <= -0.055240:
                                                                    return 3
                                                                else:
                                                                    if features["E(DOWN) - agent_row"] <= -7.998486:
                                                                        if features["E(RIGHT) - T(DOWN)"] <= 0.312864:
                                                                            return 0
                                                                        else:
                                                                            return 3
                                                                    else:
                                                                        return 3
                                                    else:
                                                        if features["T(T(up)) - agent_column"] <= -1.877076:
                                                            return 3
                                                        else:
                                                            return 0
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -8.922639:
                                                        return 0
                                                    else:
                                                        return 3
                                            else:
                                                if features["T(RIGHT) - agent_row"] <= -2.849495:
                                                    if features["E(RIGHT) - T(E(UP))"] <= 0.042241:
                                                        if features["agent_row - agent_column"] <= 2.500000:
                                                            return 3
                                                        else:
                                                            if features["E(RIGHT)"] <= 0.420524:
                                                                return 0
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["T(up) - time_left"] <= -0.169993:
                                                            if features["T(up) - agent_column"] <= -8.000000:
                                                                if features["T(DOWN) - T(E(UP))"] <= 0.536072:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(LEFT) - T(E(RIGHT))"] <= -0.261256:
                                                                return 3
                                                            else:
                                                                if features["T(DOWN) - T(E(LEFT))"] <= 0.044708:
                                                                    return 3
                                                                else:
                                                                    if features["E(LEFT) - T(DOWN)"] <= -0.398284:
                                                                        return 3
                                                                    else:
                                                                        return 0
                                                else:
                                                    if features["T(E(LEFT)) - time_left"] <= -0.011967:
                                                        return 3
                                                    else:
                                                        if features["E(DOWN) - T(RIGHT)"] <= -0.401567:
                                                            return 3
                                                        else:
                                                            return 1
                                    else:
                                        return 0
                            else:
                                if features["T(RIGHT) - T(E(LEFT))"] <= 0.359067:
                                    if features["E(DOWN) - E(LEFT)"] <= -0.000368:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.005395:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        if features["E(RIGHT) - T(E(UP))"] <= 0.016843:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    if features["T(E(RIGHT)) - time_left"] <= 0.342024:
                                        if features["E(UP) - time_left"] <= 0.266232:
                                            if features["T(LEFT) - T(E(UP))"] <= -0.327043:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -1.998716:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        return 3
                    else:
                        if features["E(DOWN) - T(T(DOWN))"] <= 0.176524:
                            if features["E(LEFT) - T(LEFT)"] <= 0.106949:
                                if features["T(RIGHT) - T(E(RIGHT))"] <= -0.228713:
                                    if features["T(LEFT) - T(E(LEFT))"] <= 0.293409:
                                        if features["T(E(RIGHT)) - time_left"] <= 0.366712:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 3
                                else:
                                    if features["T(LEFT) - agent_column"] <= -2.999828:
                                        if features["T(T(RIGHT)) - time_left"] <= -0.279827:
                                            return 3
                                        else:
                                            if features["T(DOWN) - T(E(DOWN))"] <= -0.197924:
                                                if features["T(T(DOWN)) - agent_row"] <= -8.969134:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(up) - agent_row"] <= -0.999992:
                                                    if features["T(DOWN) - T(E(UP))"] <= 0.536291:
                                                        if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.024809:
                                                            return 0
                                                        else:
                                                            if features["T(E(RIGHT)) - T(T(LEFT))"] <= -0.334480:
                                                                return 3
                                                            else:
                                                                if features["T(RIGHT) - agent_column"] <= -3.482043:
                                                                    return 0
                                                                else:
                                                                    if features["T(LEFT) - T(RIGHT)"] <= -0.405232:
                                                                        return 0
                                                                    else:
                                                                        return 1
                                                    else:
                                                        if features["E(LEFT) - T(LEFT)"] <= 0.071716:
                                                            return 3
                                                        else:
                                                            return 0
                                                else:
                                                    return 3
                                    else:
                                        if features["T(E(RIGHT)) - agent_row"] <= -8.593582:
                                            if features["E(UP) - T(E(RIGHT))"] <= -0.139052:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["T(E(UP)) - T(T(RIGHT))"] <= -0.179575:
                                                return 0
                                            else:
                                                if features["T(E(UP)) - T(E(DOWN))"] <= 0.239164:
                                                    return 3
                                                else:
                                                    return 0
                            else:
                                if features["T(E(LEFT)) - time_left"] <= -0.217805:
                                    return 3
                                else:
                                    if features["T(DOWN) - T(RIGHT)"] <= -0.000002:
                                        if features["E(LEFT) - T(RIGHT)"] <= -0.334266:
                                            if features["T(E(DOWN)) - T(E(RIGHT))"] <= -0.509405:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 0
                                    else:
                                        return 0
                        else:
                            if features["E(LEFT) - T(LEFT)"] <= 0.118801:
                                if features["T(LEFT) - time_left"] <= -0.109796:
                                    if features["E(UP) - T(RIGHT)"] <= 0.132423:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.077361:
                                        return 0
                                    else:
                                        return 3
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.238914:
                                    if features["E(UP) - E(RIGHT)"] <= -0.180705:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    if features["agent_row - time_left"] <= 4.880000:
                                        return 3
                                    else:
                                        return 0
            else:
                if features["E(UP)"] <= 0.016355:
                    if features["E(RIGHT) - T(T(RIGHT))"] <= 0.032250:
                        if features["E(DOWN) - time_left"] <= 0.216230:
                            if features["E(RIGHT)"] <= 0.005627:
                                if features["E(LEFT) - T(E(LEFT))"] <= -0.056493:
                                    return 1
                                else:
                                    if features["T(T(LEFT)) - time_left"] <= -0.542271:
                                        if features["T(DOWN) - T(E(DOWN))"] <= -0.316794:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        return 1
                            else:
                                if features["agent_row - time_left"] <= -0.380000:
                                    return 3
                                else:
                                    if features["T(DOWN) - T(E(LEFT))"] <= 0.164707:
                                        if features["E(DOWN) - time_left"] <= 0.118915:
                                            if features["T(LEFT) - T(T(up))"] <= 0.304401:
                                                if features["T(E(LEFT)) - time_left"] <= -0.177305:
                                                    return 3
                                                else:
                                                    if features["T(E(DOWN))"] <= 0.331365:
                                                        return 2
                                                    else:
                                                        if features["E(DOWN) - T(up)"] <= 0.484947:
                                                            return 1
                                                        else:
                                                            return 2
                                            else:
                                                return 3
                                        else:
                                            if features["E(UP) - T(DOWN)"] <= -0.325756:
                                                return 1
                                            else:
                                                if features["T(DOWN) - T(E(RIGHT))"] <= 0.164032:
                                                    return 3
                                                else:
                                                    return 2
                                    else:
                                        if features["E(LEFT) - T(DOWN)"] <= -0.065330:
                                            if features["T(LEFT) - T(T(DOWN))"] <= -0.501184:
                                                return 3
                                            else:
                                                if features["T(T(DOWN)) - time_left"] <= -0.389387:
                                                    if features["E(RIGHT) - T(T(RIGHT))"] <= -0.183604:
                                                        return 3
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(LEFT) - T(T(RIGHT))"] <= -0.027342:
                                                        return 1
                                                    else:
                                                        if features["T(T(DOWN)) - time_left"] <= -0.021418:
                                                            return 1
                                                        else:
                                                            if features["E(RIGHT) - agent_column"] <= -11.951357:
                                                                return 1
                                                            else:
                                                                return 3
                                        else:
                                            if features["E(RIGHT) - time_left"] <= -0.330128:
                                                return 0
                                            else:
                                                return 1
                        else:
                            if features["E(RIGHT) - T(RIGHT)"] <= 0.045494:
                                if features["E(LEFT) - T(E(LEFT))"] <= 0.148033:
                                    if features["E(RIGHT) - T(E(UP))"] <= 0.279664:
                                        if features["T(DOWN) - T(E(UP))"] <= 0.606374:
                                            if features["E(UP)"] <= 0.010594:
                                                return 1
                                            else:
                                                if features["T(E(DOWN)) - agent_row"] <= -0.650170:
                                                    return 1
                                                else:
                                                    if features["E(LEFT)"] <= 0.170842:
                                                        return 3
                                                    else:
                                                        return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(RIGHT) - T(E(UP))"] <= 0.289711:
                                            if features["E(UP) - T(LEFT)"] <= -0.022390:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 1
                                else:
                                    if features["T(E(DOWN)) - agent_column"] <= -7.509966:
                                        return 1
                                    else:
                                        if features["T(T(LEFT))"] <= 0.206628:
                                            if features["E(RIGHT) - T(RIGHT)"] <= -0.029619:
                                                return 3
                                            else:
                                                return 2
                                        else:
                                            return 3
                            else:
                                if features["E(UP) - T(E(LEFT))"] <= -0.176118:
                                    if features["E(RIGHT) - time_left"] <= 0.081070:
                                        if features["T(DOWN) - T(LEFT)"] <= 0.000013:
                                            return 1
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -8.456498:
                                                if features["E(DOWN) - agent_column"] <= -10.611008:
                                                    return 1
                                                else:
                                                    if features["T(LEFT) - T(E(LEFT))"] <= 0.066871:
                                                        return 2
                                                    else:
                                                        return 1
                                            else:
                                                if features["T(E(UP)) - agent_row"] <= -8.995186:
                                                    return 2
                                                else:
                                                    return 1
                                    else:
                                        return 1
                                else:
                                    if features["T(DOWN) - agent_row"] <= 0.301171:
                                        if features["E(UP) - T(up)"] <= 0.000000:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - T(T(LEFT))"] <= 0.201764:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        return 3
                    else:
                        if features["E(RIGHT) - agent_row"] <= -0.633889:
                            if features["E(DOWN) - agent_row"] <= -11.200462:
                                if features["E(DOWN) - agent_column"] <= -12.171856:
                                    return 1
                                else:
                                    return 3
                            else:
                                if features["E(UP) - E(DOWN)"] <= -0.800690:
                                    if features["E(RIGHT) - agent_row"] <= -2.132139:
                                        if features["T(T(RIGHT)) - agent_column"] <= -4.722807:
                                            if features["T(DOWN) - agent_column"] <= -12.230971:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - agent_row"] <= -10.134033:
                                                    return 3
                                                else:
                                                    if features["T(DOWN) - T(T(RIGHT))"] <= 0.475014:
                                                        if features["T(E(RIGHT)) - agent_column"] <= -11.259383:
                                                            return 3
                                                        else:
                                                            if features["E(UP) - agent_column"] <= -9.999997:
                                                                return 1
                                                            else:
                                                                if features["E(RIGHT) - agent_column"] <= -7.132568:
                                                                    if features["T(up) - T(LEFT)"] <= 0.450731:
                                                                        return 3
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    if features["T(E(RIGHT)) - agent_column"] <= -7.242915:
                                                                        return 1
                                                                    else:
                                                                        if features["E(LEFT) - agent_column"] <= -6.000000:
                                                                            return 3
                                                                        else:
                                                                            if features["T(T(LEFT)) - agent_row"] <= -3.669241:
                                                                                return 1
                                                                            else:
                                                                                return 3
                                                    else:
                                                        return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -11.681000:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(UP)"] <= 0.000043:
                                        if features["T(DOWN) - T(LEFT)"] <= 0.484643:
                                            if features["E(UP) - agent_column"] <= -8.999997:
                                                return 1
                                            else:
                                                if features["T(T(DOWN)) - time_left"] <= 0.105254:
                                                    if features["E(UP)"] <= 0.000002:
                                                        if features["T(T(RIGHT)) - agent_row"] <= -11.698855:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                                        else:
                                            if features["T(up) - T(E(RIGHT))"] <= -0.597858:
                                                if features["T(LEFT) - agent_column"] <= -5.999925:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["T(E(UP)) - T(T(up))"] <= -0.539140:
                                                    return 3
                                                else:
                                                    return 1
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= 0.339238:
                                            if features["T(E(LEFT)) - time_left"] <= 0.015110:
                                                if features["E(UP) - T(up)"] <= 0.006539:
                                                    if features["E(DOWN) - T(LEFT)"] <= 0.167817:
                                                        if features["E(UP) - agent_column"] <= -8.998132:
                                                            return 1
                                                        else:
                                                            if features["E(RIGHT) - T(LEFT)"] <= -0.433950:
                                                                return 1
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["E(DOWN) - T(E(LEFT))"] <= 0.323620:
                                                            return 3
                                                        else:
                                                            if features["E(DOWN) - agent_column"] <= -11.267557:
                                                                return 1
                                                            else:
                                                                if features["E(DOWN) - T(E(DOWN))"] <= 0.310226:
                                                                    if features["E(DOWN) - T(E(RIGHT))"] <= 0.123956:
                                                                        if features["agent_row - agent_column"] <= 0.500000:
                                                                            return 1
                                                                        else:
                                                                            if features["T(up) - T(E(LEFT))"] <= -0.008490:
                                                                                if features["T(E(UP)) - T(T(RIGHT))"] <= -0.208374:
                                                                                    return 2
                                                                                else:
                                                                                    return 1
                                                                            else:
                                                                                return 3
                                                                    else:
                                                                        return 1
                                                                else:
                                                                    return 3
                                                else:
                                                    return 3
                                            else:
                                                if features["T(LEFT) - T(E(DOWN))"] <= 0.300905:
                                                    if features["E(DOWN) - time_left"] <= 0.288338:
                                                        if features["T(DOWN) - T(T(LEFT))"] <= -0.254319:
                                                            return 0
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["T(E(RIGHT)) - time_left"] <= 0.307640:
                                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.715415:
                                                                if features["E(LEFT) - T(E(RIGHT))"] <= 0.182914:
                                                                    if features["E(UP) - T(RIGHT)"] <= 0.006023:
                                                                        return 1
                                                                    else:
                                                                        if features["E(RIGHT) - agent_row"] <= -0.753878:
                                                                            return 1
                                                                        else:
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
                                            if features["T(LEFT) - T(E(RIGHT))"] <= -0.354482:
                                                if features["T(DOWN) - time_left"] <= 0.243148:
                                                    if features["T(T(up)) - T(T(RIGHT))"] <= 0.016912:
                                                        return 1
                                                    else:
                                                        if features["T(E(DOWN)) - time_left"] <= 0.194145:
                                                            return 1
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(RIGHT) - T(DOWN)"] <= -0.376506:
                                                        return 1
                                                    else:
                                                        if features["T(RIGHT) - agent_row"] <= -9.998846:
                                                            return 1
                                                        else:
                                                            return 3
                                            else:
                                                if features["E(RIGHT) - T(E(DOWN))"] <= 0.117919:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - agent_column"] <= -11.243144:
                                                        return 1
                                                    else:
                                                        return 3
                        else:
                            if features["E(LEFT) - agent_row"] <= -0.999993:
                                return 1
                            else:
                                if features["agent_column - time_left"] <= 12.520000:
                                    if features["E(RIGHT) - time_left"] <= 0.256825:
                                        if features["E(UP) - E(DOWN)"] <= -0.425245:
                                            if features["E(RIGHT) - T(LEFT)"] <= 0.337752:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(RIGHT) - T(E(RIGHT))"] <= -0.417556:
                                                return 2
                                            else:
                                                if features["T(RIGHT) - time_left"] <= -0.409987:
                                                    return 3
                                                else:
                                                    if features["E(RIGHT) - agent_column"] <= -7.618695:
                                                        if features["E(LEFT) - E(RIGHT)"] <= -0.028054:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(DOWN) - T(RIGHT)"] <= 0.000474:
                                                            return 1
                                                        else:
                                                            return 3
                                    else:
                                        if features["T(E(DOWN)) - agent_column"] <= -0.642585:
                                            if features["E(RIGHT) - T(E(UP))"] <= 0.342128:
                                                if features["T(DOWN) - T(RIGHT)"] <= 0.000005:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                        else:
                                            return 1
                                else:
                                    return 1
                else:
                    if features["E(LEFT) - T(E(RIGHT))"] <= 0.071056:
                        if features["E(LEFT) - T(LEFT)"] <= 0.092547:
                            if features["T(RIGHT) - T(T(RIGHT))"] <= 0.005860:
                                if features["E(UP) - T(E(LEFT))"] <= -0.127794:
                                    if features["E(UP) - T(E(DOWN))"] <= -0.308278:
                                        if features["E(DOWN) - time_left"] <= 0.408976:
                                            if features["E(LEFT) - T(RIGHT)"] <= -0.130972:
                                                return 1
                                            else:
                                                if features["T(RIGHT) - T(E(DOWN))"] <= -0.185770:
                                                    if features["T(E(UP)) - T(E(LEFT))"] <= -0.087354:
                                                        if features["E(LEFT) - time_left"] <= 0.181783:
                                                            return 1
                                                        else:
                                                            if features["E(LEFT) - T(E(DOWN))"] <= -0.054016:
                                                                return 1
                                                            else:
                                                                return 2
                                                    else:
                                                        if features["T(RIGHT) - T(E(LEFT))"] <= -0.146587:
                                                            return 3
                                                        else:
                                                            return 2
                                                else:
                                                    if features["T(E(DOWN)) - T(T(up))"] <= 0.340629:
                                                        if features["T(E(UP)) - time_left"] <= 0.040020:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 2
                                        else:
                                            if features["T(up) - agent_row"] <= -0.978694:
                                                return 0
                                            else:
                                                return 2
                                    else:
                                        if features["E(RIGHT) - T(T(DOWN))"] <= -0.158951:
                                            if features["T(DOWN) - T(LEFT)"] <= 0.001429:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.266649:
                                                return 3
                                            else:
                                                if features["E(LEFT) - T(E(LEFT))"] <= 0.134523:
                                                    if features["E(DOWN) - T(E(UP))"] <= 0.166767:
                                                        if features["T(DOWN) - T(LEFT)"] <= -0.000168:
                                                            return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 2
                                else:
                                    if features["T(RIGHT) - T(E(RIGHT))"] <= 0.010094:
                                        if features["E(DOWN) - E(RIGHT)"] <= 0.160092:
                                            if features["T(up) - T(LEFT)"] <= 0.000074:
                                                if features["E(DOWN) - time_left"] <= 0.177542:
                                                    if features["T(E(DOWN)) - T(E(LEFT))"] <= 0.071727:
                                                        if features["T(E(RIGHT)) - T(T(RIGHT))"] <= 0.062326:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(LEFT) - time_left"] <= -0.206945:
                                                        return 1
                                                    else:
                                                        if features["T(E(DOWN)) - time_left"] <= 0.359660:
                                                            return 3
                                                        else:
                                                            if features["T(RIGHT) - time_left"] <= 0.279870:
                                                                return 3
                                                            else:
                                                                return 0
                                            else:
                                                return 1
                                        else:
                                            if features["T(RIGHT)"] <= 0.127971:
                                                if features["E(UP) - agent_column"] <= -9.970677:
                                                    if features["T(E(UP)) - T(T(RIGHT))"] <= -0.015262:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(RIGHT) - time_left"] <= -0.189519:
                                                        return 0
                                                    else:
                                                        return 1
                                            else:
                                                if features["E(UP) - T(E(UP))"] <= -0.065064:
                                                    return 2
                                                else:
                                                    if features["T(up) - agent_column"] <= -9.953303:
                                                        return 2
                                                    else:
                                                        return 3
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -3.999977:
                                            return 0
                                        else:
                                            return 1
                            else:
                                if features["T(LEFT)"] <= 0.011218:
                                    if features["T(DOWN) - T(RIGHT)"] <= -0.000000:
                                        if features["T(RIGHT) - T(E(DOWN))"] <= 0.366496:
                                            return 1
                                        else:
                                            return 3
                                    else:
                                        if features["T(RIGHT) - agent_column"] <= -4.544067:
                                            if features["T(RIGHT) - T(E(UP))"] <= 0.365592:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 3
                                else:
                                    if features["T(up) - T(LEFT)"] <= -0.210965:
                                        return 2
                                    else:
                                        if features["T(DOWN) - time_left"] <= 0.361795:
                                            return 3
                                        else:
                                            if features["T(RIGHT) - T(E(RIGHT))"] <= 0.003237:
                                                return 1
                                            else:
                                                return 3
                        else:
                            if features["E(DOWN)"] <= 0.346338:
                                if features["E(RIGHT) - T(up)"] <= 0.171075:
                                    if features["T(up) - T(E(UP))"] <= -0.003528:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["T(DOWN) - T(RIGHT)"] <= 0.000038:
                                        if features["E(LEFT) - T(RIGHT)"] <= -0.388771:
                                            return 0
                                        else:
                                            if features["E(DOWN) - T(E(LEFT))"] <= 0.236835:
                                                if features["T(DOWN) - time_left"] <= 0.262911:
                                                    return 3
                                                else:
                                                    if features["T(E(RIGHT)) - T(T(up))"] <= 0.197803:
                                                        return 2
                                                    else:
                                                        return 0
                                            else:
                                                return 3
                                    else:
                                        if features["T(E(LEFT)) - time_left"] <= -0.143646:
                                            if features["agent_row - agent_column"] <= -6.500000:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.172107:
                                                return 0
                                            else:
                                                if features["T(DOWN) - agent_column"] <= -4.505393:
                                                    return 0
                                                else:
                                                    return 3
                            else:
                                if features["T(E(DOWN)) - time_left"] <= 0.315921:
                                    if features["E(UP) - T(up)"] <= 0.073249:
                                        if features["E(RIGHT) - T(E(LEFT))"] <= 0.122422:
                                            return 3
                                        else:
                                            if features["T(E(RIGHT)) - time_left"] <= 0.467725:
                                                return 3
                                            else:
                                                return 2
                                    else:
                                        if features["T(up) - T(LEFT)"] <= 0.000001:
                                            if features["T(DOWN)"] <= 0.548777:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 3
                                else:
                                    if features["T(up) - T(E(LEFT))"] <= -0.104391:
                                        if features["T(LEFT)"] <= 0.000043:
                                            if features["T(T(DOWN)) - agent_row"] <= -5.893427:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 3
                                    else:
                                        if features["E(UP) - T(E(LEFT))"] <= 0.056400:
                                            return 1
                                        else:
                                            return 3
                    else:
                        if features["E(UP) - T(E(DOWN))"] <= -0.276682:
                            if features["E(DOWN) - time_left"] <= 0.310171:
                                if features["T(LEFT) - agent_row"] <= -5.506954:
                                    if features["E(RIGHT) - T(E(UP))"] <= 0.035728:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.079244:
                                            return 2
                                        else:
                                            return 3
                                    else:
                                        if features["E(UP) - T(E(DOWN))"] <= -0.339750:
                                            if features["E(DOWN) - time_left"] <= 0.207661:
                                                if features["E(LEFT) - T(up)"] <= 0.292835:
                                                    return 3
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(UP) - T(E(UP))"] <= -0.028155:
                                                return 0
                                            else:
                                                return 3
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -0.926001:
                                        if features["T(T(LEFT)) - T(T(RIGHT))"] <= 0.187263:
                                            if features["T(LEFT) - T(T(RIGHT))"] <= 0.119555:
                                                if features["E(DOWN) - time_left"] <= 0.125863:
                                                    return 3
                                                else:
                                                    if features["E(LEFT)"] <= 0.281614:
                                                        if features["T(E(DOWN)) - T(T(DOWN))"] <= 0.022574:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["T(DOWN) - T(LEFT)"] <= -0.000089:
                                                            return 1
                                                        else:
                                                            if features["E(UP)"] <= 0.021631:
                                                                return 1
                                                            else:
                                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["T(E(UP)) - T(T(LEFT))"] <= -0.313406:
                                                if features["T(LEFT) - time_left"] <= 0.155809:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["T(RIGHT) - T(E(UP))"] <= 0.019803:
                                                    return 2
                                                else:
                                                    return 3
                                    else:
                                        if features["E(DOWN) - T(DOWN)"] <= 0.012941:
                                            if features["T(LEFT) - agent_column"] <= -8.565364:
                                                return 0
                                            else:
                                                return 1
                                        else:
                                            return 2
                            else:
                                if features["T(LEFT) - T(T(up))"] <= 0.111327:
                                    if features["E(LEFT) - T(up)"] <= 0.277248:
                                        return 1
                                    else:
                                        if features["T(up) - T(E(DOWN))"] <= -0.297149:
                                            if features["T(DOWN) - T(LEFT)"] <= 0.000292:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 1
                                else:
                                    if features["T(RIGHT)"] <= 0.152406:
                                        if features["E(LEFT) - T(E(LEFT))"] <= -0.013261:
                                            if features["agent_row - agent_column"] <= -7.500000:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 1
                                    else:
                                        if features["T(E(UP)) - agent_row"] <= -1.907287:
                                            return 0
                                        else:
                                            return 3
                        else:
                            if features["T(E(LEFT)) - T(T(up))"] <= 0.166798:
                                if features["E(DOWN) - time_left"] <= 0.267309:
                                    if features["T(T(LEFT)) - time_left"] <= 0.206077:
                                        if features["T(T(up)) - T(T(DOWN))"] <= 0.187445:
                                            return 0
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= 0.067861:
                                                return 2
                                            else:
                                                if features["T(E(UP)) - time_left"] <= -0.022391:
                                                    return 3
                                                else:
                                                    return 1
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.406980:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - time_left"] <= -0.014395:
                                                return 3
                                            else:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.003065:
                                                    return 3
                                                else:
                                                    return 2
                                else:
                                    if features["E(RIGHT) - T(T(DOWN))"] <= -0.127487:
                                        if features["T(E(LEFT)) - T(T(LEFT))"] <= -0.017376:
                                            return 3
                                        else:
                                            if features["T(LEFT) - time_left"] <= 0.333893:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        if features["T(up) - T(E(LEFT))"] <= -0.284503:
                                            if features["T(DOWN) - T(LEFT)"] <= 0.000015:
                                                return 3
                                            else:
                                                if features["T(LEFT) - T(E(UP))"] <= 0.308874:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["T(RIGHT) - T(E(DOWN))"] <= -0.017390:
                                                return 1
                                            else:
                                                return 3
                            else:
                                if features["T(DOWN) - T(E(DOWN))"] <= -0.100089:
                                    if features["T(up) - T(LEFT)"] <= -0.004594:
                                        if features["T(E(RIGHT)) - agent_row"] <= -4.940822:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(DOWN) - time_left"] <= 0.225828:
                                            return 0
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= -0.326816:
                                                return 1
                                            else:
                                                return 2
                                else:
                                    if features["E(UP) - time_left"] <= -0.070055:
                                        if features["T(LEFT) - agent_row"] <= -0.601259:
                                            if features["E(UP) - E(DOWN)"] <= -0.341539:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 3
                                    else:
                                        if features["E(LEFT)"] <= 0.315389:
                                            if features["T(LEFT) - T(E(UP))"] <= 0.478060:
                                                return 0
                                            else:
                                                if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.051323:
                                                    return 0
                                                else:
                                                    return 3
                                        else:
                                            if features["T(E(DOWN)) - time_left"] <= 0.330871:
                                                return 0
                                            else:
                                                return 2
        else:
            if features["E(UP) - E(RIGHT)"] <= 0.152010:
                if features["E(DOWN) - time_left"] <= 0.247113:
                    if features["T(E(UP)) - T(E(RIGHT))"] <= 0.087548:
                        if features["T(RIGHT) - T(T(LEFT))"] <= 0.187556:
                            if features["T(DOWN) - T(T(up))"] <= 0.388726:
                                if features["E(DOWN) - T(T(DOWN))"] <= -0.009208:
                                    if features["E(UP) - E(LEFT)"] <= -0.098980:
                                        if features["T(RIGHT) - agent_column"] <= -10.999970:
                                            if features["T(RIGHT)"] <= 0.044841:
                                                if features["T(RIGHT)"] <= 0.000081:
                                                    if features["agent_row - time_left"] <= 0.480000:
                                                        return 0
                                                    else:
                                                        if features["T(LEFT) - agent_row"] <= -1.688877:
                                                            return 2
                                                        else:
                                                            if features["T(DOWN) - T(LEFT)"] <= -0.000011:
                                                                return 1
                                                            else:
                                                                return 2
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(RIGHT) - time_left"] <= -0.079144:
                                                if features["E(LEFT) - T(E(LEFT))"] <= 0.059058:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(DOWN) - T(RIGHT)"] <= 0.021683:
                                                    return 3
                                                else:
                                                    return 0
                                    else:
                                        if features["E(DOWN)"] <= 0.000007:
                                            if features["E(UP) - E(DOWN)"] <= 0.801215:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["T(E(UP)) - T(E(RIGHT))"] <= 0.049181:
                                                if features["E(UP) - T(T(up))"] <= 0.041027:
                                                    if features["E(UP) - T(up)"] <= 0.016756:
                                                        return 3
                                                    else:
                                                        if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.022302:
                                                            return 0
                                                        else:
                                                            return 3
                                                else:
                                                    if features["T(RIGHT) - T(E(RIGHT))"] <= -0.011540:
                                                        if features["E(RIGHT) - agent_row"] <= -1.410263:
                                                            if features["E(UP) - T(RIGHT)"] <= 0.447537:
                                                                if features["T(LEFT) - T(E(DOWN))"] <= 0.371380:
                                                                    return 3
                                                                else:
                                                                    if features["T(RIGHT) - agent_row"] <= -8.999990:
                                                                        return 0
                                                                    else:
                                                                        return 3
                                                            else:
                                                                if features["E(UP) - agent_row"] <= -2.217009:
                                                                    if features["T(T(RIGHT)) - time_left"] <= -0.040333:
                                                                        return 3
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["E(UP) - T(T(RIGHT))"] <= 0.281720:
                                                            if features["E(DOWN) - E(LEFT)"] <= -0.041705:
                                                                if features["E(UP) - time_left"] <= 0.365377:
                                                                    if features["agent_row - time_left"] <= 7.860000:
                                                                        if features["T(DOWN) - T(LEFT)"] <= -0.002019:
                                                                            return 3
                                                                        else:
                                                                            return 0
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    return 3
                                                            else:
                                                                if features["T(up) - T(RIGHT)"] <= 0.030387:
                                                                    if features["T(T(RIGHT)) - time_left"] <= 0.006885:
                                                                        return 3
                                                                    else:
                                                                        return 0
                                                                else:
                                                                    return 3
                                                        else:
                                                            if features["E(LEFT) - T(T(LEFT))"] <= -0.559331:
                                                                return 0
                                                            else:
                                                                return 3
                                            else:
                                                if features["T(E(DOWN)) - agent_row"] <= -7.787758:
                                                    if features["E(UP) - T(up)"] <= 0.008086:
                                                        if features["E(UP) - time_left"] <= 0.225317:
                                                            return 3
                                                        else:
                                                            if features["E(DOWN) - T(E(DOWN))"] <= -0.082999:
                                                                return 3
                                                            else:
                                                                if features["T(E(RIGHT))"] <= 0.333113:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                    else:
                                                        if features["T(T(up)) - T(T(LEFT))"] <= 0.075179:
                                                            if features["T(DOWN) - T(E(DOWN))"] <= -0.034639:
                                                                return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            return 3
                                                else:
                                                    if features["T(LEFT) - agent_row"] <= -6.666616:
                                                        return 3
                                                    else:
                                                        if features["T(LEFT) - T(T(RIGHT))"] <= 0.290154:
                                                            if features["T(T(DOWN)) - agent_column"] <= -8.719964:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            return 3
                                else:
                                    if features["T(E(DOWN)) - time_left"] <= 0.152858:
                                        if features["T(T(DOWN)) - time_left"] <= 0.130153:
                                            if features["E(UP) - agent_column"] <= -12.866786:
                                                if features["T(LEFT) - time_left"] <= 0.120912:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["T(RIGHT)"] <= 0.114076:
                                                    if features["T(up)"] <= 0.000002:
                                                        return 0
                                                    else:
                                                        if features["T(RIGHT) - T(E(DOWN))"] <= -0.197701:
                                                            if features["T(LEFT) - T(E(RIGHT))"] <= 0.401696:
                                                                if features["E(RIGHT) - agent_column"] <= -11.925126:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["T(LEFT) - T(E(RIGHT))"] <= 0.414450:
                                                                if features["T(up) - time_left"] <= 0.788734:
                                                                    if features["T(E(LEFT)) - agent_column"] <= -1.979570:
                                                                        if features["T(RIGHT) - time_left"] <= -0.049984:
                                                                            return 3
                                                                        else:
                                                                            return 0
                                                                    else:
                                                                        if features["T(up) - T(T(RIGHT))"] <= 0.145004:
                                                                            return 0
                                                                        else:
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
                                        if features["T(LEFT) - time_left"] <= 0.584062:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.226376:
                                                if features["T(E(DOWN)) - T(T(DOWN))"] <= 0.069507:
                                                    if features["T(E(RIGHT)) - T(T(RIGHT))"] <= -0.032340:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(DOWN) - T(LEFT)"] <= -0.000013:
                                                        if features["E(RIGHT) - T(up)"] <= 0.140259:
                                                            if features["T(E(LEFT)) - agent_row"] <= -3.730188:
                                                                return 3
                                                            else:
                                                                return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 0
                                            else:
                                                if features["T(RIGHT)"] <= 0.000161:
                                                    if features["agent_row - agent_column"] <= -7.500000:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(LEFT) - agent_column"] <= -12.711174:
                                                        return 2
                                                    else:
                                                        return 0
                                        else:
                                            if features["T(E(DOWN)) - agent_row"] <= -7.709841:
                                                return 0
                                            else:
                                                if features["T(E(RIGHT)) - agent_column"] <= -8.832130:
                                                    return 0
                                                else:
                                                    return 3
                            else:
                                if features["E(RIGHT) - agent_row"] <= -1.492242:
                                    if features["T(DOWN) - T(LEFT)"] <= -0.000012:
                                        if features["E(UP) - E(DOWN)"] <= 0.306216:
                                            if features["E(UP) - time_left"] <= -0.002030:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.475520:
                                                    if features["T(E(UP)) - T(E(RIGHT))"] <= -0.065910:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    return 3
                                        else:
                                            return 0
                                    else:
                                        if features["T(E(UP)) - time_left"] <= -0.166923:
                                            if features["T(T(LEFT)) - time_left"] <= -0.266898:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["T(E(LEFT)) - time_left"] <= 0.020793:
                                                if features["T(LEFT) - agent_row"] <= -1.796199:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(LEFT) - T(E(UP))"] <= 0.580961:
                                                    if features["E(RIGHT) - T(E(DOWN))"] <= 0.646381:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(T(RIGHT)) - time_left"] <= 0.040057:
                                                        return 3
                                                    else:
                                                        return 0
                                else:
                                    if features["E(RIGHT) - T(T(up))"] <= 0.011034:
                                        return 1
                                    else:
                                        if features["E(LEFT)"] <= 0.000015:
                                            return 0
                                        else:
                                            return 3
                        else:
                            if features["T(E(LEFT)) - time_left"] <= -0.092883:
                                if features["E(RIGHT) - T(T(up))"] <= -0.149601:
                                    if features["T(E(UP)) - T(T(RIGHT))"] <= -0.353707:
                                        return 1
                                    else:
                                        return 0
                                else:
                                    if features["E(LEFT) - T(DOWN)"] <= 0.000337:
                                        if features["T(up) - time_left"] <= -0.449999:
                                            return 3
                                        else:
                                            if features["T(up) - agent_row"] <= -2.998514:
                                                if features["T(E(UP))"] <= 0.000884:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 3
                                    else:
                                        if features["E(RIGHT) - T(E(LEFT))"] <= 0.188182:
                                            return 0
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= -0.720299:
                                                return 0
                                            else:
                                                if features["T(RIGHT) - agent_column"] <= -2.393451:
                                                    return 3
                                                else:
                                                    return 0
                            else:
                                if features["T(LEFT)"] <= 0.097847:
                                    if features["E(UP) - time_left"] <= 0.237182:
                                        if features["T(T(RIGHT))"] <= 0.359277:
                                            if features["T(up) - T(DOWN)"] <= 0.002914:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 2
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -1.999997:
                                            if features["T(up) - T(T(RIGHT))"] <= 0.238051:
                                                return 0
                                            else:
                                                if features["E(DOWN) - T(RIGHT)"] <= -0.473724:
                                                    return 0
                                                else:
                                                    if features["E(RIGHT) - T(E(UP))"] <= -0.001356:
                                                        return 0
                                                    else:
                                                        return 3
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= -0.099708:
                                        return 0
                                    else:
                                        return 3
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.212334:
                            if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.104413:
                                if features["T(up) - T(E(RIGHT))"] <= 0.147461:
                                    if features["E(LEFT) - agent_column"] <= -10.702654:
                                        if features["E(RIGHT) - T(T(RIGHT))"] <= 0.005180:
                                            if features["E(UP) - T(RIGHT)"] <= 0.048926:
                                                return 2
                                            else:
                                                if features["E(LEFT) - time_left"] <= 0.273916:
                                                    return 0
                                                else:
                                                    return 2
                                        else:
                                            if features["T(E(RIGHT))"] <= 0.081515:
                                                return 0
                                            else:
                                                if features["E(DOWN) - T(LEFT)"] <= -0.281764:
                                                    return 0
                                                else:
                                                    return 3
                                    else:
                                        if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.105672:
                                            if features["T(up) - T(E(DOWN))"] <= 0.240361:
                                                if features["T(RIGHT)"] <= 0.000019:
                                                    return 0
                                                else:
                                                    if features["T(T(LEFT)) - agent_column"] <= -10.973569:
                                                        return 2
                                                    else:
                                                        if features["T(T(up)) - T(T(DOWN))"] <= 0.124317:
                                                            if features["T(up) - T(T(up))"] <= 0.116855:
                                                                return 0
                                                            else:
                                                                return 3
                                                        else:
                                                            if features["E(LEFT) - T(up)"] <= -0.000068:
                                                                return 3
                                                            else:
                                                                return 0
                                            else:
                                                if features["T(RIGHT) - time_left"] <= 0.194337:
                                                    return 3
                                                else:
                                                    return 0
                                        else:
                                            if features["T(up) - T(E(RIGHT))"] <= 0.106070:
                                                return 0
                                            else:
                                                return 2
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.248421:
                                        if features["T(E(LEFT)) - time_left"] <= 0.199302:
                                            if features["T(DOWN) - T(E(LEFT))"] <= -0.190509:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["E(RIGHT) - T(E(LEFT))"] <= -0.241432:
                                                if features["T(up) - T(E(DOWN))"] <= 0.535804:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                if features["E(RIGHT) - agent_row"] <= -5.691687:
                                                    return 0
                                                else:
                                                    return 2
                                    else:
                                        if features["E(LEFT) - time_left"] <= 0.347278:
                                            if features["T(up) - T(E(DOWN))"] <= 0.634294:
                                                if features["T(T(up)) - T(T(DOWN))"] <= -0.145197:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(T(RIGHT)) - agent_column"] <= -11.386960:
                                                return 1
                                            else:
                                                return 3
                            else:
                                if features["T(T(up)) - T(T(RIGHT))"] <= 0.080546:
                                    if features["T(DOWN) - time_left"] <= -0.069683:
                                        if features["T(LEFT) - T(E(DOWN))"] <= -0.000445:
                                            return 0
                                        else:
                                            if features["T(LEFT) - T(E(LEFT))"] <= 0.480508:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        if features["T(E(UP)) - T(T(up))"] <= -0.002233:
                                            if features["T(T(RIGHT))"] <= 0.280367:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 0
                                else:
                                    if features["T(up) - time_left"] <= 0.016004:
                                        if features["T(T(LEFT)) - time_left"] <= 0.448911:
                                            if features["T(E(DOWN)) - T(T(DOWN))"] <= 0.010035:
                                                if features["E(LEFT) - T(E(LEFT))"] <= -0.034382:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                        else:
                                            return 3
                                    else:
                                        return 3
                        else:
                            if features["E(DOWN) - E(RIGHT)"] <= -0.860155:
                                if features["E(LEFT)"] <= 0.000007:
                                    if features["E(LEFT) - T(RIGHT)"] <= -0.000004:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["T(E(RIGHT)) - T(T(up))"] <= 0.188712:
                                        return 3
                                    else:
                                        return 0
                            else:
                                if features["E(RIGHT) - T(E(LEFT))"] <= 0.384169:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.012763:
                                        return 0
                                    else:
                                        if features["T(RIGHT) - agent_column"] <= -2.999999:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    if features["E(LEFT)"] <= 0.000096:
                                        return 0
                                    else:
                                        if features["E(UP) - agent_column"] <= -11.249699:
                                            return 0
                                        else:
                                            if features["E(DOWN)"] <= 0.000015:
                                                return 0
                                            else:
                                                if features["T(RIGHT) - agent_row"] <= -6.886938:
                                                    return 0
                                                else:
                                                    return 3
                else:
                    if features["E(LEFT) - T(E(RIGHT))"] <= 0.177670:
                        if features["T(T(LEFT)) - T(T(RIGHT))"] <= 0.101520:
                            if features["E(DOWN) - T(up)"] <= 0.087500:
                                if features["T(E(UP)) - T(E(LEFT))"] <= -0.083771:
                                    return 2
                                else:
                                    return 3
                            else:
                                if features["E(LEFT) - time_left"] <= 0.253723:
                                    return 1
                                else:
                                    if features["T(RIGHT) - T(E(RIGHT))"] <= -0.070856:
                                        if features["T(DOWN) - T(E(RIGHT))"] <= -0.168741:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 2
                        else:
                            if features["T(RIGHT) - T(T(up))"] <= -0.014531:
                                return 1
                            else:
                                return 2
                    else:
                        if features["T(T(DOWN)) - T(T(LEFT))"] <= -0.102837:
                            if features["T(up) - T(E(LEFT))"] <= -0.349952:
                                return 2
                            else:
                                return 1
                        else:
                            if features["T(up) - T(LEFT)"] <= -0.217317:
                                if features["T(RIGHT) - T(E(LEFT))"] <= -0.286264:
                                    if features["T(DOWN) - T(LEFT)"] <= -0.000001:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.237901:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -9.530818:
                                            return 2
                                        else:
                                            return 0
                                else:
                                    return 0
                            else:
                                if features["T(DOWN) - agent_column"] <= -9.477319:
                                    return 2
                                else:
                                    if features["T(up) - T(E(UP))"] <= -0.164618:
                                        return 0
                                    else:
                                        return 2
            else:
                if features["E(UP) - T(E(LEFT))"] <= 0.010816:
                    if features["E(LEFT) - time_left"] <= 0.321014:
                        if features["T(DOWN)"] <= 0.000003:
                            if features["E(DOWN) - T(up)"] <= -0.365385:
                                if features["E(DOWN) - T(up)"] <= -0.626701:
                                    return 0
                                else:
                                    if features["agent_row - agent_column"] <= -0.500000:
                                        return 2
                                    else:
                                        return 0
                            else:
                                if features["T(E(DOWN)) - time_left"] <= -0.069611:
                                    return 0
                                else:
                                    if features["E(LEFT) - T(RIGHT)"] <= 0.271807:
                                        return 0
                                    else:
                                        return 2
                        else:
                            if features["E(UP) - T(E(DOWN))"] <= 0.031148:
                                if features["T(DOWN) - T(E(DOWN))"] <= 0.083541:
                                    if features["E(UP) - E(RIGHT)"] <= 0.189702:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    if features["T(E(UP)) - time_left"] <= -0.169504:
                                        if features["E(UP) - agent_column"] <= -6.680049:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        return 0
                            else:
                                if features["T(DOWN) - time_left"] <= -0.149992:
                                    if features["T(up) - agent_row"] <= -4.999681:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(LEFT) - agent_column"] <= -10.596171:
                                        if features["E(LEFT) - time_left"] <= 0.270865:
                                            if features["agent_row - agent_column"] <= -8.500000:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                                    else:
                                        return 0
                    else:
                        if features["T(up) - T(T(DOWN))"] <= 0.063199:
                            return 0
                        else:
                            if features["T(T(LEFT)) - agent_row"] <= -10.704960:
                                return 3
                            else:
                                if features["E(LEFT) - T(T(LEFT))"] <= -0.005331:
                                    return 1
                                else:
                                    return 2
                else:
                    if features["E(UP) - time_left"] <= 0.273542:
                        if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.072330:
                            if features["T(DOWN) - T(E(UP))"] <= -0.613061:
                                if features["T(T(LEFT)) - time_left"] <= -0.506629:
                                    return 2
                                else:
                                    return 3
                            else:
                                if features["E(UP) - T(T(DOWN))"] <= 0.818719:
                                    if features["E(RIGHT) - T(DOWN)"] <= 0.036762:
                                        return 0
                                    else:
                                        if features["T(DOWN) - time_left"] <= -0.024688:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    return 3
                        else:
                            if features["E(RIGHT) - T(DOWN)"] <= 0.121814:
                                if features["T(RIGHT)"] <= 0.000029:
                                    if features["E(RIGHT) - agent_row"] <= -6.941865:
                                        if features["E(UP) - T(E(DOWN))"] <= -0.020949:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.069819:
                                            return 0
                                        else:
                                            if features["T(up) - T(RIGHT)"] <= 0.000000:
                                                return 0
                                            else:
                                                return 3
                                else:
                                    if features["T(up) - time_left"] <= -0.759833:
                                        return 3
                                    else:
                                        if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.072287:
                                            return 3
                                        else:
                                            return 0
                            else:
                                if features["T(E(UP)) - T(T(DOWN))"] <= 0.490538:
                                    return 3
                                else:
                                    return 0
                    else:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.034035:
                            if features["E(LEFT) - T(E(LEFT))"] <= 0.146232:
                                if features["T(up) - T(T(up))"] <= 0.229150:
                                    if features["E(DOWN) - T(T(DOWN))"] <= 0.002397:
                                        return 0
                                    else:
                                        if features["E(RIGHT)"] <= 0.146577:
                                            if features["T(LEFT) - T(E(UP))"] <= -0.160162:
                                                return 2
                                            else:
                                                return 3
                                        else:
                                            return 0
                                else:
                                    if features["E(LEFT) - T(T(DOWN))"] <= 0.243667:
                                        if features["E(RIGHT) - T(up)"] <= -0.257151:
                                            return 0
                                        else:
                                            if features["T(E(LEFT)) - agent_column"] <= -6.732797:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        return 2
                            else:
                                if features["T(DOWN) - time_left"] <= -0.070000:
                                    return 3
                                else:
                                    return 0
                        else:
                            if features["E(RIGHT) - agent_row"] <= -11.827215:
                                if features["T(LEFT) - time_left"] <= 0.632129:
                                    if features["T(up) - T(E(LEFT))"] <= 0.023927:
                                        if features["T(E(RIGHT)) - T(T(up))"] <= 0.067609:
                                            if features["E(LEFT) - time_left"] <= 0.236507:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 0
                                    else:
                                        if features["T(LEFT) - T(T(DOWN))"] <= 0.404671:
                                            if features["E(DOWN) - T(up)"] <= -0.875260:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 0
                                else:
                                    if features["E(RIGHT) - T(E(DOWN))"] <= 0.154964:
                                        if features["E(LEFT) - T(E(UP))"] <= -0.077222:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        return 0
                            else:
                                if features["E(UP) - T(E(RIGHT))"] <= 0.100725:
                                    return 0
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -0.401599:
                                        return 0
                                    else:
                                        return 3
    else:
        if features["E(DOWN) - E(LEFT)"] <= 0.000000:
            if features["E(UP) - E(LEFT)"] <= 0.000000:
                if features["E(LEFT) - time_left"] <= 0.325169:
                    if features["E(UP)"] <= 0.011044:
                        if features["E(UP) - time_left"] <= -0.435082:
                            if features["T(T(DOWN)) - agent_column"] <= -3.942951:
                                if features["T(E(RIGHT))"] <= 0.000145:
                                    if features["T(up) - time_left"] <= -0.649674:
                                        return 0
                                    else:
                                        return 1
                                else:
                                    if features["T(E(RIGHT)) - agent_row"] <= 0.165701:
                                        if features["E(DOWN) - T(E(DOWN))"] <= 0.039858:
                                            if features["E(UP) - E(RIGHT)"] <= 0.000355:
                                                return 2
                                            else:
                                                if features["T(E(DOWN)) - T(T(up))"] <= 0.065508:
                                                    if features["T(LEFT) - T(E(DOWN))"] <= 0.306672:
                                                        return 2
                                                    else:
                                                        if features["E(LEFT) - time_left"] <= -0.043035:
                                                            return 0
                                                        else:
                                                            return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["E(UP)"] <= 0.000938:
                                                if features["T(T(DOWN)) - time_left"] <= -0.238899:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                    else:
                                        if features["T(LEFT) - agent_row"] <= 0.366999:
                                            return 2
                                        else:
                                            return 3
                            else:
                                if features["T(T(DOWN)) - time_left"] <= -0.284731:
                                    if features["E(DOWN) - agent_row"] <= -5.655729:
                                        return 0
                                    else:
                                        if features["T(E(LEFT)) - agent_row"] <= -0.625525:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    return 2
                        else:
                            if features["E(RIGHT) - T(RIGHT)"] <= -0.000004:
                                return 2
                            else:
                                if features["E(UP) - T(E(RIGHT))"] <= 0.002740:
                                    if features["E(RIGHT) - T(T(DOWN))"] <= -0.143566:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.000177:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        return 2
                                else:
                                    if features["T(DOWN) - T(T(up))"] <= 0.198868:
                                        return 2
                                    else:
                                        return 1
                    else:
                        if features["E(LEFT) - E(RIGHT)"] <= 0.365380:
                            if features["E(UP)"] <= 0.349352:
                                if features["E(UP) - E(LEFT)"] <= -0.042535:
                                    if features["E(DOWN) - T(E(UP))"] <= 0.157479:
                                        if features["T(up) - T(E(RIGHT))"] <= 0.144958:
                                            if features["E(LEFT) - T(E(UP))"] <= 0.331809:
                                                if features["T(up) - T(E(RIGHT))"] <= 0.018140:
                                                    if features["E(UP)"] <= 0.155427:
                                                        if features["T(T(DOWN)) - T(T(RIGHT))"] <= 0.025291:
                                                            return 3
                                                        else:
                                                            if features["E(LEFT) - T(LEFT)"] <= -0.009777:
                                                                return 0
                                                            else:
                                                                return 2
                                                    else:
                                                        if features["T(RIGHT) - agent_column"] <= -10.999993:
                                                            if features["E(DOWN) - T(DOWN)"] <= -0.438168:
                                                                return 2
                                                            else:
                                                                if features["T(LEFT) - T(T(RIGHT))"] <= 0.114168:
                                                                    return 2
                                                                else:
                                                                    if features["E(DOWN) - T(LEFT)"] <= -0.144444:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                        else:
                                                            return 0
                                                else:
                                                    if features["T(E(LEFT)) - time_left"] <= 0.242258:
                                                        return 0
                                                    else:
                                                        return 2
                                            else:
                                                return 2
                                        else:
                                            if features["time_left"] <= 0.100000:
                                                return 2
                                            else:
                                                if features["T(T(DOWN)) - agent_column"] <= -12.793445:
                                                    return 2
                                                else:
                                                    return 0
                                    else:
                                        if features["E(RIGHT) - T(up)"] <= 0.001966:
                                            if features["E(DOWN) - T(E(LEFT))"] <= 0.024225:
                                                return 2
                                            else:
                                                if features["T(up) - T(RIGHT)"] <= 0.000146:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            if features["T(up)"] <= 0.019307:
                                                if features["T(up) - agent_row"] <= -1.999931:
                                                    if features["E(UP) - agent_column"] <= -7.718590:
                                                        if features["E(UP) - T(LEFT)"] <= -0.207063:
                                                            if features["T(E(UP)) - agent_row"] <= -6.990844:
                                                                return 2
                                                            else:
                                                                if features["T(E(RIGHT)) - time_left"] <= -0.035628:
                                                                    return 0
                                                                else:
                                                                    if features["T(DOWN) - T(LEFT)"] <= -0.000013:
                                                                        return 1
                                                                    else:
                                                                        return 2
                                                        else:
                                                            if features["E(UP) - T(E(LEFT))"] <= 0.062844:
                                                                if features["agent_column - time_left"] <= 12.840000:
                                                                    return 2
                                                                else:
                                                                    return 3
                                                            else:
                                                                return 1
                                                    else:
                                                        return 0
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                else:
                                    if features["T(LEFT) - time_left"] <= -0.428358:
                                        return 0
                                    else:
                                        return 2
                            else:
                                if features["T(up) - T(E(RIGHT))"] <= 0.363560:
                                    if features["T(LEFT)"] <= 0.358130:
                                        if features["T(T(LEFT)) - agent_column"] <= -10.578247:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["T(T(up))"] <= 0.332890:
                                            return 0
                                        else:
                                            if features["E(LEFT) - T(up)"] <= 0.381591:
                                                return 2
                                            else:
                                                return 0
                                else:
                                    return 2
                        else:
                            if features["E(RIGHT)"] <= 0.018638:
                                if features["E(RIGHT) - time_left"] <= -0.495863:
                                    if features["E(UP) - time_left"] <= -0.720683:
                                        return 2
                                    else:
                                        if features["T(E(LEFT)) - T(T(RIGHT))"] <= 0.311316:
                                            if features["T(RIGHT) - T(E(DOWN))"] <= -0.285747:
                                                if features["T(up) - T(RIGHT)"] <= -0.000039:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["E(DOWN) - T(T(LEFT))"] <= -0.016504:
                                                    if features["T(DOWN) - T(T(up))"] <= 0.006437:
                                                        if features["T(up) - agent_row"] <= -4.535666:
                                                            return 0
                                                        else:
                                                            if features["T(T(RIGHT)) - agent_row"] <= -2.634625:
                                                                return 1
                                                            else:
                                                                return 2
                                                    else:
                                                        if features["T(LEFT) - T(E(RIGHT))"] <= -0.141383:
                                                            return 3
                                                        else:
                                                            if features["T(DOWN) - T(E(RIGHT))"] <= 0.419256:
                                                                return 2
                                                            else:
                                                                return 0
                                                else:
                                                    if features["E(DOWN) - T(DOWN)"] <= -0.358473:
                                                        return 1
                                                    else:
                                                        return 3
                                        else:
                                            if features["T(E(UP)) - time_left"] <= -0.038379:
                                                return 0
                                            else:
                                                return 1
                                else:
                                    if features["E(DOWN) - E(RIGHT)"] <= 0.003255:
                                        return 2
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -13.996428:
                                            return 0
                                        else:
                                            if features["T(E(UP)) - T(T(up))"] <= 0.061765:
                                                if features["E(DOWN) - T(E(UP))"] <= 0.355896:
                                                    return 2
                                                else:
                                                    if features["T(E(LEFT)) - T(T(RIGHT))"] <= -0.010756:
                                                        if features["T(DOWN) - time_left"] <= 0.403218:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        return 2
                                            else:
                                                if features["T(DOWN) - time_left"] <= -0.109467:
                                                    if features["E(DOWN) - T(E(DOWN))"] <= 0.247001:
                                                        return 2
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(DOWN) - time_left"] <= -0.107905:
                                                        return 0
                                                    else:
                                                        if features["T(up) - T(T(DOWN))"] <= -0.633121:
                                                            return 0
                                                        else:
                                                            return 2
                            else:
                                if features["E(DOWN) - T(E(UP))"] <= 0.137924:
                                    if features["E(DOWN) - T(DOWN)"] <= -0.300750:
                                        if features["T(up) - T(E(RIGHT))"] <= -0.076079:
                                            return 0
                                        else:
                                            if features["T(T(DOWN)) - agent_column"] <= -10.350135:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        if features["E(UP) - time_left"] <= 0.265539:
                                            if features["T(T(LEFT)) - time_left"] <= -0.075687:
                                                if features["T(E(RIGHT)) - agent_column"] <= -2.766758:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(E(UP)) - T(T(up))"] <= 0.143598:
                                                    if features["T(E(DOWN)) - T(E(LEFT))"] <= 0.054554:
                                                        return 2
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(T(DOWN)) - agent_row"] <= -7.643794:
                                                        return 0
                                                    else:
                                                        return 2
                                        else:
                                            return 0
                                else:
                                    if features["T(E(LEFT)) - time_left"] <= -0.132679:
                                        if features["E(UP) - T(T(RIGHT))"] <= -0.141996:
                                            if features["E(UP) - T(RIGHT)"] <= 0.104624:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 0
                                    else:
                                        if features["agent_column - time_left"] <= 4.800000:
                                            return 3
                                        else:
                                            if features["agent_row - time_left"] <= 2.860000:
                                                return 1
                                            else:
                                                return 2
                else:
                    if features["E(DOWN)"] <= 0.662705:
                        if features["E(UP)"] <= 0.817261:
                            if features["E(RIGHT) - T(up)"] <= 0.000162:
                                if features["T(T(up)) - agent_column"] <= -13.924463:
                                    if features["E(LEFT) - T(T(LEFT))"] <= 0.003097:
                                        return 1
                                    else:
                                        if features["E(LEFT) - T(E(DOWN))"] <= 0.102232:
                                            if features["T(E(DOWN)) - T(T(LEFT))"] <= 0.299834:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["E(UP) - T(up)"] <= 0.245746:
                                                return 2
                                            else:
                                                return 0
                                else:
                                    if features["E(UP)"] <= 0.673480:
                                        if features["E(RIGHT) - T(E(DOWN))"] <= 0.011051:
                                            if features["E(LEFT) - T(E(DOWN))"] <= 0.066031:
                                                if features["T(E(DOWN)) - T(T(LEFT))"] <= -0.027709:
                                                    if features["T(E(UP)) - T(E(RIGHT))"] <= 0.032914:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["T(DOWN) - T(LEFT)"] <= -0.404234:
                                                    if features["E(RIGHT)"] <= 0.000005:
                                                        return 2
                                                    else:
                                                        if features["E(UP) - T(E(LEFT))"] <= -0.021496:
                                                            return 2
                                                        else:
                                                            if features["E(DOWN) - T(E(LEFT))"] <= -0.291759:
                                                                return 2
                                                            else:
                                                                return 0
                                                else:
                                                    if features["E(DOWN) - agent_column"] <= -0.431560:
                                                        if features["E(RIGHT)"] <= 0.067381:
                                                            return 2
                                                        else:
                                                            if features["E(RIGHT)"] <= 0.069993:
                                                                return 0
                                                            else:
                                                                return 2
                                                    else:
                                                        return 1
                                        else:
                                            return 0
                                    else:
                                        if features["E(RIGHT)"] <= 0.000010:
                                            if features["T(T(DOWN)) - agent_column"] <= -1.307265:
                                                if features["T(E(DOWN)) - agent_column"] <= -12.829240:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -9.990005:
                                                return 0
                                            else:
                                                if features["T(E(RIGHT)) - agent_column"] <= -1.886261:
                                                    return 2
                                                else:
                                                    if features["T(E(LEFT)) - agent_row"] <= -3.855846:
                                                        return 0
                                                    else:
                                                        if features["T(E(DOWN)) - agent_column"] <= -0.985611:
                                                            return 2
                                                        else:
                                                            return 0
                            else:
                                if features["E(UP) - E(LEFT)"] <= -0.182324:
                                    if features["E(DOWN) - time_left"] <= 0.289319:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.044300:
                                            if features["T(DOWN) - agent_column"] <= -9.459497:
                                                return 2
                                            else:
                                                if features["E(UP) - T(E(RIGHT))"] <= 0.056219:
                                                    return 2
                                                else:
                                                    if features["T(DOWN) - T(E(DOWN))"] <= 0.218276:
                                                        return 2
                                                    else:
                                                        if features["T(DOWN) - agent_row"] <= -3.363854:
                                                            return 0
                                                        else:
                                                            return 2
                                        else:
                                            return 2
                                    else:
                                        if features["E(RIGHT) - T(E(LEFT))"] <= -0.323815:
                                            if features["E(DOWN) - T(DOWN)"] <= -0.460486:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["E(RIGHT)"] <= 0.004379:
                                                return 2
                                            else:
                                                return 1
                                else:
                                    if features["T(E(UP)) - agent_row"] <= -3.750374:
                                        if features["T(E(RIGHT))"] <= 0.037499:
                                            return 2
                                        else:
                                            if features["E(RIGHT)"] <= 0.011335:
                                                if features["E(UP) - T(E(LEFT))"] <= 0.373236:
                                                    if features["E(DOWN) - T(LEFT)"] <= -0.291278:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                                            else:
                                                if features["T(E(DOWN)) - agent_row"] <= -7.934741:
                                                    if features["T(LEFT) - agent_row"] <= -10.612760:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    return 0
                                    else:
                                        return 2
                        else:
                            if features["E(RIGHT) - agent_column"] <= -11.999998:
                                if features["T(up) - agent_column"] <= -11.236381:
                                    return 0
                                else:
                                    return 2
                            else:
                                if features["T(LEFT) - T(RIGHT)"] <= 0.617485:
                                    if features["E(RIGHT) - agent_row"] <= -10.999996:
                                        return 2
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -7.999999:
                                            if features["E(DOWN) - agent_row"] <= -9.999878:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(LEFT) - agent_row"] <= -5.997996:
                                                return 2
                                            else:
                                                if features["T(E(UP)) - agent_column"] <= -11.738319:
                                                    return 2
                                                else:
                                                    if features["T(T(DOWN)) - time_left"] <= 0.234331:
                                                        if features["E(DOWN)"] <= 0.000004:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 0
                                else:
                                    return 0
                    else:
                        if features["E(DOWN) - E(RIGHT)"] <= 0.854967:
                            if features["E(RIGHT)"] <= 0.000042:
                                if features["T(T(RIGHT)) - agent_column"] <= -11.934174:
                                    return 2
                                else:
                                    if features["E(DOWN) - E(LEFT)"] <= -0.009873:
                                        if features["T(DOWN) - agent_row"] <= -4.528627:
                                            if features["T(LEFT) - agent_column"] <= -3.469730:
                                                return 2
                                            else:
                                                if features["T(E(LEFT)) - agent_row"] <= -9.806614:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            return 2
                                    else:
                                        return 2
                            else:
                                if features["E(LEFT) - agent_row"] <= -9.296237:
                                    return 2
                                else:
                                    if features["E(UP) - agent_row"] <= -4.999890:
                                        if features["T(LEFT) - agent_row"] <= -9.733828:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(RIGHT) - agent_column"] <= -1.999380:
                                            return 2
                                        else:
                                            return 1
                        else:
                            if features["T(up) - T(LEFT)"] <= -0.006163:
                                if features["E(UP) - E(RIGHT)"] <= -0.000011:
                                    return 2
                                else:
                                    if features["E(LEFT) - agent_row"] <= -11.132235:
                                        if features["T(E(UP)) - agent_column"] <= -12.999232:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -8.697640:
                                            return 1
                                        else:
                                            if features["T(E(LEFT)) - agent_row"] <= -4.670258:
                                                if features["T(E(UP)) - agent_column"] <= -8.785217:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                return 2
                            else:
                                if features["E(LEFT) - agent_row"] <= -0.131985:
                                    if features["T(DOWN) - agent_row"] <= -4.451543:
                                        if features["T(E(RIGHT)) - agent_row"] <= -11.763014:
                                            return 2
                                        else:
                                            if features["T(T(up)) - agent_column"] <= -5.501965:
                                                return 1
                                            else:
                                                return 2
                                    else:
                                        return 2
                                else:
                                    return 1
            else:
                if features["E(LEFT) - E(RIGHT)"] <= 0.799568:
                    if features["E(DOWN) - agent_row"] <= -1.999915:
                        if features["T(up) - T(E(DOWN))"] <= 0.350635:
                            if features["E(DOWN) - T(up)"] <= 0.000016:
                                if features["E(DOWN) - E(RIGHT)"] <= 0.000141:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.001692:
                                        if features["E(RIGHT) - agent_column"] <= -8.999927:
                                            if features["T(T(up)) - agent_row"] <= -13.818646:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(DOWN)"] <= 0.000011:
                                                return 0
                                            else:
                                                if features["T(T(LEFT)) - time_left"] <= -0.582592:
                                                    return 3
                                                else:
                                                    if features["E(RIGHT) - T(E(LEFT))"] <= -0.283148:
                                                        if features["E(DOWN)"] <= 0.000163:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 0
                                    else:
                                        if features["agent_row - agent_column"] <= 0.500000:
                                            return 0
                                        else:
                                            return 2
                                else:
                                    return 2
                            else:
                                if features["E(RIGHT) - T(up)"] <= 0.045971:
                                    if features["E(DOWN) - agent_column"] <= -11.998149:
                                        return 0
                                    else:
                                        if features["T(T(DOWN)) - agent_column"] <= -2.627471:
                                            if features["E(LEFT) - agent_column"] <= -4.397701:
                                                if features["E(LEFT) - agent_column"] <= -10.529072:
                                                    if features["E(RIGHT) - T(T(up))"] <= -0.002310:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(DOWN) - agent_column"] <= -9.999750:
                                                        return 0
                                                    else:
                                                        if features["E(DOWN) - agent_column"] <= -7.995044:
                                                            if features["E(RIGHT) - T(up)"] <= 0.018213:
                                                                return 2
                                                            else:
                                                                return 0
                                                        else:
                                                            return 0
                                            else:
                                                if features["E(UP) - E(LEFT)"] <= 0.030112:
                                                    if features["T(E(LEFT)) - T(E(RIGHT))"] <= 0.048662:
                                                        return 0
                                                    else:
                                                        if features["T(RIGHT) - T(T(RIGHT))"] <= -0.668811:
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
                            if features["agent_row - time_left"] <= 13.780000:
                                if features["T(T(LEFT)) - time_left"] <= -0.669612:
                                    if features["T(LEFT) - T(E(UP))"] <= 0.068751:
                                        if features["E(LEFT) - T(E(DOWN))"] <= 0.512781:
                                            return 2
                                        else:
                                            return 3
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN)"] <= 0.000044:
                                        if features["T(E(LEFT)) - agent_column"] <= -4.658159:
                                            return 0
                                        else:
                                            if features["T(E(RIGHT)) - time_left"] <= -0.803176:
                                                if features["T(T(DOWN))"] <= 0.151358:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["T(T(up)) - agent_row"] <= -7.990059:
                                                    return 0
                                                else:
                                                    if features["T(up) - time_left"] <= 0.118135:
                                                        return 3
                                                    else:
                                                        return 0
                                    else:
                                        if features["E(RIGHT) - T(E(LEFT))"] <= -0.336562:
                                            if features["T(up) - T(E(DOWN))"] <= 0.353352:
                                                return 2
                                            else:
                                                if features["T(RIGHT) - T(T(up))"] <= -0.268246:
                                                    if features["E(LEFT) - T(T(LEFT))"] <= 0.366622:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(LEFT) - T(T(DOWN))"] <= 0.145366:
                                                        return 0
                                                    else:
                                                        return 2
                                        else:
                                            return 0
                            else:
                                if features["E(UP) - T(E(RIGHT))"] <= 0.312447:
                                    return 0
                                else:
                                    return 2
                    else:
                        if features["T(up) - T(DOWN)"] <= -0.246242:
                            if features["E(LEFT) - T(DOWN)"] <= 0.161581:
                                return 0
                            else:
                                return 2
                        else:
                            return 0
                else:
                    if features["T(E(DOWN)) - agent_column"] <= -7.925128:
                        if features["E(UP) - T(LEFT)"] <= 0.296475:
                            return 0
                        else:
                            if features["E(RIGHT) - agent_column"] <= -11.999974:
                                return 0
                            else:
                                if features["T(DOWN) - agent_column"] <= -10.529315:
                                    return 2
                                else:
                                    if features["E(DOWN)"] <= 0.000005:
                                        if features["E(DOWN) - agent_column"] <= -9.000000:
                                            return 0
                                        else:
                                            if features["T(E(LEFT)) - T(T(RIGHT))"] <= 0.023636:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        return 2
                    else:
                        if features["T(E(RIGHT)) - time_left"] <= 0.184524:
                            if features["T(E(RIGHT)) - time_left"] <= -0.604769:
                                return 1
                            else:
                                if features["T(up) - T(LEFT)"] <= -0.653255:
                                    if features["T(up) - agent_column"] <= -2.000000:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["E(UP)"] <= 0.867970:
                                        if features["T(T(DOWN)) - agent_column"] <= -5.766065:
                                            if features["T(DOWN) - T(E(RIGHT))"] <= 0.686078:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["T(up) - agent_column"] <= -3.676717:
                                                if features["T(DOWN) - agent_row"] <= -9.999997:
                                                    return 2
                                                else:
                                                    if features["agent_row - agent_column"] <= -4.500000:
                                                        return 2
                                                    else:
                                                        if features["T(E(LEFT)) - T(T(LEFT))"] <= 0.115256:
                                                            if features["E(DOWN) - T(up)"] <= 0.000001:
                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["T(T(up)) - agent_row"] <= -0.962621:
                                                                return 2
                                                            else:
                                                                return 0
                                            else:
                                                return 2
                                    else:
                                        if features["T(E(DOWN)) - agent_column"] <= -1.874916:
                                            return 2
                                        else:
                                            if features["agent_row - time_left"] <= 4.660000:
                                                return 2
                                            else:
                                                return 0
                        else:
                            if features["E(RIGHT) - agent_column"] <= -1.999931:
                                return 2
                            else:
                                if features["E(DOWN) - E(LEFT)"] <= -0.868056:
                                    return 2
                                else:
                                    return 0
        else:
            if features["E(DOWN)"] <= 0.867656:
                if features["E(UP)"] <= 0.000013:
                    if features["T(LEFT) - agent_row"] <= -10.831268:
                        if features["E(LEFT) - agent_row"] <= -11.236518:
                            return 2
                        else:
                            if features["E(LEFT) - agent_row"] <= -11.200412:
                                if features["T(E(LEFT)) - agent_column"] <= -3.628514:
                                    return 1
                                else:
                                    if features["T(T(up)) - agent_column"] <= -2.146365:
                                        return 2
                                    else:
                                        return 1
                            else:
                                if features["E(DOWN) - T(E(RIGHT))"] <= 0.529206:
                                    return 1
                                else:
                                    return 2
                    else:
                        if features["E(LEFT) - agent_row"] <= 0.351040:
                            if features["T(DOWN) - T(E(RIGHT))"] <= 0.479345:
                                if features["E(DOWN) - E(RIGHT)"] <= 0.799620:
                                    if features["T(E(UP)) - T(T(up))"] <= 0.416282:
                                        if features["E(DOWN) - agent_row"] <= -10.238043:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.003741:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(DOWN) - agent_column"] <= -8.132667:
                                        if features["T(DOWN) - agent_column"] <= -12.780684:
                                            if features["T(T(up)) - agent_column"] <= -12.889101:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 1
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -7.710068:
                                            return 2
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -3.999971:
                                                return 1
                                            else:
                                                return 2
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= -0.137414:
                                    return 1
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.850960:
                                        if features["agent_row - agent_column"] <= 4.500000:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 2
                        else:
                            if features["E(LEFT) - time_left"] <= 0.344470:
                                return 1
                            else:
                                if features["E(RIGHT) - agent_column"] <= -1.998123:
                                    return 2
                                else:
                                    return 1
                else:
                    if features["T(E(RIGHT)) - agent_row"] <= -9.982925:
                        if features["T(E(RIGHT)) - agent_row"] <= -10.939584:
                            if features["E(LEFT) - time_left"] <= -0.076719:
                                return 3
                            else:
                                if features["T(RIGHT) - agent_column"] <= -1.710854:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["T(LEFT) - agent_column"] <= -9.330721:
                                if features["E(UP) - E(DOWN)"] <= -0.730860:
                                    return 1
                                else:
                                    return 2
                            else:
                                if features["E(UP) - E(DOWN)"] <= -0.756237:
                                    return 1
                                else:
                                    return 2
                    else:
                        if features["T(up) - time_left"] <= -0.066855:
                            if features["E(DOWN) - T(E(UP))"] <= 0.332826:
                                if features["E(LEFT) - time_left"] <= -0.473533:
                                    return 0
                                else:
                                    if features["E(RIGHT)"] <= 0.010203:
                                        if features["T(LEFT) - T(E(DOWN))"] <= 0.151794:
                                            if features["E(LEFT) - T(E(LEFT))"] <= 0.228165:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 1
                                    else:
                                        if features["E(LEFT) - T(E(UP))"] <= 0.320049:
                                            if features["E(UP) - E(RIGHT)"] <= -0.042801:
                                                if features["T(RIGHT) - T(E(RIGHT))"] <= -0.029418:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(E(UP)) - T(E(LEFT))"] <= -0.122956:
                                                    if features["T(LEFT) - T(E(LEFT))"] <= 0.026240:
                                                        return 2
                                                    else:
                                                        if features["T(RIGHT) - T(E(UP))"] <= -0.071329:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    return 3
                                        else:
                                            return 0
                            else:
                                if features["T(DOWN) - T(E(RIGHT))"] <= 0.331521:
                                    if features["T(RIGHT) - time_left"] <= -0.069890:
                                        if features["T(T(RIGHT)) - agent_column"] <= -10.834491:
                                            if features["agent_column - time_left"] <= 12.540000:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["E(DOWN) - T(DOWN)"] <= 0.397041:
                                                if features["T(RIGHT) - T(T(LEFT))"] <= 0.139675:
                                                    if features["E(DOWN) - E(LEFT)"] <= 0.027450:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                    else:
                                        if features["E(RIGHT) - agent_column"] <= -1.999945:
                                            if features["T(E(DOWN)) - T(E(LEFT))"] <= 0.111029:
                                                if features["T(T(RIGHT)) - agent_row"] <= -4.656040:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - E(LEFT)"] <= 0.055081:
                                                        return 2
                                                    else:
                                                        return 1
                                            else:
                                                if features["E(DOWN) - time_left"] <= 0.126899:
                                                    return 3
                                                else:
                                                    if features["E(RIGHT)"] <= 0.000054:
                                                        return 2
                                                    else:
                                                        return 1
                                        else:
                                            return 1
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.180441:
                                        if features["T(E(RIGHT)) - agent_row"] <= -7.991827:
                                            return 2
                                        else:
                                            if features["T(up) - agent_row"] <= -3.999735:
                                                if features["T(up) - time_left"] <= -0.689902:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                    else:
                                        if features["T(E(UP)) - agent_row"] <= -4.953301:
                                            if features["T(DOWN) - T(E(DOWN))"] <= -0.047874:
                                                if features["E(UP) - E(DOWN)"] <= -0.675309:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(RIGHT) - T(up)"] <= 0.009939:
                                                if features["T(LEFT) - agent_row"] <= -1.573609:
                                                    if features["E(DOWN) - T(E(UP))"] <= 0.355984:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(UP) - agent_column"] <= -5.999688:
                                                        return 1
                                                    else:
                                                        return 2
                                            else:
                                                if features["E(DOWN) - T(T(DOWN))"] <= 0.584370:
                                                    return 1
                                                else:
                                                    return 2
                        else:
                            if features["E(DOWN) - T(E(UP))"] <= 0.203396:
                                return 3
                            else:
                                if features["T(LEFT) - agent_column"] <= -12.625475:
                                    return 1
                                else:
                                    if features["T(T(up)) - agent_column"] <= -12.808300:
                                        if features["E(LEFT) - E(RIGHT)"] <= 0.344359:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 1
            else:
                if features["E(DOWN) - agent_column"] <= -9.131965:
                    if features["T(E(RIGHT)) - agent_row"] <= -11.797545:
                        return 2
                    else:
                        if features["E(RIGHT) - agent_row"] <= 0.000002:
                            if features["T(E(RIGHT)) - agent_row"] <= -2.996092:
                                if features["T(E(LEFT)) - agent_row"] <= -3.636901:
                                    return 1
                                else:
                                    return 2
                            else:
                                return 1
                        else:
                            return 2
                else:
                    if features["T(RIGHT) - agent_row"] <= -4.591140:
                        if features["T(LEFT) - agent_row"] <= -7.990901:
                            if features["E(UP) - agent_column"] <= -4.999997:
                                if features["T(LEFT) - agent_column"] <= -7.710257:
                                    return 2
                                else:
                                    return 1
                            else:
                                if features["T(E(UP)) - agent_column"] <= -0.790355:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["agent_row - agent_column"] <= 5.500000:
                                if features["T(LEFT) - agent_row"] <= -4.999977:
                                    return 1
                                else:
                                    return 2
                            else:
                                return 2
                    else:
                        if features["agent_row - time_left"] <= 1.580000:
                            if features["T(E(LEFT)) - agent_row"] <= 0.119453:
                                if features["T(E(DOWN)) - agent_column"] <= -1.692126:
                                    if features["E(UP) - E(RIGHT)"] <= -0.000053:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                return 2
                        else:
                            return 2


def interpretable_action(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability,agent_position, time_left, gamma, size, valid_actions):
    input_representation = symbolic_representation(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability, agent_position, time_left, gamma, size)
    input_combinations   = get_feature_vector(input_representation)
    symbole_to_value     = {name: input_combinations[i] for i, name in enumerate(symbole_names)}
    action               = Index_to_Action[interpretable_strategy(symbole_to_value)]
    if action in valid_actions:
        return action
    else:
        return random.choice(valid_actions)
