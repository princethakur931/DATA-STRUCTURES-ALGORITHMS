# find the missing number in an array 

nums = list(map(int,input('nums = ').split()))

'''def missing_value(nums):
    n = len(nums)
    arrsum = 0
    for i in range(n):
        arrsum += nums[i]
    
    totalsum = (n * (n + 1)) // 2
    return totalsum - arrsum'''

# time ==>  o(N)   SPACE ==> O(1)


'''def missing_value(nums):
    n = len(nums)
    dic = {i:0 for i in range(n+1)}
    for i in nums:
        dic[i] = 1
    for i in dic:
        if dic[i] == 0:
            return i'''
# time ==> o(n)   space==> o(n)

'''def missing_value(nums):
    n = len(nums)
    xor1 =  0
    xor2 = 1
    for i in range(n+1):
        xor1 ^= i

    for i in nums:
        xor2 ^= i

    return xor1 ^ xor2
        
print(missing_value(nums))'''


# find missing values in sorted array   [0,1,2,4,5,6,7] ==> 3

'''def missing(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i+1] - nums[i] != 1:
            return nums[i] + 1'''


# find all missing numbers   e.g., arr = [4,3,2,7,8,2,3,1]  ==> [5,6]

def missing(nums):
    n = len(nums)
    d = {}
    for i in range(1,n+1):
        d[i] = 0

    for i in nums:
        d[i] = d.get(i,0) + 1
    
    for k in d.copy().keys():
        if d[k] != 0:
            del(d[k])
    return list(d)

print(missing(nums))

