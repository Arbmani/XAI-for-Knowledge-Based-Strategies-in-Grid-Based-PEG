import random
from INTERPRETER_2ND import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'T(E(UP))', 'T(E(DOWN))', 'T(E(LEFT))', 'T(E(RIGHT))', 'T(T(up))', 'T(T(DOWN))', 'T(T(LEFT))', 'T(T(RIGHT))', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - T(E(UP))', 'E(UP) - T(E(DOWN))', 'E(UP) - T(E(LEFT))', 'E(UP) - T(E(RIGHT))', 'E(UP) - T(T(up))', 'E(UP) - T(T(DOWN))', 'E(UP) - T(T(LEFT))', 'E(UP) - T(T(RIGHT))', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - T(E(UP))', 'E(DOWN) - T(E(DOWN))', 'E(DOWN) - T(E(LEFT))', 'E(DOWN) - T(E(RIGHT))', 'E(DOWN) - T(T(up))', 'E(DOWN) - T(T(DOWN))', 'E(DOWN) - T(T(LEFT))', 'E(DOWN) - T(T(RIGHT))', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - T(E(UP))', 'E(LEFT) - T(E(DOWN))', 'E(LEFT) - T(E(LEFT))', 'E(LEFT) - T(E(RIGHT))', 'E(LEFT) - T(T(up))', 'E(LEFT) - T(T(DOWN))', 'E(LEFT) - T(T(LEFT))', 'E(LEFT) - T(T(RIGHT))', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - T(E(UP))', 'E(RIGHT) - T(E(DOWN))', 'E(RIGHT) - T(E(LEFT))', 'E(RIGHT) - T(E(RIGHT))', 'E(RIGHT) - T(T(up))', 'E(RIGHT) - T(T(DOWN))', 'E(RIGHT) - T(T(LEFT))', 'E(RIGHT) - T(T(RIGHT))', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - T(E(UP))', 'T(up) - T(E(DOWN))', 'T(up) - T(E(LEFT))', 'T(up) - T(E(RIGHT))', 'T(up) - T(T(up))', 'T(up) - T(T(DOWN))', 'T(up) - T(T(LEFT))', 'T(up) - T(T(RIGHT))', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - T(E(UP))', 'T(DOWN) - T(E(DOWN))', 'T(DOWN) - T(E(LEFT))', 'T(DOWN) - T(E(RIGHT))', 'T(DOWN) - T(T(up))', 'T(DOWN) - T(T(DOWN))', 'T(DOWN) - T(T(LEFT))', 'T(DOWN) - T(T(RIGHT))', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - T(E(UP))', 'T(LEFT) - T(E(DOWN))', 'T(LEFT) - T(E(LEFT))', 'T(LEFT) - T(E(RIGHT))', 'T(LEFT) - T(T(up))', 'T(LEFT) - T(T(DOWN))', 'T(LEFT) - T(T(LEFT))', 'T(LEFT) - T(T(RIGHT))', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - T(E(UP))', 'T(RIGHT) - T(E(DOWN))', 'T(RIGHT) - T(E(LEFT))', 'T(RIGHT) - T(E(RIGHT))', 'T(RIGHT) - T(T(up))', 'T(RIGHT) - T(T(DOWN))', 'T(RIGHT) - T(T(LEFT))', 'T(RIGHT) - T(T(RIGHT))', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'T(E(UP)) - T(E(DOWN))', 'T(E(UP)) - T(E(LEFT))', 'T(E(UP)) - T(E(RIGHT))', 'T(E(UP)) - T(T(up))', 'T(E(UP)) - T(T(DOWN))', 'T(E(UP)) - T(T(LEFT))', 'T(E(UP)) - T(T(RIGHT))', 'T(E(UP)) - agent_row', 'T(E(UP)) - agent_column', 'T(E(UP)) - time_left', 'T(E(DOWN)) - T(E(LEFT))', 'T(E(DOWN)) - T(E(RIGHT))', 'T(E(DOWN)) - T(T(up))', 'T(E(DOWN)) - T(T(DOWN))', 'T(E(DOWN)) - T(T(LEFT))', 'T(E(DOWN)) - T(T(RIGHT))', 'T(E(DOWN)) - agent_row', 'T(E(DOWN)) - agent_column', 'T(E(DOWN)) - time_left', 'T(E(LEFT)) - T(E(RIGHT))', 'T(E(LEFT)) - T(T(up))', 'T(E(LEFT)) - T(T(DOWN))', 'T(E(LEFT)) - T(T(LEFT))', 'T(E(LEFT)) - T(T(RIGHT))', 'T(E(LEFT)) - agent_row', 'T(E(LEFT)) - agent_column', 'T(E(LEFT)) - time_left', 'T(E(RIGHT)) - T(T(up))', 'T(E(RIGHT)) - T(T(DOWN))', 'T(E(RIGHT)) - T(T(LEFT))', 'T(E(RIGHT)) - T(T(RIGHT))', 'T(E(RIGHT)) - agent_row', 'T(E(RIGHT)) - agent_column', 'T(E(RIGHT)) - time_left', 'T(T(up)) - T(T(DOWN))', 'T(T(up)) - T(T(LEFT))', 'T(T(up)) - T(T(RIGHT))', 'T(T(up)) - agent_row', 'T(T(up)) - agent_column', 'T(T(up)) - time_left', 'T(T(DOWN)) - T(T(LEFT))', 'T(T(DOWN)) - T(T(RIGHT))', 'T(T(DOWN)) - agent_row', 'T(T(DOWN)) - agent_column', 'T(T(DOWN)) - time_left', 'T(T(LEFT)) - T(T(RIGHT))', 'T(T(LEFT)) - agent_row', 'T(T(LEFT)) - agent_column', 'T(T(LEFT)) - time_left', 'T(T(RIGHT)) - agent_row', 'T(T(RIGHT)) - agent_column', 'T(T(RIGHT)) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(RIGHT)"] <= -0.000063:
        if features["E(DOWN) - E(RIGHT)"] <= -0.000046:
            if features["E(LEFT)"] <= 0.061205:
                if features["E(DOWN) - T(E(UP))"] <= 0.068957:
                    if features["E(UP) - T(T(up))"] <= 0.070289:
                        if features["E(RIGHT) - time_left"] <= 0.281037:
                            if features["E(LEFT)"] <= 0.001358:
                                if features["E(RIGHT) - T(E(DOWN))"] <= -0.068809:
                                    return 1
                                else:
                                    return 3
                            else:
                                if features["E(UP) - time_left"] <= 0.208640:
                                    if features["E(UP) - E(RIGHT)"] <= -0.096991:
                                        if features["T(DOWN)"] <= 0.138156:
                                            return 3
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -10.626912:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        if features["E(LEFT) - agent_column"] <= -0.964382:
                                            return 3
                                        else:
                                            return 0
                                else:
                                    return 3
                        else:
                            if features["E(LEFT) - time_left"] <= 0.044557:
                                if features["T(RIGHT) - agent_column"] <= 0.429038:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.170117:
                                        if features["E(UP) - E(RIGHT)"] <= -0.000336:
                                            if features["E(RIGHT) - T(E(DOWN))"] <= 0.009990:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 0
                                    else:
                                        if features["E(UP) - time_left"] <= 0.162495:
                                            if features["E(LEFT) - T(E(UP))"] <= -0.194156:
                                                if features["E(DOWN) - T(E(DOWN))"] <= 0.399073:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                        else:
                                            return 2
                                else:
                                    if features["E(UP) - T(DOWN)"] <= 0.118576:
                                        return 3
                                    else:
                                        return 1
                            else:
                                if features["T(T(up)) - T(T(LEFT))"] <= 0.220347:
                                    return 2
                                else:
                                    if features["T(T(up)) - agent_row"] <= -9.216949:
                                        return 3
                                    else:
                                        return 1
                    else:
                        if features["T(LEFT) - time_left"] <= -0.119999:
                            if features["E(LEFT)"] <= 0.000094:
                                if features["E(RIGHT) - T(T(LEFT))"] <= 0.711409:
                                    if features["E(RIGHT) - time_left"] <= -0.106666:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["T(up) - time_left"] <= 0.082215:
                                        if features["E(RIGHT) - T(T(LEFT))"] <= 0.849495:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                            else:
                                if features["E(DOWN) - E(LEFT)"] <= 0.045144:
                                    if features["E(DOWN) - agent_row"] <= -1.999709:
                                        if features["E(UP) - T(up)"] <= 0.625590:
                                            if features["T(E(UP)) - time_left"] <= -0.350581:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - T(E(LEFT))"] <= 0.296072:
                                                    if features["T(E(RIGHT)) - agent_column"] <= -5.656484:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(UP) - T(T(up))"] <= 0.583459:
                                                        return 3
                                                    else:
                                                        return 0
                                        else:
                                            return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT) - agent_column"] <= -7.484754:
                                        if features["T(E(DOWN)) - T(T(RIGHT))"] <= -0.004438:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 3
                        else:
                            if features["E(RIGHT) - agent_column"] <= -11.200958:
                                return 0
                            else:
                                if features["E(LEFT)"] <= 0.000030:
                                    if features["E(LEFT) - E(RIGHT)"] <= -0.800686:
                                        if features["T(RIGHT) - agent_column"] <= -9.999990:
                                            return 3
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -0.999986:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(UP) - E(RIGHT)"] <= -0.075976:
                                        return 3
                                    else:
                                        if features["T(E(UP)) - T(E(DOWN))"] <= 0.306749:
                                            return 3
                                        else:
                                            if features["T(RIGHT) - T(E(RIGHT))"] <= 0.036757:
                                                if features["E(DOWN) - T(E(RIGHT))"] <= -0.085346:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["T(RIGHT) - T(E(DOWN))"] <= 0.651956:
                                                    return 0
                                                else:
                                                    return 3
                else:
                    if features["E(UP) - agent_row"] <= -0.998725:
                        if features["E(LEFT)"] <= 0.000012:
                            if features["E(UP) - E(RIGHT)"] <= -0.802849:
                                if features["T(LEFT) - agent_row"] <= -12.809425:
                                    if features["T(up) - agent_column"] <= -5.999862:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(UP) - agent_row"] <= -6.999963:
                                        if features["E(DOWN) - E(RIGHT)"] <= -0.076421:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(UP)"] <= 0.000282:
                                            if features["T(RIGHT) - time_left"] <= 0.271440:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 1
                            else:
                                if features["T(T(up)) - agent_column"] <= 0.130058:
                                    if features["E(RIGHT) - agent_column"] <= -11.200908:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -4.606645:
                                        return 3
                                    else:
                                        return 1
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.340537:
                                if features["T(LEFT)"] <= 0.002616:
                                    if features["T(up) - T(RIGHT)"] <= -0.404301:
                                        return 1
                                    else:
                                        if features["T(E(LEFT)) - agent_column"] <= -0.972347:
                                            if features["T(up) - T(T(DOWN))"] <= -0.286108:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - time_left"] <= -0.022977:
                                                    return 1
                                                else:
                                                    if features["T(DOWN) - agent_row"] <= -10.999922:
                                                        return 3
                                                    else:
                                                        if features["T(E(RIGHT)) - agent_column"] <= -3.665533:
                                                            return 1
                                                        else:
                                                            return 3
                                        else:
                                            if features["T(DOWN) - time_left"] <= -0.099956:
                                                return 3
                                            else:
                                                return 1
                                else:
                                    if features["T(LEFT) - T(T(RIGHT))"] <= -0.080042:
                                        if features["T(RIGHT) - T(T(LEFT))"] <= 0.332699:
                                            if features["E(LEFT) - T(E(LEFT))"] <= -0.005441:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        if features["E(LEFT) - time_left"] <= -0.100118:
                                            return 1
                                        else:
                                            return 3
                            else:
                                if features["E(LEFT) - E(RIGHT)"] <= -0.493848:
                                    if features["E(RIGHT) - agent_row"] <= -11.252567:
                                        if features["E(UP) - agent_column"] <= -11.999924:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.126398:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        if features["E(UP) - agent_row"] <= -9.999994:
                                            return 1
                                        else:
                                            if features["T(LEFT) - T(RIGHT)"] <= -0.481636:
                                                if features["E(DOWN) - T(RIGHT)"] <= -0.354562:
                                                    return 3
                                                else:
                                                    if features["E(UP) - T(E(UP))"] <= 0.086670:
                                                        if features["E(DOWN) - E(RIGHT)"] <= -0.212944:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -10.280332:
                                                    return 1
                                                else:
                                                    if features["E(UP) - E(LEFT)"] <= -0.000194:
                                                        return 1
                                                    else:
                                                        return 3
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= 0.366936:
                                        if features["E(UP) - T(RIGHT)"] <= -0.282980:
                                            return 1
                                        else:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.241990:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        if features["E(UP) - T(E(DOWN))"] <= -0.307494:
                                            return 1
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.006904:
                                                return 3
                                            else:
                                                if features["E(DOWN) - T(E(RIGHT))"] <= -0.024278:
                                                    return 3
                                                else:
                                                    return 1
                    else:
                        if features["E(LEFT) - agent_column"] <= -0.996284:
                            return 3
                        else:
                            return 1
            else:
                if features["T(E(UP)) - T(T(up))"] <= 0.006688:
                    if features["E(DOWN) - T(E(RIGHT))"] <= -0.176057:
                        if features["E(LEFT) - agent_column"] <= -1.921788:
                            if features["E(RIGHT) - T(E(DOWN))"] <= 0.199647:
                                if features["T(up) - T(RIGHT)"] <= -0.492849:
                                    return 2
                                else:
                                    return 1
                            else:
                                if features["E(DOWN) - E(RIGHT)"] <= -0.148623:
                                    return 3
                                else:
                                    return 1
                        else:
                            return 2
                    else:
                        if features["E(LEFT) - T(up)"] <= 0.060130:
                            if features["E(RIGHT) - T(DOWN)"] <= 0.224881:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.391892:
                                    return 1
                                else:
                                    return 3
                            else:
                                return 1
                        else:
                            if features["E(RIGHT) - T(RIGHT)"] <= 0.025459:
                                if features["E(RIGHT) - T(E(LEFT))"] <= 0.215385:
                                    return 2
                                else:
                                    return 1
                            else:
                                return 3
                else:
                    if features["E(RIGHT) - T(RIGHT)"] <= 0.003896:
                        if features["E(LEFT) - E(RIGHT)"] <= -0.236718:
                            if features["E(DOWN)"] <= 0.174549:
                                if features["E(LEFT) - T(DOWN)"] <= -0.010930:
                                    return 3
                                else:
                                    if features["T(up) - time_left"] <= 0.427390:
                                        return 2
                                    else:
                                        return 3
                            else:
                                if features["T(DOWN) - T(E(UP))"] <= -0.246358:
                                    if features["E(LEFT) - T(RIGHT)"] <= -0.581953:
                                        return 3
                                    else:
                                        return 2
                                else:
                                    return 1
                        else:
                            if features["T(E(UP)) - T(T(LEFT))"] <= 0.159627:
                                if features["T(T(up)) - time_left"] <= 0.074755:
                                    if features["E(DOWN) - T(E(UP))"] <= -0.044267:
                                        if features["T(T(RIGHT)) - agent_row"] <= -8.867273:
                                            return 3
                                        else:
                                            return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN) - T(E(UP))"] <= -0.175963:
                                        return 3
                                    else:
                                        return 1
                            else:
                                if features["T(RIGHT) - agent_column"] <= -1.416308:
                                    if features["T(RIGHT) - agent_row"] <= -6.451110:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 0
                    else:
                        if features["T(DOWN) - T(RIGHT)"] <= -0.000001:
                            if features["E(UP) - E(LEFT)"] <= 0.150336:
                                if features["T(E(RIGHT)) - time_left"] <= 0.405234:
                                    return 1
                                else:
                                    return 3
                            else:
                                if features["T(DOWN) - agent_column"] <= -6.999998:
                                    return 1
                                else:
                                    if features["T(E(RIGHT)) - time_left"] <= 0.183211:
                                        return 1
                                    else:
                                        return 3
                        else:
                            return 3
        else:
            if features["E(LEFT) - T(E(RIGHT))"] <= 0.140065:
                if features["E(DOWN) - agent_row"] <= -12.131467:
                    if features["E(RIGHT) - T(up)"] <= 0.017064:
                        return 1
                    else:
                        return 3
                else:
                    if features["E(UP) - T(LEFT)"] <= 0.077781:
                        if features["E(RIGHT) - T(RIGHT)"] <= 0.209504:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.338002:
                                if features["E(LEFT) - T(LEFT)"] <= 0.056588:
                                    if features["T(E(RIGHT)) - time_left"] <= -0.598638:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    if features["E(RIGHT) - time_left"] <= -0.321333:
                                        return 2
                                    else:
                                        return 1
                            else:
                                if features["E(UP)"] <= 0.000028:
                                    if features["T(DOWN) - time_left"] <= -0.689922:
                                        return 2
                                    else:
                                        if features["E(DOWN) - E(RIGHT)"] <= -0.000010:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["T(DOWN) - agent_column"] <= -0.614062:
                                        if features["T(DOWN) - agent_row"] <= -11.999786:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 3
                        else:
                            if features["T(E(RIGHT)) - agent_row"] <= -2.679749:
                                if features["E(UP)"] <= 0.000009:
                                    return 1
                                else:
                                    if features["agent_row - agent_column"] <= 0.500000:
                                        if features["E(DOWN) - E(RIGHT)"] <= 0.013074:
                                            if features["E(UP) - agent_column"] <= -10.999843:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -4.586734:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        if features["T(LEFT) - T(E(DOWN))"] <= 0.429331:
                                            return 1
                                        else:
                                            return 3
                            else:
                                if features["E(LEFT) - T(E(RIGHT))"] <= -0.191808:
                                    if features["T(RIGHT) - agent_column"] <= -0.665801:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.270483:
                                            return 1
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -11.200444:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        return 1
                                else:
                                    return 1
                    else:
                        if features["T(up) - T(RIGHT)"] <= 0.000039:
                            if features["E(RIGHT) - T(E(UP))"] <= 0.066803:
                                if features["E(DOWN) - time_left"] <= 0.243933:
                                    return 2
                                else:
                                    if features["T(DOWN) - T(E(RIGHT))"] <= -0.241267:
                                        return 1
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.455131:
                                            return 1
                                        else:
                                            return 2
                            else:
                                if features["T(DOWN) - T(E(RIGHT))"] <= 0.032093:
                                    return 1
                                else:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.253320:
                                        return 2
                                    else:
                                        if features["T(E(LEFT)) - agent_column"] <= -4.965494:
                                            return 0
                                        else:
                                            return 3
                        else:
                            if features["E(LEFT) - agent_column"] <= -8.734434:
                                return 2
                            else:
                                return 1
            else:
                if features["agent_row - agent_column"] <= -6.500000:
                    if features["E(DOWN) - time_left"] <= 0.365213:
                        if features["T(E(RIGHT)) - agent_column"] <= -8.968587:
                            if features["T(DOWN) - T(T(LEFT))"] <= 0.035482:
                                if features["T(RIGHT) - T(E(UP))"] <= -0.022029:
                                    return 1
                                else:
                                    return 2
                            else:
                                if features["E(DOWN) - T(up)"] <= 0.428528:
                                    if features["T(E(DOWN)) - T(T(LEFT))"] <= 0.000849:
                                        if features["E(LEFT) - agent_row"] <= -1.650067:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 2
                                else:
                                    return 1
                        else:
                            if features["T(LEFT) - T(E(LEFT))"] <= 0.009581:
                                return 2
                            else:
                                if features["T(DOWN) - T(E(DOWN))"] <= 0.049773:
                                    return 1
                                else:
                                    return 2
                    else:
                        if features["E(UP) - T(LEFT)"] <= -0.290360:
                            if features["E(UP) - T(up)"] <= 0.001202:
                                return 1
                            else:
                                if features["E(LEFT) - T(E(RIGHT))"] <= 0.169654:
                                    return 1
                                else:
                                    return 2
                        else:
                            if features["E(DOWN) - T(LEFT)"] <= 0.414432:
                                if features["T(LEFT) - time_left"] <= 0.339967:
                                    return 2
                                else:
                                    return 3
                            else:
                                return 1
                else:
                    if features["T(LEFT) - agent_row"] <= -11.999909:
                        if features["T(DOWN) - agent_column"] <= -0.999978:
                            if features["T(up) - agent_row"] <= -12.389777:
                                if features["E(LEFT) - time_left"] <= 0.169383:
                                    return 1
                                else:
                                    return 2
                            else:
                                return 2
                        else:
                            return 1
                    else:
                        if features["E(DOWN) - E(LEFT)"] <= 0.000050:
                            if features["E(DOWN) - agent_column"] <= -0.633405:
                                if features["E(LEFT) - T(LEFT)"] <= 0.773540:
                                    return 1
                                else:
                                    return 2
                            else:
                                return 1
                        else:
                            if features["E(UP) - T(LEFT)"] <= 0.095825:
                                if features["time_left"] <= 0.170000:
                                    if features["E(UP) - T(E(UP))"] <= 0.097385:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    if features["T(E(UP)) - agent_column"] <= -0.999286:
                                        if features["T(up) - agent_row"] <= -6.981251:
                                            if features["T(up) - T(RIGHT)"] <= 0.000814:
                                                if features["E(UP)"] <= 0.000056:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["E(RIGHT) - agent_row"] <= -11.996783:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            return 1
                                    else:
                                        return 1
                            else:
                                if features["T(up) - T(RIGHT)"] <= 0.203883:
                                    if features["T(E(UP)) - T(E(RIGHT))"] <= 0.002028:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    return 1
    else:
        if features["E(UP) - E(LEFT)"] <= -0.000009:
            if features["E(DOWN) - E(LEFT)"] <= -0.151177:
                if features["E(UP)"] <= 0.662776:
                    if features["E(RIGHT) - T(DOWN)"] <= 0.000262:
                        if features["E(LEFT) - time_left"] <= 0.146303:
                            if features["T(RIGHT) - T(T(DOWN))"] <= -0.148891:
                                if features["E(UP) - T(LEFT)"] <= -0.230958:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["E(DOWN) - E(LEFT)"] <= -0.231362:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["E(RIGHT) - T(up)"] <= 0.000108:
                                if features["E(UP) - agent_column"] <= -0.458538:
                                    if features["E(DOWN) - T(E(LEFT))"] <= -0.075664:
                                        return 2
                                    else:
                                        if features["E(LEFT) - T(E(DOWN))"] <= 0.144754:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    return 0
                            else:
                                return 2
                    else:
                        if features["T(DOWN) - time_left"] <= -0.099962:
                            if features["E(DOWN) - T(T(DOWN))"] <= 0.035857:
                                if features["T(up) - T(T(LEFT))"] <= -0.119850:
                                    return 0
                                else:
                                    if features["E(UP) - E(RIGHT)"] <= 0.374599:
                                        if features["E(DOWN) - T(RIGHT)"] <= -0.452002:
                                            return 2
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.094824:
                                                if features["T(DOWN)"] <= 0.000060:
                                                    if features["T(E(RIGHT)) - agent_column"] <= -7.941223:
                                                        return 2
                                                    else:
                                                        if features["E(RIGHT) - T(DOWN)"] <= 0.003871:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                    else:
                                        return 2
                            else:
                                if features["E(LEFT) - T(up)"] <= 0.021922:
                                    if features["T(E(DOWN)) - agent_column"] <= -8.847611:
                                        return 2
                                    else:
                                        if features["E(RIGHT) - T(E(UP))"] <= -0.308221:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    return 2
                        else:
                            if features["E(RIGHT) - T(up)"] <= -0.437488:
                                return 2
                            else:
                                if features["T(E(UP)) - T(E(RIGHT))"] <= 0.118745:
                                    if features["E(UP) - T(up)"] <= -0.100880:
                                        return 1
                                    else:
                                        return 2
                                else:
                                    return 2
                else:
                    if features["E(RIGHT) - agent_column"] <= -1.999878:
                        if features["E(RIGHT)"] <= 0.000053:
                            if features["E(LEFT)"] <= 0.803477:
                                return 2
                            else:
                                if features["agent_row - agent_column"] <= 8.500000:
                                    if features["agent_row - agent_column"] <= -2.500000:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 0
                        else:
                            if features["E(DOWN) - agent_row"] <= -11.999971:
                                return 0
                            else:
                                return 2
                    else:
                        return 0
            else:
                if features["E(DOWN) - E(LEFT)"] <= 0.000006:
                    if features["E(RIGHT)"] <= 0.000075:
                        if features["E(UP) - E(LEFT)"] <= -0.823531:
                            if features["E(RIGHT) - agent_column"] <= -1.999952:
                                if features["agent_row - agent_column"] <= -0.500000:
                                    return 1
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -11.999973:
                                        return 2
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -2.999892:
                                            return 1
                                        else:
                                            return 2
                            else:
                                return 1
                        else:
                            if features["T(RIGHT) - T(E(LEFT))"] <= -0.600858:
                                return 2
                            else:
                                if features["E(UP) - E(LEFT)"] <= -0.751404:
                                    if features["T(up) - agent_column"] <= -0.816651:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 2
                    else:
                        if features["E(LEFT) - T(T(LEFT))"] <= 0.029338:
                            if features["T(E(DOWN)) - T(T(LEFT))"] <= -0.088780:
                                if features["E(UP) - time_left"] <= 0.210684:
                                    if features["T(RIGHT)"] <= 0.000028:
                                        if features["T(up) - agent_row"] <= -8.476417:
                                            if features["T(DOWN) - T(E(RIGHT))"] <= -0.060766:
                                                return 3
                                            else:
                                                return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(LEFT) - T(T(up))"] <= 0.236210:
                                            if features["E(UP) - T(up)"] <= 0.039544:
                                                if features["E(LEFT) - T(E(DOWN))"] <= 0.136232:
                                                    return 1
                                                else:
                                                    if features["T(T(RIGHT)) - agent_column"] <= -8.888239:
                                                        return 2
                                                    else:
                                                        return 1
                                            else:
                                                return 2
                                        else:
                                            return 2
                                else:
                                    if features["T(E(DOWN)) - T(T(up))"] <= -0.110307:
                                        if features["T(up) - T(LEFT)"] <= -0.006804:
                                            return 0
                                        else:
                                            return 1
                                    else:
                                        if features["T(DOWN) - T(E(DOWN))"] <= -0.149457:
                                            return 1
                                        else:
                                            return 2
                            else:
                                if features["T(E(DOWN)) - T(T(up))"] <= 0.248904:
                                    if features["E(UP) - T(E(RIGHT))"] <= 0.117102:
                                        if features["T(DOWN) - time_left"] <= 0.337427:
                                            if features["T(E(DOWN)) - T(T(DOWN))"] <= -0.033824:
                                                return 2
                                            else:
                                                if features["T(T(LEFT)) - T(T(RIGHT))"] <= 0.349082:
                                                    return 1
                                                else:
                                                    return 2
                                        else:
                                            if features["T(T(DOWN)) - T(T(RIGHT))"] <= 0.225694:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        return 2
                                else:
                                    return 2
                        else:
                            if features["T(up) - T(RIGHT)"] <= 0.000028:
                                if features["T(E(UP)) - time_left"] <= 0.001364:
                                    if features["agent_column - time_left"] <= 1.450000:
                                        return 1
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= -0.003936:
                                            if features["E(RIGHT) - T(up)"] <= 0.011176:
                                                return 2
                                            else:
                                                if features["E(DOWN) - agent_row"] <= -5.580650:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            return 2
                                else:
                                    return 2
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.101765:
                                    if features["T(E(DOWN)) - T(T(DOWN))"] <= 0.004549:
                                        if features["T(RIGHT) - T(E(UP))"] <= -0.150489:
                                            if features["T(T(up)) - agent_row"] <= -5.814597:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -6.780006:
                                                return 2
                                            else:
                                                if features["T(RIGHT) - agent_column"] <= -5.854697:
                                                    return 1
                                                else:
                                                    return 2
                                    else:
                                        if features["T(E(LEFT)) - T(T(DOWN))"] <= 0.118775:
                                            if features["T(DOWN) - T(T(RIGHT))"] <= -0.006604:
                                                return 2
                                            else:
                                                if features["E(LEFT)"] <= 0.453203:
                                                    if features["T(RIGHT) - T(E(RIGHT))"] <= 0.003609:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 2
                                        else:
                                            if features["E(LEFT) - time_left"] <= 0.301920:
                                                if features["T(up) - T(T(RIGHT))"] <= 0.020166:
                                                    return 2
                                                else:
                                                    if features["T(E(UP)) - agent_column"] <= -8.954576:
                                                        if features["T(RIGHT) - T(T(LEFT))"] <= -0.325949:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        return 1
                                            else:
                                                if features["T(LEFT) - T(RIGHT)"] <= 0.495717:
                                                    return 2
                                                else:
                                                    if features["E(LEFT) - T(LEFT)"] <= -0.303886:
                                                        return 2
                                                    else:
                                                        return 1
                                else:
                                    if features["E(DOWN) - agent_column"] <= -8.734299:
                                        if features["T(up) - T(LEFT)"] <= 0.603664:
                                            if features["T(E(UP)) - T(E(RIGHT))"] <= 0.073552:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.592495:
                                                    return 2
                                                else:
                                                    if features["T(up) - T(LEFT)"] <= 0.000099:
                                                        if features["T(up) - agent_row"] <= -7.559699:
                                                            if features["E(DOWN) - T(E(RIGHT))"] <= 0.146811:
                                                                return 3
                                                            else:
                                                                return 1
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                        else:
                                            return 2
                                    else:
                                        return 1
                else:
                    if features["E(DOWN) - agent_row"] <= -12.129219:
                        return 2
                    else:
                        if features["E(RIGHT) - T(T(up))"] <= -0.000046:
                            if features["E(UP) - E(LEFT)"] <= -0.861075:
                                if features["T(RIGHT) - agent_column"] <= -1.096103:
                                    if features["T(E(UP)) - agent_column"] <= -3.999623:
                                        return 1
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -3.132098:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    return 1
                            else:
                                if features["E(RIGHT) - T(up)"] <= 0.000062:
                                    return 1
                                else:
                                    if features["T(RIGHT) - T(E(UP))"] <= -0.004799:
                                        if features["E(LEFT) - T(T(DOWN))"] <= 0.014361:
                                            return 3
                                        else:
                                            return 2
                                    else:
                                        return 1
                        else:
                            if features["E(LEFT) - T(E(DOWN))"] <= -0.014088:
                                return 1
                            else:
                                return 2
        else:
            if features["E(DOWN)"] <= 0.006076:
                if features["E(UP) - E(LEFT)"] <= 0.267283:
                    if features["E(DOWN) - agent_row"] <= -1.999995:
                        if features["E(LEFT) - time_left"] <= 0.143812:
                            if features["E(RIGHT) - T(RIGHT)"] <= 0.025456:
                                if features["E(UP) - E(DOWN)"] <= 0.474541:
                                    if features["E(RIGHT) - agent_column"] <= -6.873317:
                                        if features["E(UP) - T(T(RIGHT))"] <= 0.334370:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        return 0
                                else:
                                    if features["E(RIGHT)"] <= 0.000656:
                                        return 0
                                    else:
                                        return 2
                            else:
                                if features["T(LEFT) - agent_column"] <= -3.677528:
                                    if features["T(E(RIGHT))"] <= 0.036222:
                                        return 2
                                    else:
                                        if features["T(up) - T(LEFT)"] <= 0.001077:
                                            return 3
                                        else:
                                            return 2
                                else:
                                    if features["E(DOWN) - T(E(UP))"] <= -0.326875:
                                        if features["E(DOWN) - time_left"] <= -0.539619:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        return 3
                        else:
                            if features["E(UP)"] <= 0.822424:
                                if features["E(DOWN) - T(DOWN)"] <= 0.000006:
                                    if features["E(UP)"] <= 0.668954:
                                        if features["T(up) - T(RIGHT)"] <= 0.348711:
                                            return 0
                                        else:
                                            if features["E(DOWN)"] <= 0.002417:
                                                return 0
                                            else:
                                                if features["T(LEFT) - time_left"] <= 0.298922:
                                                    if features["T(E(UP)) - T(T(LEFT))"] <= 0.082220:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    return 2
                                    else:
                                        if features["E(DOWN)"] <= 0.000008:
                                            return 0
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -1.999821:
                                                if features["T(RIGHT) - agent_row"] <= -2.707085:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                else:
                                    if features["T(E(RIGHT)) - time_left"] <= 0.023389:
                                        if features["E(UP) - T(T(up))"] <= 0.142552:
                                            if features["T(DOWN)"] <= 0.000036:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            if features["T(up) - agent_column"] <= -7.513665:
                                                if features["T(up) - T(LEFT)"] <= 0.000669:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                    else:
                                        if features["T(LEFT) - T(T(DOWN))"] <= 0.079493:
                                            if features["agent_row - agent_column"] <= 3.500000:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 0
                            else:
                                if features["T(T(up)) - agent_column"] <= -1.953116:
                                    if features["E(RIGHT) - agent_row"] <= -4.999991:
                                        if features["E(UP) - agent_column"] <= -5.132574:
                                            if features["T(E(LEFT)) - agent_column"] <= -7.349474:
                                                return 2
                                            else:
                                                if features["E(UP) - agent_row"] <= -8.132611:
                                                    if features["T(E(DOWN)) - agent_row"] <= -11.880440:
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
                                    return 0
                    else:
                        return 2
                else:
                    if features["E(RIGHT) - T(T(RIGHT))"] <= 0.035874:
                        if features["T(E(LEFT)) - agent_row"] <= -13.962626:
                            if features["E(RIGHT) - time_left"] <= 0.290791:
                                return 0
                            else:
                                return 3
                        else:
                            if features["E(UP) - time_left"] <= 0.279894:
                                if features["E(LEFT) - T(E(DOWN))"] <= 0.004725:
                                    if features["E(RIGHT) - time_left"] <= -0.799786:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    return 2
                            else:
                                return 0
                    else:
                        if features["E(RIGHT)"] <= 0.799610:
                            if features["E(LEFT) - T(DOWN)"] <= 0.000384:
                                if features["T(E(RIGHT)) - agent_row"] <= -1.831218:
                                    if features["T(E(LEFT)) - agent_row"] <= -13.747152:
                                        return 3
                                    else:
                                        if features["E(DOWN)"] <= 0.000036:
                                            if features["T(T(RIGHT)) - time_left"] <= -0.690256:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 0
                                else:
                                    if features["T(DOWN) - agent_row"] <= -0.984823:
                                        if features["E(UP) - agent_row"] <= -1.237214:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                            else:
                                if features["E(LEFT) - agent_row"] <= -13.997157:
                                    return 3
                                else:
                                    if features["T(E(UP)) - time_left"] <= -0.339096:
                                        return 2
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= -0.002492:
                                            if features["E(UP) - time_left"] <= 0.386028:
                                                if features["T(RIGHT) - time_left"] <= -0.199970:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                        else:
                                            if features["T(up) - T(T(RIGHT))"] <= 0.125106:
                                                return 0
                                            else:
                                                if features["T(E(UP)) - T(E(RIGHT))"] <= -0.004366:
                                                    return 3
                                                else:
                                                    return 0
                        else:
                            if features["T(E(LEFT)) - agent_row"] <= -0.961707:
                                if features["T(up) - agent_column"] <= -12.376530:
                                    if features["T(E(DOWN)) - agent_row"] <= -9.907446:
                                        return 3
                                    else:
                                        return 0
                                else:
                                    if features["T(up) - T(RIGHT)"] <= -0.583695:
                                        return 0
                                    else:
                                        if features["T(up) - agent_column"] <= -1.844016:
                                            return 3
                                        else:
                                            return 0
                            else:
                                return 3
            else:
                if features["E(RIGHT) - T(T(RIGHT))"] <= 0.004982:
                    if features["E(UP) - E(DOWN)"] <= 0.364775:
                        if features["T(DOWN)"] <= 0.000094:
                            if features["T(RIGHT) - T(T(up))"] <= 0.335519:
                                if features["E(LEFT) - T(E(RIGHT))"] <= 0.170355:
                                    if features["T(LEFT) - T(E(LEFT))"] <= -0.155204:
                                        return 1
                                    else:
                                        if features["E(DOWN) - time_left"] <= -0.167738:
                                            if features["E(RIGHT) - T(up)"] <= -0.272080:
                                                return 2
                                            else:
                                                return 3
                                        else:
                                            if features["T(up) - T(LEFT)"] <= 0.000074:
                                                return 3
                                            else:
                                                if features["T(E(UP)) - T(E(LEFT))"] <= 0.211398:
                                                    return 1
                                                else:
                                                    return 3
                                else:
                                    if features["E(DOWN) - T(E(LEFT))"] <= -0.273276:
                                        return 2
                                    else:
                                        if features["T(T(up)) - agent_column"] <= -8.515317:
                                            return 2
                                        else:
                                            return 1
                            else:
                                return 2
                        else:
                            if features["E(LEFT) - T(T(LEFT))"] <= 0.013199:
                                if features["T(E(DOWN)) - time_left"] <= 0.104677:
                                    if features["E(UP)"] <= 0.282102:
                                        return 1
                                    else:
                                        if features["T(T(RIGHT)) - agent_column"] <= -1.484578:
                                            if features["T(T(up))"] <= 0.373793:
                                                if features["E(RIGHT) - T(T(RIGHT))"] <= 0.004229:
                                                    if features["T(RIGHT) - time_left"] <= 0.023704:
                                                        return 2
                                                    else:
                                                        if features["E(UP) - E(RIGHT)"] <= 0.006599:
                                                            return 1
                                                        else:
                                                            return 2
                                                else:
                                                    return 0
                                            else:
                                                if features["E(LEFT) - T(T(LEFT))"] <= -0.005619:
                                                    if features["E(DOWN) - T(T(up))"] <= -0.295947:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 0
                                        else:
                                            if features["T(T(up)) - T(T(LEFT))"] <= 0.284301:
                                                return 0
                                            else:
                                                return 3
                                else:
                                    if features["E(DOWN) - T(T(up))"] <= -0.134002:
                                        if features["T(T(up)) - agent_row"] <= -10.644285:
                                            if features["T(RIGHT) - T(T(up))"] <= -0.032945:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(T(LEFT)) - agent_row"] <= -8.759359:
                                                if features["T(LEFT) - T(T(LEFT))"] <= -0.046224:
                                                    return 1
                                                else:
                                                    return 0
                                            else:
                                                return 2
                                    else:
                                        if features["E(UP) - T(T(DOWN))"] <= 0.078387:
                                            if features["E(DOWN) - T(T(DOWN))"] <= -0.101063:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["T(E(LEFT)) - agent_row"] <= -8.783016:
                                                return 1
                                            else:
                                                if features["E(UP) - time_left"] <= 0.326002:
                                                    return 2
                                                else:
                                                    return 1
                            else:
                                if features["T(RIGHT) - time_left"] <= -0.007663:
                                    if features["T(E(RIGHT)) - agent_column"] <= -8.801539:
                                        return 2
                                    else:
                                        if features["T(E(DOWN)) - T(E(RIGHT))"] <= -0.100794:
                                            if features["E(UP) - agent_column"] <= -2.615054:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 1
                                else:
                                    if features["T(RIGHT) - agent_column"] <= -1.428814:
                                        if features["E(UP) - T(E(DOWN))"] <= 0.311308:
                                            if features["E(UP) - T(E(UP))"] <= 0.236103:
                                                if features["E(RIGHT) - T(RIGHT)"] <= 0.037577:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 1
                                        else:
                                            if features["T(E(DOWN)) - time_left"] <= 0.015947:
                                                if features["T(E(DOWN)) - T(E(LEFT))"] <= -0.429230:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["T(E(UP)) - agent_column"] <= -3.116712:
                                                    return 0
                                                else:
                                                    return 3
                                    else:
                                        return 0
                    else:
                        if features["E(UP) - time_left"] <= 0.370856:
                            if features["T(E(DOWN)) - T(T(RIGHT))"] <= -0.241777:
                                if features["E(RIGHT)"] <= 0.283442:
                                    if features["T(LEFT) - agent_row"] <= -9.999638:
                                        if features["T(DOWN) - T(LEFT)"] <= 0.000008:
                                            if features["T(E(UP)) - T(E(LEFT))"] <= 0.094569:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 0
                                    else:
                                        return 2
                                else:
                                    return 3
                            else:
                                if features["T(T(up)) - T(T(LEFT))"] <= -0.049127:
                                    if features["T(RIGHT) - T(T(up))"] <= -0.085603:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(E(DOWN))"] <= 0.032494:
                                        return 0
                                    else:
                                        if features["T(DOWN) - T(LEFT)"] <= -0.286452:
                                            return 2
                                        else:
                                            if features["T(T(DOWN)) - agent_row"] <= -9.788798:
                                                return 0
                                            else:
                                                return 2
                        else:
                            if features["T(up) - T(E(DOWN))"] <= 0.366633:
                                if features["T(E(DOWN)) - T(T(RIGHT))"] <= -0.090255:
                                    return 0
                                else:
                                    if features["agent_column - time_left"] <= 9.910000:
                                        return 2
                                    else:
                                        return 0
                            else:
                                if features["T(DOWN) - T(T(DOWN))"] <= -0.016443:
                                    if features["T(E(UP)) - T(E(LEFT))"] <= 0.110475:
                                        return 2
                                    else:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.226344:
                                            return 0
                                        else:
                                            return 3
                                else:
                                    return 1
                else:
                    if features["T(RIGHT) - T(T(LEFT))"] <= -0.242191:
                        if features["T(DOWN) - T(E(RIGHT))"] <= -0.040962:
                            if features["T(up) - T(LEFT)"] <= 0.000004:
                                return 3
                            else:
                                if features["T(RIGHT) - T(E(LEFT))"] <= -0.133783:
                                    return 1
                                else:
                                    if features["E(LEFT) - E(RIGHT)"] <= 0.081215:
                                        return 3
                                    else:
                                        return 2
                        else:
                            if features["T(E(UP)) - time_left"] <= -0.166229:
                                return 2
                            else:
                                if features["T(up) - T(LEFT)"] <= -0.001722:
                                    if features["E(RIGHT) - T(E(UP))"] <= -0.086889:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 2
                    else:
                        if features["E(UP) - E(DOWN)"] <= 0.332213:
                            if features["T(E(LEFT))"] <= 0.179778:
                                if features["T(up) - T(RIGHT)"] <= -0.013901:
                                    if features["T(E(DOWN)) - agent_row"] <= -8.586633:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(up) - T(LEFT)"] <= 0.404357:
                                        if features["T(E(RIGHT)) - T(T(RIGHT))"] <= -0.002350:
                                            return 2
                                        else:
                                            if features["T(T(up)) - agent_column"] <= -8.934669:
                                                return 2
                                            else:
                                                return 3
                                    else:
                                        if features["E(UP) - T(E(DOWN))"] <= 0.191651:
                                            if features["E(LEFT) - T(up)"] <= -0.444088:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["E(RIGHT) - time_left"] <= 0.034039:
                                                return 2
                                            else:
                                                if features["E(DOWN) - E(RIGHT)"] <= -0.144978:
                                                    return 3
                                                else:
                                                    return 1
                            else:
                                if features["T(E(UP)) - time_left"] <= 0.308583:
                                    if features["T(DOWN) - T(LEFT)"] <= -0.000000:
                                        if features["T(DOWN) - T(E(DOWN))"] <= 0.005640:
                                            if features["E(UP) - E(DOWN)"] <= 0.177359:
                                                if features["T(LEFT) - T(T(RIGHT))"] <= 0.061582:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -8.784472:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(LEFT) - T(T(LEFT))"] <= -0.002035:
                                        if features["E(UP) - T(T(RIGHT))"] <= 0.051533:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.074503:
                                            if features["T(LEFT) - agent_row"] <= -9.660471:
                                                return 0
                                            else:
                                                return 1
                                        else:
                                            return 3
                        else:
                            if features["E(LEFT) - T(LEFT)"] <= 0.258029:
                                if features["E(UP) - T(up)"] <= 0.003245:
                                    if features["E(RIGHT) - time_left"] <= 0.222097:
                                        if features["T(E(LEFT)) - agent_row"] <= -7.805418:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        if features["T(LEFT) - T(E(UP))"] <= -0.371220:
                                            return 0
                                        else:
                                            if features["E(LEFT) - T(up)"] <= -0.356455:
                                                return 3
                                            else:
                                                return 0
                                else:
                                    if features["T(E(UP))"] <= 0.347439:
                                        if features["T(E(DOWN)) - T(E(RIGHT))"] <= -0.253545:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        if features["T(RIGHT) - T(E(RIGHT))"] <= -0.265301:
                                            return 3
                                        else:
                                            if features["T(E(RIGHT)) - time_left"] <= 0.322945:
                                                if features["T(T(RIGHT)) - time_left"] <= 0.203644:
                                                    if features["T(up) - T(T(LEFT))"] <= 0.254519:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    if features["T(E(RIGHT)) - T(T(RIGHT))"] <= -0.016847:
                                                        if features["E(DOWN) - E(RIGHT)"] <= -0.289747:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 0
                                            else:
                                                if features["T(DOWN) - T(T(RIGHT))"] <= -0.290308:
                                                    return 2
                                                else:
                                                    return 0
                            else:
                                if features["E(RIGHT) - T(up)"] <= -0.291316:
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
