import random
from INTERPRETER_2ND import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'T(E(UP))', 'T(E(DOWN))', 'T(E(LEFT))', 'T(E(RIGHT))', 'T(T(up))', 'T(T(DOWN))', 'T(T(LEFT))', 'T(T(RIGHT))', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - T(E(UP))', 'E(UP) - T(E(DOWN))', 'E(UP) - T(E(LEFT))', 'E(UP) - T(E(RIGHT))', 'E(UP) - T(T(up))', 'E(UP) - T(T(DOWN))', 'E(UP) - T(T(LEFT))', 'E(UP) - T(T(RIGHT))', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - T(E(UP))', 'E(DOWN) - T(E(DOWN))', 'E(DOWN) - T(E(LEFT))', 'E(DOWN) - T(E(RIGHT))', 'E(DOWN) - T(T(up))', 'E(DOWN) - T(T(DOWN))', 'E(DOWN) - T(T(LEFT))', 'E(DOWN) - T(T(RIGHT))', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - T(E(UP))', 'E(LEFT) - T(E(DOWN))', 'E(LEFT) - T(E(LEFT))', 'E(LEFT) - T(E(RIGHT))', 'E(LEFT) - T(T(up))', 'E(LEFT) - T(T(DOWN))', 'E(LEFT) - T(T(LEFT))', 'E(LEFT) - T(T(RIGHT))', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - T(E(UP))', 'E(RIGHT) - T(E(DOWN))', 'E(RIGHT) - T(E(LEFT))', 'E(RIGHT) - T(E(RIGHT))', 'E(RIGHT) - T(T(up))', 'E(RIGHT) - T(T(DOWN))', 'E(RIGHT) - T(T(LEFT))', 'E(RIGHT) - T(T(RIGHT))', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - T(E(UP))', 'T(up) - T(E(DOWN))', 'T(up) - T(E(LEFT))', 'T(up) - T(E(RIGHT))', 'T(up) - T(T(up))', 'T(up) - T(T(DOWN))', 'T(up) - T(T(LEFT))', 'T(up) - T(T(RIGHT))', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - T(E(UP))', 'T(DOWN) - T(E(DOWN))', 'T(DOWN) - T(E(LEFT))', 'T(DOWN) - T(E(RIGHT))', 'T(DOWN) - T(T(up))', 'T(DOWN) - T(T(DOWN))', 'T(DOWN) - T(T(LEFT))', 'T(DOWN) - T(T(RIGHT))', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - T(E(UP))', 'T(LEFT) - T(E(DOWN))', 'T(LEFT) - T(E(LEFT))', 'T(LEFT) - T(E(RIGHT))', 'T(LEFT) - T(T(up))', 'T(LEFT) - T(T(DOWN))', 'T(LEFT) - T(T(LEFT))', 'T(LEFT) - T(T(RIGHT))', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - T(E(UP))', 'T(RIGHT) - T(E(DOWN))', 'T(RIGHT) - T(E(LEFT))', 'T(RIGHT) - T(E(RIGHT))', 'T(RIGHT) - T(T(up))', 'T(RIGHT) - T(T(DOWN))', 'T(RIGHT) - T(T(LEFT))', 'T(RIGHT) - T(T(RIGHT))', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'T(E(UP)) - T(E(DOWN))', 'T(E(UP)) - T(E(LEFT))', 'T(E(UP)) - T(E(RIGHT))', 'T(E(UP)) - T(T(up))', 'T(E(UP)) - T(T(DOWN))', 'T(E(UP)) - T(T(LEFT))', 'T(E(UP)) - T(T(RIGHT))', 'T(E(UP)) - agent_row', 'T(E(UP)) - agent_column', 'T(E(UP)) - time_left', 'T(E(DOWN)) - T(E(LEFT))', 'T(E(DOWN)) - T(E(RIGHT))', 'T(E(DOWN)) - T(T(up))', 'T(E(DOWN)) - T(T(DOWN))', 'T(E(DOWN)) - T(T(LEFT))', 'T(E(DOWN)) - T(T(RIGHT))', 'T(E(DOWN)) - agent_row', 'T(E(DOWN)) - agent_column', 'T(E(DOWN)) - time_left', 'T(E(LEFT)) - T(E(RIGHT))', 'T(E(LEFT)) - T(T(up))', 'T(E(LEFT)) - T(T(DOWN))', 'T(E(LEFT)) - T(T(LEFT))', 'T(E(LEFT)) - T(T(RIGHT))', 'T(E(LEFT)) - agent_row', 'T(E(LEFT)) - agent_column', 'T(E(LEFT)) - time_left', 'T(E(RIGHT)) - T(T(up))', 'T(E(RIGHT)) - T(T(DOWN))', 'T(E(RIGHT)) - T(T(LEFT))', 'T(E(RIGHT)) - T(T(RIGHT))', 'T(E(RIGHT)) - agent_row', 'T(E(RIGHT)) - agent_column', 'T(E(RIGHT)) - time_left', 'T(T(up)) - T(T(DOWN))', 'T(T(up)) - T(T(LEFT))', 'T(T(up)) - T(T(RIGHT))', 'T(T(up)) - agent_row', 'T(T(up)) - agent_column', 'T(T(up)) - time_left', 'T(T(DOWN)) - T(T(LEFT))', 'T(T(DOWN)) - T(T(RIGHT))', 'T(T(DOWN)) - agent_row', 'T(T(DOWN)) - agent_column', 'T(T(DOWN)) - time_left', 'T(T(LEFT)) - T(T(RIGHT))', 'T(T(LEFT)) - agent_row', 'T(T(LEFT)) - agent_column', 'T(T(LEFT)) - time_left', 'T(T(RIGHT)) - agent_row', 'T(T(RIGHT)) - agent_column', 'T(T(RIGHT)) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(RIGHT)"] <= -0.000027:
        if features["E(DOWN) - E(RIGHT)"] <= -0.000045:
            if features["E(LEFT)"] <= 0.061088:
                if features["E(DOWN) - T(E(UP))"] <= 0.087089:
                    if features["E(UP) - E(RIGHT)"] <= -0.231175:
                        return 3
                    else:
                        if features["time_left"] <= 0.130000:
                            if features["E(UP) - E(LEFT)"] <= 0.213388:
                                if features["T(LEFT) - time_left"] <= 0.006868:
                                    return 3
                                else:
                                    return 2
                            else:
                                if features["T(LEFT) - T(E(UP))"] <= -0.383256:
                                    return 3
                                else:
                                    if features["E(RIGHT) - agent_column"] <= 0.433255:
                                        if features["E(LEFT) - time_left"] <= 0.046650:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(RIGHT) - T(up)"] <= 0.183167:
                                            return 1
                                        else:
                                            return 3
                        else:
                            return 3
                else:
                    if features["E(UP) - agent_row"] <= -0.998725:
                        if features["E(LEFT)"] <= 0.000011:
                            if features["E(LEFT) - E(RIGHT)"] <= -0.802056:
                                if features["T(LEFT) - agent_row"] <= -12.816344:
                                    return 3
                                else:
                                    return 1
                            else:
                                if features["T(T(up)) - agent_column"] <= 0.132787:
                                    return 3
                                else:
                                    return 1
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.339345:
                                if features["T(LEFT)"] <= 0.002950:
                                    return 3
                                else:
                                    return 1
                            else:
                                if features["E(DOWN) - E(RIGHT)"] <= -0.034944:
                                    if features["T(LEFT)"] <= 0.006313:
                                        return 3
                                    else:
                                        if features["T(RIGHT)"] <= 0.409354:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["E(DOWN) - agent_row"] <= -11.253242:
                                        return 3
                                    else:
                                        return 1
                    else:
                        if features["E(LEFT) - agent_column"] <= -0.969653:
                            return 3
                        else:
                            return 1
            else:
                if features["T(E(UP)) - T(T(up))"] <= 0.006232:
                    if features["E(DOWN) - T(RIGHT)"] <= -0.199348:
                        if features["T(LEFT) - agent_column"] <= -1.930036:
                            if features["E(LEFT) - T(E(UP))"] <= -0.183837:
                                return 3
                            else:
                                return 1
                        else:
                            return 2
                    else:
                        return 1
                else:
                    if features["T(DOWN) - T(RIGHT)"] <= -0.000001:
                        if features["E(LEFT)"] <= 0.099705:
                            return 3
                        else:
                            if features["T(up) - T(RIGHT)"] <= -0.000014:
                                if features["T(DOWN) - T(E(UP))"] <= -0.221480:
                                    return 2
                                else:
                                    return 1
                            else:
                                return 1
                    else:
                        return 3
        else:
            if features["E(LEFT) - T(E(RIGHT))"] <= 0.140074:
                if features["E(DOWN) - agent_row"] <= -12.131877:
                    return 3
                else:
                    if features["E(UP) - T(LEFT)"] <= 0.063156:
                        if features["E(RIGHT) - T(T(DOWN))"] <= 0.081216:
                            return 1
                        else:
                            if features["T(up) - T(T(DOWN))"] <= -0.290705:
                                return 3
                            else:
                                return 1
                    else:
                        if features["T(up) - T(RIGHT)"] <= -0.000021:
                            if features["E(RIGHT) - T(E(UP))"] <= 0.061935:
                                return 2
                            else:
                                return 1
                        else:
                            return 1
            else:
                if features["T(up) - agent_row"] <= -12.278811:
                    return 2
                else:
                    if features["agent_row - agent_column"] <= -6.500000:
                        if features["T(up) - T(LEFT)"] <= -0.292578:
                            if features["T(RIGHT) - time_left"] <= -0.017227:
                                if features["E(RIGHT) - T(LEFT)"] <= -0.369233:
                                    return 1
                                else:
                                    return 2
                            else:
                                return 1
                        else:
                            return 2
                    else:
                        return 1
    else:
        if features["E(UP) - E(LEFT)"] <= -0.000007:
            if features["E(DOWN) - E(LEFT)"] <= -0.151117:
                if features["E(UP)"] <= 0.662925:
                    if features["E(DOWN) - T(DOWN)"] <= 0.043890:
                        return 2
                    else:
                        if features["T(DOWN) - time_left"] <= -0.099983:
                            if features["T(up) - T(T(LEFT))"] <= -0.119698:
                                return 0
                            else:
                                return 2
                        else:
                            return 2
                else:
                    if features["E(RIGHT) - agent_column"] <= -1.999885:
                        return 2
                    else:
                        return 0
            else:
                if features["E(LEFT) - T(T(LEFT))"] <= 0.022197:
                    if features["E(LEFT) - T(DOWN)"] <= 0.090494:
                        if features["E(LEFT) - T(E(UP))"] <= 0.299931:
                            if features["E(UP) - T(up)"] <= 0.051442:
                                return 1
                            else:
                                return 2
                        else:
                            return 2
                    else:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.065769:
                            if features["T(E(UP)) - T(E(RIGHT))"] <= 0.099668:
                                return 1
                            else:
                                if features["E(UP) - time_left"] <= 0.210442:
                                    if features["T(up) - T(T(up))"] <= -0.007159:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    if features["E(DOWN) - E(RIGHT)"] <= 0.009381:
                                        return 0
                                    else:
                                        return 2
                        else:
                            return 3
                else:
                    if features["E(DOWN) - E(LEFT)"] <= 0.000008:
                        if features["E(RIGHT)"] <= 0.000028:
                            if features["E(LEFT)"] <= 0.824639:
                                return 2
                            else:
                                if features["T(T(up)) - agent_column"] <= -0.997839:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["T(up) - T(RIGHT)"] <= 0.000005:
                                return 2
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.125867:
                                    if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.089219:
                                        if features["T(RIGHT) - time_left"] <= -0.079996:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(RIGHT) - T(E(LEFT))"] <= -0.287937:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    return 1
                    else:
                        if features["E(LEFT)"] <= 0.863159:
                            if features["E(UP)"] <= 0.000066:
                                return 1
                            else:
                                return 2
                        else:
                            return 1
        else:
            if features["E(DOWN)"] <= 0.005315:
                if features["E(LEFT) - T(T(LEFT))"] <= 0.015674:
                    if features["E(RIGHT) - T(T(RIGHT))"] <= 0.037628:
                        if features["T(E(LEFT)) - agent_row"] <= -13.965623:
                            return 3
                        else:
                            return 0
                    else:
                        if features["E(RIGHT)"] <= 0.864141:
                            if features["E(LEFT) - agent_row"] <= -13.997240:
                                return 3
                            else:
                                if features["E(DOWN)"] <= 0.000038:
                                    if features["T(RIGHT) - agent_row"] <= -1.725747:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 0
                        else:
                            return 3
                else:
                    if features["E(UP) - E(DOWN)"] <= 0.803976:
                        if features["E(DOWN) - T(DOWN)"] <= -0.000005:
                            return 0
                        else:
                            if features["T(E(UP))"] <= 0.356589:
                                if features["E(UP) - agent_column"] <= -6.613058:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 0
                    else:
                        if features["E(DOWN) - agent_column"] <= -1.999998:
                            return 2
                        else:
                            return 0
            else:
                if features["E(RIGHT) - T(RIGHT)"] <= 0.194288:
                    if features["E(UP) - E(DOWN)"] <= 0.336412:
                        if features["T(E(LEFT)) - T(T(LEFT))"] <= -0.118478:
                            if features["E(LEFT) - T(LEFT)"] <= 0.204340:
                                return 3
                            else:
                                return 2
                        else:
                            if features["T(T(DOWN)) - agent_row"] <= -9.812414:
                                if features["T(T(DOWN)) - agent_row"] <= -9.833643:
                                    if features["E(UP) - time_left"] <= 0.306979:
                                        if features["T(up) - agent_column"] <= -1.473400:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["T(E(UP))"] <= 0.355138:
                                            if features["T(E(LEFT))"] <= 0.048879:
                                                return 3
                                            else:
                                                return 2
                                        else:
                                            if features["T(up) - T(RIGHT)"] <= 0.221558:
                                                if features["T(T(LEFT)) - time_left"] <= 0.275027:
                                                    return 0
                                                else:
                                                    return 1
                                            else:
                                                return 2
                                else:
                                    if features["E(UP) - time_left"] <= 0.280889:
                                        return 2
                                    else:
                                        return 0
                            else:
                                if features["E(DOWN) - time_left"] <= 0.210888:
                                    return 2
                                else:
                                    return 1
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.125661:
                            if features["E(LEFT)"] <= 0.283895:
                                return 0
                            else:
                                return 2
                        else:
                            if features["E(UP) - time_left"] <= 0.323566:
                                return 3
                            else:
                                if features["E(UP) - T(up)"] <= -0.000724:
                                    return 2
                                else:
                                    return 0
                else:
                    if features["T(up) - T(LEFT)"] <= -0.000022:
                        if features["E(UP) - T(up)"] <= 0.415506:
                            return 3
                        else:
                            return 0
                    else:
                        if features["E(UP) - T(E(LEFT))"] <= 0.247313:
                            if features["E(DOWN) - T(E(LEFT))"] <= -0.203676:
                                return 2
                            else:
                                return 1
                        else:
                            return 3


def interpretable_action(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability,agent_position, time_left, gamma, size, valid_actions):
    input_representation = symbolic_representation(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability, agent_position, time_left, gamma, size)
    input_combinations   = get_feature_vector(input_representation)
    symbole_to_value     = {name: input_combinations[i] for i, name in enumerate(symbole_names)}
    action               = Index_to_Action[interpretable_strategy(symbole_to_value)]
    if action in valid_actions:
        return action
    else:
        return random.choice(valid_actions)
