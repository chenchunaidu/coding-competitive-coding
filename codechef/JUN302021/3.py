import math
def is_valid(N,K,arr):
    no_of_ones = 0
    no_of_neg_ones = 0
    time = 0
    too_slow = False
    for i in arr:
        if(i==-1):
            no_of_neg_ones+=1
        if(i<=1 and i!=-1):
            no_of_ones+=1
        if(i>K):
            too_slow=True
    if(N-no_of_neg_ones<(math.ceil(N/2))):
        print("Rejected")
    elif(too_slow):
        print("Too Slow")
    elif(no_of_ones==N):
        print("Bot")
    else:
        print("Accepted")
    
        

t =  int(input())
for i in range(t):
    N,K = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    is_valid(N,K,arr)
    