import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(DOWN)"] <= -0.315546:
        if features["E(LEFT) - E(RIGHT)"] <= 0.285376:
            if features["E(LEFT) - E(RIGHT)"] <= -0.321605:
                if features["E(RIGHT) - agent_column"] <= -11.265720:
                    if features["T(up) - agent_row"] <= -9.856620:
                        return 3
                    else:
                        return 1
                else:
                    if features["E(DOWN) - agent_row"] <= -11.208409:
                        return 3
                    else:
                        if features["E(RIGHT) - agent_row"] <= -3.507849:
                            if features["E(RIGHT) - agent_row"] <= -8.400445:
                                if features["E(UP) - E(DOWN)"] <= -0.658624:
                                    return 1
                                else:
                                    return 3
                            else:
                                if features["E(DOWN) - T(up)"] <= 0.616728:
                                    return 1
                                else:
                                    return 3
                        else:
                            if features["E(DOWN) - time_left"] <= 0.331955:
                                return 1
                            else:
                                if features["agent_row - agent_column"] <= 0.500000:
                                    return 3
                                else:
                                    return 1
            else:
                if features["E(UP)"] <= 0.009784:
                    return 1
                else:
                    if features["T(up) - agent_row"] <= -0.955066:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.184325:
                            if features["T(DOWN) - time_left"] <= 0.000081:
                                if features["E(LEFT) - T(DOWN)"] <= -0.217701:
                                    return 3
                                else:
                                    return 1
                            else:
                                if features["E(LEFT) - T(DOWN)"] <= -0.276983:
                                    return 1
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -0.965483:
                                        return 1
                                    else:
                                        return 0
                        else:
                            return 3
                    else:
                        return 0
        else:
            if features["T(DOWN) - agent_column"] <= -2.243012:
                if features["E(LEFT) - agent_row"] <= -11.208409:
                    return 2
                else:
                    if features["T(RIGHT) - agent_column"] <= -10.951967:
                        if features["E(DOWN) - T(LEFT)"] <= -0.050684:
                            return 2
                        else:
                            return 1
                    else:
                        if features["E(DOWN) - agent_row"] <= -3.503436:
                            if features["T(DOWN) - agent_column"] <= -3.420766:
                                if features["E(LEFT) - T(RIGHT)"] <= 0.656929:
                                    return 2
                                else:
                                    return 1
                            else:
                                return 1
                        else:
                            return 2
            else:
                return 1
    else:
        if features["E(LEFT) - E(RIGHT)"] <= 0.365277:
            if features["E(LEFT) - E(RIGHT)"] <= -0.365750:
                if features["E(UP) - E(DOWN)"] <= 0.311758:
                    if features["E(UP) - T(up)"] <= 0.007441:
                        if features["E(LEFT)"] <= 0.009784:
                            return 3
                        else:
                            return 2
                    else:
                        if features["E(UP) - T(LEFT)"] <= 0.180651:
                            return 3
                        else:
                            if features["T(LEFT) - time_left"] <= -0.170000:
                                return 0
                            else:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.398195:
                                    return 3
                                else:
                                    return 0
                else:
                    if features["E(RIGHT) - agent_column"] <= -11.225466:
                        return 0
                    else:
                        if features["E(LEFT) - agent_row"] <= -1.970219:
                            if features["E(RIGHT) - agent_column"] <= -2.449438:
                                if features["agent_row - time_left"] <= 12.630000:
                                    if features["E(UP) - T(up)"] <= 0.662359:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 3
                            else:
                                if features["agent_row - time_left"] <= 8.950000:
                                    if features["agent_row - time_left"] <= 2.500000:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    return 3
                        else:
                            return 3
            else:
                if features["E(UP) - E(DOWN)"] <= 0.382163:
                    if features["E(LEFT) - T(DOWN)"] <= 0.066116:
                        if features["E(UP) - time_left"] <= 0.177650:
                            if features["E(DOWN) - E(LEFT)"] <= 0.227053:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.207405:
                                    if features["E(DOWN)"] <= 0.365281:
                                        if features["E(UP) - E(RIGHT)"] <= -0.222336:
                                            return 3
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -4.633750:
                                                if features["T(up) - T(LEFT)"] <= -0.133229:
                                                    if features["E(RIGHT) - T(LEFT)"] <= -0.361518:
                                                        return 2
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                            else:
                                                if features["E(UP) - E(DOWN)"] <= -0.166920:
                                                    if features["E(UP) - T(DOWN)"] <= -0.180096:
                                                        if features["E(LEFT) - T(up)"] <= 0.105314:
                                                            return 2
                                                        else:
                                                            if features["agent_row - time_left"] <= 1.450000:
                                                                return 1
                                                            else:
                                                                return 2
                                                    else:
                                                        if features["agent_column - time_left"] <= 8.930000:
                                                            if features["E(RIGHT) - time_left"] <= 0.313376:
                                                                return 0
                                                            else:
                                                                return 1
                                                        else:
                                                            return 1
                                                else:
                                                    return 2
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.045169:
                                            return 0
                                        else:
                                            if features["T(RIGHT) - time_left"] <= 0.313141:
                                                return 0
                                            else:
                                                return 1
                                else:
                                    if features["T(LEFT) - agent_column"] <= -5.840096:
                                        if features["E(RIGHT) - T(LEFT)"] <= -0.215572:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                            else:
                                if features["T(up) - agent_row"] <= -4.763723:
                                    if features["T(DOWN) - agent_column"] <= -0.723196:
                                        return 3
                                    else:
                                        return 2
                                else:
                                    if features["E(LEFT) - T(RIGHT)"] <= 0.020951:
                                        return 1
                                    else:
                                        return 3
                        else:
                            if features["T(RIGHT) - agent_row"] <= -4.669163:
                                if features["E(LEFT) - T(DOWN)"] <= 0.032521:
                                    if features["E(DOWN) - T(up)"] <= 0.245430:
                                        if features["E(DOWN) - agent_column"] <= -2.727674:
                                            return 0
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -1.759487:
                                                if features["agent_row - time_left"] <= 8.990000:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                    else:
                                        return 0
                                else:
                                    if features["E(LEFT) - T(DOWN)"] <= 0.034946:
                                        return 3
                                    else:
                                        if features["E(UP) - time_left"] <= 0.367642:
                                            if features["T(up) - T(RIGHT)"] <= 0.060404:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 0
                            else:
                                return 2
                    else:
                        if features["E(UP) - T(up)"] <= 0.247230:
                            if features["T(DOWN)"] <= 0.112355:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.247230:
                                    if features["E(RIGHT)"] <= 0.069298:
                                        if features["E(UP) - E(DOWN)"] <= 0.298806:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["E(UP) - T(LEFT)"] <= 0.216570:
                                            if features["E(LEFT)"] <= 0.351171:
                                                if features["E(UP) - E(LEFT)"] <= 0.162046:
                                                    return 1
                                                else:
                                                    if features["T(up)"] <= 0.396347:
                                                        return 3
                                                    else:
                                                        if features["T(DOWN) - time_left"] <= 0.060590:
                                                            return 1
                                                        else:
                                                            return 0
                                            else:
                                                if features["E(UP) - time_left"] <= 0.208719:
                                                    return 1
                                                else:
                                                    return 2
                                        else:
                                            if features["T(up) - agent_column"] <= -7.597022:
                                                return 2
                                            else:
                                                if features["E(DOWN) - E(RIGHT)"] <= -0.252924:
                                                    return 3
                                                else:
                                                    if features["T(LEFT) - T(RIGHT)"] <= -0.280604:
                                                        return 2
                                                    else:
                                                        return 1
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.193121:
                                        return 3
                                    else:
                                        return 1
                            else:
                                if features["E(LEFT) - T(LEFT)"] <= -0.006717:
                                    return 2
                                else:
                                    if features["T(up)"] <= 0.331008:
                                        if features["E(UP) - T(DOWN)"] <= 0.055318:
                                            if features["agent_row - time_left"] <= 7.890000:
                                                return 3
                                            else:
                                                return 2
                                        else:
                                            return 3
                                    else:
                                        if features["E(UP) - E(DOWN)"] <= 0.181615:
                                            return 0
                                        else:
                                            if features["E(RIGHT) - time_left"] <= 0.234148:
                                                return 1
                                            else:
                                                return 3
                        else:
                            if features["E(UP) - T(RIGHT)"] <= -0.273785:
                                return 2
                            else:
                                if features["agent_row - agent_column"] <= -2.500000:
                                    return 3
                                else:
                                    return 0
                else:
                    if features["E(UP) - time_left"] <= 0.207885:
                        if features["E(DOWN) - E(LEFT)"] <= -0.123791:
                            if features["E(RIGHT) - time_left"] <= -0.283022:
                                return 2
                            else:
                                return 3
                        else:
                            return 0
                    else:
                        if features["E(LEFT) - T(LEFT)"] <= 0.239209:
                            if features["E(UP) - time_left"] <= 0.368657:
                                if features["T(RIGHT) - agent_row"] <= -13.948006:
                                    return 3
                                else:
                                    return 0
                            else:
                                return 0
                        else:
                            if features["E(LEFT) - T(up)"] <= 0.072531:
                                return 2
                            else:
                                return 0
        else:
            if features["E(UP) - E(LEFT)"] <= -0.075044:
                if features["E(RIGHT)"] <= 0.009784:
                    if features["E(UP) - T(up)"] <= 0.267490:
                        if features["E(DOWN) - time_left"] <= 0.322095:
                            return 2
                        else:
                            return 1
                    else:
                        return 2
                else:
                    return 3
            else:
                if features["T(up) - agent_row"] <= -1.915457:
                    if features["E(UP) - agent_column"] <= -1.160498:
                        if features["E(UP) - T(DOWN)"] <= 0.599718:
                            if features["T(RIGHT) - agent_row"] <= -2.908846:
                                if features["E(DOWN) - agent_row"] <= -12.981985:
                                    return 2
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= -0.000625:
                                        return 2
                                    else:
                                        return 0
                            else:
                                return 2
                        else:
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
