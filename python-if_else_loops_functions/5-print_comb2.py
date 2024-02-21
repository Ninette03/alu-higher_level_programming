#!/usr/bin/python3
numbers = ''.join("{:02d}, ".format(i) if i < 99 else "{:02d}".format(i) for i in range(100))

print(numbers)
