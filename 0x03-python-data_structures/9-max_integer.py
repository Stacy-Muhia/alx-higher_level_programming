#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    huge = my_list[0]
    for i in range(1, len(my_list)):
        if huge < my_list[i]:
            huge = my_list[i]
        else:
            continue
    return huge
