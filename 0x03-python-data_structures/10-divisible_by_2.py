#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = []
    for x in my_list:
        if x % 2 == 0:
            list2.append(True)
        else:
            list2.append(False)
        return list2
