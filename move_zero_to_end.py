# question 1. moves all zeros of an numsay in the last of an numsay 

# example : [1,0,2,4,0,3,0,0,8,7]  ====> [1,2,4,3,8,7,0,0,0,0]

''' edge casse: len=1 return nums  else: left = 0 ---> right = 1
while right < n : ---> nums[right] != 0 ----> milgya to fir left += 1 and then left or right ko swap krege ---> 
nums[left],nums[right] = nums[right],nums[left] ---> right += 1

dry run  ===> 1 0 2 4 0 3 0 0 8 7 ==> 1 2 0 4 0 3 0 0 8 7 ==> 1 2 4 3 8 7 0 0 0 0

dry run ==> 0 1 2 0 ==> 1 2 0 0 
'''
# Approach 1 

def move_zero(nums):
    n = len(nums)
    if n<=1:
        return 
    left=right=0
    while right<n:
        if nums[right] != 0:
            nums[left],nums[right]=nums[right],nums[left]
            left += 1
        right += 1

# time complexity ==> loop jo hai wo O(N) times execute ho rha hai then overall tc O(N)  space ==> O(1)

# Approach 2nd   ==> [0,1,2,3,4] ==> len = 5  ==> [1,2,3,4]  ==> len = 4 ==> 5-4

def move_zero(nums):
    n = len(nums)
    list = []
    for i in range(n):
        if nums[i] != 0:
            list.append(nums[i])
    
    for i in range(len(list)):
        nums[i]=list[i]
    
    for i in range(len(list),n):
        nums[i] = 0


nums = list(map(int,input('list = ').split()))
move_zero(nums)
print(nums)

# tc ==> O(N)   and sc ===> O(N) bcz here we use a extra list 