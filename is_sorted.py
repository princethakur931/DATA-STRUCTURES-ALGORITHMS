# question 1: check if an array is sorted or not

arr = list(map(int,input('Enter numbers: ').split()))

'''
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(is_sorted(arr))


Worst case me poora array traverse hoga.

Time Complexity: O(n) ✅
Space Complexity: O(1) ✅ '''

# question 2. Check if Array is Strictly Sorted
# Equal elements allowed nahi.
# example : [1, 2, 2, 3]  ----->  Output: False

'''
def is_strictly_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            return False
    return True

print(is_strictly_sorted(arr))                    '''

# question 3. Check if Array is Sorted in Descending Order
# Example : [9, 7, 5, 2]      ---->      Output: True

'''def is_desc(arr):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            return False
    return True

print(is_desc(arr))         '''

# question 4. Check if Array is Sorted Either Ascending or Descending

'''def is_asc_or_desc(arr):
    n = len(arr)
    if n<=1:
        return 'array is sorted in both orde asc & desc'
    elif arr[0]>arr[1]:
        for i in range(2,n-1):
            if arr[i]<arr[i+1]:
                return 'not sorted'
        return 'sorted in desc!!'
    elif arr[0]<arr[1]:
        for i in range(2,n-1):
            if arr[i]>arr[i+1]:
                return 'not sorted'
        return 'sorted in asc!!'        


print(is_asc_or_desc(arr))    '''

# question 5. Find First Index Where Sorting Breaks
# Example : [1,2,7,4,5] ----> Output: 2    ----> Because: 7 > 4

'''def index_sortingbreak(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return i
    return 'array is sorted'

print(index_sortingbreak(arr))'''

# question 6. Count Number of Violations
# Example : [1,5,3,8,6] ----> Violations: 5 > 3 , 8 > 6  ---> Output: 2

'''def sort_violation(arr):
    violation = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            violation += 1
    return violation

print(sort_violation(arr))'''

