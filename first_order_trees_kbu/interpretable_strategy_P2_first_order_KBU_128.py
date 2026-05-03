import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(DOWN)"] <= -0.364744:
        if features["E(LEFT) - E(RIGHT)"] <= 0.329779:
            if features["E(RIGHT)"] <= 0.345813:
                if features["E(UP)"] <= 0.006477:
                    if features["E(LEFT) - T(LEFT)"] <= 0.003955:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.018016:
                            if features["T(up) - T(DOWN)"] <= -0.510883:
                                if features["E(RIGHT)"] <= 0.259036:
                                    if features["E(LEFT)"] <= 0.340574:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    if features["T(DOWN) - T(RIGHT)"] <= 0.323623:
                                        return 3
                                    else:
                                        return 2
                            else:
                                return 1
                        else:
                            if features["E(UP) - E(LEFT)"] <= -0.249159:
                                return 1
                            else:
                                return 3
                    else:
                        if features["agent_row - agent_column"] <= -6.500000:
                            return 2
                        else:
                            return 1
                else:
                    if features["T(up) - T(DOWN)"] <= -0.373673:
                        return 2
                    else:
                        return 0
            else:
                if features["E(RIGHT) - agent_column"] <= -11.208409:
                    return 1
                else:
                    if features["E(RIGHT) - agent_row"] <= -11.208409:
                        return 3
                    else:
                        if features["E(RIGHT) - agent_column"] <= -7.456818:
                            return 1
                        else:
                            if features["E(RIGHT) - agent_column"] <= -0.555235:
                                return 3
                            else:
                                if features["E(DOWN) - agent_row"] <= -8.399529:
                                    return 3
                                else:
                                    return 1
        else:
            if features["E(LEFT) - agent_row"] <= -11.208409:
                return 2
            else:
                if features["E(RIGHT) - agent_column"] <= -12.978880:
                    return 1
                else:
                    if features["agent_row - time_left"] <= 2.860000:
                        return 2
                    else:
                        if features["E(UP) - E(DOWN)"] <= -0.805255:
                            if features["T(RIGHT) - agent_row"] <= -11.398285:
                                return 1
                            else:
                                return 2
                        else:
                            if features["T(up) - agent_column"] <= -2.736485:
                                if features["E(DOWN) - agent_row"] <= -9.341376:
                                    if features["E(DOWN)"] <= 0.708946:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                return 1
    else:
        if features["E(LEFT) - E(RIGHT)"] <= -0.370323:
            if features["E(UP) - E(DOWN)"] <= 0.338461:
                if features["E(LEFT)"] <= 0.011180:
                    return 3
                else:
                    return 2
            else:
                if features["T(LEFT) - agent_row"] <= -1.949268:
                    if features["E(RIGHT) - agent_column"] <= -11.208409:
                        return 0
                    else:
                        if features["T(DOWN) - agent_column"] <= -2.764088:
                            return 3
                        else:
                            if features["E(UP) - T(LEFT)"] <= 0.384356:
                                return 3
                            else:
                                return 0
                else:
                    return 3
        else:
            if features["E(UP) - E(DOWN)"] <= 0.365161:
                if features["E(LEFT) - E(RIGHT)"] <= 0.380634:
                    if features["E(UP) - T(RIGHT)"] <= 0.089651:
                        if features["agent_column - time_left"] <= 9.900000:
                            if features["E(UP)"] <= 0.171336:
                                if features["E(DOWN)"] <= 0.371879:
                                    if features["E(RIGHT) - T(LEFT)"] <= 0.168712:
                                        if features["E(DOWN) - time_left"] <= -0.067823:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.016179:
                                            if features["E(RIGHT) - agent_column"] <= -3.667711:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(up) - time_left"] <= -0.180000:
                                                return 2
                                            else:
                                                return 1
                                else:
                                    if features["T(up)"] <= 0.042996:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.262993:
                                            if features["E(LEFT) - T(up)"] <= 0.069255:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 2
                                    else:
                                        return 0
                            else:
                                if features["T(up) - agent_row"] <= -8.675020:
                                    if features["T(up) - T(LEFT)"] <= 0.234018:
                                        return 0
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.033449:
                                            if features["E(LEFT) - agent_row"] <= -9.733760:
                                                if features["agent_row - agent_column"] <= 4.500000:
                                                    return 2
                                                else:
                                                    if features["T(LEFT) - T(RIGHT)"] <= -0.343437:
                                                        return 0
                                                    else:
                                                        if features["E(UP) - time_left"] <= 0.325195:
                                                            return 0
                                                        else:
                                                            return 3
                                            else:
                                                return 2
                                        else:
                                            return 1
                                else:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.305050:
                                        if features["T(up) - agent_row"] <= -8.670113:
                                            if features["E(DOWN) - time_left"] <= 0.069997:
                                                return 2
                                            else:
                                                return 3
                                        else:
                                            if features["E(DOWN)"] <= 0.200386:
                                                return 0
                                            else:
                                                if features["T(up) - T(LEFT)"] <= 0.156142:
                                                    if features["E(DOWN) - T(RIGHT)"] <= -0.122009:
                                                        if features["T(LEFT) - time_left"] <= 0.046476:
                                                            if features["T(DOWN) - time_left"] <= 0.374311:
                                                                if features["E(DOWN) - time_left"] <= -0.071994:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                            else:
                                                                if features["E(DOWN) - E(RIGHT)"] <= 0.030529:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                        else:
                                                            if features["E(RIGHT) - time_left"] <= 0.379924:
                                                                if features["E(UP) - time_left"] <= 0.265819:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                            else:
                                                                return 3
                                                    else:
                                                        if features["T(LEFT)"] <= 0.324980:
                                                            if features["E(DOWN)"] <= 0.354903:
                                                                if features["T(RIGHT) - agent_row"] <= -4.676378:
                                                                    return 2
                                                                else:
                                                                    if features["E(RIGHT) - time_left"] <= 0.204300:
                                                                        return 2
                                                                    else:
                                                                        if features["T(DOWN) - agent_column"] <= -2.679036:
                                                                            return 3
                                                                        else:
                                                                            return 2
                                                            else:
                                                                if features["T(up) - time_left"] <= 0.116542:
                                                                    return 0
                                                                else:
                                                                    return 1
                                                        else:
                                                            return 0
                                                else:
                                                    return 2
                                    else:
                                        if features["T(RIGHT) - agent_column"] <= -7.356850:
                                            return 2
                                        else:
                                            return 1
                        else:
                            if features["E(DOWN) - E(LEFT)"] <= 0.173422:
                                if features["E(DOWN) - T(RIGHT)"] <= -0.609692:
                                    return 0
                                else:
                                    return 2
                            else:
                                return 1
                    else:
                        if features["E(LEFT) - T(LEFT)"] <= 0.280487:
                            if features["E(LEFT) - T(up)"] <= 0.257678:
                                if features["T(RIGHT) - agent_row"] <= -10.983821:
                                    if features["T(RIGHT)"] <= 0.100525:
                                        if features["E(DOWN)"] <= 0.016179:
                                            return 0
                                        else:
                                            if features["agent_column - time_left"] <= 9.840000:
                                                return 3
                                            else:
                                                return 2
                                    else:
                                        if features["E(DOWN)"] <= 0.016179:
                                            return 0
                                        else:
                                            return 1
                                else:
                                    if features["E(RIGHT) - T(up)"] <= -0.386965:
                                        if features["E(UP) - agent_column"] <= -6.768718:
                                            if features["E(LEFT) - time_left"] <= 0.268930:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 3
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.309607:
                                            return 3
                                        else:
                                            if features["T(up) - time_left"] <= 0.000811:
                                                return 0
                                            else:
                                                return 3
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.283524:
                                    if features["T(LEFT) - agent_row"] <= -4.402717:
                                        if features["E(DOWN) - T(LEFT)"] <= -0.176435:
                                            if features["E(DOWN) - E(LEFT)"] <= -0.030325:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        if features["agent_column - time_left"] <= 9.780000:
                                            if features["T(LEFT) - time_left"] <= 0.374654:
                                                return 0
                                            else:
                                                return 1
                                        else:
                                            return 2
                                else:
                                    return 1
                        else:
                            if features["E(UP) - T(up)"] <= 0.276544:
                                if features["E(DOWN) - agent_column"] <= -7.717715:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 0
                else:
                    if features["E(UP)"] <= 0.377370:
                        if features["E(LEFT) - time_left"] <= 0.286482:
                            if features["E(UP) - T(up)"] <= 0.290888:
                                return 2
                            else:
                                return 0
                        else:
                            return 2
                    else:
                        if features["agent_column - time_left"] <= 4.720000:
                            return 0
                        else:
                            return 2
            else:
                if features["E(LEFT) - E(RIGHT)"] <= 0.311758:
                    if features["E(DOWN)"] <= 0.009784:
                        if features["E(LEFT) - T(LEFT)"] <= 0.241836:
                            if features["E(DOWN) - T(up)"] <= -0.482758:
                                if features["E(RIGHT) - T(up)"] <= -0.129583:
                                    return 0
                                else:
                                    return 3
                            else:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.362817:
                                    return 3
                                else:
                                    return 0
                        else:
                            return 0
                    else:
                        return 1
                else:
                    if features["T(DOWN) - agent_row"] <= -0.863734:
                        if features["T(up) - agent_column"] <= -1.902892:
                            if features["E(UP) - agent_row"] <= -9.194745:
                                return 2
                            else:
                                if features["E(LEFT) - T(RIGHT)"] <= 0.545636:
                                    if features["T(up) - T(LEFT)"] <= -0.176715:
                                        if features["T(DOWN) - agent_row"] <= -5.472375:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 0
                                else:
                                    if features["agent_row - agent_column"] <= -1.500000:
                                        if features["T(up) - agent_row"] <= -2.156573:
                                            return 0
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= 0.791030:
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
