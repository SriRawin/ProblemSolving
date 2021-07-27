
def sockMerchant(n, ar):
    pair=0
    for k in range (0,len(ar)):
        for i in range(0 , len(ar)):
            for j in range(i+1,len(ar)):
                if ar[i]==ar[j]:
                     pair=pair+1
                     del ar[i]
                     del ar[j-1]
                     break
    print(pair)

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
