def cons(nums):
    count = 0
    result = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            if count > result:
                result = count
            count = 0
    if count > result:
        result = count
    return result

nums = list(map(int,input().split()))

print(cons(nums))