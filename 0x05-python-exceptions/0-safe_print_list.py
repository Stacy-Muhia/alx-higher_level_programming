#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    element = 0

    for y in range(x):

        try:
            print("{}".format(my_list[y]), end="")
            element += 1
        except IndexError:
            break

    print("")
    return element
