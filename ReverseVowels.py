def reverseVowels(s: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    n = len(s)
    l = 0
    r = n-1
    s = [char for char in s]
    while(l <= r):
        while(s[l] not in vowels and l < r):
            l += 1
        while(s[r] not in vowels and l < r):
            r -= 1
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    print("".join(s))


s = "hello"
reverseVowels(s)
