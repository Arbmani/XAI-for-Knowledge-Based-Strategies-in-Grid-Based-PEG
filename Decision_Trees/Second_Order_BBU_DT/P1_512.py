import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbol_names = ['Evader(UP)', 'Evader(DOWN)', 'Evader(LEFT)', 'Evader(RIGHT)', 'Teammate(UP)', 'Teammate(DOWN)', 'Teammate(LEFT)', 'Teammate(RIGHT)', 'Teammate(Evader(UP))', 'Teammate(Evader(DOWN))', 'Teammate(Evader(LEFT))', 'Teammate(Evader(RIGHT))', 'Teammate(Teammate(UP))', 'Teammate(Teammate(DOWN))', 'Teammate(Teammate(LEFT))', 'Teammate(Teammate(RIGHT))', 'Agent_Row', 'Agent_Column', 'Time_Left', 'Evader(UP) - Evader(DOWN)', 'Evader(UP) - Evader(LEFT)', 'Evader(UP) - Evader(RIGHT)', 'Evader(UP) - Teammate(UP)', 'Evader(UP) - Teammate(DOWN)', 'Evader(UP) - Teammate(LEFT)', 'Evader(UP) - Teammate(RIGHT)', 'Evader(UP) - Teammate(Evader(UP))', 'Evader(UP) - Teammate(Evader(DOWN))', 'Evader(UP) - Teammate(Evader(LEFT))', 'Evader(UP) - Teammate(Evader(RIGHT))', 'Evader(UP) - Teammate(Teammate(UP))', 'Evader(UP) - Teammate(Teammate(DOWN))', 'Evader(UP) - Teammate(Teammate(LEFT))', 'Evader(UP) - Teammate(Teammate(RIGHT))', 'Evader(UP) - Agent_Row', 'Evader(UP) - Agent_Column', 'Evader(UP) - Time_Left', 'Evader(DOWN) - Evader(LEFT)', 'Evader(DOWN) - Evader(RIGHT)', 'Evader(DOWN) - Teammate(UP)', 'Evader(DOWN) - Teammate(DOWN)', 'Evader(DOWN) - Teammate(LEFT)', 'Evader(DOWN) - Teammate(RIGHT)', 'Evader(DOWN) - Teammate(Evader(UP))', 'Evader(DOWN) - Teammate(Evader(DOWN))', 'Evader(DOWN) - Teammate(Evader(LEFT))', 'Evader(DOWN) - Teammate(Evader(RIGHT))', 'Evader(DOWN) - Teammate(Teammate(UP))', 'Evader(DOWN) - Teammate(Teammate(DOWN))', 'Evader(DOWN) - Teammate(Teammate(LEFT))', 'Evader(DOWN) - Teammate(Teammate(RIGHT))', 'Evader(DOWN) - Agent_Row', 'Evader(DOWN) - Agent_Column', 'Evader(DOWN) - Time_Left', 'Evader(LEFT) - Evader(RIGHT)', 'Evader(LEFT) - Teammate(UP)', 'Evader(LEFT) - Teammate(DOWN)', 'Evader(LEFT) - Teammate(LEFT)', 'Evader(LEFT) - Teammate(RIGHT)', 'Evader(LEFT) - Teammate(Evader(UP))', 'Evader(LEFT) - Teammate(Evader(DOWN))', 'Evader(LEFT) - Teammate(Evader(LEFT))', 'Evader(LEFT) - Teammate(Evader(RIGHT))', 'Evader(LEFT) - Teammate(Teammate(UP))', 'Evader(LEFT) - Teammate(Teammate(DOWN))', 'Evader(LEFT) - Teammate(Teammate(LEFT))', 'Evader(LEFT) - Teammate(Teammate(RIGHT))', 'Evader(LEFT) - Agent_Row', 'Evader(LEFT) - Agent_Column', 'Evader(LEFT) - Time_Left', 'Evader(RIGHT) - Teammate(UP)', 'Evader(RIGHT) - Teammate(DOWN)', 'Evader(RIGHT) - Teammate(LEFT)', 'Evader(RIGHT) - Teammate(RIGHT)', 'Evader(RIGHT) - Teammate(Evader(UP))', 'Evader(RIGHT) - Teammate(Evader(DOWN))', 'Evader(RIGHT) - Teammate(Evader(LEFT))', 'Evader(RIGHT) - Teammate(Evader(RIGHT))', 'Evader(RIGHT) - Teammate(Teammate(UP))', 'Evader(RIGHT) - Teammate(Teammate(DOWN))', 'Evader(RIGHT) - Teammate(Teammate(LEFT))', 'Evader(RIGHT) - Teammate(Teammate(RIGHT))', 'Evader(RIGHT) - Agent_Row', 'Evader(RIGHT) - Agent_Column', 'Evader(RIGHT) - Time_Left', 'Teammate(UP) - Teammate(DOWN)', 'Teammate(UP) - Teammate(LEFT)', 'Teammate(UP) - Teammate(RIGHT)', 'Teammate(UP) - Teammate(Evader(UP))', 'Teammate(UP) - Teammate(Evader(DOWN))', 'Teammate(UP) - Teammate(Evader(LEFT))', 'Teammate(UP) - Teammate(Evader(RIGHT))', 'Teammate(UP) - Teammate(Teammate(UP))', 'Teammate(UP) - Teammate(Teammate(DOWN))', 'Teammate(UP) - Teammate(Teammate(LEFT))', 'Teammate(UP) - Teammate(Teammate(RIGHT))', 'Teammate(UP) - Agent_Row', 'Teammate(UP) - Agent_Column', 'Teammate(UP) - Time_Left', 'Teammate(DOWN) - Teammate(LEFT)', 'Teammate(DOWN) - Teammate(RIGHT)', 'Teammate(DOWN) - Teammate(Evader(UP))', 'Teammate(DOWN) - Teammate(Evader(DOWN))', 'Teammate(DOWN) - Teammate(Evader(LEFT))', 'Teammate(DOWN) - Teammate(Evader(RIGHT))', 'Teammate(DOWN) - Teammate(Teammate(UP))', 'Teammate(DOWN) - Teammate(Teammate(DOWN))', 'Teammate(DOWN) - Teammate(Teammate(LEFT))', 'Teammate(DOWN) - Teammate(Teammate(RIGHT))', 'Teammate(DOWN) - Agent_Row', 'Teammate(DOWN) - Agent_Column', 'Teammate(DOWN) - Time_Left', 'Teammate(LEFT) - Teammate(RIGHT)', 'Teammate(LEFT) - Teammate(Evader(UP))', 'Teammate(LEFT) - Teammate(Evader(DOWN))', 'Teammate(LEFT) - Teammate(Evader(LEFT))', 'Teammate(LEFT) - Teammate(Evader(RIGHT))', 'Teammate(LEFT) - Teammate(Teammate(UP))', 'Teammate(LEFT) - Teammate(Teammate(DOWN))', 'Teammate(LEFT) - Teammate(Teammate(LEFT))', 'Teammate(LEFT) - Teammate(Teammate(RIGHT))', 'Teammate(LEFT) - Agent_Row', 'Teammate(LEFT) - Agent_Column', 'Teammate(LEFT) - Time_Left', 'Teammate(RIGHT) - Teammate(Evader(UP))', 'Teammate(RIGHT) - Teammate(Evader(DOWN))', 'Teammate(RIGHT) - Teammate(Evader(LEFT))', 'Teammate(RIGHT) - Teammate(Evader(RIGHT))', 'Teammate(RIGHT) - Teammate(Teammate(UP))', 'Teammate(RIGHT) - Teammate(Teammate(DOWN))', 'Teammate(RIGHT) - Teammate(Teammate(LEFT))', 'Teammate(RIGHT) - Teammate(Teammate(RIGHT))', 'Teammate(RIGHT) - Agent_Row', 'Teammate(RIGHT) - Agent_Column', 'Teammate(RIGHT) - Time_Left', 'Teammate(Evader(UP)) - Teammate(Evader(DOWN))', 'Teammate(Evader(UP)) - Teammate(Evader(LEFT))', 'Teammate(Evader(UP)) - Teammate(Evader(RIGHT))', 'Teammate(Evader(UP)) - Teammate(Teammate(UP))', 'Teammate(Evader(UP)) - Teammate(Teammate(DOWN))', 'Teammate(Evader(UP)) - Teammate(Teammate(LEFT))', 'Teammate(Evader(UP)) - Teammate(Teammate(RIGHT))', 'Teammate(Evader(UP)) - Agent_Row', 'Teammate(Evader(UP)) - Agent_Column', 'Teammate(Evader(UP)) - Time_Left', 'Teammate(Evader(DOWN)) - Teammate(Evader(LEFT))', 'Teammate(Evader(DOWN)) - Teammate(Evader(RIGHT))', 'Teammate(Evader(DOWN)) - Teammate(Teammate(UP))', 'Teammate(Evader(DOWN)) - Teammate(Teammate(DOWN))', 'Teammate(Evader(DOWN)) - Teammate(Teammate(LEFT))', 'Teammate(Evader(DOWN)) - Teammate(Teammate(RIGHT))', 'Teammate(Evader(DOWN)) - Agent_Row', 'Teammate(Evader(DOWN)) - Agent_Column', 'Teammate(Evader(DOWN)) - Time_Left', 'Teammate(Evader(LEFT)) - Teammate(Evader(RIGHT))', 'Teammate(Evader(LEFT)) - Teammate(Teammate(UP))', 'Teammate(Evader(LEFT)) - Teammate(Teammate(DOWN))', 'Teammate(Evader(LEFT)) - Teammate(Teammate(LEFT))', 'Teammate(Evader(LEFT)) - Teammate(Teammate(RIGHT))', 'Teammate(Evader(LEFT)) - Agent_Row', 'Teammate(Evader(LEFT)) - Agent_Column', 'Teammate(Evader(LEFT)) - Time_Left', 'Teammate(Evader(RIGHT)) - Teammate(Teammate(UP))', 'Teammate(Evader(RIGHT)) - Teammate(Teammate(DOWN))', 'Teammate(Evader(RIGHT)) - Teammate(Teammate(LEFT))', 'Teammate(Evader(RIGHT)) - Teammate(Teammate(RIGHT))', 'Teammate(Evader(RIGHT)) - Agent_Row', 'Teammate(Evader(RIGHT)) - Agent_Column', 'Teammate(Evader(RIGHT)) - Time_Left', 'Teammate(Teammate(UP)) - Teammate(Teammate(DOWN))', 'Teammate(Teammate(UP)) - Teammate(Teammate(LEFT))', 'Teammate(Teammate(UP)) - Teammate(Teammate(RIGHT))', 'Teammate(Teammate(UP)) - Agent_Row', 'Teammate(Teammate(UP)) - Agent_Column', 'Teammate(Teammate(UP)) - Time_Left', 'Teammate(Teammate(DOWN)) - Teammate(Teammate(LEFT))', 'Teammate(Teammate(DOWN)) - Teammate(Teammate(RIGHT))', 'Teammate(Teammate(DOWN)) - Agent_Row', 'Teammate(Teammate(DOWN)) - Agent_Column', 'Teammate(Teammate(DOWN)) - Time_Left', 'Teammate(Teammate(LEFT)) - Teammate(Teammate(RIGHT))', 'Teammate(Teammate(LEFT)) - Agent_Row', 'Teammate(Teammate(LEFT)) - Agent_Column', 'Teammate(Teammate(LEFT)) - Time_Left', 'Teammate(Teammate(RIGHT)) - Agent_Row', 'Teammate(Teammate(RIGHT)) - Agent_Column', 'Teammate(Teammate(RIGHT)) - Time_Left', 'Agent_Row - Agent_Column', 'Agent_Row - Time_Left', 'Agent_Column - Time_Left']


