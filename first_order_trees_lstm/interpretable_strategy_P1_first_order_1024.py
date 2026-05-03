import random
from INTERPRETER import symbolic_representation, get_feature_vector
from environment import Index_to_Action
symbole_names = ['E(UP)', 'E(DOWN)', 'E(LEFT)', 'E(RIGHT)', 'T(up)', 'T(DOWN)', 'T(LEFT)', 'T(RIGHT)', 'agent_row', 'agent_column', 'time_left', 'E(UP) - E(DOWN)', 'E(UP) - E(LEFT)', 'E(UP) - E(RIGHT)', 'E(UP) - T(up)', 'E(UP) - T(DOWN)', 'E(UP) - T(LEFT)', 'E(UP) - T(RIGHT)', 'E(UP) - agent_row', 'E(UP) - agent_column', 'E(UP) - time_left', 'E(DOWN) - E(LEFT)', 'E(DOWN) - E(RIGHT)', 'E(DOWN) - T(up)', 'E(DOWN) - T(DOWN)', 'E(DOWN) - T(LEFT)', 'E(DOWN) - T(RIGHT)', 'E(DOWN) - agent_row', 'E(DOWN) - agent_column', 'E(DOWN) - time_left', 'E(LEFT) - E(RIGHT)', 'E(LEFT) - T(up)', 'E(LEFT) - T(DOWN)', 'E(LEFT) - T(LEFT)', 'E(LEFT) - T(RIGHT)', 'E(LEFT) - agent_row', 'E(LEFT) - agent_column', 'E(LEFT) - time_left', 'E(RIGHT) - T(up)', 'E(RIGHT) - T(DOWN)', 'E(RIGHT) - T(LEFT)', 'E(RIGHT) - T(RIGHT)', 'E(RIGHT) - agent_row', 'E(RIGHT) - agent_column', 'E(RIGHT) - time_left', 'T(up) - T(DOWN)', 'T(up) - T(LEFT)', 'T(up) - T(RIGHT)', 'T(up) - agent_row', 'T(up) - agent_column', 'T(up) - time_left', 'T(DOWN) - T(LEFT)', 'T(DOWN) - T(RIGHT)', 'T(DOWN) - agent_row', 'T(DOWN) - agent_column', 'T(DOWN) - time_left', 'T(LEFT) - T(RIGHT)', 'T(LEFT) - agent_row', 'T(LEFT) - agent_column', 'T(LEFT) - time_left', 'T(RIGHT) - agent_row', 'T(RIGHT) - agent_column', 'T(RIGHT) - time_left', 'agent_row - agent_column', 'agent_row - time_left', 'agent_column - time_left']


