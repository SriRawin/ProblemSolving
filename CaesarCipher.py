import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    k=k if k <=26 else k%26
    encrypted_cipher=""
    original_alphabet = "abcdefghijklmnopqrstuvwxyz"
    original_alphabet_list = list(original_alphabet)
    rotated_alphabet_list = original_alphabet_list[k:]+original_alphabet_list[:k]
    for char in s:
        index=original_alphabet_list.index(char) if char in original_alphabet else None
        if char.isupper():
            temp=char.lower()
            index=original_alphabet_list.index(temp)
            encrypted_cipher+=rotated_alphabet_list[index].upper()
        elif char.islower():
            encrypted_cipher+=rotated_alphabet_list[index]
        else:
            encrypted_cipher+=char
    return encrypted_cipher

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
