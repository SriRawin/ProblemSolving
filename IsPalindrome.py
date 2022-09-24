import re


def isPalindrome(s: str):
    print(s[::-1])
    result_str = ""
    for char in s:
        if char.isalnum():
            result_str += char.lower()
    for i in range(len(result_str)//2):
        if result_str[i] != result_str[-1-i]:
            print(False)
            return

    print(True)


s = "race a car"
isPalindrome(s)
