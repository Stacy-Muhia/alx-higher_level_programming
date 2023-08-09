#!/usr/bin/python3
def uppercase(str):
    for upc in str:
        if ord(upc) >= 97 and ord(upc) <= 122:
            upc = chr(ord(upc) - 32)
        print("{:s}".format(upc), end='')

    print('\n', end="")
