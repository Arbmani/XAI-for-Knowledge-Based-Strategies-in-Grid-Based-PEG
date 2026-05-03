import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(DOWN) - E(LEFT)"] <= 0.000000:
        if features["E(UP) - E(LEFT)"] <= -0.260534:
            if features["E(RIGHT)"] <= 0.000123:
                if features["E(DOWN) - E(RIGHT)"] <= 0.800890:
                    return 2
                else:
                    if features["E(UP) - E(RIGHT)"] <= 0.000000:
                        return 2
                    else:
                        return 1
            else:
                if features["E(DOWN)"] <= 0.376073:
                    if features["E(RIGHT)"] <= 0.015449:
                        if features["E(RIGHT) - time_left"] <= -0.046396:
                            return 2
                        else:
                            if features["T(up) - T(RIGHT)"] <= 0.042950:
                                return 2
                            else:
                                return 0
                    else:
                        if features["E(RIGHT) - agent_column"] <= -12.982530:
                            return 0
                        else:
                            return 2
                else:
                    if features["E(RIGHT)"] <= 0.016624:
                        return 2
                    else:
                        return 1
        else:
            if features["E(UP) - E(LEFT)"] <= 0.000090:
                if features["E(RIGHT)"] <= 0.001364:
                    if features["E(RIGHT) - T(RIGHT)"] <= -0.000000:
                        return 2
                    else:
                        if features["E(DOWN) - T(up)"] <= 0.150423:
                            if features["E(DOWN) - agent_column"] <= -13.964280:
                                return 0
                            else:
                                if features["T(up) - time_left"] <= 0.276839:
                                    return 0
                                else:
                                    return 2
                        else:
                            if features["E(DOWN) - T(LEFT)"] <= -0.194361:
                                return 2
                            else:
                                return 1
                else:
                    if features["E(RIGHT) - T(DOWN)"] <= 0.058540:
                        if features["E(UP) - time_left"] <= 0.057564:
                            if features["T(DOWN) - agent_row"] <= -2.977401:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.008792:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 0
                        else:
                            if features["T(RIGHT)"] <= 0.005975:
                                if features["E(DOWN) - E(RIGHT)"] <= 0.175959:
                                    if features["E(UP) - agent_row"] <= -10.658101:
                                        if features["T(DOWN)"] <= 0.019973:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 0
                                else:
                                    return 2
                            else:
                                if features["T(RIGHT) - time_left"] <= 0.188770:
                                    return 0
                                else:
                                    if features["T(LEFT) - time_left"] <= 0.218291:
                                        return 0
                                    else:
                                        return 3
                    else:
                        if features["T(RIGHT) - agent_row"] <= -7.999975:
                            if features["E(LEFT) - time_left"] <= 0.283304:
                                return 3
                            else:
                                return 0
                        else:
                            if features["E(UP)"] <= 0.221381:
                                return 1
                            else:
                                if features["T(RIGHT)"] <= 0.000000:
                                    return 3
                                else:
                                    return 2
            else:
                if features["E(UP) - E(RIGHT)"] <= 0.115772:
                    if features["E(DOWN) - T(DOWN)"] <= 0.053066:
                        if features["E(DOWN) - agent_row"] <= -2.000000:
                            if features["E(UP) - E(RIGHT)"] <= -0.000002:
                                if features["E(DOWN)"] <= 0.111192:
                                    return 3
                                else:
                                    return 0
                            else:
                                if features["E(DOWN) - T(LEFT)"] <= 0.003255:
                                    if features["E(RIGHT)"] <= 0.799727:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.000049:
                                            if features["E(LEFT)"] <= 0.285972:
                                                return 0
                                            else:
                                                if features["T(LEFT)"] <= 0.301926:
                                                    return 3
                                                else:
                                                    return 0
                                        else:
                                            return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(DOWN) - T(up)"] <= 0.058183:
                                        if features["T(up) - agent_row"] <= -7.510401:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 0
                        else:
                            return 3
                    else:
                        if features["T(up) - T(RIGHT)"] <= -0.000001:
                            if features["E(DOWN) - agent_row"] <= -8.820894:
                                return 0
                            else:
                                return 2
                        else:
                            if features["E(UP) - time_left"] <= 0.310156:
                                return 3
                            else:
                                return 0
                else:
                    if features["E(LEFT)"] <= 0.671500:
                        if features["E(DOWN) - T(DOWN)"] <= 0.056198:
                            return 0
                        else:
                            if features["T(up) - agent_row"] <= -8.609601:
                                return 0
                            else:
                                return 3
                    else:
                        if features["E(DOWN) - agent_row"] <= -1.999999:
                            if features["E(UP) - T(DOWN)"] <= 0.800268:
                                return 0
                            else:
                                return 2
                        else:
                            return 0
    else:
        if features["E(DOWN) - E(RIGHT)"] <= 0.000011:
            if features["E(UP) - E(RIGHT)"] <= -0.142747:
                if features["E(DOWN) - E(RIGHT)"] <= -0.171835:
                    return 3
                else:
                    if features["E(UP) - agent_column"] <= -12.999891:
                        return 1
                    else:
                        if features["E(LEFT) - agent_column"] <= -1.932839:
                            if features["E(LEFT) - time_left"] <= 0.104123:
                                return 3
                            else:
                                if features["T(up) - T(LEFT)"] <= 0.025948:
                                    return 1
                                else:
                                    return 2
                        else:
                            if features["E(LEFT) - T(up)"] <= -0.001698:
                                if features["T(up) - time_left"] <= 0.109795:
                                    return 3
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -5.587533:
                                        return 3
                                    else:
                                        return 1
                            else:
                                if features["T(DOWN) - T(RIGHT)"] <= 0.000014:
                                    return 1
                                else:
                                    return 3
            else:
                if features["E(RIGHT) - agent_column"] <= -11.200371:
                    if features["E(UP) - agent_row"] <= -6.412579:
                        return 3
                    else:
                        return 0
                else:
                    if features["E(LEFT) - agent_column"] <= -5.844290:
                        if features["E(UP)"] <= 0.662940:
                            return 3
                        else:
                            if features["E(UP) - E(RIGHT)"] <= 0.000183:
                                return 3
                            else:
                                return 0
                    else:
                        if features["E(LEFT) - E(RIGHT)"] <= -0.225343:
                            if features["T(LEFT) - agent_column"] <= -0.998837:
                                if features["E(LEFT) - T(up)"] <= 0.016987:
                                    if features["E(DOWN) - time_left"] <= 0.193839:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 0
                            else:
                                if features["E(UP) - T(RIGHT)"] <= -0.131956:
                                    return 3
                                else:
                                    if features["E(UP) - agent_column"] <= -0.696999:
                                        return 3
                                    else:
                                        return 0
                        else:
                            if features["E(LEFT) - T(DOWN)"] <= 0.017698:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.202648:
                                    if features["T(LEFT)"] <= 0.238607:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(LEFT) - agent_column"] <= -3.851546:
                                        return 0
                                    else:
                                        return 2
                            else:
                                if features["T(up) - T(RIGHT)"] <= -0.000012:
                                    return 2
                                else:
                                    return 3
        else:
            if features["E(DOWN) - E(RIGHT)"] <= 0.187525:
                if features["E(UP) - E(DOWN)"] <= -0.330338:
                    if features["E(UP) - E(DOWN)"] <= -0.800630:
                        return 3
                    else:
                        if features["E(UP)"] <= 0.000001:
                            return 1
                        else:
                            if features["E(UP) - E(LEFT)"] <= -0.074390:
                                return 1
                            else:
                                if features["T(LEFT) - agent_column"] <= -1.973888:
                                    if features["E(RIGHT) - agent_column"] <= -10.336407:
                                        return 1
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -1.999965:
                                            if features["E(LEFT) - agent_row"] <= -11.897228:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 3
                                else:
                                    return 1
                else:
                    if features["E(LEFT) - agent_row"] <= -4.725177:
                        if features["T(up) - T(LEFT)"] <= -0.000036:
                            if features["T(up)"] <= 0.000000:
                                return 0
                            else:
                                return 3
                        else:
                            return 1
                    else:
                        if features["E(UP) - E(RIGHT)"] <= -0.127471:
                            if features["E(RIGHT)"] <= 0.322921:
                                return 1
                            else:
                                if features["T(LEFT) - T(RIGHT)"] <= -0.365927:
                                    return 1
                                else:
                                    return 3
                        else:
                            if features["E(DOWN) - T(DOWN)"] <= 0.295394:
                                if features["E(UP) - time_left"] <= -0.063149:
                                    return 1
                                else:
                                    if features["T(DOWN) - time_left"] <= 0.479022:
                                        return 0
                                    else:
                                        return 1
                            else:
                                return 1
            else:
                if features["E(LEFT)"] <= 0.729326:
                    if features["E(UP)"] <= 0.000063:
                        if features["E(RIGHT) - time_left"] <= -0.689475:
                            return 2
                        else:
                            return 1
                    else:
                        if features["E(DOWN)"] <= 0.388817:
                            if features["E(RIGHT)"] <= 0.015787:
                                if features["E(DOWN) - T(LEFT)"] <= 0.004964:
                                    return 2
                                else:
                                    return 1
                            else:
                                if features["E(UP) - time_left"] <= 0.016201:
                                    return 1
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= -0.000043:
                                        return 1
                                    else:
                                        return 0
                        else:
                            if features["E(UP) - time_left"] <= 0.023703:
                                if features["E(DOWN) - agent_row"] <= -9.515645:
                                    return 1
                                else:
                                    if features["T(DOWN) - T(RIGHT)"] <= 0.433960:
                                        if features["E(LEFT) - agent_row"] <= -0.621525:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 1
                            else:
                                return 0
                else:
                    if features["T(LEFT) - agent_row"] <= -1.741010:
                        if features["E(DOWN) - agent_row"] <= -11.200878:
                            return 2
                        else:
                            return 1
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
