import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(RIGHT)"] <= -0.000000:
        if features["E(LEFT) - E(RIGHT)"] <= -0.297094:
            if features["E(DOWN) - E(RIGHT)"] <= -0.211732:
                if features["E(UP) - E(RIGHT)"] <= -0.149560:
                    return 3
                else:
                    if features["E(LEFT)"] <= 0.000013:
                        if features["E(DOWN) - E(RIGHT)"] <= -0.800676:
                            return 0
                        else:
                            if features["E(UP) - agent_column"] <= 0.355618:
                                return 3
                            else:
                                return 0
                    else:
                        if features["E(DOWN) - T(LEFT)"] <= 0.003317:
                            if features["E(LEFT) - agent_column"] <= -3.999545:
                                if features["E(DOWN) - agent_column"] <= -10.997350:
                                    return 0
                                else:
                                    return 3
                            else:
                                return 0
                        else:
                            if features["E(LEFT)"] <= 0.009738:
                                if features["agent_row - time_left"] <= 12.950000:
                                    return 3
                                else:
                                    return 0
                            else:
                                return 3
            else:
                if features["E(DOWN) - E(RIGHT)"] <= 0.000005:
                    if features["E(LEFT)"] <= 0.001843:
                        if features["E(RIGHT) - agent_column"] <= -11.209213:
                            return 1
                        else:
                            return 3
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.370132:
                            if features["T(up) - T(LEFT)"] <= 0.000000:
                                return 3
                            else:
                                if features["T(LEFT)"] <= 0.013732:
                                    if features["T(RIGHT) - agent_column"] <= -1.593410:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    return 1
                        else:
                            return 3
                else:
                    if features["E(DOWN) - agent_row"] <= -11.223721:
                        return 3
                    else:
                        if features["E(RIGHT)"] <= 0.860628:
                            if features["E(RIGHT) - agent_row"] <= 0.337696:
                                return 1
                            else:
                                if features["E(RIGHT) - time_left"] <= 0.312497:
                                    if features["E(DOWN) - time_left"] <= -0.242060:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 3
                        else:
                            if features["T(LEFT) - agent_row"] <= -6.637433:
                                return 1
                            else:
                                return 3
        else:
            if features["E(UP) - T(up)"] <= 0.011759:
                if features["E(DOWN) - E(LEFT)"] <= 0.099465:
                    if features["E(UP) - T(DOWN)"] <= 0.230093:
                        if features["E(DOWN) - E(LEFT)"] <= 0.000057:
                            if features["E(DOWN) - E(LEFT)"] <= -0.171916:
                                return 2
                            else:
                                if features["E(DOWN) - agent_column"] <= -2.132491:
                                    if features["E(UP) - time_left"] <= 0.015401:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN) - agent_column"] <= -0.132174:
                                        return 1
                                    else:
                                        return 2
                        else:
                            if features["E(LEFT) - agent_row"] <= -12.132407:
                                return 2
                            else:
                                if features["E(LEFT) - agent_column"] <= -12.634139:
                                    return 2
                                else:
                                    if features["time_left"] <= 0.110000:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.369512:
                                            return 1
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= -0.398676:
                                                return 1
                                            else:
                                                return 2
                                    else:
                                        return 1
                    else:
                        if features["E(LEFT) - T(LEFT)"] <= 0.003455:
                            return 3
                        else:
                            if features["T(LEFT)"] <= 0.000000:
                                return 2
                            else:
                                return 1
                else:
                    return 1
            else:
                if features["E(RIGHT) - T(RIGHT)"] <= 0.143876:
                    if features["E(RIGHT) - agent_row"] <= -4.685858:
                        if features["E(UP) - agent_row"] <= -4.880718:
                            if features["E(LEFT) - T(LEFT)"] <= 0.123447:
                                if features["E(DOWN) - T(RIGHT)"] <= -0.286476:
                                    return 0
                                else:
                                    return 1
                            else:
                                return 2
                        else:
                            if features["T(DOWN) - agent_column"] <= -1.500968:
                                return 2
                            else:
                                return 0
                    else:
                        if features["E(DOWN) - time_left"] <= 0.247675:
                            if features["E(DOWN) - T(DOWN)"] <= -0.226842:
                                return 0
                            else:
                                return 2
                        else:
                            return 1
                else:
                    if features["E(DOWN) - time_left"] <= 0.299833:
                        return 3
                    else:
                        if features["T(up)"] <= 0.000000:
                            return 3
                        else:
                            return 1
    else:
        if features["E(UP) - E(LEFT)"] <= -0.000030:
            if features["E(DOWN) - E(LEFT)"] <= -0.171915:
                if features["E(UP)"] <= 0.662889:
                    if features["E(RIGHT) - T(RIGHT)"] <= 0.000000:
                        return 2
                    else:
                        if features["E(UP) - T(up)"] <= 0.301454:
                            return 2
                        else:
                            return 0
                else:
                    if features["E(RIGHT) - agent_column"] <= -1.999995:
                        return 2
                    else:
                        return 0
            else:
                if features["E(UP) - T(RIGHT)"] <= 0.000000:
                    if features["E(RIGHT) - agent_column"] <= -1.999997:
                        return 2
                    else:
                        return 1
                else:
                    if features["E(UP) - T(LEFT)"] <= -0.083756:
                        if features["T(RIGHT)"] <= 0.012803:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.276562:
                                if features["E(UP) - T(up)"] <= 0.149877:
                                    return 1
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.529145:
                                        return 2
                                    else:
                                        return 3
                            else:
                                if features["agent_column - time_left"] <= 13.990000:
                                    if features["agent_column - time_left"] <= 12.950000:
                                        if features["E(DOWN) - agent_column"] <= -9.615190:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(DOWN) - T(LEFT)"] <= -0.145469:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    return 2
                        else:
                            if features["T(up)"] <= 0.185291:
                                if features["E(RIGHT) - time_left"] <= -0.033819:
                                    return 2
                                else:
                                    return 1
                            else:
                                if features["E(UP) - T(RIGHT)"] <= 0.068878:
                                    return 2
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.348333:
                                        if features["E(DOWN) - agent_row"] <= -7.763823:
                                            if features["E(UP) - agent_column"] <= -8.740408:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 1
                                    else:
                                        return 2
                    else:
                        if features["E(DOWN) - agent_column"] <= -7.783486:
                            return 2
                        else:
                            if features["E(UP) - T(up)"] <= -0.015402:
                                return 1
                            else:
                                return 2
        else:
            if features["E(UP) - E(DOWN)"] <= 0.363752:
                if features["E(UP) - E(LEFT)"] <= 0.127116:
                    if features["T(LEFT) - T(RIGHT)"] <= 0.289785:
                        if features["E(DOWN) - T(DOWN)"] <= 0.014026:
                            if features["T(up)"] <= 0.389408:
                                if features["E(RIGHT) - time_left"] <= 0.230585:
                                    if features["E(DOWN)"] <= 0.036324:
                                        return 0
                                    else:
                                        if features["T(up)"] <= 0.000079:
                                            return 2
                                        else:
                                            if features["E(UP) - T(up)"] <= -0.013475:
                                                return 0
                                            else:
                                                return 2
                                else:
                                    return 0
                            else:
                                return 0
                        else:
                            if features["E(UP) - E(RIGHT)"] <= 0.083751:
                                if features["T(DOWN) - T(LEFT)"] <= -0.000000:
                                    return 1
                                else:
                                    return 2
                            else:
                                return 2
                    else:
                        if features["T(up)"] <= 0.351253:
                            return 0
                        else:
                            return 2
                else:
                    if features["E(UP) - E(DOWN)"] <= 0.283892:
                        if features["T(LEFT) - agent_row"] <= -10.456088:
                            if features["E(DOWN)"] <= 0.019563:
                                return 0
                            else:
                                return 1
                        else:
                            if features["E(UP) - time_left"] <= 0.254256:
                                return 2
                            else:
                                return 0
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.321402:
                            if features["agent_row - time_left"] <= 6.870000:
                                return 2
                            else:
                                return 0
                        else:
                            return 3
            else:
                if features["E(LEFT) - T(LEFT)"] <= 0.250779:
                    if features["E(RIGHT) - agent_row"] <= -0.569924:
                        if features["E(UP) - time_left"] <= 0.339702:
                            if features["E(DOWN)"] <= 0.000785:
                                return 0
                            else:
                                if features["E(RIGHT)"] <= 0.065964:
                                    return 2
                                else:
                                    return 0
                        else:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.303005:
                                return 0
                            else:
                                if features["E(DOWN)"] <= 0.000001:
                                    if features["E(UP)"] <= 0.808728:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 0
                    else:
                        return 3
                else:
                    if features["E(DOWN) - agent_row"] <= -1.999960:
                        if features["E(DOWN) - T(DOWN)"] <= -0.000000:
                            if features["E(UP) - E(DOWN)"] <= 0.802816:
                                return 0
                            else:
                                if features["T(DOWN) - agent_column"] <= -1.748794:
                                    return 2
                                else:
                                    return 0
                        else:
                            if features["E(RIGHT) - agent_column"] <= -7.904948:
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
