# question 1. remove duplicate element from an array

arr = list(map(int,input('List = ').split()))
k = int(input('k = '))

def remove_duplicate(arr):
    n = len(arr)
    if n<=1:
        return arr
    l=0
    r=1
    while r<n:
        if arr[l] != arr[r]:
            l += 1
            arr[l],arr[r] = arr[r],arr[l]
        r += 1
    return arr[:l+1]

print(remove_duplicate(arr))

# question 2.right rotate of an array from one place 

# approach 1. BRUTE / BETTER

def right_rotate(arr):
    n = len(arr)
    arr[:] = arr[n-1:] + arr[:n-1]
    return

# approach 2.optimal way 

def right_rotate(arr):
    n=len(arr)
    temp = arr[n-1]
    for i in range(n-2,-1,-1):           
        arr[i+1] = arr[i]
    arr[0]=temp
    return

right_rotate(arr)
print(arr)


# question 3. right rotate of array from k position

''' index      0 1 2 3 4
     data      1 2 3 4 5
    rotate     5 1 2 3 4    1st rotation    len=5   to yadi 5 ka multiple ayya to humne wahi pehla array wapass milega 
    k=10 baar rotate krne se accha modulo nikal kr utna baar rotate krege  '''

def k_rotation(arr,k):
    n = len(arr)
    rotation = k % n
    for _ in range(rotation):         
        last = arr.pop()
        arr.insert(0,last)
    return 
    
'''TIME COMPLEXITY : to humara loop kitne baar chalega? ---->  jitna rotation hoga means O(r)   pop()---> O(1)  insert() ----> O(n)
    Overall time complexity ====> O(r * n)
'''

def k_rotation(arr,k):
    n = len(arr)
    rotation = k % n
    arr[:] = arr[n-rotation:] + arr[:n-rotation]
    return 
    
k_rotation(arr,k)   
# time complexity ==> slicing ho rha hai ---> O(R) + O(N-R) ===> overall time complexity ==> O(N)  Space Complexity ===> O(1)

def reverse(arr,left,right):
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1

n = len(arr)
rotation =  k % n
reverse(arr,n-rotation,n-1)
reverse(arr,0,n-rotation-1)
reverse(arr,0,n-1)
print('Output =',arr)