def interpretable_strategy(features):
    if features["Evader(UP) - Evader(RIGHT)"] <= -0.000063:
        if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.000046:
            if features["Evader(LEFT)"] <= 0.061205:
                if features["Evader(DOWN) - Teammate(Evader(UP))"] <= 0.068957:
                    if features["Evader(UP) - Teammate(Teammate(UP))"] <= 0.070289:
                        if features["Evader(RIGHT) - Time_Left"] <= 0.281037:
                            if features["Evader(LEFT)"] <= 0.001358:
                                if features["Evader(RIGHT) - Teammate(Evader(DOWN))"] <= -0.068809:
                                    return 1 # WALK DOWN
                                else:
                                    return 3 # WALK RIGHT
                            else:
                                if features["Evader(UP) - Time_Left"] <= 0.208640:
                                    if features["Evader(UP) - Evader(RIGHT)"] <= -0.096991:
                                        if features["Teammate(DOWN)"] <= 0.138156:
                                            return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(RIGHT) - Agent_Row"] <= -10.626912:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 1 # WALK DOWN
                                    else:
                                        if features["Evader(LEFT) - Agent_Column"] <= -0.964382:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                else:
                                    return 3 # WALK RIGHT
                        else:
                            if features["Evader(LEFT) - Time_Left"] <= 0.044557:
                                if features["Teammate(RIGHT) - Agent_Column"] <= 0.429038:
                                    if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.170117:
                                        if features["Evader(UP) - Evader(RIGHT)"] <= -0.000336:
                                            if features["Evader(RIGHT) - Teammate(Evader(DOWN))"] <= 0.009990:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        if features["Evader(UP) - Time_Left"] <= 0.162495:
                                            if features["Evader(LEFT) - Teammate(Evader(UP))"] <= -0.194156:
                                                if features["Evader(DOWN) - Teammate(Evader(DOWN))"] <= 0.399073:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    return 1 # WALK DOWN
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            return 2 # WALK LEFT
                                else:
                                    if features["Evader(UP) - Teammate(DOWN)"] <= 0.118576:
                                        return 3 # WALK RIGHT
                                    else:
                                        return 1 # WALK DOWN
                            else:
                                if features["Teammate(Teammate(UP)) - Teammate(Teammate(LEFT))"] <= 0.220347:
                                    return 2 # WALK LEFT
                                else:
                                    if features["Teammate(Teammate(UP)) - Agent_Row"] <= -9.216949:
                                        return 3 # WALK RIGHT
                                    else:
                                        return 1 # WALK DOWN
                    else:
                        if features["Teammate(LEFT) - Time_Left"] <= -0.119999:
                            if features["Evader(LEFT)"] <= 0.000094:
                                if features["Evader(RIGHT) - Teammate(Teammate(LEFT))"] <= 0.711409:
                                    if features["Evader(RIGHT) - Time_Left"] <= -0.106666:
                                        return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                                else:
                                    if features["Teammate(UP) - Time_Left"] <= 0.082215:
                                        if features["Evader(RIGHT) - Teammate(Teammate(LEFT))"] <= 0.849495:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                            else:
                                if features["Evader(DOWN) - Evader(LEFT)"] <= 0.045144:
                                    if features["Evader(DOWN) - Agent_Row"] <= -1.999709:
                                        if features["Evader(UP) - Teammate(UP)"] <= 0.625590:
                                            if features["Teammate(Evader(UP)) - Time_Left"] <= -0.350581:
                                                return 1 # WALK DOWN
                                            else:
                                                if features["Evader(RIGHT) - Teammate(Evader(LEFT))"] <= 0.296072:
                                                    if features["Teammate(Evader(RIGHT)) - Agent_Column"] <= -5.656484:
                                                        return 0 # WALK UP
                                                    else:
                                                        return 3 # WALK RIGHT
                                                else:
                                                    if features["Evader(UP) - Teammate(Teammate(UP))"] <= 0.583459:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        return 0 # WALK UP
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                                else:
                                    if features["Evader(RIGHT) - Agent_Column"] <= -7.484754:
                                        if features["Teammate(Evader(DOWN)) - Teammate(Teammate(RIGHT))"] <= -0.004438:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        return 3 # WALK RIGHT
                        else:
                            if features["Evader(RIGHT) - Agent_Column"] <= -11.200958:
                                return 0 # WALK UP
                            else:
                                if features["Evader(LEFT)"] <= 0.000030:
                                    if features["Evader(LEFT) - Evader(RIGHT)"] <= -0.800686:
                                        if features["Teammate(RIGHT) - Agent_Column"] <= -9.999990:
                                            return 3 # WALK RIGHT
                                        else:
                                            if features["Evader(DOWN) - Agent_Column"] <= -0.999986:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                                else:
                                    if features["Evader(UP) - Evader(RIGHT)"] <= -0.075976:
                                        return 3 # WALK RIGHT
                                    else:
                                        if features["Teammate(Evader(UP)) - Teammate(Evader(DOWN))"] <= 0.306749:
                                            return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(RIGHT) - Teammate(Evader(RIGHT))"] <= 0.036757:
                                                if features["Evader(DOWN) - Teammate(Evader(RIGHT))"] <= -0.085346:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    return 1 # WALK DOWN
                                            else:
                                                if features["Teammate(RIGHT) - Teammate(Evader(DOWN))"] <= 0.651956:
                                                    return 0 # WALK UP
                                                else:
                                                    return 3 # WALK RIGHT
                else:
                    if features["Evader(UP) - Agent_Row"] <= -0.998725:
                        if features["Evader(LEFT)"] <= 0.000012:
                            if features["Evader(UP) - Evader(RIGHT)"] <= -0.802849:
                                if features["Teammate(LEFT) - Agent_Row"] <= -12.809425:
                                    if features["Teammate(UP) - Agent_Column"] <= -5.999862:
                                        return 1 # WALK DOWN
                                    else:
                                        return 3 # WALK RIGHT
                                else:
                                    if features["Evader(UP) - Agent_Row"] <= -6.999963:
                                        if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.076421:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        if features["Evader(UP)"] <= 0.000282:
                                            if features["Teammate(RIGHT) - Time_Left"] <= 0.271440:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            return 1 # WALK DOWN
                            else:
                                if features["Teammate(Teammate(UP)) - Agent_Column"] <= 0.130058:
                                    if features["Evader(RIGHT) - Agent_Column"] <= -11.200908:
                                        return 1 # WALK DOWN
                                    else:
                                        return 3 # WALK RIGHT
                                else:
                                    if features["Evader(RIGHT) - Agent_Row"] <= -4.606645:
                                        return 3 # WALK RIGHT
                                    else:
                                        return 1 # WALK DOWN
                        else:
                            if features["Evader(RIGHT) - Time_Left"] <= 0.340537:
                                if features["Teammate(LEFT)"] <= 0.002616:
                                    if features["Teammate(UP) - Teammate(RIGHT)"] <= -0.404301:
                                        return 1 # WALK DOWN
                                    else:
                                        if features["Teammate(Evader(LEFT)) - Agent_Column"] <= -0.972347:
                                            if features["Teammate(UP) - Teammate(Teammate(DOWN))"] <= -0.286108:
                                                return 3 # WALK RIGHT
                                            else:
                                                if features["Evader(RIGHT) - Time_Left"] <= -0.022977:
                                                    return 1 # WALK DOWN
                                                else:
                                                    if features["Teammate(DOWN) - Agent_Row"] <= -10.999922:
                                                        return 3 # WALK RIGHT
                                                    else:
                                                        if features["Teammate(Evader(RIGHT)) - Agent_Column"] <= -3.665533:
                                                            return 1 # WALK DOWN
                                                        else:
                                                            return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(DOWN) - Time_Left"] <= -0.099956:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 1 # WALK DOWN
                                else:
                                    if features["Teammate(LEFT) - Teammate(Teammate(RIGHT))"] <= -0.080042:
                                        if features["Teammate(RIGHT) - Teammate(Teammate(LEFT))"] <= 0.332699:
                                            if features["Evader(LEFT) - Teammate(Evader(LEFT))"] <= -0.005441:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            return 3 # WALK RIGHT
                                    else:
                                        if features["Evader(LEFT) - Time_Left"] <= -0.100118:
                                            return 1 # WALK DOWN
                                        else:
                                            return 3 # WALK RIGHT
                            else:
                                if features["Evader(LEFT) - Evader(RIGHT)"] <= -0.493848:
                                    if features["Evader(RIGHT) - Agent_Row"] <= -11.252567:
                                        if features["Evader(UP) - Agent_Column"] <= -11.999924:
                                            return 1 # WALK DOWN
                                        else:
                                            if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.126398:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                    else:
                                        if features["Evader(UP) - Agent_Row"] <= -9.999994:
                                            return 1 # WALK DOWN
                                        else:
                                            if features["Teammate(LEFT) - Teammate(RIGHT)"] <= -0.481636:
                                                if features["Evader(DOWN) - Teammate(RIGHT)"] <= -0.354562:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    if features["Evader(UP) - Teammate(Evader(UP))"] <= 0.086670:
                                                        if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.212944:
                                                            return 3 # WALK RIGHT
                                                        else:
                                                            return 1 # WALK DOWN
                                                    else:
                                                        return 1 # WALK DOWN
                                            else:
                                                if features["Evader(RIGHT) - Agent_Column"] <= -10.280332:
                                                    return 1 # WALK DOWN
                                                else:
                                                    if features["Evader(UP) - Evader(LEFT)"] <= -0.000194:
                                                        return 1 # WALK DOWN
                                                    else:
                                                        return 3 # WALK RIGHT
                                else:
                                    if features["Evader(RIGHT) - Teammate(LEFT)"] <= 0.366936:
                                        if features["Evader(UP) - Teammate(RIGHT)"] <= -0.282980:
                                            return 1 # WALK DOWN
                                        else:
                                            if features["Evader(DOWN) - Evader(LEFT)"] <= 0.241990:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                    else:
                                        if features["Evader(UP) - Teammate(Evader(DOWN))"] <= -0.307494:
                                            return 1 # WALK DOWN
                                        else:
                                            if features["Evader(LEFT) - Teammate(LEFT)"] <= 0.006904:
                                                return 3 # WALK RIGHT
                                            else:
                                                if features["Evader(DOWN) - Teammate(Evader(RIGHT))"] <= -0.024278:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    return 1 # WALK DOWN
                    else:
                        if features["Evader(LEFT) - Agent_Column"] <= -0.996284:
                            return 3 # WALK RIGHT
                        else:
                            return 1 # WALK DOWN
            else:
                if features["Teammate(Evader(UP)) - Teammate(Teammate(UP))"] <= 0.006688:
                    if features["Evader(DOWN) - Teammate(Evader(RIGHT))"] <= -0.176057:
                        if features["Evader(LEFT) - Agent_Column"] <= -1.921788:
                            if features["Evader(RIGHT) - Teammate(Evader(DOWN))"] <= 0.199647:
                                if features["Teammate(UP) - Teammate(RIGHT)"] <= -0.492849:
                                    return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
                            else:
                                if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.148623:
                                    return 3 # WALK RIGHT
                                else:
                                    return 1 # WALK DOWN
                        else:
                            return 2 # WALK LEFT
                    else:
                        if features["Evader(LEFT) - Teammate(UP)"] <= 0.060130:
                            if features["Evader(RIGHT) - Teammate(DOWN)"] <= 0.224881:
                                if features["Evader(RIGHT) - Teammate(LEFT)"] <= 0.391892:
                                    return 1 # WALK DOWN
                                else:
                                    return 3 # WALK RIGHT
                            else:
                                return 1 # WALK DOWN
                        else:
                            if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.025459:
                                if features["Evader(RIGHT) - Teammate(Evader(LEFT))"] <= 0.215385:
                                    return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
                            else:
                                return 3 # WALK RIGHT
                else:
                    if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.003896:
                        if features["Evader(LEFT) - Evader(RIGHT)"] <= -0.236718:
                            if features["Evader(DOWN)"] <= 0.174549:
                                if features["Evader(LEFT) - Teammate(DOWN)"] <= -0.010930:
                                    return 3 # WALK RIGHT
                                else:
                                    if features["Teammate(UP) - Time_Left"] <= 0.427390:
                                        return 2 # WALK LEFT
                                    else:
                                        return 3 # WALK RIGHT
                            else:
                                if features["Teammate(DOWN) - Teammate(Evader(UP))"] <= -0.246358:
                                    if features["Evader(LEFT) - Teammate(RIGHT)"] <= -0.581953:
                                        return 3 # WALK RIGHT
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
                        else:
                            if features["Teammate(Evader(UP)) - Teammate(Teammate(LEFT))"] <= 0.159627:
                                if features["Teammate(Teammate(UP)) - Time_Left"] <= 0.074755:
                                    if features["Evader(DOWN) - Teammate(Evader(UP))"] <= -0.044267:
                                        if features["Teammate(Teammate(RIGHT)) - Agent_Row"] <= -8.867273:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 2 # WALK LEFT
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    if features["Evader(DOWN) - Teammate(Evader(UP))"] <= -0.175963:
                                        return 3 # WALK RIGHT
                                    else:
                                        return 1 # WALK DOWN
                            else:
                                if features["Teammate(RIGHT) - Agent_Column"] <= -1.416308:
                                    if features["Teammate(RIGHT) - Agent_Row"] <= -6.451110:
                                        return 2 # WALK LEFT
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    return 0 # WALK UP
                    else:
                        if features["Teammate(DOWN) - Teammate(RIGHT)"] <= -0.000001:
                            if features["Evader(UP) - Evader(LEFT)"] <= 0.150336:
                                if features["Teammate(Evader(RIGHT)) - Time_Left"] <= 0.405234:
                                    return 1 # WALK DOWN
                                else:
                                    return 3 # WALK RIGHT
                            else:
                                if features["Teammate(DOWN) - Agent_Column"] <= -6.999998:
                                    return 1 # WALK DOWN
                                else:
                                    if features["Teammate(Evader(RIGHT)) - Time_Left"] <= 0.183211:
                                        return 1 # WALK DOWN
                                    else:
                                        return 3 # WALK RIGHT
                        else:
                            return 3 # WALK RIGHT
        else:
            if features["Evader(LEFT) - Teammate(Evader(RIGHT))"] <= 0.140065:
                if features["Evader(DOWN) - Agent_Row"] <= -12.131467:
                    if features["Evader(RIGHT) - Teammate(UP)"] <= 0.017064:
                        return 1 # WALK DOWN
                    else:
                        return 3 # WALK RIGHT
                else:
                    if features["Evader(UP) - Teammate(LEFT)"] <= 0.077781:
                        if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.209504:
                            if features["Evader(RIGHT) - Teammate(LEFT)"] <= 0.338002:
                                if features["Evader(LEFT) - Teammate(LEFT)"] <= 0.056588:
                                    if features["Teammate(Evader(RIGHT)) - Time_Left"] <= -0.598638:
                                        return 3 # WALK RIGHT
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    if features["Evader(RIGHT) - Time_Left"] <= -0.321333:
                                        return 2 # WALK LEFT
                                    else:
                                        return 1 # WALK DOWN
                            else:
                                if features["Evader(UP)"] <= 0.000028:
                                    if features["Teammate(DOWN) - Time_Left"] <= -0.689922:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.000010:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 1 # WALK DOWN
                                else:
                                    if features["Teammate(DOWN) - Agent_Column"] <= -0.614062:
                                        if features["Teammate(DOWN) - Agent_Row"] <= -11.999786:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        return 3 # WALK RIGHT
                        else:
                            if features["Teammate(Evader(RIGHT)) - Agent_Row"] <= -2.679749:
                                if features["Evader(UP)"] <= 0.000009:
                                    return 1 # WALK DOWN
                                else:
                                    if features["Agent_Row - Agent_Column"] <= 0.500000:
                                        if features["Evader(DOWN) - Evader(RIGHT)"] <= 0.013074:
                                            if features["Evader(UP) - Agent_Column"] <= -10.999843:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(DOWN) - Agent_Column"] <= -4.586734:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                    else:
                                        if features["Teammate(LEFT) - Teammate(Evader(DOWN))"] <= 0.429331:
                                            return 1 # WALK DOWN
                                        else:
                                            return 3 # WALK RIGHT
                            else:
                                if features["Evader(LEFT) - Teammate(Evader(RIGHT))"] <= -0.191808:
                                    if features["Teammate(RIGHT) - Agent_Column"] <= -0.665801:
                                        if features["Evader(RIGHT) - Teammate(DOWN)"] <= -0.270483:
                                            return 1 # WALK DOWN
                                        else:
                                            if features["Evader(RIGHT) - Agent_Column"] <= -11.200444:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    return 1 # WALK DOWN
                    else:
                        if features["Teammate(UP) - Teammate(RIGHT)"] <= 0.000039:
                            if features["Evader(RIGHT) - Teammate(Evader(UP))"] <= 0.066803:
                                if features["Evader(DOWN) - Time_Left"] <= 0.243933:
                                    return 2 # WALK LEFT
                                else:
                                    if features["Teammate(DOWN) - Teammate(Evader(RIGHT))"] <= -0.241267:
                                        return 1 # WALK DOWN
                                    else:
                                        if features["Evader(RIGHT) - Teammate(DOWN)"] <= -0.455131:
                                            return 1 # WALK DOWN
                                        else:
                                            return 2 # WALK LEFT
                            else:
                                if features["Teammate(DOWN) - Teammate(Evader(RIGHT))"] <= 0.032093:
                                    return 1 # WALK DOWN
                                else:
                                    if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.253320:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(Evader(LEFT)) - Agent_Column"] <= -4.965494:
                                            return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                        else:
                            if features["Evader(LEFT) - Agent_Column"] <= -8.734434:
                                return 2 # WALK LEFT
                            else:
                                return 1 # WALK DOWN
            else:
                if features["Agent_Row - Agent_Column"] <= -6.500000:
                    if features["Evader(DOWN) - Time_Left"] <= 0.365213:
                        if features["Teammate(Evader(RIGHT)) - Agent_Column"] <= -8.968587:
                            if features["Teammate(DOWN) - Teammate(Teammate(LEFT))"] <= 0.035482:
                                if features["Teammate(RIGHT) - Teammate(Evader(UP))"] <= -0.022029:
                                    return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                            else:
                                if features["Evader(DOWN) - Teammate(UP)"] <= 0.428528:
                                    if features["Teammate(Evader(DOWN)) - Teammate(Teammate(LEFT))"] <= 0.000849:
                                        if features["Evader(LEFT) - Agent_Row"] <= -1.650067:
                                            return 1 # WALK DOWN
                                        else:
                                            return 2 # WALK LEFT
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
                        else:
                            if features["Teammate(LEFT) - Teammate(Evader(LEFT))"] <= 0.009581:
                                return 2 # WALK LEFT
                            else:
                                if features["Teammate(DOWN) - Teammate(Evader(DOWN))"] <= 0.049773:
                                    return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                    else:
                        if features["Evader(UP) - Teammate(LEFT)"] <= -0.290360:
                            if features["Evader(UP) - Teammate(UP)"] <= 0.001202:
                                return 1 # WALK DOWN
                            else:
                                if features["Evader(LEFT) - Teammate(Evader(RIGHT))"] <= 0.169654:
                                    return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                        else:
                            if features["Evader(DOWN) - Teammate(LEFT)"] <= 0.414432:
                                if features["Teammate(LEFT) - Time_Left"] <= 0.339967:
                                    return 2 # WALK LEFT
                                else:
                                    return 3 # WALK RIGHT
                            else:
                                return 1 # WALK DOWN
                else:
                    if features["Teammate(LEFT) - Agent_Row"] <= -11.999909:
                        if features["Teammate(DOWN) - Agent_Column"] <= -0.999978:
                            if features["Teammate(UP) - Agent_Row"] <= -12.389777:
                                if features["Evader(LEFT) - Time_Left"] <= 0.169383:
                                    return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                            else:
                                return 2 # WALK LEFT
                        else:
                            return 1 # WALK DOWN
                    else:
                        if features["Evader(DOWN) - Evader(LEFT)"] <= 0.000050:
                            if features["Evader(DOWN) - Agent_Column"] <= -0.633405:
                                if features["Evader(LEFT) - Teammate(LEFT)"] <= 0.773540:
                                    return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                            else:
                                return 1 # WALK DOWN
                        else:
                            if features["Evader(UP) - Teammate(LEFT)"] <= 0.095825:
                                if features["Time_Left"] <= 0.170000:
                                    if features["Evader(UP) - Teammate(Evader(UP))"] <= 0.097385:
                                        return 1 # WALK DOWN
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    if features["Teammate(Evader(UP)) - Agent_Column"] <= -0.999286:
                                        if features["Teammate(UP) - Agent_Row"] <= -6.981251:
                                            if features["Teammate(UP) - Teammate(RIGHT)"] <= 0.000814:
                                                if features["Evader(UP)"] <= 0.000056:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 2 # WALK LEFT
                                            else:
                                                if features["Evader(RIGHT) - Agent_Row"] <= -11.996783:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 1 # WALK DOWN
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        return 1 # WALK DOWN
                            else:
                                if features["Teammate(UP) - Teammate(RIGHT)"] <= 0.203883:
                                    if features["Teammate(Evader(UP)) - Teammate(Evader(RIGHT))"] <= 0.002028:
                                        return 1 # WALK DOWN
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
    else:
        if features["Evader(UP) - Evader(LEFT)"] <= -0.000009:
            if features["Evader(DOWN) - Evader(LEFT)"] <= -0.151177:
                if features["Evader(UP)"] <= 0.662776:
                    if features["Evader(RIGHT) - Teammate(DOWN)"] <= 0.000262:
                        if features["Evader(LEFT) - Time_Left"] <= 0.146303:
                            if features["Teammate(RIGHT) - Teammate(Teammate(DOWN))"] <= -0.148891:
                                if features["Evader(UP) - Teammate(LEFT)"] <= -0.230958:
                                    return 2 # WALK LEFT
                                else:
                                    return 0 # WALK UP
                            else:
                                if features["Evader(DOWN) - Evader(LEFT)"] <= -0.231362:
                                    return 2 # WALK LEFT
                                else:
                                    return 1 # WALK DOWN
                        else:
                            if features["Evader(RIGHT) - Teammate(UP)"] <= 0.000108:
                                if features["Evader(UP) - Agent_Column"] <= -0.458538:
                                    if features["Evader(DOWN) - Teammate(Evader(LEFT))"] <= -0.075664:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Evader(LEFT) - Teammate(Evader(DOWN))"] <= 0.144754:
                                            return 1 # WALK DOWN
                                        else:
                                            return 2 # WALK LEFT
                                else:
                                    return 0 # WALK UP
                            else:
                                return 2 # WALK LEFT
                    else:
                        if features["Teammate(DOWN) - Time_Left"] <= -0.099962:
                            if features["Evader(DOWN) - Teammate(Teammate(DOWN))"] <= 0.035857:
                                if features["Teammate(UP) - Teammate(Teammate(LEFT))"] <= -0.119850:
                                    return 0 # WALK UP
                                else:
                                    if features["Evader(UP) - Evader(RIGHT)"] <= 0.374599:
                                        if features["Evader(DOWN) - Teammate(RIGHT)"] <= -0.452002:
                                            return 2 # WALK LEFT
                                        else:
                                            if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.094824:
                                                if features["Teammate(DOWN)"] <= 0.000060:
                                                    if features["Teammate(Evader(RIGHT)) - Agent_Column"] <= -7.941223:
                                                        return 2 # WALK LEFT
                                                    else:
                                                        if features["Evader(RIGHT) - Teammate(DOWN)"] <= 0.003871:
                                                            return 2 # WALK LEFT
                                                        else:
                                                            return 1 # WALK DOWN
                                                else:
                                                    return 2 # WALK LEFT
                                            else:
                                                return 1 # WALK DOWN
                                    else:
                                        return 2 # WALK LEFT
                            else:
                                if features["Evader(LEFT) - Teammate(UP)"] <= 0.021922:
                                    if features["Teammate(Evader(DOWN)) - Agent_Column"] <= -8.847611:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Evader(RIGHT) - Teammate(Evader(UP))"] <= -0.308221:
                                            return 2 # WALK LEFT
                                        else:
                                            return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                        else:
                            if features["Evader(RIGHT) - Teammate(UP)"] <= -0.437488:
                                return 2 # WALK LEFT
                            else:
                                if features["Teammate(Evader(UP)) - Teammate(Evader(RIGHT))"] <= 0.118745:
                                    if features["Evader(UP) - Teammate(UP)"] <= -0.100880:
                                        return 1 # WALK DOWN
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 2 # WALK LEFT
                else:
                    if features["Evader(RIGHT) - Agent_Column"] <= -1.999878:
                        if features["Evader(RIGHT)"] <= 0.000053:
                            if features["Evader(LEFT)"] <= 0.803477:
                                return 2 # WALK LEFT
                            else:
                                if features["Agent_Row - Agent_Column"] <= 8.500000:
                                    if features["Agent_Row - Agent_Column"] <= -2.500000:
                                        return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 0 # WALK UP
                        else:
                            if features["Evader(DOWN) - Agent_Row"] <= -11.999971:
                                return 0 # WALK UP
                            else:
                                return 2 # WALK LEFT
                    else:
                        return 0 # WALK UP
            else:
                if features["Evader(DOWN) - Evader(LEFT)"] <= 0.000006:
                    if features["Evader(RIGHT)"] <= 0.000075:
                        if features["Evader(UP) - Evader(LEFT)"] <= -0.823531:
                            if features["Evader(RIGHT) - Agent_Column"] <= -1.999952:
                                if features["Agent_Row - Agent_Column"] <= -0.500000:
                                    return 1 # WALK DOWN
                                else:
                                    if features["Evader(RIGHT) - Agent_Row"] <= -11.999973:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(DOWN) - Agent_Column"] <= -2.999892:
                                            return 1 # WALK DOWN
                                        else:
                                            return 2 # WALK LEFT
                            else:
                                return 1 # WALK DOWN
                        else:
                            if features["Teammate(RIGHT) - Teammate(Evader(LEFT))"] <= -0.600858:
                                return 2 # WALK LEFT
                            else:
                                if features["Evader(UP) - Evader(LEFT)"] <= -0.751404:
                                    if features["Teammate(UP) - Agent_Column"] <= -0.816651:
                                        return 2 # WALK LEFT
                                    else:
                                        return 1 # WALK DOWN
                                else:
                                    return 2 # WALK LEFT
                    else:
                        if features["Evader(LEFT) - Teammate(Teammate(LEFT))"] <= 0.029338:
                            if features["Teammate(Evader(DOWN)) - Teammate(Teammate(LEFT))"] <= -0.088780:
                                if features["Evader(UP) - Time_Left"] <= 0.210684:
                                    if features["Teammate(RIGHT)"] <= 0.000028:
                                        if features["Teammate(UP) - Agent_Row"] <= -8.476417:
                                            if features["Teammate(DOWN) - Teammate(Evader(RIGHT))"] <= -0.060766:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 2 # WALK LEFT
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        if features["Evader(LEFT) - Teammate(Teammate(UP))"] <= 0.236210:
                                            if features["Evader(UP) - Teammate(UP)"] <= 0.039544:
                                                if features["Evader(LEFT) - Teammate(Evader(DOWN))"] <= 0.136232:
                                                    return 1 # WALK DOWN
                                                else:
                                                    if features["Teammate(Teammate(RIGHT)) - Agent_Column"] <= -8.888239:
                                                        return 2 # WALK LEFT
                                                    else:
                                                        return 1 # WALK DOWN
                                            else:
                                                return 2 # WALK LEFT
                                        else:
                                            return 2 # WALK LEFT
                                else:
                                    if features["Teammate(Evader(DOWN)) - Teammate(Teammate(UP))"] <= -0.110307:
                                        if features["Teammate(UP) - Teammate(LEFT)"] <= -0.006804:
                                            return 0 # WALK UP
                                        else:
                                            return 1 # WALK DOWN
                                    else:
                                        if features["Teammate(DOWN) - Teammate(Evader(DOWN))"] <= -0.149457:
                                            return 1 # WALK DOWN
                                        else:
                                            return 2 # WALK LEFT
                            else:
                                if features["Teammate(Evader(DOWN)) - Teammate(Teammate(UP))"] <= 0.248904:
                                    if features["Evader(UP) - Teammate(Evader(RIGHT))"] <= 0.117102:
                                        if features["Teammate(DOWN) - Time_Left"] <= 0.337427:
                                            if features["Teammate(Evader(DOWN)) - Teammate(Teammate(DOWN))"] <= -0.033824:
                                                return 2 # WALK LEFT
                                            else:
                                                if features["Teammate(Teammate(LEFT)) - Teammate(Teammate(RIGHT))"] <= 0.349082:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 2 # WALK LEFT
                                        else:
                                            if features["Teammate(Teammate(DOWN)) - Teammate(Teammate(RIGHT))"] <= 0.225694:
                                                return 1 # WALK DOWN
                                            else:
                                                return 3 # WALK RIGHT
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 2 # WALK LEFT
                        else:
                            if features["Teammate(UP) - Teammate(RIGHT)"] <= 0.000028:
                                if features["Teammate(Evader(UP)) - Time_Left"] <= 0.001364:
                                    if features["Agent_Column - Time_Left"] <= 1.450000:
                                        return 1 # WALK DOWN
                                    else:
                                        if features["Teammate(UP) - Teammate(RIGHT)"] <= -0.003936:
                                            if features["Evader(RIGHT) - Teammate(UP)"] <= 0.011176:
                                                return 2 # WALK LEFT
                                            else:
                                                if features["Evader(DOWN) - Agent_Row"] <= -5.580650:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 1 # WALK DOWN
                                        else:
                                            return 2 # WALK LEFT
                                else:
                                    return 2 # WALK LEFT
                            else:
                                if features["Evader(RIGHT) - Teammate(DOWN)"] <= 0.101765:
                                    if features["Teammate(Evader(DOWN)) - Teammate(Teammate(DOWN))"] <= 0.004549:
                                        if features["Teammate(RIGHT) - Teammate(Evader(UP))"] <= -0.150489:
                                            if features["Teammate(Teammate(UP)) - Agent_Row"] <= -5.814597:
                                                return 2 # WALK LEFT
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            if features["Evader(DOWN) - Agent_Column"] <= -6.780006:
                                                return 2 # WALK LEFT
                                            else:
                                                if features["Teammate(RIGHT) - Agent_Column"] <= -5.854697:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(Evader(LEFT)) - Teammate(Teammate(DOWN))"] <= 0.118775:
                                            if features["Teammate(DOWN) - Teammate(Teammate(RIGHT))"] <= -0.006604:
                                                return 2 # WALK LEFT
                                            else:
                                                if features["Evader(LEFT)"] <= 0.453203:
                                                    if features["Teammate(RIGHT) - Teammate(Evader(RIGHT))"] <= 0.003609:
                                                        return 1 # WALK DOWN
                                                    else:
                                                        return 3 # WALK RIGHT
                                                else:
                                                    return 2 # WALK LEFT
                                        else:
                                            if features["Evader(LEFT) - Time_Left"] <= 0.301920:
                                                if features["Teammate(UP) - Teammate(Teammate(RIGHT))"] <= 0.020166:
                                                    return 2 # WALK LEFT
                                                else:
                                                    if features["Teammate(Evader(UP)) - Agent_Column"] <= -8.954576:
                                                        if features["Teammate(RIGHT) - Teammate(Teammate(LEFT))"] <= -0.325949:
                                                            return 1 # WALK DOWN
                                                        else:
                                                            return 2 # WALK LEFT
                                                    else:
                                                        return 1 # WALK DOWN
                                            else:
                                                if features["Teammate(LEFT) - Teammate(RIGHT)"] <= 0.495717:
                                                    return 2 # WALK LEFT
                                                else:
                                                    if features["Evader(LEFT) - Teammate(LEFT)"] <= -0.303886:
                                                        return 2 # WALK LEFT
                                                    else:
                                                        return 1 # WALK DOWN
                                else:
                                    if features["Evader(DOWN) - Agent_Column"] <= -8.734299:
                                        if features["Teammate(UP) - Teammate(LEFT)"] <= 0.603664:
                                            if features["Teammate(Evader(UP)) - Teammate(Evader(RIGHT))"] <= 0.073552:
                                                return 1 # WALK DOWN
                                            else:
                                                if features["Evader(RIGHT) - Teammate(LEFT)"] <= -0.592495:
                                                    return 2 # WALK LEFT
                                                else:
                                                    if features["Teammate(UP) - Teammate(LEFT)"] <= 0.000099:
                                                        if features["Teammate(UP) - Agent_Row"] <= -7.559699:
                                                            if features["Evader(DOWN) - Teammate(Evader(RIGHT))"] <= 0.146811:
                                                                return 3 # WALK RIGHT
                                                            else:
                                                                return 1 # WALK DOWN
                                                        else:
                                                            return 1 # WALK DOWN
                                                    else:
                                                        return 1 # WALK DOWN
                                        else:
                                            return 2 # WALK LEFT
                                    else:
                                        return 1 # WALK DOWN
                else:
                    if features["Evader(DOWN) - Agent_Row"] <= -12.129219:
                        return 2 # WALK LEFT
                    else:
                        if features["Evader(RIGHT) - Teammate(Teammate(UP))"] <= -0.000046:
                            if features["Evader(UP) - Evader(LEFT)"] <= -0.861075:
                                if features["Teammate(RIGHT) - Agent_Column"] <= -1.096103:
                                    if features["Teammate(Evader(UP)) - Agent_Column"] <= -3.999623:
                                        return 1 # WALK DOWN
                                    else:
                                        if features["Evader(DOWN) - Agent_Row"] <= -3.132098:
                                            return 2 # WALK LEFT
                                        else:
                                            return 1 # WALK DOWN
                                else:
                                    return 1 # WALK DOWN
                            else:
                                if features["Evader(RIGHT) - Teammate(UP)"] <= 0.000062:
                                    return 1 # WALK DOWN
                                else:
                                    if features["Teammate(RIGHT) - Teammate(Evader(UP))"] <= -0.004799:
                                        if features["Evader(LEFT) - Teammate(Teammate(DOWN))"] <= 0.014361:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 2 # WALK LEFT
                                    else:
                                        return 1 # WALK DOWN
                        else:
                            if features["Evader(LEFT) - Teammate(Evader(DOWN))"] <= -0.014088:
                                return 1 # WALK DOWN
                            else:
                                return 2 # WALK LEFT
        else:
            if features["Evader(DOWN)"] <= 0.006076:
                if features["Evader(UP) - Evader(LEFT)"] <= 0.267283:
                    if features["Evader(DOWN) - Agent_Row"] <= -1.999995:
                        if features["Evader(LEFT) - Time_Left"] <= 0.143812:
                            if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.025456:
                                if features["Evader(UP) - Evader(DOWN)"] <= 0.474541:
                                    if features["Evader(RIGHT) - Agent_Column"] <= -6.873317:
                                        if features["Evader(UP) - Teammate(Teammate(RIGHT))"] <= 0.334370:
                                            return 2 # WALK LEFT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 0 # WALK UP
                                else:
                                    if features["Evader(RIGHT)"] <= 0.000656:
                                        return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                            else:
                                if features["Teammate(LEFT) - Agent_Column"] <= -3.677528:
                                    if features["Teammate(Evader(RIGHT))"] <= 0.036222:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(UP) - Teammate(LEFT)"] <= 0.001077:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 2 # WALK LEFT
                                else:
                                    if features["Evader(DOWN) - Teammate(Evader(UP))"] <= -0.326875:
                                        if features["Evader(DOWN) - Time_Left"] <= -0.539619:
                                            return 2 # WALK LEFT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                        else:
                            if features["Evader(UP)"] <= 0.822424:
                                if features["Evader(DOWN) - Teammate(DOWN)"] <= 0.000006:
                                    if features["Evader(UP)"] <= 0.668954:
                                        if features["Teammate(UP) - Teammate(RIGHT)"] <= 0.348711:
                                            return 0 # WALK UP
                                        else:
                                            if features["Evader(DOWN)"] <= 0.002417:
                                                return 0 # WALK UP
                                            else:
                                                if features["Teammate(LEFT) - Time_Left"] <= 0.298922:
                                                    if features["Teammate(Evader(UP)) - Teammate(Teammate(LEFT))"] <= 0.082220:
                                                        return 0 # WALK UP
                                                    else:
                                                        return 2 # WALK LEFT
                                                else:
                                                    return 2 # WALK LEFT
                                    else:
                                        if features["Evader(DOWN)"] <= 0.000008:
                                            return 0 # WALK UP
                                        else:
                                            if features["Evader(RIGHT) - Agent_Column"] <= -1.999821:
                                                if features["Teammate(RIGHT) - Agent_Row"] <= -2.707085:
                                                    return 0 # WALK UP
                                                else:
                                                    return 2 # WALK LEFT
                                            else:
                                                return 0 # WALK UP
                                else:
                                    if features["Teammate(Evader(RIGHT)) - Time_Left"] <= 0.023389:
                                        if features["Evader(UP) - Teammate(Teammate(UP))"] <= 0.142552:
                                            if features["Teammate(DOWN)"] <= 0.000036:
                                                return 0 # WALK UP
                                            else:
                                                return 2 # WALK LEFT
                                        else:
                                            if features["Teammate(UP) - Agent_Column"] <= -7.513665:
                                                if features["Teammate(UP) - Teammate(LEFT)"] <= 0.000669:
                                                    return 0 # WALK UP
                                                else:
                                                    return 2 # WALK LEFT
                                            else:
                                                return 0 # WALK UP
                                    else:
                                        if features["Teammate(LEFT) - Teammate(Teammate(DOWN))"] <= 0.079493:
                                            if features["Agent_Row - Agent_Column"] <= 3.500000:
                                                return 2 # WALK LEFT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            return 0 # WALK UP
                            else:
                                if features["Teammate(Teammate(UP)) - Agent_Column"] <= -1.953116:
                                    if features["Evader(RIGHT) - Agent_Row"] <= -4.999991:
                                        if features["Evader(UP) - Agent_Column"] <= -5.132574:
                                            if features["Teammate(Evader(LEFT)) - Agent_Column"] <= -7.349474:
                                                return 2 # WALK LEFT
                                            else:
                                                if features["Evader(UP) - Agent_Row"] <= -8.132611:
                                                    if features["Teammate(Evader(DOWN)) - Agent_Row"] <= -11.880440:
                                                        return 2 # WALK LEFT
                                                    else:
                                                        return 0 # WALK UP
                                                else:
                                                    return 2 # WALK LEFT
                                        else:
                                            return 2 # WALK LEFT
                                    else:
                                        return 0 # WALK UP
                                else:
                                    return 0 # WALK UP
                    else:
                        return 2 # WALK LEFT
                else:
                    if features["Evader(RIGHT) - Teammate(Teammate(RIGHT))"] <= 0.035874:
                        if features["Teammate(Evader(LEFT)) - Agent_Row"] <= -13.962626:
                            if features["Evader(RIGHT) - Time_Left"] <= 0.290791:
                                return 0 # WALK UP
                            else:
                                return 3 # WALK RIGHT
                        else:
                            if features["Evader(UP) - Time_Left"] <= 0.279894:
                                if features["Evader(LEFT) - Teammate(Evader(DOWN))"] <= 0.004725:
                                    if features["Evader(RIGHT) - Time_Left"] <= -0.799786:
                                        return 2 # WALK LEFT
                                    else:
                                        return 0 # WALK UP
                                else:
                                    return 2 # WALK LEFT
                            else:
                                return 0 # WALK UP
                    else:
                        if features["Evader(RIGHT)"] <= 0.799610:
                            if features["Evader(LEFT) - Teammate(DOWN)"] <= 0.000384:
                                if features["Teammate(Evader(RIGHT)) - Agent_Row"] <= -1.831218:
                                    if features["Teammate(Evader(LEFT)) - Agent_Row"] <= -13.747152:
                                        return 3 # WALK RIGHT
                                    else:
                                        if features["Evader(DOWN)"] <= 0.000036:
                                            if features["Teammate(Teammate(RIGHT)) - Time_Left"] <= -0.690256:
                                                return 2 # WALK LEFT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            return 0 # WALK UP
                                else:
                                    if features["Teammate(DOWN) - Agent_Row"] <= -0.984823:
                                        if features["Evader(UP) - Agent_Row"] <= -1.237214:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                            else:
                                if features["Evader(LEFT) - Agent_Row"] <= -13.997157:
                                    return 3 # WALK RIGHT
                                else:
                                    if features["Teammate(Evader(UP)) - Time_Left"] <= -0.339096:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Evader(LEFT) - Teammate(LEFT)"] <= -0.002492:
                                            if features["Evader(UP) - Time_Left"] <= 0.386028:
                                                if features["Teammate(RIGHT) - Time_Left"] <= -0.199970:
                                                    return 0 # WALK UP
                                                else:
                                                    return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            if features["Teammate(UP) - Teammate(Teammate(RIGHT))"] <= 0.125106:
                                                return 0 # WALK UP
                                            else:
                                                if features["Teammate(Evader(UP)) - Teammate(Evader(RIGHT))"] <= -0.004366:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    return 0 # WALK UP
                        else:
                            if features["Teammate(Evader(LEFT)) - Agent_Row"] <= -0.961707:
                                if features["Teammate(UP) - Agent_Column"] <= -12.376530:
                                    if features["Teammate(Evader(DOWN)) - Agent_Row"] <= -9.907446:
                                        return 3 # WALK RIGHT
                                    else:
                                        return 0 # WALK UP
                                else:
                                    if features["Teammate(UP) - Teammate(RIGHT)"] <= -0.583695:
                                        return 0 # WALK UP
                                    else:
                                        if features["Teammate(UP) - Agent_Column"] <= -1.844016:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                            else:
                                return 3 # WALK RIGHT
            else:
                if features["Evader(RIGHT) - Teammate(Teammate(RIGHT))"] <= 0.004982:
                    if features["Evader(UP) - Evader(DOWN)"] <= 0.364775:
                        if features["Teammate(DOWN)"] <= 0.000094:
                            if features["Teammate(RIGHT) - Teammate(Teammate(UP))"] <= 0.335519:
                                if features["Evader(LEFT) - Teammate(Evader(RIGHT))"] <= 0.170355:
                                    if features["Teammate(LEFT) - Teammate(Evader(LEFT))"] <= -0.155204:
                                        return 1 # WALK DOWN
                                    else:
                                        if features["Evader(DOWN) - Time_Left"] <= -0.167738:
                                            if features["Evader(RIGHT) - Teammate(UP)"] <= -0.272080:
                                                return 2 # WALK LEFT
                                            else:
                                                return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(UP) - Teammate(LEFT)"] <= 0.000074:
                                                return 3 # WALK RIGHT
                                            else:
                                                if features["Teammate(Evader(UP)) - Teammate(Evader(LEFT))"] <= 0.211398:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 3 # WALK RIGHT
                                else:
                                    if features["Evader(DOWN) - Teammate(Evader(LEFT))"] <= -0.273276:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(Teammate(UP)) - Agent_Column"] <= -8.515317:
                                            return 2 # WALK LEFT
                                        else:
                                            return 1 # WALK DOWN
                            else:
                                return 2 # WALK LEFT
                        else:
                            if features["Evader(LEFT) - Teammate(Teammate(LEFT))"] <= 0.013199:
                                if features["Teammate(Evader(DOWN)) - Time_Left"] <= 0.104677:
                                    if features["Evader(UP)"] <= 0.282102:
                                        return 1 # WALK DOWN
                                    else:
                                        if features["Teammate(Teammate(RIGHT)) - Agent_Column"] <= -1.484578:
                                            if features["Teammate(Teammate(UP))"] <= 0.373793:
                                                if features["Evader(RIGHT) - Teammate(Teammate(RIGHT))"] <= 0.004229:
                                                    if features["Teammate(RIGHT) - Time_Left"] <= 0.023704:
                                                        return 2 # WALK LEFT
                                                    else:
                                                        if features["Evader(UP) - Evader(RIGHT)"] <= 0.006599:
                                                            return 1 # WALK DOWN
                                                        else:
                                                            return 2 # WALK LEFT
                                                else:
                                                    return 0 # WALK UP
                                            else:
                                                if features["Evader(LEFT) - Teammate(Teammate(LEFT))"] <= -0.005619:
                                                    if features["Evader(DOWN) - Teammate(Teammate(UP))"] <= -0.295947:
                                                        return 2 # WALK LEFT
                                                    else:
                                                        return 1 # WALK DOWN
                                                else:
                                                    return 0 # WALK UP
                                        else:
                                            if features["Teammate(Teammate(UP)) - Teammate(Teammate(LEFT))"] <= 0.284301:
                                                return 0 # WALK UP
                                            else:
                                                return 3 # WALK RIGHT
                                else:
                                    if features["Evader(DOWN) - Teammate(Teammate(UP))"] <= -0.134002:
                                        if features["Teammate(Teammate(UP)) - Agent_Row"] <= -10.644285:
                                            if features["Teammate(RIGHT) - Teammate(Teammate(UP))"] <= -0.032945:
                                                return 1 # WALK DOWN
                                            else:
                                                return 2 # WALK LEFT
                                        else:
                                            if features["Teammate(Teammate(LEFT)) - Agent_Row"] <= -8.759359:
                                                if features["Teammate(LEFT) - Teammate(Teammate(LEFT))"] <= -0.046224:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 0 # WALK UP
                                            else:
                                                return 2 # WALK LEFT
                                    else:
                                        if features["Evader(UP) - Teammate(Teammate(DOWN))"] <= 0.078387:
                                            if features["Evader(DOWN) - Teammate(Teammate(DOWN))"] <= -0.101063:
                                                return 2 # WALK LEFT
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            if features["Teammate(Evader(LEFT)) - Agent_Row"] <= -8.783016:
                                                return 1 # WALK DOWN
                                            else:
                                                if features["Evader(UP) - Time_Left"] <= 0.326002:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 1 # WALK DOWN
                            else:
                                if features["Teammate(RIGHT) - Time_Left"] <= -0.007663:
                                    if features["Teammate(Evader(RIGHT)) - Agent_Column"] <= -8.801539:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(Evader(DOWN)) - Teammate(Evader(RIGHT))"] <= -0.100794:
                                            if features["Evader(UP) - Agent_Column"] <= -2.615054:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            return 1 # WALK DOWN
                                else:
                                    if features["Teammate(RIGHT) - Agent_Column"] <= -1.428814:
                                        if features["Evader(UP) - Teammate(Evader(DOWN))"] <= 0.311308:
                                            if features["Evader(UP) - Teammate(Evader(UP))"] <= 0.236103:
                                                if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.037577:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 0 # WALK UP
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            if features["Teammate(Evader(DOWN)) - Time_Left"] <= 0.015947:
                                                if features["Teammate(Evader(DOWN)) - Teammate(Evader(LEFT))"] <= -0.429230:
                                                    return 0 # WALK UP
                                                else:
                                                    return 2 # WALK LEFT
                                            else:
                                                if features["Teammate(Evader(UP)) - Agent_Column"] <= -3.116712:
                                                    return 0 # WALK UP
                                                else:
                                                    return 3 # WALK RIGHT
                                    else:
                                        return 0 # WALK UP
                    else:
                        if features["Evader(UP) - Time_Left"] <= 0.370856:
                            if features["Teammate(Evader(DOWN)) - Teammate(Teammate(RIGHT))"] <= -0.241777:
                                if features["Evader(RIGHT)"] <= 0.283442:
                                    if features["Teammate(LEFT) - Agent_Row"] <= -9.999638:
                                        if features["Teammate(DOWN) - Teammate(LEFT)"] <= 0.000008:
                                            if features["Teammate(Evader(UP)) - Teammate(Evader(LEFT))"] <= 0.094569:
                                                return 2 # WALK LEFT
                                            else:
                                                return 0 # WALK UP
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    return 3 # WALK RIGHT
                            else:
                                if features["Teammate(Teammate(UP)) - Teammate(Teammate(LEFT))"] <= -0.049127:
                                    if features["Teammate(RIGHT) - Teammate(Teammate(UP))"] <= -0.085603:
                                        return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    if features["Teammate(Evader(DOWN))"] <= 0.032494:
                                        return 0 # WALK UP
                                    else:
                                        if features["Teammate(DOWN) - Teammate(LEFT)"] <= -0.286452:
                                            return 2 # WALK LEFT
                                        else:
                                            if features["Teammate(Teammate(DOWN)) - Agent_Row"] <= -9.788798:
                                                return 0 # WALK UP
                                            else:
                                                return 2 # WALK LEFT
                        else:
                            if features["Teammate(UP) - Teammate(Evader(DOWN))"] <= 0.366633:
                                if features["Teammate(Evader(DOWN)) - Teammate(Teammate(RIGHT))"] <= -0.090255:
                                    return 0 # WALK UP
                                else:
                                    if features["Agent_Column - Time_Left"] <= 9.910000:
                                        return 2 # WALK LEFT
                                    else:
                                        return 0 # WALK UP
                            else:
                                if features["Teammate(DOWN) - Teammate(Teammate(DOWN))"] <= -0.016443:
                                    if features["Teammate(Evader(UP)) - Teammate(Evader(LEFT))"] <= 0.110475:
                                        return 2 # WALK LEFT
                                    else:
                                        if features["Evader(RIGHT) - Teammate(RIGHT)"] <= 0.226344:
                                            return 0 # WALK UP
                                        else:
                                            return 3 # WALK RIGHT
                                else:
                                    return 1 # WALK DOWN
                else:
                    if features["Teammate(RIGHT) - Teammate(Teammate(LEFT))"] <= -0.242191:
                        if features["Teammate(DOWN) - Teammate(Evader(RIGHT))"] <= -0.040962:
                            if features["Teammate(UP) - Teammate(LEFT)"] <= 0.000004:
                                return 3 # WALK RIGHT
                            else:
                                if features["Teammate(RIGHT) - Teammate(Evader(LEFT))"] <= -0.133783:
                                    return 1 # WALK DOWN
                                else:
                                    if features["Evader(LEFT) - Evader(RIGHT)"] <= 0.081215:
                                        return 3 # WALK RIGHT
                                    else:
                                        return 2 # WALK LEFT
                        else:
                            if features["Teammate(Evader(UP)) - Time_Left"] <= -0.166229:
                                return 2 # WALK LEFT
                            else:
                                if features["Teammate(UP) - Teammate(LEFT)"] <= -0.001722:
                                    if features["Evader(RIGHT) - Teammate(Evader(UP))"] <= -0.086889:
                                        return 0 # WALK UP
                                    else:
                                        return 3 # WALK RIGHT
                                else:
                                    return 2 # WALK LEFT
                    else:
                        if features["Evader(UP) - Evader(DOWN)"] <= 0.332213:
                            if features["Teammate(Evader(LEFT))"] <= 0.179778:
                                if features["Teammate(UP) - Teammate(RIGHT)"] <= -0.013901:
                                    if features["Teammate(Evader(DOWN)) - Agent_Row"] <= -8.586633:
                                        return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    if features["Teammate(UP) - Teammate(LEFT)"] <= 0.404357:
                                        if features["Teammate(Evader(RIGHT)) - Teammate(Teammate(RIGHT))"] <= -0.002350:
                                            return 2 # WALK LEFT
                                        else:
                                            if features["Teammate(Teammate(UP)) - Agent_Column"] <= -8.934669:
                                                return 2 # WALK LEFT
                                            else:
                                                return 3 # WALK RIGHT
                                    else:
                                        if features["Evader(UP) - Teammate(Evader(DOWN))"] <= 0.191651:
                                            if features["Evader(LEFT) - Teammate(UP)"] <= -0.444088:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            if features["Evader(RIGHT) - Time_Left"] <= 0.034039:
                                                return 2 # WALK LEFT
                                            else:
                                                if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.144978:
                                                    return 3 # WALK RIGHT
                                                else:
                                                    return 1 # WALK DOWN
                            else:
                                if features["Teammate(Evader(UP)) - Time_Left"] <= 0.308583:
                                    if features["Teammate(DOWN) - Teammate(LEFT)"] <= -0.000000:
                                        if features["Teammate(DOWN) - Teammate(Evader(DOWN))"] <= 0.005640:
                                            if features["Evader(UP) - Evader(DOWN)"] <= 0.177359:
                                                if features["Teammate(LEFT) - Teammate(Teammate(RIGHT))"] <= 0.061582:
                                                    return 1 # WALK DOWN
                                                else:
                                                    return 3 # WALK RIGHT
                                            else:
                                                if features["Evader(RIGHT) - Agent_Column"] <= -8.784472:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 1 # WALK DOWN
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        return 2 # WALK LEFT
                                else:
                                    if features["Teammate(LEFT) - Teammate(Teammate(LEFT))"] <= -0.002035:
                                        if features["Evader(UP) - Teammate(Teammate(RIGHT))"] <= 0.051533:
                                            return 0 # WALK UP
                                        else:
                                            return 2 # WALK LEFT
                                    else:
                                        if features["Evader(DOWN) - Teammate(RIGHT)"] <= 0.074503:
                                            if features["Teammate(LEFT) - Agent_Row"] <= -9.660471:
                                                return 0 # WALK UP
                                            else:
                                                return 1 # WALK DOWN
                                        else:
                                            return 3 # WALK RIGHT
                        else:
                            if features["Evader(LEFT) - Teammate(LEFT)"] <= 0.258029:
                                if features["Evader(UP) - Teammate(UP)"] <= 0.003245:
                                    if features["Evader(RIGHT) - Time_Left"] <= 0.222097:
                                        if features["Teammate(Evader(LEFT)) - Agent_Row"] <= -7.805418:
                                            return 0 # WALK UP
                                        else:
                                            return 2 # WALK LEFT
                                    else:
                                        if features["Teammate(LEFT) - Teammate(Evader(UP))"] <= -0.371220:
                                            return 0 # WALK UP
                                        else:
                                            if features["Evader(LEFT) - Teammate(UP)"] <= -0.356455:
                                                return 3 # WALK RIGHT
                                            else:
                                                return 0 # WALK UP
                                else:
                                    if features["Teammate(Evader(UP))"] <= 0.347439:
                                        if features["Teammate(Evader(DOWN)) - Teammate(Evader(RIGHT))"] <= -0.253545:
                                            return 3 # WALK RIGHT
                                        else:
                                            return 0 # WALK UP
                                    else:
                                        if features["Teammate(RIGHT) - Teammate(Evader(RIGHT))"] <= -0.265301:
                                            return 3 # WALK RIGHT
                                        else:
                                            if features["Teammate(Evader(RIGHT)) - Time_Left"] <= 0.322945:
                                                if features["Teammate(Teammate(RIGHT)) - Time_Left"] <= 0.203644:
                                                    if features["Teammate(UP) - Teammate(Teammate(LEFT))"] <= 0.254519:
                                                        return 0 # WALK UP
                                                    else:
                                                        return 2 # WALK LEFT
                                                else:
                                                    if features["Teammate(Evader(RIGHT)) - Teammate(Teammate(RIGHT))"] <= -0.016847:
                                                        if features["Evader(DOWN) - Evader(RIGHT)"] <= -0.289747:
                                                            return 0 # WALK UP
                                                        else:
                                                            return 2 # WALK LEFT
                                                    else:
                                                        return 0 # WALK UP
                                            else:
                                                if features["Teammate(DOWN) - Teammate(Teammate(RIGHT))"] <= -0.290308:
                                                    return 2 # WALK LEFT
                                                else:
                                                    return 0 # WALK UP
                            else:
                                if features["Evader(RIGHT) - Teammate(UP)"] <= -0.291316:
                                    return 2 # WALK LEFT
                                else:
                                    return 0 # WALK UP


def interpretable_action(Evader_Probability_Grid, Teammate_Probability_Grid, Teammate_Evader_Probability_Grid, Teammate_Teammate_Probability_Grid, Main_Agent_Position, Time_Left, Gamma, Size, Valid_Actions):
    input_representation = symbolic_representation(Evader_Probability_Grid, Teammate_Probability_Grid, Teammate_Evader_Probability_Grid, Teammate_Teammate_Probability_Grid, Main_Agent_Position, Time_Left, Gamma, Size)
    input_combinations   = get_feature_vector(input_representation)
    symbol_to_value     = {name: input_combinations[i] for i, name in enumerate(symbol_names)}
    action               = Index_to_Action[interpretable_strategy(symbol_to_value)]
    if action in Valid_Actions:
        return action
    else:
        return random.choice(Valid_Actions)
