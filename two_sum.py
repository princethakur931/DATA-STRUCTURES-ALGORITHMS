nums = [2,5,5,11]
target = 10
n = len(nums)
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i] + nums[j] == target:
            print([i,j])