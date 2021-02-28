import math

def get_max_value(X,N):
    return math.floor(X**(1/N))
def get_power_sum(list_of_countable_nums,_sum,X,N,i):
    if(_sum==X):
        return 1
    elif(_sum>X or i>=len(list_of_countable_nums)):
        return 0
    return get_power_sum(list_of_countable_nums,_sum+(list_of_countable_nums[i]**N),X,N,i+1)+get_power_sum(list_of_countable_nums,_sum,X,N,i+1)

X = int(input())
N = int(input())
list_of_countable_nums = range(get_max_value(X,N)+1)
_sum = 0
i=0
print(get_power_sum(list_of_countable_nums,_sum,X,N,i)//2)