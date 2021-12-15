def sansaXor(arr):
    n = len(arr)
    result = 0
    for i in range(len(arr)):
        for _ in range(arr[i] * (i+1) * (n-i)):
            result ^= arr[i]
            print(result)


sansaXor([98, 74, 12])
