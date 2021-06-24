#!/usr/bin/python3
# returns weighted average of all int tuple


def weight_average(my_list=[]):
    """returns the weighted average of all int tuple"""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    sw = 0
    w = 0
    for tupl in my_list:
        # score is tupl[0] and weight it tupl[1]
        sw += (tupl[0] * tupl[1])
        w += tupl[1]
    return (sw / w)
