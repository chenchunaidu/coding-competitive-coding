t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr_sum = sum(arr)
    if(arr_sum%2==0):
        print(1)
    else:
        print(2)