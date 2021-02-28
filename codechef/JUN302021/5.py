def short_sub_removed(n,s):
    lis = [1]*n
    for i in range (1 , n): 
        for j in range(0 , i): 
            if s[i] >= s[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
    return n-max(lis)
    # i=1
    # j=0
    # while(j<n and i<n):
    #     if(s[i]==s[j]):
    #         result_arr[j]+=1
    #     if(i==j):
    #         j=0
    #         i+=1
    #     j+=1
    # print(result_arr)
    # print(max(result_arr))
t = int(input())
for i in range(t):
    N=int(input())
    string=input()
    print(short_sub_removed(N,string))