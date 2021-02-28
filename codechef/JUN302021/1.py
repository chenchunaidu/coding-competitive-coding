def checkIsPair(a,b,c):
    if((a+b==c)or(b+c==a) or (c+a)==b):
        return "YES"
    return "NO"
t = int(input())
for i in range(t):
    a,b,c = list(map(int,input().split()))
    print(checkIsPair(a,b,c))
