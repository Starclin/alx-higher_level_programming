#!/usr/bin/python3
for num in range(10):
    for nums in range(10):
        print("{}{}, ".format(num, nums), end="")
        if num == 9 and nums == 9:
            print("{}\n".format("")) 
