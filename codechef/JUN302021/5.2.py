import sys
def short_sub_removed(n,s):
    no_of_ones = 0
    no_of_zeros = 0
    no_of_ones_counted = 0
    ans = sys.maxsize
    for i in s:
        if(i=='0'):
            no_of_zeros+=1
        else:
            no_of_ones+=1
    for i in s:
        if(i=='0'):
            no_of_zeros-=1
        else:
            no_of_ones_counted +=1
        ans = min(no_of_zeros+no_of_ones_counted,ans)
    return ans
    
t = int(input())
for i in range(t):
    N=int(input())
    string=input()
    print(short_sub_removed(N,string))