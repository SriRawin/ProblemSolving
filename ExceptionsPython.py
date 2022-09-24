import math
import os
import random
import re
import sys


def strORint(input_str):
    try:
        int(input_str)
        print(input_str)
    except ValueError:
        print("Bad String")


if __name__ == '__main__':
    S = input()
    strORint(S)
