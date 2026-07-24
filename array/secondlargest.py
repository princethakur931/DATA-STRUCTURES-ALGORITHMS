# find the second largest element of an array

''' --------------- EXAMPLE -------------
arr = [1,2,4,7,7,5]
output = 5
'''

# write your code here

def secondlargest(nums):
    n = len(nums)
    if n<=1:
        return 0
    max1 = float('-inf')
    max2 = float('-inf')
    for i in range(n):
        if nums[i] > max1:
            max2 = max1
            max1 = nums[i]
        elif nums[i] > max2 and nums[i] != max1:
            max2 = nums[i]

    return max2

# time complexity  : o(n)    space : o(1)

print(secondlargest(list(map(int,input('enter nums= ').split()))))