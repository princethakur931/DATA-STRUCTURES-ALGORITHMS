'''
------------------ LOWER BOUND ----------------------------

LOWER BOUND MEANS THE INDEX OF FIRST ELEMENT OF SORTED ARRAY THAT IS GREATER THEN OR EQUAL (>=) TO TARGET VALUE.   VALUE >= TARGET
EXAMPLE : NUMS = [2,3,4,5,6,7]   TARGET=5    OUTPUT=3

DRY RUN:   VALUES: 2 3 4 5 6 7         2>=5 NO | 3>=5 NO | 4>=5 NO | 5>=5 YES --> INDEX:3 JO KI OUTPUT HAI 
           INDEX:  0 1 2 3 4 5      

NOTE: LOWER BOUND YE BINARY SEARCH KA EK CONCEPT HAI JO SIRF SORTED ARRAY PE HE KAAM KRTA HAI.
'''

def LowerBound(nums,target):
    low = 0
    high = len(nums) - 1

    while low<=high:
        mid = (low+high) // 2
        if nums[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1
    return low 

print(LowerBound(list(map(int,input('NUMS = ').split())),int(input('target = '))))

'''
------------------ UPPER BOUND ----------------------------

UPPER BOUND MEANS THE INDEX OF FIRST ELEMENT OF SORTED ARRAY THAT IS STRICTLY GREATER THEN (>) TARGET VALUE.   VALUE > TARGET
EXAMPLE : NUMS = [2,3,5,5,5,7]   TARGET=5    OUTPUT=5

DRY RUN:   VALUES: 2 3 5 5 5 7         2>5 NO | 3>5 NO | 5>5 NO | 5>5 NO | 5>5 NO | 7>5 YES --> INDEX:5 JO KI OUTPUT HAI 
           INDEX:  0 1 2 3 4 5      

NOTE: UPPER BOUND YE BINARY SEARCH KA EK CONCEPT HAI JO SIRF SORTED ARRAY PE HE KAAM KRTA HAI.
'''

def UpperBound(nums,target):
    low = 0
    high = len(nums) - 1

    while low<=high:
        mid = (low+high) // 2
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low 

# print(UpperBound(list(map(int,input('NUMS = ').split())),int(input('target = '))))