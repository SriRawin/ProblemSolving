digits = [4, 3, 2, 1]
digit = [str(i) for i in digits]
num = ''.join(digit)
result = 1+int(num)
ans = [int(char) for char in str(result)]
print(ans)