def interpretable_strategy(features):
    if features["E(UP) - E(RIGHT)"] <= -0.000000:
        if features["E(LEFT) - E(RIGHT)"] <= -0.322624:
            if features["E(DOWN) - E(RIGHT)"] <= -0.000005:
                if features["E(LEFT)"] <= 0.000289:
                    if features["E(UP) - E(DOWN)"] <= 0.799314:
                        if features["E(DOWN)"] <= 0.800865:
                            if features["agent_column - time_left"] <= -0.030000:
                                if features["E(UP) - agent_column"] <= 0.284891:
                                    if features["E(RIGHT) - time_left"] <= 0.191938:
                                        if features["T(DOWN) - agent_row"] <= -8.787694:
                                            if features["E(RIGHT) - T(DOWN)"] <= 0.146094:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= -0.008403:
                                                if features["E(DOWN) - time_left"] <= -0.284262:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["agent_row - time_left"] <= 7.770000:
                                                    return 1
                                                else:
                                                    if features["E(UP) - agent_row"] <= -8.853891:
                                                        return 1
                                                    else:
                                                        return 3
                                    else:
                                        if features["E(DOWN) - T(up)"] <= 0.160635:
                                            return 3
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= -0.239505:
                                                return 3
                                            else:
                                                if features["E(UP) - agent_row"] <= -5.945212:
                                                    return 3
                                                else:
                                                    return 1
                                else:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.401524:
                                        if features["E(UP) - time_left"] <= -0.200171:
                                            return 1
                                        else:
                                            return 0
                                    else:
                                        return 0
                            else:
                                if features["E(LEFT)"] <= 0.000015:
                                    if features["E(UP) - agent_column"] <= 0.356067:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.000000:
                                            if features["E(UP) - T(up)"] <= 0.308963:
                                                if features["E(UP) - E(DOWN)"] <= -0.677108:
                                                    if features["E(RIGHT) - agent_column"] <= -11.205722:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(RIGHT) - time_left"] <= -0.275267:
                                                        return 2
                                                    else:
                                                        return 3
                                            else:
                                                if features["T(LEFT) - time_left"] <= -0.469936:
                                                    return 0
                                                else:
                                                    if features["E(UP) - agent_column"] <= -11.214703:
                                                        return 0
                                                    else:
                                                        if features["E(RIGHT) - agent_column"] <= 0.350050:
                                                            return 3
                                                        else:
                                                            return 0
                                        else:
                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.133880:
                                                if features["T(up) - agent_row"] <= -7.644047:
                                                    if features["E(UP) - time_left"] <= 0.061268:
                                                        if features["E(DOWN) - agent_row"] <= -9.403765:
                                                            return 3
                                                        else:
                                                            if features["T(up) - agent_column"] <= -7.999475:
                                                                return 1
                                                            else:
                                                                return 3
                                                    else:
                                                        return 3
                                                else:
                                                    if features["T(DOWN) - time_left"] <= -0.579696:
                                                        return 1
                                                    else:
                                                        return 3
                                            else:
                                                return 3
                                    else:
                                        return 0
                                else:
                                    if features["E(UP) - E(RIGHT)"] <= -0.167959:
                                        if features["E(DOWN) - E(RIGHT)"] <= -0.154695:
                                            return 3
                                        else:
                                            if features["E(DOWN) - agent_row"] <= -11.247476:
                                                return 3
                                            else:
                                                if features["E(UP) - agent_column"] <= -9.999706:
                                                    if features["E(DOWN) - agent_row"] <= -6.297199:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - agent_column"] <= -11.279306:
                                                            return 1
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(LEFT) - T(RIGHT)"] <= -0.501224:
                                                        if features["E(UP) - E(DOWN)"] <= -0.720744:
                                                            return 1
                                                        else:
                                                            if features["T(up) - time_left"] <= -0.199712:
                                                                return 1
                                                            else:
                                                                return 3
                                                    else:
                                                        return 3
                                    else:
                                        if features["T(up) - agent_column"] <= -10.741609:
                                            return 0
                                        else:
                                            if features["E(UP) - agent_column"] <= -3.251221:
                                                if features["T(RIGHT) - agent_row"] <= -10.502921:
                                                    if features["T(RIGHT) - agent_column"] <= -9.999990:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                            else:
                                                if features["E(DOWN)"] <= 0.002632:
                                                    if features["E(RIGHT) - agent_row"] <= -1.205293:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                        else:
                            if features["E(LEFT) - agent_column"] <= -12.999999:
                                return 1
                            else:
                                if features["agent_row - time_left"] <= 12.200000:
                                    if features["T(LEFT) - agent_row"] <= -7.734592:
                                        if features["E(RIGHT) - agent_row"] <= -9.132280:
                                            if features["E(RIGHT) - agent_row"] <= -11.132016:
                                                if features["E(UP) - E(LEFT)"] <= 0.000010:
                                                    if features["E(UP) - E(LEFT)"] <= 0.000000:
                                                        return 1
                                                    else:
                                                        if features["T(DOWN) - T(RIGHT)"] <= -0.405888:
                                                            return 1
                                                        else:
                                                            return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["T(up) - T(LEFT)"] <= 0.431080:
                                                    if features["E(UP)"] <= 0.000000:
                                                        return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 1
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -3.131959:
                                                if features["agent_row - agent_column"] <= 3.500000:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                return 1
                                    else:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.320652:
                                            return 3
                                        else:
                                            if features["E(UP) - agent_row"] <= -2.999997:
                                                if features["E(RIGHT) - time_left"] <= 0.227326:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["E(UP) - E(LEFT)"] <= 0.000000:
                                                    return 3
                                                else:
                                                    return 1
                                else:
                                    return 3
                    else:
                        if features["E(LEFT) - T(DOWN)"] <= -0.000000:
                            if features["E(DOWN) - agent_row"] <= -10.999962:
                                if features["E(UP) - agent_column"] <= -10.136029:
                                    if features["agent_row - agent_column"] <= 1.500000:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    if features["T(DOWN) - agent_column"] <= -4.999614:
                                        return 3
                                    else:
                                        if features["E(RIGHT) - agent_row"] <= -10.131985:
                                            return 0
                                        else:
                                            return 3
                            else:
                                if features["E(RIGHT) - agent_row"] <= -1.132003:
                                    if features["T(DOWN) - T(LEFT)"] <= -0.605477:
                                        return 3
                                    else:
                                        if features["E(DOWN) - E(LEFT)"] <= 0.000003:
                                            if features["E(DOWN) - agent_row"] <= -1.999999:
                                                if features["T(up) - agent_column"] <= -0.512060:
                                                    if features["E(UP) - agent_column"] <= -1.132088:
                                                        if features["E(DOWN) - agent_column"] <= -4.000000:
                                                            if features["E(UP) - agent_row"] <= -3.200488:
                                                                return 3
                                                            else:
                                                                if features["agent_row - agent_column"] <= -1.500000:
                                                                    return 0
                                                                else:
                                                                    return 3
                                                        else:
                                                            if features["agent_row - time_left"] <= 2.690000:
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
                                            if features["E(UP)"] <= 0.865773:
                                                return 0
                                            else:
                                                if features["E(LEFT)"] <= 0.000000:
                                                    return 0
                                                else:
                                                    if features["T(LEFT) - agent_column"] <= -0.999962:
                                                        return 0
                                                    else:
                                                        return 3
                                else:
                                    if features["E(UP) - T(DOWN)"] <= 0.823152:
                                        return 3
                                    else:
                                        return 0
                        else:
                            if features["T(up) - agent_column"] <= -11.491474:
                                return 0
                            else:
                                if features["T(LEFT)"] <= 0.000000:
                                    return 0
                                else:
                                    return 3
                else:
                    if features["E(DOWN) - E(RIGHT)"] <= -0.226110:
                        if features["E(UP) - E(DOWN)"] <= 0.338583:
                            if features["E(LEFT)"] <= 0.008572:
                                return 3
                            else:
                                if features["E(LEFT) - T(up)"] <= -0.237620:
                                    if features["T(up) - time_left"] <= 0.195909:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.331476:
                                            if features["T(up) - T(DOWN)"] <= 0.104331:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -1.668649:
                                                return 3
                                            else:
                                                return 1
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.005403:
                                            return 3
                                        else:
                                            if features["E(UP) - agent_column"] <= -2.672335:
                                                return 3
                                            else:
                                                if features["E(UP)"] <= 0.386362:
                                                    return 3
                                                else:
                                                    return 2
                                else:
                                    if features["T(LEFT) - agent_column"] <= -3.999986:
                                        return 3
                                    else:
                                        if features["E(UP)"] <= 0.280346:
                                            if features["agent_row - time_left"] <= 2.680000:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -1.259154:
                                                if features["T(RIGHT) - time_left"] <= 0.297556:
                                                    if features["T(up) - T(LEFT)"] <= -0.000005:
                                                        return 0
                                                    else:
                                                        return 3
                                                else:
                                                    return 0
                                            else:
                                                return 3
                        else:
                            if features["E(UP) - T(RIGHT)"] <= 0.005822:
                                if features["E(DOWN) - T(RIGHT)"] <= -0.395304:
                                    if features["E(DOWN) - T(RIGHT)"] <= -0.416171:
                                        if features["E(DOWN)"] <= 0.003009:
                                            return 0
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -4.992319:
                                                if features["T(RIGHT)"] <= 0.493076:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 3
                                    else:
                                        return 0
                                else:
                                    return 3
                            else:
                                if features["E(LEFT) - T(DOWN)"] <= -0.002478:
                                    if features["E(DOWN) - agent_row"] <= -2.996160:
                                        if features["T(up) - agent_column"] <= -3.848351:
                                            if features["E(DOWN) - agent_row"] <= -10.991379:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -10.235019:
                                                    return 0
                                                else:
                                                    if features["E(UP) - agent_column"] <= -7.335009:
                                                        if features["T(LEFT) - time_left"] <= 0.125417:
                                                            return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        return 0
                                        else:
                                            if features["agent_column - time_left"] <= 0.890000:
                                                if features["E(DOWN) - agent_row"] <= -3.999312:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                return 0
                                    else:
                                        if features["E(UP) - agent_column"] <= -1.270694:
                                            if features["E(LEFT) - agent_column"] <= -2.998954:
                                                return 3
                                            else:
                                                return 0
                                        else:
                                            return 3
                                else:
                                    if features["E(DOWN) - E(LEFT)"] <= -0.000273:
                                        if features["T(up) - agent_column"] <= -2.606514:
                                            return 3
                                        else:
                                            return 0
                                    else:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.055440:
                                            return 3
                                        else:
                                            if features["T(up) - agent_column"] <= -11.368296:
                                                return 0
                                            else:
                                                if features["E(RIGHT)"] <= 0.444888:
                                                    return 0
                                                else:
                                                    return 3
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.370131:
                            if features["E(RIGHT) - T(DOWN)"] <= -0.014038:
                                if features["E(DOWN) - T(LEFT)"] <= 0.317428:
                                    if features["E(UP) - agent_row"] <= -4.795292:
                                        if features["E(LEFT)"] <= 0.012748:
                                            return 3
                                        else:
                                            if features["T(LEFT) - time_left"] <= -0.219996:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -4.580960:
                                                    if features["T(DOWN) - T(LEFT)"] <= -0.000082:
                                                        return 3
                                                    else:
                                                        if features["T(DOWN) - T(LEFT)"] <= 0.021846:
                                                            return 0
                                                        else:
                                                            return 3
                                                else:
                                                    if features["E(DOWN) - E(LEFT)"] <= 0.143484:
                                                        return 2
                                                    else:
                                                        return 3
                                    else:
                                        if features["E(UP) - E(RIGHT)"] <= -0.268137:
                                            return 3
                                        else:
                                            return 0
                                else:
                                    if features["E(DOWN) - agent_row"] <= -4.635358:
                                        if features["E(DOWN) - time_left"] <= -0.047908:
                                            return 2
                                        else:
                                            return 3
                                    else:
                                        if features["T(up)"] <= 0.000000:
                                            if features["E(UP) - T(DOWN)"] <= -0.589273:
                                                if features["E(DOWN) - agent_column"] <= -2.615592:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["E(RIGHT) - agent_column"] <= -6.561043:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            if features["T(LEFT) - agent_column"] <= -2.999898:
                                                return 1
                                            else:
                                                return 3
                            else:
                                if features["E(UP) - T(DOWN)"] <= 0.126798:
                                    if features["agent_column - time_left"] <= 3.790000:
                                        if features["T(RIGHT)"] <= 0.407873:
                                            if features["agent_row - time_left"] <= 6.910000:
                                                if features["E(UP) - agent_row"] <= -0.982832:
                                                    if features["T(DOWN) - agent_column"] <= -0.634009:
                                                        if features["E(UP) - T(DOWN)"] <= -0.190318:
                                                            return 1
                                                        else:
                                                            if features["E(UP) - T(DOWN)"] <= 0.016761:
                                                                if features["E(UP) - T(up)"] <= 0.005290:
                                                                    return 3
                                                                else:
                                                                    if features["T(up) - T(LEFT)"] <= -0.000009:
                                                                        return 0
                                                                    else:
                                                                        return 1
                                                            else:
                                                                return 1
                                                    else:
                                                        return 3
                                                else:
                                                    return 3
                                            else:
                                                if features["T(LEFT) - agent_row"] <= -7.990099:
                                                    if features["E(LEFT) - T(up)"] <= -0.275411:
                                                        if features["agent_row - agent_column"] <= 6.500000:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["E(RIGHT) - agent_row"] <= -7.641961:
                                                            return 1
                                                        else:
                                                            if features["E(UP) - agent_column"] <= -1.869259:
                                                                return 1
                                                            else:
                                                                return 3
                                                else:
                                                    return 3
                                        else:
                                            if features["T(RIGHT)"] <= 0.424600:
                                                if features["E(LEFT) - agent_row"] <= -7.972232:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.212911:
                                                    if features["E(DOWN) - time_left"] <= 0.142746:
                                                        if features["E(DOWN) - time_left"] <= 0.061159:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(LEFT)"] <= 0.031246:
                                                            if features["E(UP) - agent_row"] <= -9.986128:
                                                                return 3
                                                            else:
                                                                if features["T(DOWN) - T(LEFT)"] <= -0.000000:
                                                                    return 1
                                                                else:
                                                                    if features["agent_row - agent_column"] <= 2.500000:
                                                                        return 1
                                                                    else:
                                                                        return 3
                                                        else:
                                                            return 1
                                                else:
                                                    if features["T(up) - agent_column"] <= -2.987667:
                                                        return 1
                                                    else:
                                                        if features["E(LEFT) - agent_row"] <= -4.950854:
                                                            return 3
                                                        else:
                                                            return 1
                                    else:
                                        if features["E(LEFT) - agent_column"] <= -4.978864:
                                            if features["E(LEFT) - time_left"] <= -0.122729:
                                                if features["E(DOWN) - E(RIGHT)"] <= -0.098223:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                if features["T(DOWN) - T(RIGHT)"] <= 0.000190:
                                                    return 1
                                                else:
                                                    return 0
                                        else:
                                            if features["E(UP)"] <= 0.275122:
                                                if features["E(RIGHT) - time_left"] <= 0.357981:
                                                    if features["E(RIGHT) - T(DOWN)"] <= 0.437520:
                                                        if features["T(up)"] <= 0.000000:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(RIGHT)"] <= 0.439832:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                return 3
                                else:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.007663:
                                        if features["T(RIGHT) - agent_row"] <= -6.716367:
                                            if features["E(RIGHT) - time_left"] <= -0.109240:
                                                if features["T(up) - agent_row"] <= -9.424752:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -6.475661:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - T(RIGHT)"] <= -0.107386:
                                                    return 3
                                                else:
                                                    if features["E(DOWN) - T(LEFT)"] <= 0.233857:
                                                        return 3
                                                    else:
                                                        return 1
                                    else:
                                        if features["E(UP) - time_left"] <= 0.137623:
                                            if features["E(LEFT) - agent_row"] <= -9.950696:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["T(LEFT)"] <= 0.000000:
                                                return 1
                                            else:
                                                return 3
                        else:
                            if features["E(LEFT) - time_left"] <= -0.057064:
                                if features["E(RIGHT) - agent_row"] <= -11.239434:
                                    return 3
                                else:
                                    if features["E(DOWN) - E(RIGHT)"] <= -0.176087:
                                        if features["T(LEFT)"] <= 0.000000:
                                            if features["E(RIGHT) - T(RIGHT)"] <= -0.065342:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            return 3
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -8.589937:
                                            if features["E(DOWN) - T(DOWN)"] <= 0.713192:
                                                return 3
                                            else:
                                                return 1
                                        else:
                                            if features["E(LEFT) - T(LEFT)"] <= -0.001237:
                                                return 3
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.351813:
                                                    return 1
                                                else:
                                                    return 3
                            else:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.009810:
                                    if features["E(UP) - T(up)"] <= -0.013045:
                                        if features["E(RIGHT) - agent_row"] <= -4.563699:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 3
                                else:
                                    if features["E(DOWN) - T(RIGHT)"] <= -0.052341:
                                        return 1
                                    else:
                                        return 3
            else:
                if features["E(DOWN) - agent_row"] <= -11.223915:
                    if features["E(DOWN) - agent_row"] <= -11.249951:
                        if features["agent_row - agent_column"] <= -0.500000:
                            return 1
                        else:
                            return 3
                    else:
                        if features["T(up) - T(LEFT)"] <= 0.447334:
                            return 3
                        else:
                            return 1
                else:
                    if features["E(RIGHT) - agent_row"] <= -0.270377:
                        if features["E(UP)"] <= 0.000000:
                            if features["E(UP) - E(DOWN)"] <= -0.806755:
                                if features["T(DOWN) - agent_row"] <= -6.310640:
                                    return 1
                                else:
                                    return 3
                            else:
                                return 1
                        else:
                            if features["E(LEFT) - E(RIGHT)"] <= -0.860802:
                                if features["T(LEFT) - agent_row"] <= -11.687012:
                                    return 1
                                else:
                                    if features["T(LEFT)"] <= 0.000003:
                                        if features["T(up) - agent_row"] <= -5.838812:
                                            if features["agent_row - agent_column"] <= 8.500000:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 3
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -10.999974:
                                            if features["E(UP) - E(LEFT)"] <= 0.000143:
                                                if features["T(up) - agent_row"] <= -10.689810:
                                                    return 3
                                                else:
                                                    return 1
                                            else:
                                                return 3
                                        else:
                                            if features["T(up) - T(LEFT)"] <= 0.518058:
                                                if features["E(UP) - agent_row"] <= -11.999992:
                                                    return 1
                                                else:
                                                    if features["agent_row - agent_column"] <= -6.500000:
                                                        return 1
                                                    else:
                                                        return 3
                                            else:
                                                return 1
                            else:
                                if features["T(DOWN) - agent_column"] <= -11.790131:
                                    return 1
                                else:
                                    if features["T(RIGHT) - time_left"] <= 0.281904:
                                        if features["E(UP)"] <= 0.000042:
                                            if features["T(up) - agent_row"] <= -8.683095:
                                                if features["E(RIGHT) - agent_column"] <= -8.267746:
                                                    return 1
                                                else:
                                                    if features["T(LEFT)"] <= 0.000000:
                                                        return 1
                                                    else:
                                                        if features["E(DOWN) - agent_column"] <= -1.195658:
                                                            if features["agent_row - agent_column"] <= 5.500000:
                                                                return 3
                                                            else:
                                                                return 1
                                                        else:
                                                            return 3
                                            else:
                                                return 1
                                        else:
                                            if features["agent_row - agent_column"] <= 2.500000:
                                                if features["T(DOWN) - agent_row"] <= -6.565909:
                                                    return 1
                                                else:
                                                    if features["E(LEFT) - agent_row"] <= -2.999713:
                                                        return 3
                                                    else:
                                                        return 1
                                            else:
                                                if features["E(UP) - T(LEFT)"] <= -0.001539:
                                                    return 3
                                                else:
                                                    return 1
                                    else:
                                        if features["T(up) - T(LEFT)"] <= -0.002369:
                                            return 1
                                        else:
                                            if features["T(DOWN) - T(RIGHT)"] <= -0.004973:
                                                return 1
                                            else:
                                                if features["T(DOWN) - T(RIGHT)"] <= -0.004347:
                                                    return 3
                                                else:
                                                    return 1
                    else:
                        if features["E(RIGHT) - time_left"] <= 0.312497:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.388932:
                                return 1
                            else:
                                if features["agent_column - time_left"] <= 0.060000:
                                    return 1
                                else:
                                    if features["E(DOWN) - agent_row"] <= 0.416380:
                                        return 3
                                    else:
                                        if features["T(RIGHT) - time_left"] <= -0.349750:
                                            return 2
                                        else:
                                            return 3
                        else:
                            return 3
        else:
            if features["E(DOWN) - time_left"] <= 0.324497:
                if features["E(LEFT) - T(up)"] <= 0.019014:
                    if features["E(DOWN) - time_left"] <= 0.087422:
                        if features["E(DOWN)"] <= 0.042268:
                            if features["T(LEFT) - time_left"] <= -0.420000:
                                if features["E(UP) - T(up)"] <= -0.037520:
                                    return 3
                                else:
                                    return 0
                            else:
                                return 3
                        else:
                            if features["E(UP) - agent_column"] <= -5.858270:
                                if features["E(LEFT) - E(RIGHT)"] <= 0.091427:
                                    if features["E(UP)"] <= 0.019478:
                                        return 1
                                    else:
                                        if features["T(up) - T(LEFT)"] <= 0.000395:
                                            return 3
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= 0.055159:
                                                if features["E(LEFT) - time_left"] <= -0.348556:
                                                    return 3
                                                else:
                                                    if features["E(RIGHT) - T(DOWN)"] <= 0.278890:
                                                        return 2
                                                    else:
                                                        return 3
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= -0.375316:
                                                    return 3
                                                else:
                                                    return 1
                                else:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.478306:
                                        if features["T(DOWN)"] <= 0.000000:
                                            return 1
                                        else:
                                            if features["E(UP)"] <= 0.086092:
                                                return 2
                                            else:
                                                if features["T(LEFT) - agent_column"] <= -8.785080:
                                                    return 3
                                                else:
                                                    return 2
                                    else:
                                        return 1
                            else:
                                if features["E(RIGHT) - T(LEFT)"] <= 0.267224:
                                    if features["E(UP) - E(DOWN)"] <= -0.367904:
                                        return 1
                                    else:
                                        if features["T(DOWN) - agent_row"] <= -9.999745:
                                            if features["E(DOWN)"] <= 0.247744:
                                                if features["E(UP) - time_left"] <= 0.149648:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 2
                                        else:
                                            if features["E(DOWN) - T(RIGHT)"] <= -0.005106:
                                                if features["E(RIGHT) - T(LEFT)"] <= 0.222704:
                                                    return 2
                                                else:
                                                    if features["E(LEFT) - time_left"] <= -0.093641:
                                                        return 1
                                                    else:
                                                        if features["E(RIGHT) - time_left"] <= 0.229390:
                                                            return 2
                                                        else:
                                                            return 3
                                            else:
                                                if features["T(up) - agent_row"] <= -2.248842:
                                                    return 3
                                                else:
                                                    return 2
                                else:
                                    if features["T(LEFT)"] <= 0.000193:
                                        if features["E(LEFT) - time_left"] <= -0.129078:
                                            if features["E(UP) - agent_row"] <= -6.961282:
                                                if features["E(DOWN) - time_left"] <= -0.145073:
                                                    if features["E(DOWN) - E(RIGHT)"] <= -0.232276:
                                                        return 3
                                                    else:
                                                        if features["E(LEFT) - T(up)"] <= -0.271381:
                                                            return 1
                                                        else:
                                                            return 3
                                                else:
                                                    if features["T(up) - agent_column"] <= 0.005735:
                                                        if features["T(LEFT) - agent_column"] <= -3.999967:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        return 3
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.140822:
                                                    if features["T(DOWN) - T(RIGHT)"] <= -0.000414:
                                                        return 1
                                                    else:
                                                        return 0
                                                else:
                                                    return 3
                                        else:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.232823:
                                                if features["T(up) - T(LEFT)"] <= 0.492622:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(DOWN) - T(LEFT)"] <= 0.000030:
                                                    return 1
                                                else:
                                                    if features["T(DOWN) - agent_row"] <= -6.999929:
                                                        return 2
                                                    else:
                                                        return 1
                                    else:
                                        if features["T(up) - time_left"] <= 0.408483:
                                            if features["E(UP)"] <= 0.364640:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 3
                    else:
                        if features["E(LEFT) - agent_column"] <= -2.851256:
                            if features["E(UP) - T(RIGHT)"] <= 0.230661:
                                if features["E(LEFT) - E(RIGHT)"] <= 0.037135:
                                    if features["T(LEFT)"] <= 0.000000:
                                        if features["E(DOWN) - E(LEFT)"] <= 0.157167:
                                            return 2
                                        else:
                                            return 1
                                    else:
                                        if features["T(RIGHT)"] <= 0.000012:
                                            if features["E(UP) - T(DOWN)"] <= 0.162397:
                                                return 1
                                            else:
                                                if features["T(DOWN)"] <= 0.000000:
                                                    return 1
                                                else:
                                                    return 3
                                        else:
                                            if features["E(UP) - agent_column"] <= -3.731578:
                                                return 1
                                            else:
                                                if features["E(LEFT) - time_left"] <= 0.181849:
                                                    if features["E(DOWN) - T(RIGHT)"] <= -0.450701:
                                                        if features["E(RIGHT) - agent_row"] <= -5.134980:
                                                            return 3
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["T(DOWN) - T(RIGHT)"] <= -0.089255:
                                                            if features["T(LEFT) - agent_row"] <= -10.999617:
                                                                return 3
                                                            else:
                                                                return 1
                                                        else:
                                                            if features["E(UP) - T(LEFT)"] <= 0.068510:
                                                                if features["E(UP) - agent_column"] <= -2.887362:
                                                                    return 1
                                                                else:
                                                                    if features["T(LEFT) - time_left"] <= 0.069533:
                                                                        if features["T(DOWN)"] <= 0.333929:
                                                                            return 2
                                                                        else:
                                                                            return 3
                                                                    else:
                                                                        return 1
                                                            else:
                                                                if features["T(RIGHT) - time_left"] <= 0.335240:
                                                                    return 1
                                                                else:
                                                                    return 3
                                                else:
                                                    return 2
                                else:
                                    if features["T(up) - T(RIGHT)"] <= -0.000206:
                                        if features["E(UP) - E(DOWN)"] <= -0.385777:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(RIGHT) - time_left"] <= 0.028520:
                                            if features["agent_row - time_left"] <= 9.770000:
                                                if features["E(LEFT) - time_left"] <= 0.247686:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["E(UP) - time_left"] <= -0.227188:
                                                    return 1
                                                else:
                                                    return 2
                                        else:
                                            return 1
                            else:
                                if features["T(DOWN) - T(RIGHT)"] <= -0.000000:
                                    if features["T(up) - agent_column"] <= -3.393456:
                                        if features["E(DOWN) - T(up)"] <= -0.534083:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 3
                                else:
                                    return 3
                        else:
                            if features["E(DOWN) - E(LEFT)"] <= 0.245436:
                                if features["E(LEFT) - T(up)"] <= -0.189888:
                                    if features["T(LEFT)"] <= 0.000002:
                                        if features["E(DOWN) - E(LEFT)"] <= 0.111418:
                                            return 2
                                        else:
                                            if features["E(RIGHT) - T(up)"] <= -0.052895:
                                                if features["T(RIGHT) - time_left"] <= 0.340232:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                    else:
                                        if features["E(DOWN) - T(up)"] <= -0.521273:
                                            return 3
                                        else:
                                            return 1
                                else:
                                    if features["E(DOWN) - time_left"] <= 0.291535:
                                        if features["E(DOWN) - E(RIGHT)"] <= -0.197068:
                                            return 0
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= -0.314869:
                                                return 1
                                            else:
                                                return 2
                                    else:
                                        return 3
                            else:
                                if features["E(UP) - T(up)"] <= 0.000001:
                                    if features["E(DOWN)"] <= 0.299870:
                                        if features["E(UP) - E(RIGHT)"] <= -0.271470:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 1
                                else:
                                    return 3
                else:
                    if features["E(RIGHT) - T(RIGHT)"] <= 0.148996:
                        if features["E(UP) - E(DOWN)"] <= -0.144740:
                            if features["E(UP) - T(LEFT)"] <= 0.002926:
                                if features["T(up) - time_left"] <= 0.110672:
                                    if features["T(RIGHT) - time_left"] <= 0.007774:
                                        if features["E(UP)"] <= 0.003821:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.004190:
                                                if features["E(DOWN) - E(LEFT)"] <= 0.002885:
                                                    if features["T(up) - agent_row"] <= -12.553380:
                                                        return 2
                                                    else:
                                                        if features["E(DOWN) - agent_row"] <= 0.301471:
                                                            return 1
                                                        else:
                                                            return 2
                                                else:
                                                    return 2
                                            else:
                                                if features["E(RIGHT) - T(RIGHT)"] <= 0.001447:
                                                    if features["T(RIGHT) - time_left"] <= 0.000156:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    return 1
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -7.848016:
                                                if features["T(RIGHT) - time_left"] <= -0.040000:
                                                    if features["E(LEFT) - E(RIGHT)"] <= 0.157869:
                                                        if features["T(up) - time_left"] <= -0.469913:
                                                            return 1
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(up) - agent_row"] <= -5.999893:
                                                            if features["T(LEFT) - time_left"] <= 0.309893:
                                                                return 1
                                                            else:
                                                                return 2
                                                        else:
                                                            if features["E(LEFT) - T(DOWN)"] <= -0.115826:
                                                                return 2
                                                            else:
                                                                return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -4.765218:
                                            if features["T(RIGHT) - agent_row"] <= -9.745587:
                                                if features["E(RIGHT) - time_left"] <= 0.055130:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["E(RIGHT) - T(up)"] <= 0.198419:
                                                    return 1
                                                else:
                                                    if features["E(UP) - E(RIGHT)"] <= -0.241418:
                                                        return 1
                                                    else:
                                                        return 2
                                        else:
                                            if features["E(DOWN) - agent_row"] <= -4.595693:
                                                return 2
                                            else:
                                                if features["E(UP) - T(up)"] <= -0.000000:
                                                    return 1
                                                else:
                                                    if features["E(DOWN) - agent_column"] <= -10.629402:
                                                        return 2
                                                    else:
                                                        return 1
                                else:
                                    if features["E(RIGHT)"] <= 0.025592:
                                        return 1
                                    else:
                                        return 2
                            else:
                                if features["E(LEFT) - T(up)"] <= 0.187034:
                                    if features["T(DOWN) - T(RIGHT)"] <= -0.000005:
                                        if features["E(RIGHT) - agent_row"] <= -4.679736:
                                            if features["E(LEFT) - T(RIGHT)"] <= -0.384779:
                                                if features["T(DOWN) - agent_row"] <= -4.499952:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                if features["T(DOWN) - time_left"] <= 0.116299:
                                                    if features["E(RIGHT) - agent_row"] <= -5.655514:
                                                        if features["T(LEFT) - time_left"] <= -0.259630:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["T(RIGHT) - agent_row"] <= -4.597722:
                                                            return 1
                                                        else:
                                                            return 2
                                                else:
                                                    return 2
                                        else:
                                            return 1
                                    else:
                                        if features["E(UP) - agent_column"] <= -4.908047:
                                            if features["T(LEFT) - agent_column"] <= -5.999063:
                                                if features["E(UP)"] <= 0.083914:
                                                    return 1
                                                else:
                                                    return 2
                                            else:
                                                return 3
                                        else:
                                            if features["E(UP) - E(DOWN)"] <= -0.218094:
                                                return 3
                                            else:
                                                if features["T(up) - agent_row"] <= -5.000000:
                                                    return 3
                                                else:
                                                    if features["T(RIGHT) - agent_column"] <= -4.414022:
                                                        return 3
                                                    else:
                                                        return 0
                                else:
                                    if features["agent_row - time_left"] <= 3.770000:
                                        if features["E(DOWN) - T(up)"] <= 0.328092:
                                            return 0
                                        else:
                                            return 1
                                    else:
                                        if features["T(up) - agent_row"] <= -6.999984:
                                            if features["T(LEFT)"] <= 0.000000:
                                                return 2
                                            else:
                                                if features["T(DOWN) - agent_column"] <= -7.166418:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            if features["agent_row - time_left"] <= 4.490000:
                                                if features["T(LEFT)"] <= 0.000000:
                                                    return 1
                                                else:
                                                    if features["E(UP) - E(LEFT)"] <= -0.085793:
                                                        return 2
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(DOWN) - T(up)"] <= 0.427361:
                                                    return 2
                                                else:
                                                    if features["T(up)"] <= 0.000031:
                                                        return 1
                                                    else:
                                                        return 2
                        else:
                            if features["E(LEFT)"] <= 0.185091:
                                if features["T(DOWN) - T(RIGHT)"] <= -0.003895:
                                    if features["E(LEFT)"] <= 0.121716:
                                        if features["T(RIGHT)"] <= 0.526001:
                                            if features["E(UP) - time_left"] <= 0.224896:
                                                if features["E(UP) - T(DOWN)"] <= -0.155445:
                                                    return 2
                                                else:
                                                    if features["E(UP) - agent_row"] <= -5.796203:
                                                        if features["E(DOWN) - time_left"] <= -0.100363:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["E(RIGHT) - T(RIGHT)"] <= -0.117139:
                                                            return 2
                                                        else:
                                                            return 1
                                            else:
                                                return 0
                                        else:
                                            return 3
                                    else:
                                        if features["T(RIGHT)"] <= 0.670316:
                                            return 2
                                        else:
                                            return 1
                                else:
                                    if features["T(LEFT)"] <= 0.000000:
                                        return 2
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -4.438587:
                                            if features["E(LEFT) - agent_row"] <= -5.890254:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            if features["T(LEFT)"] <= 0.000045:
                                                if features["E(RIGHT) - time_left"] <= 0.280986:
                                                    if features["E(DOWN) - T(DOWN)"] <= -0.281401:
                                                        if features["T(RIGHT) - agent_column"] <= -0.499273:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 2
                                                else:
                                                    return 3
                                            else:
                                                if features["agent_row - time_left"] <= 0.730000:
                                                    return 2
                                                else:
                                                    return 0
                            else:
                                if features["E(LEFT) - T(DOWN)"] <= -0.326549:
                                    if features["E(UP) - agent_row"] <= -4.746681:
                                        if features["T(DOWN) - T(RIGHT)"] <= -0.000074:
                                            return 2
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -4.347344:
                                                return 2
                                            else:
                                                return 0
                                    else:
                                        return 0
                                else:
                                    if features["E(UP) - time_left"] <= 0.216432:
                                        if features["E(UP)"] <= 0.241956:
                                            return 2
                                        else:
                                            if features["T(LEFT) - time_left"] <= 0.083192:
                                                return 2
                                            else:
                                                return 1
                                    else:
                                        if features["E(DOWN) - T(up)"] <= 0.075100:
                                            return 0
                                        else:
                                            return 2
                    else:
                        if features["T(up) - T(RIGHT)"] <= -0.000000:
                            if features["E(DOWN) - E(LEFT)"] <= 0.087274:
                                if features["T(LEFT) - agent_column"] <= -7.993488:
                                    return 2
                                else:
                                    if features["E(DOWN) - E(RIGHT)"] <= 0.083092:
                                        return 0
                                    else:
                                        return 3
                            else:
                                if features["T(LEFT) - agent_column"] <= -6.515827:
                                    if features["T(LEFT) - time_left"] <= -0.079203:
                                        return 1
                                    else:
                                        if features["E(UP) - agent_column"] <= -6.894768:
                                            if features["T(LEFT) - agent_row"] <= -2.553534:
                                                return 2
                                            else:
                                                return 3
                                        else:
                                            return 0
                                else:
                                    if features["E(UP) - T(DOWN)"] <= -0.749557:
                                        return 1
                                    else:
                                        if features["E(RIGHT) - agent_column"] <= -4.659990:
                                            if features["E(UP) - T(LEFT)"] <= -0.351290:
                                                return 3
                                            else:
                                                if features["E(UP) - agent_row"] <= -4.853048:
                                                    return 3
                                                else:
                                                    if features["E(UP) - E(DOWN)"] <= -0.272271:
                                                        return 3
                                                    else:
                                                        return 0
                                        else:
                                            return 3
                        else:
                            if features["E(DOWN) - T(DOWN)"] <= 0.314418:
                                if features["E(LEFT) - E(RIGHT)"] <= 0.140671:
                                    if features["E(RIGHT) - agent_row"] <= -8.738443:
                                        return 2
                                    else:
                                        if features["E(DOWN) - time_left"] <= 0.296418:
                                            if features["T(LEFT) - time_left"] <= -0.294040:
                                                return 1
                                            else:
                                                return 3
                                        else:
                                            return 3
                                else:
                                    if features["E(DOWN) - agent_column"] <= -6.607869:
                                        return 2
                                    else:
                                        return 1
                            else:
                                if features["T(RIGHT)"] <= 0.000000:
                                    if features["E(LEFT) - time_left"] <= 0.251436:
                                        return 3
                                    else:
                                        return 1
                                else:
                                    return 1
            else:
                if features["E(UP) - E(LEFT)"] <= -0.662078:
                    if features["E(LEFT) - agent_row"] <= -12.132389:
                        if features["E(UP) - agent_column"] <= -6.999999:
                            if features["E(DOWN) - agent_column"] <= -7.134071:
                                if features["E(DOWN) - T(LEFT)"] <= 0.849676:
                                    return 2
                                else:
                                    return 1
                            else:
                                return 1
                        else:
                            if features["T(up) - agent_column"] <= -1.345715:
                                if features["E(RIGHT) - agent_row"] <= -12.999953:
                                    if features["T(LEFT) - agent_column"] <= -3.969971:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 2
                            else:
                                return 1
                    else:
                        if features["E(DOWN) - agent_column"] <= -2.219484:
                            if features["E(UP)"] <= 0.000005:
                                if features["E(LEFT) - E(RIGHT)"] <= 0.799469:
                                    if features["T(up)"] <= 0.000000:
                                        return 2
                                    else:
                                        if features["E(UP) - E(RIGHT)"] <= -0.000504:
                                            if features["T(up) - agent_column"] <= -7.999999:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - E(LEFT)"] <= 0.000005:
                                                return 2
                                            else:
                                                return 1
                                else:
                                    if features["E(UP) - agent_row"] <= -0.999999:
                                        if features["T(DOWN) - agent_column"] <= -5.181356:
                                            if features["T(up) - agent_column"] <= -7.465907:
                                                if features["T(LEFT) - agent_row"] <= -7.700516:
                                                    if features["E(UP)"] <= 0.000003:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    if features["E(DOWN)"] <= 0.860592:
                                                        return 2
                                                    else:
                                                        return 1
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -4.131950:
                                                return 2
                                            else:
                                                if features["T(RIGHT) - time_left"] <= 0.399227:
                                                    return 1
                                                else:
                                                    return 2
                                    else:
                                        return 2
                            else:
                                if features["E(UP) - agent_column"] <= -5.999918:
                                    if features["E(LEFT) - agent_column"] <= -8.133256:
                                        if features["T(up) - agent_column"] <= -8.938586:
                                            if features["E(UP) - agent_row"] <= -6.999976:
                                                if features["T(up) - T(RIGHT)"] <= 0.563264:
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
                                    if features["E(UP) - T(RIGHT)"] <= -0.015614:
                                        if features["E(DOWN) - E(LEFT)"] <= 0.000077:
                                            return 2
                                        else:
                                            if features["T(up) - agent_column"] <= -3.955619:
                                                return 2
                                            else:
                                                if features["E(UP) - T(LEFT)"] <= 0.000006:
                                                    return 1
                                                else:
                                                    return 2
                                    else:
                                        return 1
                        else:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.867794:
                                if features["agent_row - time_left"] <= -0.110000:
                                    return 2
                                else:
                                    if features["E(DOWN) - T(DOWN)"] <= 0.851430:
                                        return 1
                                    else:
                                        if features["E(DOWN) - agent_column"] <= -0.132859:
                                            if features["T(RIGHT) - agent_column"] <= -2.329757:
                                                return 1
                                            else:
                                                return 2
                                        else:
                                            return 1
                            else:
                                if features["T(up) - agent_column"] <= -0.999792:
                                    if features["E(RIGHT) - agent_column"] <= -2.999999:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(UP) - E(RIGHT)"] <= -0.000012:
                                        return 1
                                    else:
                                        return 2
                else:
                    if features["E(LEFT) - agent_row"] <= 0.319950:
                        if features["E(UP) - T(LEFT)"] <= 0.000092:
                            if features["E(LEFT) - T(RIGHT)"] <= 0.249356:
                                if features["E(RIGHT) - T(RIGHT)"] <= 0.218069:
                                    return 1
                                else:
                                    if features["T(DOWN) - T(LEFT)"] <= 0.000720:
                                        return 1
                                    else:
                                        if features["T(DOWN) - time_left"] <= 0.606438:
                                            return 3
                                        else:
                                            return 1
                            else:
                                if features["T(up)"] <= 0.000000:
                                    if features["E(DOWN) - T(RIGHT)"] <= 0.389787:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(DOWN) - agent_row"] <= -12.208721:
                                        return 2
                                    else:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.253119:
                                            if features["agent_row - agent_column"] <= -5.500000:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(UP) - T(RIGHT)"] <= 0.000013:
                                                if features["E(RIGHT)"] <= 0.094657:
                                                    return 1
                                                else:
                                                    return 3
                                            else:
                                                if features["E(RIGHT) - time_left"] <= 0.039937:
                                                    if features["E(DOWN) - T(LEFT)"] <= -0.275166:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    if features["T(up) - time_left"] <= -0.139607:
                                                        return 3
                                                    else:
                                                        if features["E(DOWN) - time_left"] <= 0.425358:
                                                            return 1
                                                        else:
                                                            return 2
                        else:
                            if features["E(LEFT)"] <= 0.268740:
                                if features["T(up)"] <= 0.000000:
                                    if features["T(LEFT) - agent_column"] <= -5.999913:
                                        return 1
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.401719:
                                            return 1
                                        else:
                                            return 3
                                else:
                                    if features["T(up) - time_left"] <= -0.085844:
                                        if features["T(RIGHT) - agent_row"] <= -6.200501:
                                            return 3
                                        else:
                                            return 1
                                    else:
                                        return 1
                            else:
                                if features["T(up) - time_left"] <= -0.080000:
                                    if features["E(DOWN) - T(RIGHT)"] <= -0.035009:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["T(DOWN) - agent_column"] <= -10.451211:
                                        return 2
                                    else:
                                        if features["E(UP) - T(LEFT)"] <= 0.074287:
                                            if features["T(up)"] <= 0.000000:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(RIGHT) - agent_row"] <= -4.759289:
                                                return 2
                                            else:
                                                return 1
                    else:
                        if features["E(UP) - E(RIGHT)"] <= -0.035392:
                            return 1
                        else:
                            if features["E(DOWN) - agent_row"] <= 0.384961:
                                return 2
                            else:
                                if features["E(DOWN) - E(LEFT)"] <= 0.000245:
                                    return 2
                                else:
                                    return 1
    else:
        if features["E(UP) - E(LEFT)"] <= -0.000014:
            if features["E(DOWN) - E(LEFT)"] <= -0.165202:
                if features["E(UP)"] <= 0.662893:
                    if features["E(RIGHT) - T(RIGHT)"] <= -0.000000:
                        if features["E(LEFT) - time_left"] <= 0.355000:
                            if features["E(LEFT) - time_left"] <= 0.354784:
                                if features["E(DOWN) - T(RIGHT)"] <= 0.160236:
                                    if features["E(UP) - E(DOWN)"] <= 0.369074:
                                        if features["E(LEFT) - time_left"] <= -0.091398:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.353062:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(UP) - agent_column"] <= -12.614231:
                                            return 0
                                        else:
                                            if features["E(RIGHT)"] <= 0.001751:
                                                return 2
                                            else:
                                                if features["E(LEFT) - T(RIGHT)"] <= 0.438211:
                                                    if features["E(UP) - T(RIGHT)"] <= 0.393192:
                                                        if features["E(DOWN) - T(LEFT)"] <= 0.004049:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        return 2
                                                else:
                                                    return 0
                                else:
                                    if features["E(UP) - agent_column"] <= -8.774550:
                                        return 2
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.004587:
                                            return 1
                                        else:
                                            return 2
                            else:
                                return 0
                        else:
                            if features["E(UP) - agent_column"] <= -0.519548:
                                if features["E(DOWN) - time_left"] <= 0.231110:
                                    if features["E(UP) - E(DOWN)"] <= 0.614933:
                                        return 2
                                    else:
                                        if features["E(RIGHT)"] <= 0.000040:
                                            return 2
                                        else:
                                            if features["T(up) - agent_column"] <= -2.742866:
                                                return 2
                                            else:
                                                return 0
                                else:
                                    if features["E(DOWN) - E(LEFT)"] <= -0.190647:
                                        return 2
                                    else:
                                        return 1
                            else:
                                return 0
                    else:
                        if features["E(UP) - T(up)"] <= 0.301833:
                            if features["E(LEFT) - time_left"] <= 0.325982:
                                if features["E(UP) - time_left"] <= 0.322576:
                                    if features["T(RIGHT) - time_left"] <= -0.118662:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.013454:
                                            if features["E(LEFT) - T(LEFT)"] <= 0.024971:
                                                if features["T(DOWN) - T(LEFT)"] <= -0.434749:
                                                    return 2
                                                else:
                                                    if features["E(DOWN) - T(DOWN)"] <= 0.011699:
                                                        if features["E(DOWN) - E(RIGHT)"] <= 0.266293:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["T(up) - T(LEFT)"] <= -0.000684:
                                                            return 0
                                                        else:
                                                            return 1
                                            else:
                                                return 2
                                        else:
                                            if features["E(LEFT) - agent_column"] <= -10.631685:
                                                return 3
                                            else:
                                                if features["T(up) - agent_row"] <= -7.998422:
                                                    return 2
                                                else:
                                                    if features["agent_column - time_left"] <= 9.770000:
                                                        return 1
                                                    else:
                                                        return 2
                                    else:
                                        if features["T(RIGHT)"] <= 0.000007:
                                            if features["E(UP)"] <= 0.333770:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 2
                                else:
                                    return 0
                            else:
                                if features["E(DOWN) - T(DOWN)"] <= 0.247787:
                                    if features["E(UP) - T(DOWN)"] <= 0.384785:
                                        if features["E(UP) - T(up)"] <= 0.245660:
                                            return 2
                                        else:
                                            if features["T(up) - T(DOWN)"] <= -0.000219:
                                                return 2
                                            else:
                                                if features["E(DOWN) - T(up)"] <= 0.174319:
                                                    return 0
                                                else:
                                                    return 2
                                    else:
                                        return 2
                                else:
                                    return 2
                        else:
                            if features["T(DOWN) - agent_column"] <= -10.999173:
                                if features["T(DOWN) - agent_row"] <= -11.975162:
                                    return 2
                                else:
                                    if features["E(LEFT) - time_left"] <= 0.281897:
                                        return 2
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.390913:
                                            return 0
                                        else:
                                            return 2
                            else:
                                if features["T(RIGHT)"] <= 0.000004:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.548862:
                                        return 2
                                    else:
                                        if features["E(UP) - time_left"] <= 0.262475:
                                            return 3
                                        else:
                                            return 0
                                else:
                                    return 2
                else:
                    if features["E(RIGHT) - agent_column"] <= -1.999997:
                        if features["E(RIGHT)"] <= 0.000002:
                            if features["E(UP) - T(RIGHT)"] <= 0.799072:
                                if features["T(DOWN) - agent_column"] <= -1.999996:
                                    if features["E(LEFT) - E(RIGHT)"] <= 0.842348:
                                        return 2
                                    else:
                                        if features["agent_row - agent_column"] <= -0.500000:
                                            return 0
                                        else:
                                            if features["E(LEFT) - agent_column"] <= -7.132759:
                                                return 0
                                            else:
                                                return 2
                                else:
                                    if features["T(up) - agent_row"] <= -8.999999:
                                        if features["E(UP) - agent_row"] <= -10.170146:
                                            if features["E(DOWN)"] <= 0.000005:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 0
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -7.999892:
                                            return 2
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -6.451979:
                                                return 0
                                            else:
                                                return 2
                            else:
                                if features["T(up) - time_left"] <= -0.069665:
                                    return 0
                                else:
                                    return 2
                        else:
                            if features["E(DOWN) - agent_row"] <= -1.998964:
                                if features["E(UP) - E(LEFT)"] <= -0.023872:
                                    if features["E(RIGHT)"] <= 0.000082:
                                        if features["T(LEFT) - T(RIGHT)"] <= 0.567300:
                                            return 2
                                        else:
                                            return 0
                                    else:
                                        if features["E(LEFT) - agent_row"] <= -6.276628:
                                            return 2
                                        else:
                                            if features["T(RIGHT) - agent_row"] <= -4.540858:
                                                return 0
                                            else:
                                                return 2
                                else:
                                    if features["E(RIGHT) - agent_column"] <= -2.999928:
                                        if features["T(LEFT)"] <= 0.000089:
                                            return 2
                                        else:
                                            if features["agent_row - time_left"] <= 11.870000:
                                                if features["agent_row - agent_column"] <= -1.500000:
                                                    if features["T(RIGHT)"] <= 0.000015:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    if features["T(DOWN)"] <= 0.000000:
                                                        return 2
                                                    else:
                                                        return 0
                                            else:
                                                return 2
                                    else:
                                        if features["E(UP) - agent_column"] <= -2.238112:
                                            return 0
                                        else:
                                            return 2
                            else:
                                return 2
                    else:
                        if features["T(RIGHT) - time_left"] <= 0.380783:
                            if features["E(RIGHT)"] <= 0.000001:
                                if features["E(DOWN) - T(LEFT)"] <= 0.000030:
                                    return 0
                                else:
                                    return 2
                            else:
                                if features["E(LEFT) - agent_row"] <= -3.187926:
                                    if features["E(LEFT) - time_left"] <= 0.216548:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    if features["E(LEFT)"] <= 0.806832:
                                        return 0
                                    else:
                                        return 2
                        else:
                            return 0
            else:
                if features["E(UP) - T(RIGHT)"] <= 0.000000:
                    if features["E(RIGHT) - agent_column"] <= -1.999997:
                        if features["E(UP) - E(DOWN)"] <= -0.799603:
                            if features["E(RIGHT)"] <= 0.000001:
                                return 2
                            else:
                                if features["E(LEFT) - agent_row"] <= -6.150951:
                                    if features["T(up) - agent_column"] <= -10.395648:
                                        if features["T(DOWN) - agent_column"] <= -11.999778:
                                            return 1
                                        else:
                                            return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(UP) - agent_row"] <= -6.999972:
                                        return 2
                                    else:
                                        if features["E(UP) - agent_column"] <= -3.999993:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.862176:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 2
                        else:
                            if features["E(RIGHT) - time_left"] <= 0.255957:
                                if features["E(DOWN) - T(up)"] <= -0.105415:
                                    if features["T(up) - T(RIGHT)"] <= -0.000023:
                                        if features["T(up) - agent_column"] <= -2.530063:
                                            if features["E(DOWN) - agent_row"] <= -4.641011:
                                                return 2
                                            else:
                                                return 1
                                        else:
                                            return 1
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.195997:
                                            if features["E(RIGHT) - T(up)"] <= -0.562051:
                                                return 2
                                            else:
                                                if features["E(DOWN) - agent_column"] <= -7.770406:
                                                    return 2
                                                else:
                                                    if features["T(DOWN)"] <= 0.000000:
                                                        return 1
                                                    else:
                                                        return 2
                                        else:
                                            return 1
                                else:
                                    if features["T(LEFT) - agent_row"] <= -4.580688:
                                        if features["E(UP) - E(RIGHT)"] <= 0.000000:
                                            return 1
                                        else:
                                            if features["time_left"] <= 0.250000:
                                                if features["E(DOWN)"] <= 0.732860:
                                                    if features["T(DOWN) - T(RIGHT)"] <= 0.207351:
                                                        return 2
                                                    else:
                                                        if features["E(RIGHT)"] <= 0.067784:
                                                            return 2
                                                        else:
                                                            return 1
                                                else:
                                                    if features["E(UP)"] <= 0.000157:
                                                        if features["E(LEFT) - agent_column"] <= -12.208843:
                                                            return 1
                                                        else:
                                                            return 2
                                                    else:
                                                        return 2
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= 0.000928:
                                                    return 2
                                                else:
                                                    if features["E(DOWN) - T(DOWN)"] <= 0.459309:
                                                        return 2
                                                    else:
                                                        return 1
                                    else:
                                        if features["E(RIGHT)"] <= 0.000001:
                                            return 2
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -9.980785:
                                                if features["E(RIGHT) - T(up)"] <= 0.061784:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                if features["T(LEFT) - agent_row"] <= -3.677573:
                                                    if features["T(LEFT) - agent_row"] <= -4.577678:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(DOWN) - E(RIGHT)"] <= 0.081772:
                                                        return 0
                                                    else:
                                                        return 1
                            else:
                                return 0
                    else:
                        if features["E(LEFT) - E(RIGHT)"] <= 0.494603:
                            if features["E(UP) - agent_row"] <= -8.779593:
                                return 1
                            else:
                                return 2
                        else:
                            if features["E(RIGHT) - agent_row"] <= -11.999973:
                                return 2
                            else:
                                if features["E(DOWN) - T(up)"] <= 0.862506:
                                    if features["E(RIGHT)"] <= 0.000002:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(LEFT) - T(RIGHT)"] <= 0.866622:
                                        return 2
                                    else:
                                        return 1
                else:
                    if features["E(UP) - T(up)"] <= 0.168499:
                        if features["E(DOWN) - T(RIGHT)"] <= 0.103343:
                            if features["E(LEFT) - E(RIGHT)"] <= 0.061525:
                                if features["E(DOWN) - T(LEFT)"] <= -0.018927:
                                    return 1
                                else:
                                    if features["T(RIGHT)"] <= 0.248949:
                                        return 2
                                    else:
                                        if features["E(DOWN) - T(RIGHT)"] <= 0.000922:
                                            return 1
                                        else:
                                            return 0
                            else:
                                if features["E(UP) - T(up)"] <= -0.020888:
                                    if features["T(up) - time_left"] <= 0.204150:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    if features["E(LEFT)"] <= 0.355605:
                                        if features["T(RIGHT)"] <= 0.195101:
                                            return 2
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -6.783915:
                                                if features["T(up) - T(DOWN)"] <= 0.069406:
                                                    return 1
                                                else:
                                                    return 0
                                            else:
                                                return 2
                                    else:
                                        return 1
                        else:
                            if features["T(RIGHT)"] <= 0.016216:
                                if features["E(LEFT) - time_left"] <= 0.260151:
                                    if features["E(LEFT) - E(RIGHT)"] <= 0.036809:
                                        return 1
                                    else:
                                        if features["T(DOWN)"] <= 0.000000:
                                            if features["E(RIGHT) - T(up)"] <= -0.550851:
                                                if features["E(RIGHT) - agent_row"] <= -8.872311:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                        else:
                                            if features["E(LEFT) - E(RIGHT)"] <= 0.229108:
                                                if features["E(LEFT) - agent_column"] <= -9.701142:
                                                    if features["E(DOWN) - agent_row"] <= -7.795455:
                                                        if features["T(DOWN) - agent_row"] <= -8.999555:
                                                            return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        return 3
                                                else:
                                                    if features["E(DOWN) - agent_row"] <= -8.752131:
                                                        return 2
                                                    else:
                                                        return 1
                                            else:
                                                if features["E(LEFT) - time_left"] <= -0.016012:
                                                    if features["E(DOWN) - agent_column"] <= -13.770715:
                                                        if features["T(up) - time_left"] <= -0.429975:
                                                            return 0
                                                        else:
                                                            return 2
                                                    else:
                                                        if features["E(DOWN) - T(LEFT)"] <= -0.124131:
                                                            return 2
                                                        else:
                                                            if features["T(LEFT) - time_left"] <= -0.458854:
                                                                return 2
                                                            else:
                                                                if features["T(LEFT)"] <= 0.330312:
                                                                    return 2
                                                                else:
                                                                    if features["T(LEFT) - agent_row"] <= -4.105883:
                                                                        return 1
                                                                    else:
                                                                        return 0
                                                else:
                                                    if features["T(up) - time_left"] <= -0.194642:
                                                        if features["T(up) - T(RIGHT)"] <= 0.000487:
                                                            if features["E(UP) - agent_column"] <= -6.883443:
                                                                return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            if features["E(RIGHT) - T(LEFT)"] <= -0.603136:
                                                                return 2
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["T(up) - agent_column"] <= -7.762075:
                                                            if features["E(RIGHT) - T(LEFT)"] <= -0.358560:
                                                                return 2
                                                            else:
                                                                if features["E(LEFT) - T(LEFT)"] <= 0.039610:
                                                                    if features["E(RIGHT) - T(up)"] <= 0.011557:
                                                                        return 1
                                                                    else:
                                                                        return 3
                                                                else:
                                                                    return 2
                                                        else:
                                                            if features["E(DOWN) - agent_row"] <= -9.757015:
                                                                return 2
                                                            else:
                                                                return 1
                                else:
                                    if features["agent_column - time_left"] <= 13.990000:
                                        if features["agent_column - time_left"] <= 12.950000:
                                            if features["T(RIGHT)"] <= 0.001810:
                                                if features["E(DOWN) - E(LEFT)"] <= 0.000040:
                                                    if features["E(RIGHT) - T(DOWN)"] <= 0.044396:
                                                        if features["T(up) - agent_column"] <= -8.999969:
                                                            if features["T(LEFT) - agent_row"] <= -4.635297:
                                                                return 2
                                                            else:
                                                                if features["E(DOWN) - agent_column"] <= -12.701182:
                                                                    return 1
                                                                else:
                                                                    return 2
                                                        else:
                                                            if features["E(RIGHT) - T(RIGHT)"] <= 0.000000:
                                                                if features["T(DOWN) - agent_column"] <= -2.191103:
                                                                    return 2
                                                                else:
                                                                    return 1
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["T(DOWN) - T(RIGHT)"] <= 0.000007:
                                                            if features["T(LEFT) - agent_column"] <= -8.994036:
                                                                return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            if features["T(up) - agent_row"] <= -6.815083:
                                                                return 2
                                                            else:
                                                                return 1
                                                else:
                                                    return 1
                                            else:
                                                if features["E(RIGHT) - T(DOWN)"] <= -0.381916:
                                                    if features["T(LEFT) - time_left"] <= -0.018569:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 2
                                        else:
                                            if features["T(up) - agent_column"] <= -12.879459:
                                                if features["E(LEFT) - T(DOWN)"] <= 0.015237:
                                                    if features["T(RIGHT)"] <= 0.000000:
                                                        return 1
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(DOWN) - T(DOWN)"] <= 0.008988:
                                                        if features["T(up) - time_left"] <= -0.020000:
                                                            return 2
                                                        else:
                                                            return 1
                                                    else:
                                                        if features["T(RIGHT)"] <= 0.000000:
                                                            if features["E(UP) - agent_row"] <= -12.999851:
                                                                return 2
                                                            else:
                                                                return 1
                                                        else:
                                                            if features["E(RIGHT)"] <= 0.009544:
                                                                return 2
                                                            else:
                                                                return 1
                                            else:
                                                return 2
                                    else:
                                        if features["T(DOWN) - T(LEFT)"] <= -0.270259:
                                            return 1
                                        else:
                                            return 2
                            else:
                                if features["T(up) - T(DOWN)"] <= -0.109723:
                                    if features["E(RIGHT) - time_left"] <= -0.019816:
                                        if features["E(RIGHT) - T(up)"] <= -0.068453:
                                            if features["E(RIGHT) - time_left"] <= -0.071122:
                                                if features["T(DOWN) - agent_column"] <= -9.639960:
                                                    return 2
                                                else:
                                                    return 1
                                            else:
                                                return 1
                                        else:
                                            return 2
                                    else:
                                        if features["E(RIGHT) - T(LEFT)"] <= -0.149059:
                                            if features["E(UP) - T(up)"] <= 0.046832:
                                                return 1
                                            else:
                                                if features["E(UP) - E(RIGHT)"] <= 0.093354:
                                                    return 1
                                                else:
                                                    return 2
                                        else:
                                            return 2
                                else:
                                    if features["E(UP) - agent_column"] <= -9.770080:
                                        if features["E(DOWN)"] <= 0.235970:
                                            return 1
                                        else:
                                            if features["E(UP) - time_left"] <= 0.147039:
                                                if features["T(DOWN) - agent_row"] <= -8.225177:
                                                    if features["agent_column - time_left"] <= 10.870000:
                                                        return 2
                                                    else:
                                                        if features["agent_column"] <= 11.500000:
                                                            return 1
                                                        else:
                                                            return 2
                                                else:
                                                    return 1
                                            else:
                                                return 2
                                    else:
                                        if features["E(DOWN) - agent_row"] <= -7.766846:
                                            if features["E(LEFT) - agent_column"] <= -7.671755:
                                                return 2
                                            else:
                                                if features["T(LEFT) - agent_row"] <= -10.580647:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            if features["E(LEFT) - agent_row"] <= -5.572964:
                                                return 1
                                            else:
                                                return 2
                    else:
                        if features["T(up) - T(RIGHT)"] <= 0.000000:
                            if features["E(LEFT) - time_left"] <= 0.221785:
                                if features["E(UP) - agent_row"] <= -5.752408:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 2
                        else:
                            if features["E(LEFT) - T(RIGHT)"] <= 0.348182:
                                if features["E(RIGHT) - T(LEFT)"] <= -0.535835:
                                    return 2
                                else:
                                    if features["T(up) - agent_row"] <= -7.999994:
                                        return 0
                                    else:
                                        if features["E(DOWN) - T(up)"] <= 0.303021:
                                            if features["E(DOWN) - E(RIGHT)"] <= 0.006151:
                                                return 0
                                            else:
                                                return 3
                                        else:
                                            return 1
                            else:
                                if features["T(LEFT) - time_left"] <= 0.568781:
                                    if features["E(DOWN) - E(RIGHT)"] <= 0.202424:
                                        if features["agent_row - time_left"] <= 7.890000:
                                            if features["E(LEFT) - time_left"] <= 0.317949:
                                                return 3
                                            else:
                                                if features["E(RIGHT) - agent_row"] <= -5.869162:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            return 2
                                    else:
                                        if features["agent_column - time_left"] <= 9.690000:
                                            return 1
                                        else:
                                            return 2
                                else:
                                    return 2
        else:
            if features["E(UP) - E(DOWN)"] <= 0.358045:
                if features["E(LEFT) - T(LEFT)"] <= -0.028506:
                    if features["T(DOWN) - time_left"] <= -0.099090:
                        if features["T(up) - T(LEFT)"] <= -0.000089:
                            if features["E(RIGHT) - agent_row"] <= -7.775919:
                                if features["E(UP) - time_left"] <= 0.241376:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.324992:
                                        return 0
                                    else:
                                        return 3
                                else:
                                    return 0
                            else:
                                if features["E(UP) - time_left"] <= 0.023701:
                                    return 2
                                else:
                                    return 3
                        else:
                            if features["E(UP) - E(DOWN)"] <= 0.267046:
                                return 1
                            else:
                                if features["T(DOWN) - agent_column"] <= -6.999979:
                                    if features["T(RIGHT) - agent_column"] <= -8.998466:
                                        return 2
                                    else:
                                        return 1
                                else:
                                    return 0
                    else:
                        if features["E(DOWN) - agent_row"] <= -8.892519:
                            if features["E(UP) - E(LEFT)"] <= 0.058716:
                                if features["T(up) - T(LEFT)"] <= 0.000079:
                                    return 0
                                else:
                                    return 2
                            else:
                                if features["T(RIGHT) - time_left"] <= -0.139648:
                                    return 2
                                else:
                                    return 0
                        else:
                            if features["T(DOWN) - T(LEFT)"] <= -0.000134:
                                if features["E(LEFT) - time_left"] <= 0.171596:
                                    if features["T(DOWN) - agent_row"] <= -5.380075:
                                        return 3
                                    else:
                                        if features["T(RIGHT) - time_left"] <= -0.159994:
                                            return 3
                                        else:
                                            if features["E(LEFT) - T(DOWN)"] <= 0.158128:
                                                return 0
                                            else:
                                                return 2
                                else:
                                    if features["E(DOWN) - T(LEFT)"] <= -0.439769:
                                        if features["E(DOWN) - agent_column"] <= -5.829616:
                                            if features["E(RIGHT) - T(LEFT)"] <= -0.586823:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            return 3
                                    else:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.215318:
                                            return 0
                                        else:
                                            if features["E(RIGHT) - T(up)"] <= -0.031043:
                                                return 2
                                            else:
                                                if features["T(LEFT) - agent_row"] <= -8.411110:
                                                    return 0
                                                else:
                                                    return 3
                            else:
                                if features["E(DOWN) - time_left"] <= -0.116629:
                                    return 2
                                else:
                                    return 0
                else:
                    if features["E(UP) - E(LEFT)"] <= 0.127855:
                        if features["E(DOWN) - T(DOWN)"] <= 0.014026:
                            if features["T(up)"] <= 0.389861:
                                if features["E(RIGHT) - agent_row"] <= -12.923332:
                                    return 0
                                else:
                                    if features["T(LEFT) - T(RIGHT)"] <= 0.055219:
                                        if features["T(LEFT) - time_left"] <= 0.199228:
                                            if features["T(DOWN) - T(RIGHT)"] <= 0.000563:
                                                if features["E(UP) - T(LEFT)"] <= 0.023075:
                                                    return 1
                                                else:
                                                    if features["T(up)"] <= 0.363266:
                                                        if features["E(DOWN)"] <= 0.002679:
                                                            return 0
                                                        else:
                                                            if features["E(DOWN) - time_left"] <= 0.181042:
                                                                if features["T(up)"] <= 0.000000:
                                                                    return 0
                                                                else:
                                                                    if features["E(DOWN) - time_left"] <= -0.297471:
                                                                        return 0
                                                                    else:
                                                                        return 2
                                                            else:
                                                                return 1
                                                    else:
                                                        if features["E(RIGHT) - time_left"] <= 0.160139:
                                                            return 0
                                                        else:
                                                            return 1
                                            else:
                                                if features["E(UP) - agent_column"] <= -7.637026:
                                                    if features["E(DOWN) - agent_row"] <= -8.908229:
                                                        return 0
                                                    else:
                                                        return 2
                                                else:
                                                    if features["E(RIGHT) - T(RIGHT)"] <= -0.498963:
                                                        return 2
                                                    else:
                                                        return 0
                                        else:
                                            if features["T(LEFT) - T(RIGHT)"] <= 0.054115:
                                                if features["T(LEFT) - agent_row"] <= -10.754976:
                                                    return 1
                                                else:
                                                    return 0
                                            else:
                                                return 1
                                    else:
                                        if features["agent_row - agent_column"] <= -3.500000:
                                            return 3
                                        else:
                                            if features["E(UP) - E(LEFT)"] <= 0.100345:
                                                if features["E(DOWN) - E(RIGHT)"] <= -0.109040:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["E(UP) - T(LEFT)"] <= 0.105909:
                                                    return 0
                                                else:
                                                    return 2
                            else:
                                if features["agent_row - agent_column"] <= -1.500000:
                                    return 3
                                else:
                                    if features["T(up) - T(LEFT)"] <= 0.076077:
                                        return 2
                                    else:
                                        if features["T(RIGHT) - agent_row"] <= -12.902694:
                                            return 2
                                        else:
                                            return 0
                        else:
                            if features["E(UP) - E(RIGHT)"] <= 0.088368:
                                if features["T(DOWN) - T(LEFT)"] <= -0.000000:
                                    if features["T(DOWN) - agent_column"] <= -4.871876:
                                        if features["T(LEFT) - T(RIGHT)"] <= 0.002742:
                                            if features["E(DOWN) - time_left"] <= -0.026289:
                                                return 1
                                            else:
                                                if features["E(DOWN) - T(RIGHT)"] <= -0.423096:
                                                    return 2
                                                else:
                                                    return 1
                                        else:
                                            return 2
                                    else:
                                        if features["T(DOWN) - T(LEFT)"] <= -0.006910:
                                            if features["E(RIGHT) - T(RIGHT)"] <= -0.034166:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            if features["E(RIGHT) - agent_row"] <= -9.798326:
                                                return 3
                                            else:
                                                return 1
                                else:
                                    return 2
                            else:
                                if features["E(DOWN) - time_left"] <= -0.045195:
                                    if features["T(LEFT) - time_left"] <= 0.128500:
                                        if features["T(DOWN) - time_left"] <= -0.219950:
                                            if features["T(RIGHT) - agent_row"] <= -10.575411:
                                                if features["E(UP) - T(LEFT)"] <= 0.305343:
                                                    return 2
                                                else:
                                                    if features["T(RIGHT) - time_left"] <= 0.078551:
                                                        return 0
                                                    else:
                                                        return 2
                                            else:
                                                return 2
                                        else:
                                            return 2
                                    else:
                                        return 3
                                else:
                                    if features["E(UP)"] <= 0.397453:
                                        if features["E(RIGHT) - T(RIGHT)"] <= 0.163726:
                                            if features["E(DOWN)"] <= 0.210282:
                                                if features["T(DOWN)"] <= 0.000000:
                                                    if features["E(DOWN) - E(LEFT)"] <= -0.128862:
                                                        return 2
                                                    else:
                                                        return 1
                                                else:
                                                    return 2
                                            else:
                                                return 1
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -7.858238:
                                                return 2
                                            else:
                                                if features["E(DOWN) - T(up)"] <= -0.532675:
                                                    return 2
                                                else:
                                                    return 1
                                    else:
                                        if features["E(LEFT) - T(LEFT)"] <= 0.312397:
                                            return 0
                                        else:
                                            return 2
                    else:
                        if features["E(UP)"] <= 0.386403:
                            if features["E(UP) - E(LEFT)"] <= 0.242114:
                                if features["E(DOWN) - agent_column"] <= -2.955298:
                                    if features["E(LEFT) - T(LEFT)"] <= 0.007350:
                                        return 1
                                    else:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.194761:
                                            if features["E(RIGHT) - T(LEFT)"] <= 0.129978:
                                                return 2
                                            else:
                                                if features["E(RIGHT) - time_left"] <= 0.188867:
                                                    if features["T(DOWN) - time_left"] <= -0.220000:
                                                        if features["T(DOWN) - agent_column"] <= -8.999925:
                                                            return 3
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["T(DOWN) - T(RIGHT)"] <= 0.000358:
                                                            return 2
                                                        else:
                                                            return 0
                                                else:
                                                    return 0
                                        else:
                                            if features["T(up) - T(LEFT)"] <= 0.207672:
                                                return 2
                                            else:
                                                if features["E(UP) - E(DOWN)"] <= 0.238999:
                                                    if features["T(LEFT)"] <= 0.000000:
                                                        return 2
                                                    else:
                                                        if features["E(UP) - T(up)"] <= -0.165908:
                                                            return 3
                                                        else:
                                                            return 1
                                                else:
                                                    if features["E(LEFT) - agent_column"] <= -9.856555:
                                                        return 3
                                                    else:
                                                        if features["E(LEFT) - T(up)"] <= -0.243433:
                                                            return 0
                                                        else:
                                                            return 2
                                else:
                                    if features["T(LEFT) - time_left"] <= 0.019117:
                                        if features["E(LEFT) - time_left"] <= -0.093709:
                                            if features["E(DOWN) - time_left"] <= -0.416080:
                                                if features["E(RIGHT) - agent_column"] <= -0.796529:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["E(DOWN)"] <= 0.044838:
                                                    return 3
                                                else:
                                                    if features["T(up) - T(RIGHT)"] <= -0.456444:
                                                        return 2
                                                    else:
                                                        return 1
                                        else:
                                            if features["T(DOWN) - agent_row"] <= -10.999998:
                                                return 1
                                            else:
                                                if features["E(RIGHT) - T(LEFT)"] <= 0.309134:
                                                    return 2
                                                else:
                                                    return 0
                                    else:
                                        if features["T(LEFT)"] <= 0.131968:
                                            return 1
                                        else:
                                            return 2
                            else:
                                if features["T(LEFT) - time_left"] <= 0.024269:
                                    if features["E(DOWN)"] <= 0.000019:
                                        return 0
                                    else:
                                        if features["E(UP) - T(up)"] <= -0.013721:
                                            if features["T(LEFT) - agent_row"] <= -11.999998:
                                                if features["E(UP) - agent_column"] <= -1.633924:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["agent_row - time_left"] <= 6.830000:
                                                    return 1
                                                else:
                                                    if features["E(LEFT) - T(DOWN)"] <= 0.041687:
                                                        return 3
                                                    else:
                                                        if features["T(up) - T(RIGHT)"] <= -0.000208:
                                                            return 0
                                                        else:
                                                            return 3
                                        else:
                                            if features["T(DOWN) - agent_column"] <= -1.973265:
                                                if features["T(LEFT)"] <= 0.083267:
                                                    return 0
                                                else:
                                                    return 1
                                            else:
                                                if features["T(DOWN) - agent_column"] <= -1.968152:
                                                    return 3
                                                else:
                                                    return 1
                                else:
                                    if features["T(up)"] <= 0.337878:
                                        return 1
                                    else:
                                        if features["E(UP) - T(LEFT)"] <= 0.270977:
                                            return 1
                                        else:
                                            return 3
                        else:
                            if features["time_left"] <= 0.150000:
                                if features["E(LEFT) - T(LEFT)"] <= 0.052471:
                                    if features["E(RIGHT) - T(RIGHT)"] <= -0.003890:
                                        if features["T(RIGHT) - agent_row"] <= -5.613347:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.229518:
                                            return 0
                                        else:
                                            if features["E(DOWN) - T(LEFT)"] <= -0.016915:
                                                return 1
                                            else:
                                                return 0
                                else:
                                    if features["E(RIGHT) - time_left"] <= 0.159866:
                                        if features["E(RIGHT) - T(up)"] <= -0.156382:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        if features["T(up) - T(RIGHT)"] <= -0.000147:
                                            return 0
                                        else:
                                            if features["T(RIGHT) - agent_column"] <= -3.400140:
                                                return 0
                                            else:
                                                return 3
                            else:
                                if features["E(DOWN) - T(up)"] <= -0.371441:
                                    if features["agent_row - time_left"] <= 6.730000:
                                        if features["T(LEFT) - agent_column"] <= -4.999992:
                                            return 0
                                        else:
                                            return 1
                                    else:
                                        return 0
                                else:
                                    if features["T(up) - T(LEFT)"] <= -0.000098:
                                        return 0
                                    else:
                                        if features["agent_row - time_left"] <= 7.650000:
                                            return 2
                                        else:
                                            return 0
            else:
                if features["E(LEFT) - T(LEFT)"] <= 0.249267:
                    if features["E(RIGHT) - agent_row"] <= -0.626827:
                        if features["E(UP) - time_left"] <= 0.328538:
                            if features["E(DOWN)"] <= 0.000022:
                                if features["T(DOWN) - time_left"] <= -0.819998:
                                    if features["E(UP) - T(RIGHT)"] <= 0.433420:
                                        return 3
                                    else:
                                        return 2
                                else:
                                    if features["T(DOWN)"] <= 0.000000:
                                        if features["E(RIGHT) - T(DOWN)"] <= 0.600410:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 0
                            else:
                                if features["E(LEFT) - E(RIGHT)"] <= 0.308636:
                                    if features["E(RIGHT)"] <= 0.383942:
                                        if features["E(RIGHT) - time_left"] <= 0.036384:
                                            if features["E(RIGHT) - agent_row"] <= -8.736910:
                                                if features["E(RIGHT) - T(DOWN)"] <= 0.281094:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["E(UP) - E(DOWN)"] <= 0.419307:
                                                    if features["E(RIGHT)"] <= 0.133772:
                                                        if features["T(up) - T(LEFT)"] <= -0.519895:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        if features["T(up) - time_left"] <= -0.299837:
                                                            return 2
                                                        else:
                                                            return 3
                                                else:
                                                    return 0
                                        else:
                                            if features["E(RIGHT) - T(LEFT)"] <= 0.345769:
                                                if features["E(RIGHT) - agent_row"] <= -6.701432:
                                                    return 0
                                                else:
                                                    if features["E(RIGHT) - T(up)"] <= -0.134838:
                                                        if features["T(RIGHT) - agent_column"] <= -6.574605:
                                                            return 2
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["T(DOWN) - T(RIGHT)"] <= -0.000287:
                                                            return 2
                                                        else:
                                                            return 0
                                            else:
                                                return 0
                                    else:
                                        if features["T(DOWN) - agent_column"] <= -2.982057:
                                            if features["T(RIGHT) - agent_column"] <= -4.519811:
                                                if features["T(RIGHT) - time_left"] <= -0.639993:
                                                    return 3
                                                else:
                                                    if features["T(up) - agent_column"] <= -11.524956:
                                                        return 0
                                                    else:
                                                        if features["E(UP) - time_left"] <= 0.254480:
                                                            return 3
                                                        else:
                                                            return 0
                                            else:
                                                if features["E(LEFT)"] <= 0.079203:
                                                    return 3
                                                else:
                                                    if features["T(LEFT) - agent_column"] <= -2.970184:
                                                        return 3
                                                    else:
                                                        return 2
                                        else:
                                            if features["T(LEFT)"] <= 0.000003:
                                                return 0
                                            else:
                                                if features["E(UP) - T(up)"] <= 0.005658:
                                                    return 3
                                                else:
                                                    return 0
                                else:
                                    if features["E(RIGHT) - T(LEFT)"] <= -0.404230:
                                        if features["E(RIGHT) - T(DOWN)"] <= -0.000040:
                                            return 0
                                        else:
                                            return 2
                                    else:
                                        if features["T(DOWN) - agent_row"] <= -11.991985:
                                            return 0
                                        else:
                                            if features["E(RIGHT) - agent_row"] <= -8.952281:
                                                return 2
                                            else:
                                                return 0
                        else:
                            if features["E(RIGHT) - T(LEFT)"] <= 0.306159:
                                if features["E(LEFT) - agent_row"] <= -0.574590:
                                    if features["E(RIGHT) - T(DOWN)"] <= 0.663453:
                                        if features["E(LEFT) - T(RIGHT)"] <= 0.662591:
                                            if features["E(DOWN) - T(RIGHT)"] <= 0.000525:
                                                if features["E(LEFT) - T(DOWN)"] <= 0.338666:
                                                    return 0
                                                else:
                                                    if features["E(UP) - E(DOWN)"] <= 0.366262:
                                                        return 2
                                                    else:
                                                        return 0
                                            else:
                                                if features["E(UP)"] <= 0.398835:
                                                    return 2
                                                else:
                                                    return 0
                                        else:
                                            return 0
                                    else:
                                        if features["T(LEFT) - agent_column"] <= -10.338389:
                                            return 0
                                        else:
                                            if features["E(DOWN) - T(DOWN)"] <= -0.000000:
                                                if features["E(LEFT) - E(RIGHT)"] <= -0.799531:
                                                    return 3
                                                else:
                                                    return 0
                                            else:
                                                return 3
                                else:
                                    return 2
                            else:
                                if features["E(UP) - T(DOWN)"] <= 0.799896:
                                    if features["E(DOWN)"] <= 0.000204:
                                        if features["E(LEFT) - agent_row"] <= -13.990661:
                                            return 3
                                        else:
                                            if features["E(DOWN) - E(RIGHT)"] <= -0.799769:
                                                if features["agent_row - agent_column"] <= -3.500000:
                                                    return 0
                                                else:
                                                    if features["E(DOWN) - E(LEFT)"] <= -0.000000:
                                                        return 3
                                                    else:
                                                        if features["E(RIGHT) - T(up)"] <= 0.698183:
                                                            return 3
                                                        else:
                                                            return 0
                                            else:
                                                return 0
                                    else:
                                        if features["E(DOWN) - T(up)"] <= -0.366874:
                                            if features["E(DOWN) - T(up)"] <= -0.374280:
                                                if features["T(DOWN)"] <= 0.000000:
                                                    if features["E(UP) - E(RIGHT)"] <= 0.106516:
                                                        if features["E(DOWN) - agent_row"] <= -12.984591:
                                                            return 0
                                                        else:
                                                            if features["E(DOWN) - agent_column"] <= -2.994879:
                                                                return 0
                                                            else:
                                                                return 3
                                                    else:
                                                        return 0
                                                else:
                                                    if features["E(LEFT) - T(LEFT)"] <= 0.007068:
                                                        if features["agent_row - agent_column"] <= 1.500000:
                                                            return 0
                                                        else:
                                                            return 3
                                                    else:
                                                        return 0
                                            else:
                                                return 3
                                        else:
                                            if features["E(RIGHT) - T(LEFT)"] <= 0.390221:
                                                if features["E(DOWN) - T(RIGHT)"] <= 0.014086:
                                                    return 0
                                                else:
                                                    return 3
                                            else:
                                                if features["T(up) - agent_column"] <= -11.000000:
                                                    return 0
                                                else:
                                                    if features["E(LEFT) - agent_row"] <= -10.928094:
                                                        return 3
                                                    else:
                                                        if features["T(DOWN) - agent_row"] <= -2.341068:
                                                            return 0
                                                        else:
                                                            if features["E(UP) - agent_row"] <= -1.244608:
                                                                return 3
                                                            else:
                                                                return 0
                                else:
                                    if features["E(DOWN) - agent_column"] <= -11.999964:
                                        if features["E(UP) - T(LEFT)"] <= 0.854450:
                                            return 0
                                        else:
                                            return 3
                                    else:
                                        return 3
                    else:
                        if features["E(RIGHT) - agent_column"] <= -11.302425:
                            return 0
                        else:
                            if features["T(up) - T(RIGHT)"] <= -0.642450:
                                return 0
                            else:
                                return 3
                else:
                    if features["E(DOWN) - agent_row"] <= -1.999958:
                        if features["E(DOWN) - T(DOWN)"] <= -0.000000:
                            if features["E(UP) - E(DOWN)"] <= 0.802212:
                                if features["E(DOWN)"] <= 0.000509:
                                    if features["E(DOWN) - time_left"] <= -0.810000:
                                        return 2
                                    else:
                                        return 0
                                else:
                                    if features["E(UP) - time_left"] <= 0.295999:
                                        return 2
                                    else:
                                        return 0
                            else:
                                if features["T(DOWN) - agent_column"] <= -1.949298:
                                    if features["E(UP) - agent_row"] <= -12.131950:
                                        return 2
                                    else:
                                        if features["T(RIGHT) - time_left"] <= 0.287886:
                                            if features["agent_row - agent_column"] <= -5.500000:
                                                if features["T(up) - agent_column"] <= -12.999990:
                                                    return 0
                                                else:
                                                    return 2
                                            else:
                                                if features["E(RIGHT) - agent_row"] <= -1.999994:
                                                    if features["T(RIGHT) - agent_row"] <= -8.974730:
                                                        if features["E(DOWN) - agent_row"] <= -10.999998:
                                                            if features["E(UP) - time_left"] <= 0.747383:
                                                                return 0
                                                            else:
                                                                return 2
                                                        else:
                                                            return 0
                                                    else:
                                                        if features["E(UP) - E(DOWN)"] <= 0.867849:
                                                            if features["E(UP) - E(LEFT)"] <= 0.000111:
                                                                return 0
                                                            else:
                                                                if features["agent_row - agent_column"] <= -4.500000:
                                                                    return 0
                                                                else:
                                                                    return 2
                                                        else:
                                                            return 2
                                                else:
                                                    if features["E(UP) - agent_row"] <= -1.154596:
                                                        return 2
                                                    else:
                                                        return 0
                                        else:
                                            if features["E(DOWN) - agent_column"] <= -5.999998:
                                                if features["T(LEFT) - agent_column"] <= -7.000000:
                                                    return 2
                                                else:
                                                    return 0
                                            else:
                                                return 2
                                else:
                                    if features["E(UP) - agent_column"] <= -1.133485:
                                        return 2
                                    else:
                                        return 0
                        else:
                            if features["E(RIGHT) - agent_column"] <= -7.881203:
                                if features["E(UP) - E(LEFT)"] <= 0.104996:
                                    if features["E(DOWN)"] <= 0.003648:
                                        return 2
                                    else:
                                        if features["agent_row - agent_column"] <= 3.500000:
                                            if features["E(LEFT) - time_left"] <= -0.074329:
                                                return 0
                                            else:
                                                return 2
                                        else:
                                            return 0
                                else:
                                    if features["T(up) - T(RIGHT)"] <= 0.010492:
                                        return 2
                                    else:
                                        return 0
                            else:
                                if features["E(UP) - agent_column"] <= -0.314335:
                                    if features["E(LEFT) - T(DOWN)"] <= 0.767310:
                                        if features["T(up) - T(RIGHT)"] <= -0.004077:
                                            if features["E(UP) - time_left"] <= 0.260444:
                                                return 2
                                            else:
                                                return 0
                                        else:
                                            if features["E(RIGHT) - time_left"] <= -0.040391:
                                                if features["E(DOWN) - T(LEFT)"] <= 0.018340:
                                                    if features["E(RIGHT) - agent_row"] <= -12.980141:
                                                        return 2
                                                    else:
                                                        return 0
                                                else:
                                                    return 2
                                            else:
                                                return 0
                                    else:
                                        if features["T(up) - agent_column"] <= -6.503399:
                                            return 0
                                        else:
                                            if features["E(RIGHT) - agent_column"] <= -1.999994:
                                                return 2
                                            else:
                                                return 0
                                else:
                                    return 0
                    else:
                        if features["E(DOWN) - agent_column"] <= -2.999955:
                            if features["T(RIGHT) - agent_row"] <= -0.999999:
                                if features["E(UP) - E(LEFT)"] <= 0.104198:
                                    return 2
                                else:
                                    return 0
                            else:
                                return 2
                        else:
                            if features["E(DOWN) - agent_row"] <= -0.999999:
                                if features["T(DOWN) - agent_column"] <= -1.996663:
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
