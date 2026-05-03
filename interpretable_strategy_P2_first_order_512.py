import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(DOWN) - E(LEFT)"] <= 0.000000:
        if features["E(UP) - E(LEFT)"] <= -0.260635:
            if features["E(DOWN)"] <= 0.146839:
                return 2
            else:
                if features["E(RIGHT)"] <= 0.000079:
                    if features["E(LEFT)"] <= 0.803111:
                        if features["E(RIGHT) - T(RIGHT)"] <= -0.000000:
                            return 2
                        else:
                            if features["T(up) - agent_column"] <= -13.993580:
                                if features["T(LEFT) - agent_row"] <= -1.395844:
                                    if features["E(UP) - agent_column"] <= -13.999876:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 2
                            else:
                                if features["E(UP) - T(LEFT)"] <= -0.261317:
                                    if features["E(DOWN) - T(LEFT)"] <= -0.127464:
                                        return 2
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.103953:
                                            return 2
                                        else:
                                            return 0
                                else:
                                    if features["E(UP) - agent_column"] <= -13.855789:
                                        return 1
                                    else:
                                        return 0
                    else:
                        if features["E(UP) - E(RIGHT)"] <= -0.000001:
                            if features["T(DOWN) - agent_column"] <= -0.873271:
                                return 2
                            else:
                                return 1
                        else:
                            if features["T(RIGHT) - agent_row"] <= -11.919503:
                                return 2
                            else:
                                if features["E(RIGHT) - agent_column"] <= -12.000000:
                                    return 1
                                else:
                                    if features["E(DOWN) - agent_row"] <= -6.133825:
                                        return 1
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -1.132356:
                                            return 2
                                        else:
                                            return 1
                else:
                    if features["E(DOWN)"] <= 0.387015:
                        if features["E(RIGHT)"] <= 0.015520:
                            if features["T(RIGHT) - time_left"] <= -0.027207:
                                if features["E(UP) - T(LEFT)"] <= -0.284111:
                                    if features["E(RIGHT) - T(up)"] <= -0.002909:
                                        return 2
                                    else:
                                        if features["T(RIGHT) - agent_column"] <= -7.999994:
                                            if features["T(LEFT) - T(RIGHT)"] <= 0.439278:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 1
                                else:
                                    if features["E(UP) - T(up)"] <= 0.015231:
                                        if features["E(DOWN) - agent_column"] <= -11.729556:
                                            if features["E(DOWN) - T(DOWN)"] <= -0.002734:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                                    else:
                                        return 2
                            else:
                                if features["E(UP) - time_left"] <= 0.009955:
                                    return 2
                                else:
                                    return 0
                        else:
                            if features["E(RIGHT) - agent_column"] <= -12.982530:
                                return 0
                            else:
                                if features["agent_row - time_left"] <= 8.660000:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.045812:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 3
                    else:
                        if features["E(LEFT) - agent_row"] <= -10.299774:
                            if features["E(UP) - T(RIGHT)"] <= 0.016296:
                                return 2
                            else:
                                return 3
                        else:
                            if features["E(DOWN) - agent_column"] <= -1.297948:
                                if features["E(LEFT)"] <= 0.519785:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.588101:
                                        return 2
                                    else:
                                        if features["T(up) - agent_row"] <= -1.978576:
                                            if features["T(LEFT) - time_left"] <= -0.649506:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 2
                                else:
                                    if features["T(RIGHT) - agent_row"] <= -8.856524:
                                        return 1
                                    else:
                                        return 2
                            else:
                                return 1
        else:
            if features["E(UP) - E(LEFT)"] <= 0.000090:
                if features["E(LEFT)"] <= 0.442254:
                    if features["E(RIGHT) - T(DOWN)"] <= 0.050251:
                        if features["E(RIGHT)"] <= 0.014570:
                            if features["E(DOWN) - T(up)"] <= 0.133299:
                                if features["E(DOWN)"] <= 0.002015:
                                    if features["E(UP) - E(LEFT)"] <= 0.000000:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    if features["T(up) - time_left"] <= 0.276843:
                                        if features["T(RIGHT)"] <= 0.000584:
                                            if features["agent_row - time_left"] <= 5.880000:
                                                if features["E(DOWN) - T(DOWN)"] <= 0.129542:
                                                    if features["T(up) - agent_column"] <= -12.762885:
                                                        if features["T(LEFT) - agent_column"] <= -12.617772:
                                                            if features["T(up) - T(RIGHT)"] <= 0.000010:
                                                                if features["E(LEFT) - E(RIGHT)"] <= 0.400602:
                                                                    return 1
                                                                else:
                                                                    return 2
                                                            else:
                                                                return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["T(up) - T(LEFT)"] <= -0.437740:
                                                            return 2
                                                        else:
                                                            return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["agent_column - time_left"] <= 13.320000:
                                                    return 0
                                                else:
                                                    if features["T(up) - time_left"] <= 0.230278:
                                                        if features["T(LEFT) - agent_column"] <= -13.536422:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["E(UP) - T(DOWN)"] <= 0.176473:
                                                            return 2
                                                        else:
                                                            return 0
                                        else:
                                            return 0
                                    else:
                                        if features["E(DOWN)"] <= 0.035720:
                                            if features["T(DOWN) - time_left"] <= -0.089991:
                                                if features["T(up) - T(RIGHT)"] <= 0.409174:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 0
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -10.994655:
                                                return 2
                                            else:
                                                if features["T(RIGHT)"] <= 0.003010:
                                                    if features["E(RIGHT) - agent_column"] <= -12.997567:
                                                        return 2
                                                    else:
                                                        if features["E(UP) - T(LEFT)"] <= -0.376976:
                                                            return 2
                                                        else:
                                                            return 0
                                                else:
                                                    if features["T(up) - T(DOWN)"] <= 0.285027:
                                                        return 0
                                                    else:
                                                        return 2
                            else:
                                if features["T(LEFT) - T(RIGHT)"] <= 0.367847:
                                    if features["T(up) - agent_row"] <= -8.996243:
                                        if features["T(up) - time_left"] <= -0.499940:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        if features["E(LEFT) - agent_column"] <= -12.574514:
                                            if features["E(UP) - T(LEFT)"] <= -0.225347:
                                                if features["E(DOWN) - E(LEFT)"] <= -0.028852:
                                                    return 0
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                        else:
                                            return 2
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.492152:
                                        if features["E(DOWN) - agent_row"] <= -6.842611:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.000225:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["agent_column - time_left"] <= 13.900000:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        if features["agent_row - time_left"] <= 3.740000:
                                            return 0
                                        else:
                                            if features["E(RIGHT) - T(DOWN)"] <= -0.000107:
                                                return 2
                                            else:
                                                if features["E(DOWN) - agent_row"] <= -5.805901:
                                                    return 0
                                                else:
                                                    return 2
                        else:
                            if features["E(DOWN) - T(up)"] <= 0.162417:
                                if features["E(UP) - time_left"] <= 0.037271:
                                    if features["T(LEFT) - T(RIGHT)"] <= 0.567249:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    if features["T(RIGHT) - time_left"] <= 0.189051:
                                        if features["T(up) - time_left"] <= 0.374411:
                                            if features["agent_row - agent_column"] <= 0.500000:
                                                if features["E(DOWN) - time_left"] <= 0.302106:
                                                    if features["T(RIGHT) - time_left"] <= -0.150000:
                                                        return 0
                                                    else:
                                                        if features["E(UP) - time_left"] <= 0.319301:
                                                            return 0
                                                        else:
                                                            if features["E(UP)"] <= 0.330658:
                                                                return 1
                                                            else:
                                                                return 0
                                                else:
                                                    if features["T(up) - agent_row"] <= -4.806247:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                return 2
                                        else:
                                            if features["E(DOWN) - time_left"] <= 0.048240:
                                                return 0
                                            else:
                                                return 2
                                    else:
                                        if features["T(DOWN) - T(LEFT)"] <= -0.005818:
                                            return 3
                                        else:
                                            return 0
                            else:
                                if features["agent_row - time_left"] <= 3.940000:
                                    if features["T(LEFT) - time_left"] <= 0.196027:
                                        if features["E(UP) - T(up)"] <= 0.040766:
                                            return 3
                                        else:
                                            if features["E(RIGHT) - T(DOWN)"] <= -0.384426:
                                                return 2
                                            else:
                                                if features["T(DOWN) - T(LEFT)"] <= 0.000031:
                                                    return 1
                                                else:
                                                    return 0
                                    else:
                                        if features["T(RIGHT)"] <= 0.000000:
                                            return 1
                                        else:
                                            return 0
                                else:
                                    if features["T(DOWN) - time_left"] <= 0.356422:
                                        if features["T(RIGHT)"] <= 0.000023:
                                            if features["E(UP) - T(DOWN)"] <= 0.189238:
                                                if features["agent_row - agent_column"] <= -2.500000:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                        else:
                                            if features["E(DOWN) - T(DOWN)"] <= -0.018738:
                                                if features["E(UP) - time_left"] <= 0.041340:
                                                    if features["agent_row - time_left"] <= 8.660000:
                                                        return 2
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                            else:
                                                return 3
                                    else:
                                        if features["E(UP) - T(RIGHT)"] <= 0.238926:
                                            if features["E(UP) - T(DOWN)"] <= -0.458516:
                                                if features["T(LEFT) - agent_row"] <= -9.999238:
                                                    return 3
                                                else:
                                                    if features["T(up) - agent_row"] <= -5.999967:
                                                        return 2
                                                    else:
                                                        return 1
                                            else:
                                                if features["T(DOWN) - T(LEFT)"] <= 0.537440:
                                                    if features["T(DOWN) - T(LEFT)"] <= -0.000019:
                                                        return 1
                                                    else:
                                                        return 0
                                                else:
                                                    return 2
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.340057:
                                                return 0
                                            else:
                                                return 2
                    else:
                        if features["E(DOWN)"] <= 0.247087:
                            if features["E(UP) - T(LEFT)"] <= 0.246196:
                                if features["E(UP) - E(RIGHT)"] <= 0.163379:
                                    if features["T(up) - agent_row"] <= -6.506970:
                                        if features["E(LEFT) - time_left"] <= 0.299803:
                                            return 3
                                        else:
                                            return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.308369:
                                        if features["T(RIGHT)"] <= 0.000000:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        if features["E(LEFT) - T(up)"] <= -0.174067:
                                            return 2
                                        else:
                                            return 0
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.135659:
                                    return 0
                                else:
                                    return 2
                        else:
                            if features["T(up) - agent_row"] <= -8.480681:
                                return 3
                            else:
                                if features["E(LEFT) - agent_column"] <= -8.644879:
                                    if features["E(DOWN)"] <= 0.282568:
                                        if features["E(LEFT) - time_left"] <= 0.282013:
                                            if features["T(up) - T(LEFT)"] <= 0.000065:
                                                if features["T(up) - agent_row"] <= -5.999316:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                        else:
                                            if features["T(up) - time_left"] <= -0.029105:
                                                return 1
                                            else:
                                                return 2
                                    else:
                                        return 1
                                else:
                                    return 2
                else:
                    if features["E(RIGHT) - T(RIGHT)"] <= -0.000000:
                        if features["E(RIGHT)"] <= 0.000002:
                            if features["E(UP) - E(RIGHT)"] <= 0.799613:
                                if features["E(UP) - E(LEFT)"] <= 0.000018:
                                    return 2
                                else:
                                    return 0
                            else:
                                if features["agent_row - agent_column"] <= 0.500000:
                                    if features["E(LEFT) - agent_column"] <= -12.131967:
                                        if features["E(DOWN)"] <= 0.000001:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 0
                                else:
                                    return 2
                        else:
                            if features["T(LEFT) - agent_row"] <= -1.718526:
                                if features["E(DOWN) - E(RIGHT)"] <= 0.000084:
                                    if features["E(UP) - T(LEFT)"] <= 0.820252:
                                        if features["T(DOWN) - agent_row"] <= -11.999998:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        return 2
                                else:
                                    if features["E(UP) - T(up)"] <= 0.738675:
                                        return 2
                                    else:
                                        return 0
                            else:
                                if features["E(UP) - E(LEFT)"] <= 0.000047:
                                    return 2
                                else:
                                    return 0
                    else:
                        if features["E(DOWN) - agent_column"] <= -10.870934:
                            if features["E(DOWN) - agent_row"] <= -0.999999:
                                return 0
                            else:
                                return 2
                        else:
                            if features["E(DOWN) - time_left"] <= -0.070000:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.000002:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 2
            else:
                if features["E(UP) - E(RIGHT)"] <= 0.115772:
                    if features["E(DOWN) - T(DOWN)"] <= 0.108974:
                        if features["E(LEFT) - E(RIGHT)"] <= -0.799626:
                            if features["T(DOWN) - agent_row"] <= -1.693818:
                                if features["E(UP) - agent_row"] <= -11.136879:
                                    return 3
                                else:
                                    if features["T(DOWN) - agent_column"] <= -8.999962:
                                        return 3
                                    else:
                                        return 0
                            else:
                                return 3
                        else:
                            if features["E(UP) - E(RIGHT)"] <= 0.000000:
                                if features["E(LEFT)"] <= 0.091696:
                                    if features["E(DOWN) - agent_column"] <= -0.999997:
                                        if features["E(DOWN)"] <= 0.000033:
                                            if features["agent_column"] <= 11.500000:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.006811:
                                                if features["E(LEFT) - agent_column"] <= -4.993329:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 3
                                    else:
                                        return 0
                                else:
                                    return 0
                            else:
                                if features["E(DOWN) - T(LEFT)"] <= 0.000004:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.000049:
                                        if features["E(DOWN) - agent_row"] <= -2.000000:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.018693:
                                                if features["T(LEFT) - time_left"] <= 0.052056:
                                                    if features["E(DOWN) - time_left"] <= 0.020226:
                                                        if features["T(RIGHT) - time_left"] <= -0.739844:
                                                            return 2
                                                        else:
                                                            if features["E(UP) - agent_row"] <= -13.637355:
                                                                return 3
                                                            else:
                                                                return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(LEFT)"] <= 0.285898:
                                                        return 0
                                                    else:
                                                        if features["E(UP) - time_left"] <= 0.275789:
                                                            return 0
                                                        else:
                                                            return 3
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        if features["T(RIGHT) - time_left"] <= -0.109991:
                                            if features["E(DOWN) - agent_column"] <= -11.891574:
                                                return 0
                                            else:
                                                if features["T(DOWN) - T(LEFT)"] <= 0.000474:
                                                    return 3
                                                else:
                                                    return 0
                                        else:
                                            return 0
                                else:
                                    if features["E(LEFT) - T(up)"] <= 0.127592:
                                        if features["agent_row - agent_column"] <= 5.500000:
                                            if features["E(UP) - time_left"] <= 0.314930:
                                                if features["E(UP) - agent_column"] <= -3.575331:
                                                    if features["T(up) - agent_column"] <= -6.503392:
                                                        return 3
                                                    else:
                                                        return 0
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                        else:
                                            if features["T(DOWN) - T(RIGHT)"] <= -0.258128:
                                                if features["T(DOWN)"] <= 0.000000:
                                                    return 0
                                                else:
                                                    if features["T(RIGHT) - agent_column"] <= -0.246414:
                                                        return 0
                                                    else:
                                                        return 3
                                            else:
                                                if features["E(DOWN) - agent_column"] <= -2.983575:
                                                    return 0
                                                else:
                                                    return 3
                                    else:
                                        if features["T(DOWN) - T(RIGHT)"] <= 0.000036:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.091362:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 0
                    else:
                        if features["T(DOWN) - T(LEFT)"] <= -0.000000:
                            if features["E(UP) - time_left"] <= 0.312494:
                                if features["T(RIGHT) - agent_row"] <= -5.999889:
                                    return 3
                                else:
                                    return 0
                            else:
                                return 0
                        else:
                            if features["T(up) - agent_row"] <= -8.578151:
                                return 0
                            else:
                                if features["E(LEFT) - time_left"] <= 0.025429:
                                    return 3
                                else:
                                    return 2
                else:
                    if features["E(LEFT) - E(RIGHT)"] <= 0.671682:
                        if features["E(DOWN) - T(DOWN)"] <= 0.056051:
                            if features["E(UP) - time_left"] <= 0.093179:
                                if features["E(DOWN)"] <= 0.012269:
                                    return 0
                                else:
                                    return 3
                            else:
                                if features["E(RIGHT) - T(up)"] <= 0.345339:
                                    if features["E(DOWN) - E(RIGHT)"] <= 0.003422:
                                        if features["E(LEFT) - agent_row"] <= -0.424039:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN) - agent_row"] <= -1.990800:
                                        return 0
                                    else:
                                        return 3
                        else:
                            if features["T(RIGHT) - time_left"] <= -0.089434:
                                if features["T(RIGHT) - agent_row"] <= -5.999948:
                                    if features["E(DOWN) - agent_row"] <= -8.907802:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 0
                            else:
                                return 0
                    else:
                        if features["E(DOWN) - agent_row"] <= -1.999999:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.800103:
                                if features["E(DOWN) - T(DOWN)"] <= -0.000000:
                                    return 0
                                else:
                                    if features["T(LEFT) - agent_row"] <= -10.999995:
                                        return 2
                                    else:
                                        return 0
                            else:
                                if features["T(DOWN) - T(RIGHT)"] <= 0.000000:
                                    if features["agent_row - agent_column"] <= 7.500000:
                                        return 0
                                    else:
                                        return 2
                                else:
                                    return 0
                        else:
                            if features["E(DOWN) - agent_row"] <= -0.999998:
                                if features["E(UP) - T(RIGHT)"] <= 0.777486:
                                    return 2
                                else:
                                    if features["E(RIGHT)"] <= 0.000006:
                                        return 2
                                    else:
                                        return 0
                            else:
                                return 2
    else:
        if features["E(DOWN) - E(RIGHT)"] <= 0.000010:
            if features["E(UP) - E(RIGHT)"] <= -0.136321:
                if features["E(DOWN) - E(RIGHT)"] <= -0.172396:
                    if features["T(LEFT)"] <= 0.000373:
                        return 3
                    else:
                        if features["E(LEFT) - agent_column"] <= -0.950240:
                            return 3
                        else:
                            if features["E(LEFT) - T(up)"] <= -0.183580:
                                return 3
                            else:
                                return 1
                else:
                    if features["E(LEFT) - agent_column"] <= -1.933578:
                        if features["E(DOWN) - agent_column"] <= -11.215727:
                            if features["T(RIGHT) - agent_row"] <= -3.095273:
                                if features["E(UP) - agent_column"] <= -12.999950:
                                    return 1
                                else:
                                    return 3
                            else:
                                return 1
                        else:
                            if features["E(LEFT) - time_left"] <= 0.104097:
                                if features["T(LEFT)"] <= 0.000006:
                                    if features["T(up) - T(LEFT)"] <= 0.000000:
                                        return 3
                                    else:
                                        if features["E(LEFT)"] <= 0.000000:
                                            if features["E(DOWN) - agent_column"] <= -1.167610:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= -0.352439:
                                                return 3
                                            else:
                                                if features["E(LEFT) - time_left"] <= 0.002892:
                                                    if features["E(RIGHT) - agent_row"] <= -10.301192:
                                                        return 3
                                                    else:
                                                        if features["E(DOWN) - E(RIGHT)"] <= -0.098834:
                                                            return 3
                                                        else:
                                                            return 1
                                                else:
                                                    return 1
                                else:
                                    if features["time_left"] <= 0.160000:
                                        if features["E(LEFT) - E(RIGHT)"] <= -0.217904:
                                            if features["E(UP) - E(LEFT)"] <= -0.000001:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.112908:
                                                    if features["T(up) - agent_row"] <= -2.999994:
                                                        return 3
                                                    else:
                                                        return 1
                                                else:
                                                    return 3
                                        else:
                                            if features["T(up) - agent_column"] <= -3.817902:
                                                return 3
                                            else:
                                                return 0
                                    else:
                                        if features["E(LEFT)"] <= 0.000000:
                                            return 3
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= -0.260797:
                                                if features["T(up) - agent_row"] <= -10.971850:
                                                    return 3
                                                else:
                                                    if features["T(LEFT) - agent_row"] <= -8.623130:
                                                        return 3
                                                    else:
                                                        if features["E(UP) - T(RIGHT)"] <= 0.005314:
                                                            return 3
                                                        else:
                                                            if features["E(UP) - agent_column"] <= -9.913459:
                                                                return 1
                                                            else:
                                                                if features["T(up) - time_left"] <= -0.169993:
                                                                    return 3
                                                                else:
                                                                    return 1
                                            else:
                                                if features["E(UP) - agent_row"] <= -3.859328:
                                                    if features["T(LEFT) - time_left"] <= -0.598815:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                            else:
                                if features["T(up) - T(LEFT)"] <= 0.025948:
                                    if features["E(DOWN) - T(RIGHT)"] <= -0.009013:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    return 2
                    else:
                        if features["E(RIGHT) - agent_row"] <= -3.591678:
                            if features["T(RIGHT) - agent_row"] <= -4.670251:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.150882:
                                    if features["E(LEFT)"] <= 0.105305:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    if features["E(LEFT)"] <= 0.000000:
                                        if features["E(DOWN) - agent_column"] <= 0.543509:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= -0.000468:
                                            if features["E(RIGHT) - time_left"] <= 0.270648:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 3
                            else:
                                if features["T(DOWN) - T(RIGHT)"] <= 0.000004:
                                    if features["T(LEFT) - agent_row"] <= -3.970291:
                                        if features["E(UP) - T(RIGHT)"] <= -0.413335:
                                            if features["E(RIGHT) - agent_column"] <= -0.582222:
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
                            if features["E(LEFT) - T(up)"] <= -0.001545:
                                return 3
                            else:
                                if features["E(DOWN) - agent_row"] <= -2.609331:
                                    if features["T(DOWN) - agent_column"] <= -0.633031:
                                        return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(RIGHT) - T(DOWN)"] <= 0.027520:
                                        return 1
                                    else:
                                        return 3
            else:
                if features["E(LEFT) - E(RIGHT)"] <= -0.206762:
                    if features["E(RIGHT) - agent_column"] <= -11.200378:
                        if features["E(UP) - agent_row"] <= -6.386561:
                            if features["E(UP) - E(RIGHT)"] <= -0.000029:
                                return 3
                            else:
                                return 0
                        else:
                            if features["T(RIGHT) - agent_row"] <= -1.188660:
                                if features["agent_row - agent_column"] <= -8.500000:
                                    return 0
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -3.211677:
                                        return 0
                                    else:
                                        return 3
                            else:
                                return 3
                    else:
                        if features["T(LEFT)"] <= 0.000000:
                            if features["E(UP) - agent_column"] <= 0.356869:
                                if features["T(up) - agent_column"] <= 0.273060:
                                    if features["E(LEFT) - time_left"] <= -0.010544:
                                        if features["E(UP) - time_left"] <= 0.224984:
                                            return 3
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -9.999997:
                                                return 3
                                            else:
                                                if features["E(DOWN) - agent_row"] <= -6.988807:
                                                    if features["T(RIGHT) - agent_column"] <= -0.259384:
                                                        if features["T(LEFT) - T(RIGHT)"] <= -0.496533:
                                                            if features["E(LEFT) - T(LEFT)"] <= -0.000000:
                                                                return 3
                                                            else:
                                                                return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                    else:
                                        if features["T(up) - agent_row"] <= -8.648285:
                                            if features["T(DOWN) - agent_row"] <= -9.999999:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= -0.302648:
                                                if features["T(up) - T(RIGHT)"] <= -0.000147:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 1
                                else:
                                    return 3
                            else:
                                if features["E(UP) - time_left"] <= 0.274267:
                                    if features["T(up) - time_left"] <= -0.766735:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["E(DOWN) - T(up)"] <= 0.002151:
                                        return 0
                                    else:
                                        return 3
                        else:
                            if features["E(DOWN) - time_left"] <= 0.194381:
                                if features["T(LEFT) - agent_column"] <= -0.998837:
                                    if features["E(LEFT) - T(up)"] <= 0.000016:
                                        if features["E(UP) - E(RIGHT)"] <= -0.000008:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.062134:
                                                if features["E(LEFT)"] <= 0.000002:
                                                    if features["E(RIGHT) - T(LEFT)"] <= 0.728800:
                                                        if features["T(DOWN) - time_left"] <= -0.519926:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(LEFT) - T(LEFT)"] <= 0.007020:
                                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.009927:
                                                            if features["E(LEFT)"] <= 0.002024:
                                                                if features["T(LEFT) - T(RIGHT)"] <= -0.448838:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                            else:
                                                                if features["E(RIGHT) - agent_column"] <= -5.588822:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                        else:
                                                            if features["E(LEFT)"] <= 0.148905:
                                                                if features["E(DOWN) - E(RIGHT)"] <= -0.867792:
                                                                    if features["T(LEFT) - agent_row"] <= -1.916164:
                                                                        return 0
                                                                    else:
                                                                        return 3
                                                                else:
                                                                    return 3
                                                            else:
                                                                if features["E(UP) - agent_column"] <= -4.677837:
                                                                    return 3
                                                                else:
                                                                    return 0
                                                    else:
                                                        return 3
                                            else:
                                                return 3
                                        else:
                                            if features["T(DOWN) - agent_row"] <= -1.838778:
                                                if features["E(UP) - agent_row"] <= -2.215456:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 3
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -2.913094:
                                            if features["E(UP) - agent_column"] <= -5.695964:
                                                if features["E(UP) - E(DOWN)"] <= 0.656334:
                                                    if features["T(DOWN) - time_left"] <= -0.299168:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["agent_row - time_left"] <= 2.550000:
                                                        return 3
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -4.546655:
                                                    return 0
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -7.988711:
                                                        return 0
                                                    else:
                                                        return 3
                                        else:
                                            return 3
                                else:
                                    if features["E(UP) - agent_column"] <= -0.696571:
                                        return 3
                                    else:
                                        if features["E(LEFT) - time_left"] <= 0.045940:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.001353:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 1
                            else:
                                if features["T(DOWN) - T(RIGHT)"] <= -0.115364:
                                    return 1
                                else:
                                    return 3
                else:
                    if features["T(DOWN) - agent_column"] <= -5.997584:
                        if features["T(RIGHT) - agent_row"] <= -4.999955:
                            if features["E(LEFT) - T(LEFT)"] <= 0.186934:
                                if features["T(LEFT) - agent_column"] <= -11.999710:
                                    return 0
                                else:
                                    return 3
                            else:
                                return 3
                        else:
                            return 0
                    else:
                        if features["E(RIGHT) - T(LEFT)"] <= 0.202505:
                            if features["T(LEFT) - time_left"] <= 0.230319:
                                if features["E(RIGHT) - time_left"] <= 0.343280:
                                    if features["E(DOWN) - time_left"] <= 0.298935:
                                        return 0
                                    else:
                                        return 1
                                else:
                                    return 1
                            else:
                                if features["T(RIGHT) - agent_row"] <= -4.999478:
                                    if features["T(up) - agent_row"] <= -7.481280:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 0
                        else:
                            if features["E(LEFT) - agent_column"] <= -4.803014:
                                if features["T(LEFT) - agent_row"] <= -1.999785:
                                    if features["E(UP) - T(DOWN)"] <= 0.209476:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 3
                            else:
                                if features["E(RIGHT) - T(DOWN)"] <= 0.311621:
                                    return 2
                                else:
                                    if features["E(DOWN) - agent_row"] <= -8.756348:
                                        return 0
                                    else:
                                        return 1
        else:
            if features["E(DOWN) - E(RIGHT)"] <= 0.189285:
                if features["E(UP) - E(DOWN)"] <= -0.330225:
                    if features["E(UP) - E(DOWN)"] <= -0.800714:
                        if features["T(LEFT) - T(RIGHT)"] <= -0.670243:
                            return 1
                        else:
                            if features["E(UP) - agent_column"] <= -11.999998:
                                return 1
                            else:
                                if features["T(up) - agent_column"] <= -0.999743:
                                    if features["T(DOWN) - agent_column"] <= -7.999997:
                                        return 3
                                    else:
                                        if features["E(LEFT) - agent_column"] <= -7.999928:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    return 1
                    else:
                        if features["E(UP)"] <= 0.000001:
                            if features["T(DOWN) - T(LEFT)"] <= 0.339773:
                                if features["agent_row - time_left"] <= -0.020000:
                                    if features["E(RIGHT) - T(LEFT)"] <= 0.007901:
                                        return 1
                                    else:
                                        if features["E(RIGHT) - agent_column"] <= -10.291006:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -11.223456:
                                        return 3
                                    else:
                                        if features["E(UP) - time_left"] <= -0.530000:
                                            return 2
                                        else:
                                            return 1
                            else:
                                if features["T(DOWN) - agent_column"] <= -5.259161:
                                    return 1
                                else:
                                    if features["T(DOWN) - time_left"] <= -0.115184:
                                        return 0
                                    else:
                                        return 1
                        else:
                            if features["E(UP) - E(LEFT)"] <= -0.058086:
                                if features["T(RIGHT) - agent_row"] <= -8.856040:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.125478:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    if features["E(UP) - agent_row"] <= -1.972887:
                                        if features["T(up) - time_left"] <= -0.130000:
                                            if features["T(up) - agent_column"] <= -3.994688:
                                                return 1
                                            else:
                                                if features["E(DOWN) - E(LEFT)"] <= 0.322634:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            return 1
                                    else:
                                        if features["E(UP) - T(up)"] <= 0.000751:
                                            return 1
                                        else:
                                            if features["T(up)"] <= 0.020305:
                                                if features["T(DOWN) - T(LEFT)"] <= 0.291831:
                                                    if features["E(DOWN) - T(RIGHT)"] <= 0.396670:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - time_left"] <= 0.237148:
                                                            return 1
                                                        else:
                                                            return 3
                                                else:
                                                    if features["T(DOWN) - agent_row"] <= -0.593178:
                                                        if features["T(DOWN) - T(RIGHT)"] <= -0.000005:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 1
                                            else:
                                                if features["T(RIGHT) - agent_column"] <= -6.711469:
                                                    return 1
                                                else:
                                                    return 3
                            else:
                                if features["E(RIGHT) - agent_column"] <= -10.324972:
                                    if features["T(up) - agent_row"] <= -10.999833:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    if features["T(LEFT) - agent_column"] <= -1.974769:
                                        if features["T(RIGHT) - agent_row"] <= -1.999949:
                                            if features["E(DOWN) - agent_row"] <= -10.317858:
                                                return 3
                                            else:
                                                if features["E(UP) - agent_row"] <= -8.999763:
                                                    return 1
                                                else:
                                                    if features["T(DOWN) - T(LEFT)"] <= 0.000839:
                                                        if features["E(RIGHT)"] <= 0.683529:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        return 3
                                        else:
                                            if features["T(DOWN) - T(LEFT)"] <= 0.004278:
                                                return 1
                                            else:
                                                return 3
                                    else:
                                        return 1
                else:
                    if features["E(UP) - agent_row"] <= -3.852897:
                        if features["E(DOWN) - T(DOWN)"] <= 0.287097:
                            if features["E(UP) - T(up)"] <= 0.006398:
                                if features["E(LEFT)"] <= 0.283821:
                                    return 3
                                else:
                                    return 0
                            else:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.240098:
                                    if features["E(DOWN) - T(up)"] <= 0.133602:
                                        return 0
                                    else:
                                        if features["T(LEFT)"] <= 0.000026:
                                            if features["E(LEFT) - agent_column"] <= -4.774994:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(up)"] <= 0.000000:
                                                return 0
                                            else:
                                                if features["E(RIGHT) - agent_row"] <= -8.728878:
                                                    return 3
                                                else:
                                                    if features["E(RIGHT) - T(DOWN)"] <= -0.075450:
                                                        return 1
                                                    else:
                                                        return 3
                                else:
                                    if features["T(up)"] <= 0.000000:
                                        if features["E(LEFT) - T(DOWN)"] <= -0.423131:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        return 3
                        else:
                            if features["T(RIGHT) - agent_row"] <= -8.999755:
                                return 3
                            else:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.238111:
                                    return 1
                                else:
                                    if features["T(up) - T(LEFT)"] <= -0.449122:
                                        return 3
                                    else:
                                        return 1
                    else:
                        if features["E(UP) - E(RIGHT)"] <= -0.134895:
                            if features["T(DOWN) - T(LEFT)"] <= 0.207185:
                                if features["E(UP)"] <= 0.000222:
                                    return 1
                                else:
                                    if features["T(RIGHT)"] <= 0.305175:
                                        if features["E(RIGHT)"] <= 0.297306:
                                            if features["T(DOWN) - T(LEFT)"] <= 0.000016:
                                                return 1
                                            else:
                                                return 0
                                        else:
                                            return 3
                                    else:
                                        return 1
                            else:
                                if features["agent_column - time_left"] <= 7.860000:
                                    if features["T(RIGHT) - time_left"] <= 0.394093:
                                        if features["E(LEFT)"] <= 0.000802:
                                            return 1
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -5.709096:
                                                if features["T(LEFT) - agent_row"] <= -0.880598:
                                                    if features["E(DOWN) - E(LEFT)"] <= 0.220328:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                    else:
                                        return 1
                                else:
                                    return 1
                        else:
                            if features["T(DOWN) - T(RIGHT)"] <= 0.003983:
                                if features["E(LEFT) - time_left"] <= 0.165685:
                                    return 0
                                else:
                                    return 1
                            else:
                                if features["E(RIGHT) - time_left"] <= 0.240336:
                                    if features["E(UP) - T(LEFT)"] <= -0.363633:
                                        if features["T(DOWN) - T(LEFT)"] <= 0.000010:
                                            return 1
                                        else:
                                            return 0
                                    else:
                                        if features["E(UP) - time_left"] <= -0.119266:
                                            return 1
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -0.780768:
                                                return 0
                                            else:
                                                return 3
                                else:
                                    return 1
            else:
                if features["E(LEFT)"] <= 0.729076:
                    if features["E(UP)"] <= 0.000048:
                        if features["E(DOWN) - time_left"] <= 0.146554:
                            if features["T(RIGHT) - agent_column"] <= -2.386919:
                                if features["T(DOWN) - agent_row"] <= 0.435156:
                                    return 1
                                else:
                                    return 2
                            else:
                                if features["E(UP) - agent_column"] <= -1.000000:
                                    return 2
                                else:
                                    return 1
                        else:
                            if features["E(DOWN) - agent_row"] <= -12.167450:
                                return 2
                            else:
                                if features["E(LEFT) - agent_row"] <= 0.355344:
                                    return 1
                                else:
                                    return 2
                    else:
                        if features["E(UP) - time_left"] <= 0.016201:
                            if features["E(DOWN) - E(LEFT)"] <= 0.035117:
                                if features["agent_row - agent_column"] <= -9.500000:
                                    if features["E(DOWN) - T(LEFT)"] <= 0.004989:
                                        if features["T(RIGHT) - time_left"] <= -0.229998:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["T(up) - T(LEFT)"] <= -0.331296:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    if features["E(RIGHT) - agent_row"] <= -1.961391:
                                        if features["E(RIGHT)"] <= 0.027274:
                                            if features["T(LEFT) - agent_column"] <= -10.535359:
                                                if features["T(LEFT) - agent_row"] <= -10.538240:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["T(DOWN) - time_left"] <= -0.409990:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            if features["T(up) - agent_row"] <= -8.941082:
                                                return 3
                                            else:
                                                if features["E(UP) - agent_column"] <= -11.996168:
                                                    if features["T(RIGHT)"] <= 0.018544:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -10.665069:
                                            return 3
                                        else:
                                            if features["T(DOWN) - agent_row"] <= -1.506910:
                                                return 0
                                            else:
                                                return 2
                            else:
                                if features["E(DOWN) - agent_row"] <= -8.528912:
                                    if features["E(RIGHT) - T(RIGHT)"] <= 0.018063:
                                        if features["E(DOWN)"] <= 0.425135:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        if features["T(up) - time_left"] <= 0.157180:
                                            if features["E(UP)"] <= 0.028055:
                                                if features["E(LEFT) - agent_row"] <= -9.641151:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["T(RIGHT) - agent_row"] <= -8.858527:
                                                    return 3
                                                else:
                                                    return 1
                                        else:
                                            if features["T(DOWN) - T(RIGHT)"] <= -0.000000:
                                                return 1
                                            else:
                                                return 3
                                else:
                                    if features["T(up)"] <= 0.000291:
                                        if features["E(UP) - agent_row"] <= -1.977303:
                                            return 1
                                        else:
                                            if features["E(LEFT) - time_left"] <= 0.210627:
                                                return 1
                                            else:
                                                return 2
                                    else:
                                        if features["T(up) - agent_row"] <= -0.968772:
                                            if features["E(UP) - T(up)"] <= 0.031799:
                                                if features["E(LEFT)"] <= 0.488126:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                        else:
                                            return 0
                        else:
                            if features["T(DOWN) - T(LEFT)"] <= -0.000072:
                                return 1
                            else:
                                if features["T(up) - time_left"] <= 0.007615:
                                    if features["T(LEFT) - agent_column"] <= -9.998786:
                                        if features["T(up) - agent_row"] <= -1.960448:
                                            return 2
                                        else:
                                            return 3
                                    else:
                                        return 0
                                else:
                                    return 0
                else:
                    if features["E(RIGHT) - agent_row"] <= -1.999988:
                        if features["E(DOWN) - agent_row"] <= -11.212503:
                            return 2
                        else:
                            if features["E(UP) - agent_row"] <= -7.000000:
                                if features["T(up) - agent_row"] <= -10.613458:
                                    if features["E(DOWN) - E(LEFT)"] <= 0.000437:
                                        if features["agent_column - time_left"] <= 11.880000:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 2
                                else:
                                    return 1
                            else:
                                if features["E(RIGHT) - agent_column"] <= -1.999998:
                                    if features["E(RIGHT) - agent_column"] <= -10.999999:
                                        return 1
                                    else:
                                        if features["E(UP)"] <= 0.000000:
                                            if features["T(DOWN) - T(RIGHT)"] <= 0.544274:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 2
                                else:
                                    return 1
                    else:
                        if features["E(UP) - agent_column"] <= -1.999147:
                            return 2
                        else:
                            return 1


def interpretable_action(evader_probability, teammate_probability, agent_position, time_left, gamma, size, valid_actions):
    input_representation = symbolic_representation(evader_probability, teammate_probability, agent_position, time_left, gamma, size)
    input_combinations   = get_feature_vector(input_representation)
    symbole_to_value     = {name: input_combinations[i] for i, name in enumerate(symbole_names)}
    action               = Index_to_Action[interpretable_strategy(symbole_to_value)]
    if action in valid_actions:
        return action
    else:
        return random.choice(valid_actions)
