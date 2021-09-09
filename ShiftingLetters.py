from typing import List
import re


class Solution:
    def shiftingLetters(s: str, shifts: List[int]):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        result = ""
        for i in range(len(shifts)):
            str_index = (alphabets.index(s[i])+sum(shifts[i:len(shifts)])) % 26
            result += alphabets[str_index]
        return result
    result = shiftingLetters(s="ruu", shifts=[26, 9, 17])
    print(result)
