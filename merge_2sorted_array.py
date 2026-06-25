# merge 2 sorted array/list without duplicates

list1 = list(map(int,input('list1 = ').split()))
list2 = list(map(int,input('list2 = ').split()))

# list1 --> [1 1 1 2 4 6 7]   and list2 --> [1 2 3 6 7 8 9 10]  ----> output hoga --> [1 2 4 6 7 3 8 9 10 ]

# brute force solution 

'''def merge(list1,list2):
    result = []
    for i in range(len(list1)):
        if list1[i] not in result:
           result.append(list1[i])

    for i in range(len(list2)):
        if list2[i] not in result:
           result.append(list2[i])
    result.sort()
    return result

print(merge(list1,list2))'''
# time complexity ==> O(n log n)  but space complexity ==> O(n)

# 2n solution 

#   left -->  1 1 1 2 4 6 7       
#  right ---> 1 2 3 6 7 8 9 10 

def merge(list1,list2):
    n = len(list1) 
    m = len(list2) 
    result = []
    i=j=0
    while i<n and j<m:
        if list1[i]<= list2[j]:
            if len(result) == 0 or result[-1] != list1[i]:
                result.append(list1[i])
            i += 1
        else:
            if len(result) == 0 or result[-1] != list2[j]:
                result.append(list2[j])
            j += 1
    
    while i<n:
        if len(result) == 0 or result[-1] != list1[i]:
                result.append(list1[i])
        i += 1
    
    while j<m:
        if len(result) == 0 or result[-1] != list2[j]:
                result.append(list2[j])
        j += 1
    
    return result

print(merge(list1,list2))     # time ==> O(n+m)  space == > O(n+m)