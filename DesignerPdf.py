import math
import os
import random
import re
import sys


def designerPdfViewer(h, word):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets_dict = {alphabets[i]: h[i] for i in range(26)}
    length = len(word)
    highest = 0
    for char in word:
        highest = alphabets_dict[char] if alphabets_dict[char] > highest else highest
    return highest*length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
