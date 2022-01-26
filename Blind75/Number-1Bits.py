def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n &= (n-1)
        count += 1
    return count


n = 0b00000000000000000000000000001011
result = hammingWeight(n)
print(result)
