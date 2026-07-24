
# brute force approach
'''def maxsum(nums):
    maxi = float('-inf')
    for i in range(len(nums)):
        total = 0
        for j in range(i,len(nums)):
            total += nums[j]
            maxi = max(total,maxi)
    return maxi
'''

# optimal approach - kadanes algorithm 
def maxsum(nums):
    maxi = float('-inf')
    total = 0
    for num in nums:
        total += num
        maxi = max(maxi,total)
        if total < 0:
            total = 0
    return maxi

print(maxsum(list(map(int,input('enter:').split()))))