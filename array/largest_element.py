# find the largest element of an array

''' ----------------- EXAMPLE ------------------
arr = [4,5,8,12,1,3,9]
output = 12
'''

# write the code here 

def largest(nums):
    n = len(nums)
    if n==0:
        return n
    max = float('-inf')
    for i in range(n):
        if nums[i] > max:
            max = nums[i]
    return max

# time complexity  : o(n)    space : o(1)

print(largest(list(map(int,input('enter nums= ').split()))))