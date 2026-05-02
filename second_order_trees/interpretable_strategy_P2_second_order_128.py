import random
from INTERPRETER_2ND import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'T(E(UP))', 'T(E(DOWN))', 'T(E(LEFT))', 'T(E(RIGHT))', 'T(T(up))', 'T(T(DOWN))', 'T(T(LEFT))', 'T(T(RIGHT))', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - T(E(UP))', 'E(UP) - T(E(DOWN))', 'E(UP) - T(E(LEFT))', 'E(UP) - T(E(RIGHT))', 'E(UP) - T(T(up))', 'E(UP) - T(T(DOWN))', 'E(UP) - T(T(LEFT))', 'E(UP) - T(T(RIGHT))', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - T(E(UP))', 'E(DOWN) - T(E(DOWN))', 'E(DOWN) - T(E(LEFT))', 'E(DOWN) - T(E(RIGHT))', 'E(DOWN) - T(T(up))', 'E(DOWN) - T(T(DOWN))', 'E(DOWN) - T(T(LEFT))', 'E(DOWN) - T(T(RIGHT))', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - T(E(UP))', 'E(LEFT) - T(E(DOWN))', 'E(LEFT) - T(E(LEFT))', 'E(LEFT) - T(E(RIGHT))', 'E(LEFT) - T(T(up))', 'E(LEFT) - T(T(DOWN))', 'E(LEFT) - T(T(LEFT))', 'E(LEFT) - T(T(RIGHT))', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - T(E(UP))', 'E(RIGHT) - T(E(DOWN))', 'E(RIGHT) - T(E(LEFT))', 'E(RIGHT) - T(E(RIGHT))', 'E(RIGHT) - T(T(up))', 'E(RIGHT) - T(T(DOWN))', 'E(RIGHT) - T(T(LEFT))', 'E(RIGHT) - T(T(RIGHT))', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - T(E(UP))', 'T(up) - T(E(DOWN))', 'T(up) - T(E(LEFT))', 'T(up) - T(E(RIGHT))', 'T(up) - T(T(up))', 'T(up) - T(T(DOWN))', 'T(up) - T(T(LEFT))', 'T(up) - T(T(RIGHT))', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - T(E(UP))', 'T(DOWN) - T(E(DOWN))', 'T(DOWN) - T(E(LEFT))', 'T(DOWN) - T(E(RIGHT))', 'T(DOWN) - T(T(up))', 'T(DOWN) - T(T(DOWN))', 'T(DOWN) - T(T(LEFT))', 'T(DOWN) - T(T(RIGHT))', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - T(E(UP))', 'T(LEFT) - T(E(DOWN))', 'T(LEFT) - T(E(LEFT))', 'T(LEFT) - T(E(RIGHT))', 'T(LEFT) - T(T(up))', 'T(LEFT) - T(T(DOWN))', 'T(LEFT) - T(T(LEFT))', 'T(LEFT) - T(T(RIGHT))', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - T(E(UP))', 'T(RIGHT) - T(E(DOWN))', 'T(RIGHT) - T(E(LEFT))', 'T(RIGHT) - T(E(RIGHT))', 'T(RIGHT) - T(T(up))', 'T(RIGHT) - T(T(DOWN))', 'T(RIGHT) - T(T(LEFT))', 'T(RIGHT) - T(T(RIGHT))', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'T(E(UP)) - T(E(DOWN))', 'T(E(UP)) - T(E(LEFT))', 'T(E(UP)) - T(E(RIGHT))', 'T(E(UP)) - T(T(up))', 'T(E(UP)) - T(T(DOWN))', 'T(E(UP)) - T(T(LEFT))', 'T(E(UP)) - T(T(RIGHT))', 'T(E(UP)) - agent_row', 'T(E(UP)) - agent_column', 'T(E(UP)) - time_left', 'T(E(DOWN)) - T(E(LEFT))', 'T(E(DOWN)) - T(E(RIGHT))', 'T(E(DOWN)) - T(T(up))', 'T(E(DOWN)) - T(T(DOWN))', 'T(E(DOWN)) - T(T(LEFT))', 'T(E(DOWN)) - T(T(RIGHT))', 'T(E(DOWN)) - agent_row', 'T(E(DOWN)) - agent_column', 'T(E(DOWN)) - time_left', 'T(E(LEFT)) - T(E(RIGHT))', 'T(E(LEFT)) - T(T(up))', 'T(E(LEFT)) - T(T(DOWN))', 'T(E(LEFT)) - T(T(LEFT))', 'T(E(LEFT)) - T(T(RIGHT))', 'T(E(LEFT)) - agent_row', 'T(E(LEFT)) - agent_column', 'T(E(LEFT)) - time_left', 'T(E(RIGHT)) - T(T(up))', 'T(E(RIGHT)) - T(T(DOWN))', 'T(E(RIGHT)) - T(T(LEFT))', 'T(E(RIGHT)) - T(T(RIGHT))', 'T(E(RIGHT)) - agent_row', 'T(E(RIGHT)) - agent_column', 'T(E(RIGHT)) - time_left', 'T(T(up)) - T(T(DOWN))', 'T(T(up)) - T(T(LEFT))', 'T(T(up)) - T(T(RIGHT))', 'T(T(up)) - agent_row', 'T(T(up)) - agent_column', 'T(T(up)) - time_left', 'T(T(DOWN)) - T(T(LEFT))', 'T(T(DOWN)) - T(T(RIGHT))', 'T(T(DOWN)) - agent_row', 'T(T(DOWN)) - agent_column', 'T(T(DOWN)) - time_left', 'T(T(LEFT)) - T(T(RIGHT))', 'T(T(LEFT)) - agent_row', 'T(T(LEFT)) - agent_column', 'T(T(LEFT)) - time_left', 'T(T(RIGHT)) - agent_row', 'T(T(RIGHT)) - agent_column', 'T(T(RIGHT)) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(LEFT) - E(RIGHT)"] <= 0.328223:
        if features["E(UP) - E(RIGHT)"] <= 0.000008:
            if features["E(DOWN) - E(RIGHT)"] <= -0.000019:
                if features["E(UP) - E(RIGHT)"] <= -0.178779:
                    if features["E(DOWN) - E(LEFT)"] <= 0.799831:
                        if features["E(LEFT) - T(up)"] <= 0.026435:
                            if features["E(DOWN) - T(E(UP))"] <= 0.252770:
                                return 3
                            else:
                                if features["E(LEFT)"] <= 0.000028:
                                    return 3
                                else:
                                    if features["T(up) - agent_column"] <= -0.982358:
                                        return 3
                                    else:
                                        return 1
                        else:
                            return 3
                    else:
                        if features["T(DOWN) - agent_column"] <= -12.415015:
                            return 1
                        else:
                            return 3
                else:
                    if features["E(LEFT) - T(up)"] <= 0.019067:
                        if features["T(E(UP)) - agent_column"] <= -1.692725:
                            if features["E(DOWN) - E(RIGHT)"] <= -0.865142:
                                if features["E(DOWN)"] <= 0.000022:
                                    return 3
                                else:
                                    return 0
                            else:
                                if features["T(E(UP)) - T(E(RIGHT))"] <= 0.143056:
                                    return 3
                                else:
                                    return 0
                        else:
                            if features["E(DOWN) - E(LEFT)"] <= 0.013104:
                                if features["E(RIGHT) - time_left"] <= 0.283622:
                                    return 3
                                else:
                                    if features["E(LEFT) - agent_column"] <= -1.992950:
                                        return 3
                                    else:
                                        return 0
                            else:
                                if features["T(DOWN) - T(T(DOWN))"] <= -0.009049:
                                    if features["T(DOWN) - T(E(UP))"] <= -0.318576:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["T(up) - T(T(up))"] <= -0.016569:
                                        return 3
                                    else:
                                        return 0
                    else:
                        if features["T(DOWN) - T(LEFT)"] <= -0.000016:
                            return 3
                        else:
                            if features["T(LEFT) - agent_column"] <= -2.999943:
                                return 0
                            else:
                                if features["T(E(RIGHT)) - agent_row"] <= -8.594837:
                                    return 0
                                else:
                                    return 3
            else:
                if features["E(UP)"] <= 0.010301:
                    if features["E(RIGHT) - T(T(RIGHT))"] <= 0.020582:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.033703:
                            if features["E(DOWN) - time_left"] <= 0.153222:
                                return 1
                            else:
                                if features["E(LEFT) - T(E(LEFT))"] <= 0.148033:
                                    return 1
                                else:
                                    return 3
                        else:
                            return 1
                    else:
                        if features["E(DOWN) - agent_row"] <= -1.265700:
                            if features["E(DOWN) - agent_row"] <= -11.200458:
                                return 3
                            else:
                                if features["T(DOWN) - T(LEFT)"] <= 0.367348:
                                    if features["E(UP) - E(DOWN)"] <= -0.801149:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 1
                        else:
                            if features["E(LEFT) - time_left"] <= 0.025716:
                                if features["agent_column - time_left"] <= 12.450000:
                                    return 3
                                else:
                                    return 1
                            else:
                                return 1
                else:
                    if features["E(LEFT) - T(E(RIGHT))"] <= 0.070581:
                        if features["E(UP) - T(LEFT)"] <= 0.081204:
                            if features["E(UP)"] <= 0.101354:
                                if features["T(E(DOWN)) - time_left"] <= 0.359243:
                                    return 3
                                else:
                                    if features["T(E(UP)) - time_left"] <= 0.030499:
                                        return 1
                                    else:
                                        if features["T(E(DOWN)) - T(T(DOWN))"] <= 0.001826:
                                            return 0
                                        else:
                                            return 3
                            else:
                                return 3
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= 0.000033:
                                return 3
                            else:
                                return 0
                    else:
                        if features["E(DOWN) - time_left"] <= 0.283402:
                            if features["E(UP) - T(E(DOWN))"] <= -0.233071:
                                return 3
                            else:
                                if features["T(up)"] <= 0.000007:
                                    return 0
                                else:
                                    if features["E(UP) - T(E(DOWN))"] <= 0.083625:
                                        return 3
                                    else:
                                        return 0
                        else:
                            if features["E(UP) - T(E(DOWN))"] <= -0.278007:
                                return 1
                            else:
                                if features["T(DOWN) - T(T(up))"] <= 0.252822:
                                    if features["E(DOWN) - E(LEFT)"] <= 0.066101:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 0
        else:
            if features["E(UP) - T(E(DOWN))"] <= 0.126921:
                if features["E(LEFT) - time_left"] <= 0.310215:
                    if features["E(UP)"] <= 0.093122:
                        if features["E(LEFT)"] <= 0.231646:
                            return 1
                        else:
                            if features["T(DOWN) - T(E(UP))"] <= 0.310262:
                                return 2
                            else:
                                return 1
                    else:
                        if features["T(DOWN) - T(LEFT)"] <= 0.000001:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.132614:
                                if features["E(DOWN) - T(LEFT)"] <= -0.490142:
                                    return 0
                                else:
                                    return 3
                            else:
                                if features["T(RIGHT)"] <= 0.027644:
                                    if features["E(RIGHT) - T(up)"] <= 0.086602:
                                        return 0
                                    else:
                                        if features["T(LEFT) - T(E(DOWN))"] <= 0.396829:
                                            return 3
                                        else:
                                            return 0
                                else:
                                    return 0
                        else:
                            if features["T(E(UP)) - time_left"] <= -0.208529:
                                return 3
                            else:
                                if features["T(up)"] <= 0.098893:
                                    return 0
                                else:
                                    return 3
                else:
                    if features["E(LEFT) - T(LEFT)"] <= -0.007216:
                        if features["E(UP) - T(RIGHT)"] <= 0.107556:
                            return 1
                        else:
                            return 0
                    else:
                        if features["E(LEFT) - time_left"] <= 0.365920:
                            return 2
                        else:
                            return 1
            else:
                if features["E(UP) - E(RIGHT)"] <= 0.111293:
                    if features["E(DOWN) - agent_row"] <= -1.999998:
                        if features["E(UP) - T(E(RIGHT))"] <= 0.035743:
                            if features["T(up) - T(T(RIGHT))"] <= 0.006699:
                                return 0
                            else:
                                if features["E(DOWN)"] <= 0.046146:
                                    return 0
                                else:
                                    return 3
                        else:
                            if features["E(UP) - E(DOWN)"] <= 0.804435:
                                if features["E(DOWN)"] <= 0.000010:
                                    return 0
                                else:
                                    if features["T(RIGHT) - T(T(LEFT))"] <= 0.204331:
                                        if features["T(E(RIGHT))"] <= 0.289975:
                                            return 0
                                        else:
                                            if features["T(E(UP)) - T(T(up))"] <= 0.000359:
                                                return 3
                                            else:
                                                if features["E(RIGHT)"] <= 0.303910:
                                                    return 3
                                                else:
                                                    return 0
                                    else:
                                        return 0
                            else:
                                return 0
                    else:
                        return 3
                else:
                    if features["E(UP) - T(E(LEFT))"] <= 0.010816:
                        if features["T(up) - T(E(RIGHT))"] <= 0.188014:
                            return 0
                        else:
                            if features["E(LEFT) - time_left"] <= 0.289310:
                                return 0
                            else:
                                return 2
                    else:
                        return 0
    else:
        if features["E(DOWN) - E(LEFT)"] <= 0.000001:
            if features["E(UP) - E(LEFT)"] <= -0.000000:
                if features["E(RIGHT) - T(up)"] <= 0.004446:
                    if features["E(DOWN) - E(RIGHT)"] <= 0.665843:
                        if features["E(UP) - T(RIGHT)"] <= 0.799950:
                            if features["E(LEFT) - time_left"] <= 0.090473:
                                return 2
                            else:
                                if features["E(LEFT) - agent_column"] <= -13.615266:
                                    if features["E(UP) - T(DOWN)"] <= 0.347413:
                                        if features["E(DOWN) - time_left"] <= 0.319346:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        return 0
                                else:
                                    if features["E(RIGHT)"] <= 0.000110:
                                        return 2
                                    else:
                                        if features["T(E(UP)) - T(T(up))"] <= 0.047459:
                                            if features["E(RIGHT)"] <= 0.067247:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                        else:
                            if features["E(RIGHT) - agent_column"] <= -11.999999:
                                return 0
                            else:
                                return 2
                    else:
                        if features["E(LEFT) - E(RIGHT)"] <= 0.864676:
                            return 2
                        else:
                            if features["T(LEFT) - T(T(RIGHT))"] <= 0.017326:
                                return 2
                            else:
                                return 1
                else:
                    if features["E(DOWN) - time_left"] <= 0.177600:
                        if features["E(RIGHT)"] <= 0.034202:
                            return 2
                        else:
                            return 0
                    else:
                        return 2
            else:
                if features["E(UP) - E(DOWN)"] <= 0.865424:
                    if features["E(DOWN)"] <= 0.000028:
                        if features["T(T(LEFT)) - agent_row"] <= -13.672911:
                            return 2
                        else:
                            if features["T(T(DOWN)) - time_left"] <= -0.764711:
                                return 1
                            else:
                                if features["T(E(UP)) - agent_row"] <= -1.178187:
                                    return 0
                                else:
                                    return 2
                    else:
                        if features["E(DOWN) - E(RIGHT)"] <= -0.004125:
                            return 0
                        else:
                            if features["E(DOWN) - agent_column"] <= -9.999731:
                                return 0
                            else:
                                return 2
                else:
                    if features["T(RIGHT) - agent_column"] <= -7.999971:
                        return 0
                    else:
                        return 2
        else:
            if features["E(UP)"] <= 0.000016:
                if features["E(UP) - E(DOWN)"] <= -0.800048:
                    if features["E(DOWN) - agent_column"] <= -9.131967:
                        if features["T(LEFT) - agent_row"] <= -10.987021:
                            return 2
                        else:
                            return 1
                    else:
                        if features["E(LEFT) - agent_row"] <= -4.133415:
                            return 1
                        else:
                            return 2
                else:
                    if features["T(E(DOWN)) - agent_row"] <= 0.342999:
                        return 1
                    else:
                        return 2
            else:
                if features["T(E(RIGHT)) - agent_row"] <= -10.677970:
                    return 2
                else:
                    if features["E(DOWN) - time_left"] <= 0.127045:
                        return 2
                    else:
                        if features["T(DOWN)"] <= 0.374459:
                            return 1
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
