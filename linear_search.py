# cod efor linear searching algorithm 

def linear_search(nums,target):
    length = len(nums)
    for i in range(length):
        if nums[i] == target:
            return True
    return False

nums = list(map(int,input('list = ').split()))
target=int(input('target = '))
print(linear_search(nums,target))