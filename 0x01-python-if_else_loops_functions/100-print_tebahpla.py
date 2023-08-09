#!/usr/bin/python3

for char in range(122, 96, -1):
    print(chr(char).upper() if char % 2 == 0 else chr(char).lower(), end="")
