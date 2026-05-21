import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbol_names = ['Evader(UP)', 'Evader(DOWN)', 'Evader(LEFT)', 'Evader(RIGHT)', 'Teammate(UP)', 'Teammate(DOWN)', 'Teammate(LEFT)', 'Teammate(RIGHT)', 'Agent_Row', 'Agent_Column', 'Time_Left', 'Evader(UP) - Evader(DOWN)', 'Evader(UP) - Evader(LEFT)', 'Evader(UP) - Evader(RIGHT)', 'Evader(UP) - Teammate(UP)', 'Evader(UP) - Teammate(DOWN)', 'Evader(UP) - Teammate(LEFT)', 'Evader(UP) - Teammate(RIGHT)', 'Evader(UP) - Agent_Row', 'Evader(UP) - Agent_Column', 'Evader(UP) - Time_Left', 'Evader(DOWN) - Evader(LEFT)', 'Evader(DOWN) - Evader(RIGHT)', 'Evader(DOWN) - Teammate(UP)', 'Evader(DOWN) - Teammate(DOWN)', 'Evader(DOWN) - Teammate(LEFT)', 'Evader(DOWN) - Teammate(RIGHT)', 'Evader(DOWN) - Agent_Row', 'Evader(DOWN) - Agent_Column', 'Evader(DOWN) - Time_Left', 'Evader(LEFT) - Evader(RIGHT)', 'Evader(LEFT) - Teammate(UP)', 'Evader(LEFT) - Teammate(DOWN)', 'Evader(LEFT) - Teammate(LEFT)', 'Evader(LEFT) - Teammate(RIGHT)', 'Evader(LEFT) - Agent_Row', 'Evader(LEFT) - Agent_Column', 'Evader(LEFT) - Time_Left', 'Evader(RIGHT) - Teammate(UP)', 'Evader(RIGHT) - Teammate(DOWN)', 'Evader(RIGHT) - Teammate(LEFT)', 'Evader(RIGHT) - Teammate(RIGHT)', 'Evader(RIGHT) - Agent_Row', 'Evader(RIGHT) - Agent_Column', 'Evader(RIGHT) - Time_Left', 'Teammate(UP) - Teammate(DOWN)', 'Teammate(UP) - Teammate(LEFT)', 'Teammate(UP) - Teammate(RIGHT)', 'Teammate(UP) - Agent_Row', 'Teammate(UP) - Agent_Column', 'Teammate(UP) - Time_Left', 'Teammate(DOWN) - Teammate(LEFT)', 'Teammate(DOWN) - Teammate(RIGHT)', 'Teammate(DOWN) - Agent_Row', 'Teammate(DOWN) - Agent_Column', 'Teammate(DOWN) - Time_Left', 'Teammate(LEFT) - Teammate(RIGHT)', 'Teammate(LEFT) - Agent_Row', 'Teammate(LEFT) - Agent_Column', 'Teammate(LEFT) - Time_Left', 'Teammate(RIGHT) - Agent_Row', 'Teammate(RIGHT) - Agent_Column', 'Teammate(RIGHT) - Time_Left', 'Agent_Row - Agent_Column', 'Agent_Row - Time_Left', 'Agent_Column - Time_Left']


def interpretable_strategy(features):
    if features["Evader(UP) - Evader(RIGHT)"] <= -0.183067:
        if features["Agent_Row - Agent_Column"] <= 0.500000:
            return 1 # WALK RIGHT
        else:
            return 3 # WALK UP
    else:
        if features["Evader(DOWN) - Evader(LEFT)"] <= -0.278728:
            if features["Agent_Row - Agent_Column"] <= -0.500000:
                return 2 # WALK DOWN
            else:
                return 0 # WALK LEFT
        else:
            if features["Evader(DOWN) - Teammate(DOWN)"] <= 0.065915:
                if features["Evader(DOWN) - Agent_Column"] <= -8.796049:
                    return 2 # WALK DOWN
                else:
                    if features["Evader(UP) - Evader(RIGHT)"] <= 0.009080:
                        return 2 # WALK DOWN
                    else:
                        return 0 # WALK LEFT
            else:
                return 3 # WALK UP


def interpretable_action(Evader_Probability_Grid, Teammate_Probability_Grid, Teammate_Evader_Probability_Grid, Teammate_Teammate_Probability_Grid, Main_Agent_Position, Time_Left, Gamma, Size, Valid_Actions):
    input_representation = symbolic_representation(Evader_Probability_Grid, Teammate_Probability_Grid, Teammate_Evader_Probability_Grid, Teammate_Teammate_Probability_Grid, Main_Agent_Position, Time_Left, Gamma, Size)
    input_combinations   = get_feature_vector(input_representation)
    symbol_to_value     = {name: input_combinations[i] for i, name in enumerate(symbol_names)}
    action               = Index_to_Action[interpretable_strategy(symbol_to_value)]
    if action in Valid_Actions:
        return action
    else:
        return random.choice(Valid_Actions)
