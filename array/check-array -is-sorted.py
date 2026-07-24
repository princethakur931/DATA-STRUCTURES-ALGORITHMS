# check the given array is sorted or not

''' ------------ EXAMPLE --------------------
arr = [4,5,67,8,10,12,15]   output = True
arr = [5,4,3,8,9]  output = Flase
'''

# write your code here

def isssorted(arr):
    n = len(arr)
    if n < 2:
        return True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

# time complexity : O(n)  sapce : o(1)

print(isssorted(list(map(int,input('enter nums= ').split()))))