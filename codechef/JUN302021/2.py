def get_no_of_changes(n,arr):
    no_of_even = 0
    no_of_odd = 0
    for i in arr:
        if(i%2==0):
            no_of_even+=1
        else:
            no_of_odd+=1
    return n-max(no_of_even,no_of_odd)

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(get_no_of_changes(n,arr))