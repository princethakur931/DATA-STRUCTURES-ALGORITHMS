def binary(nums,target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print(binary(list(map(int,input('Nums = ').split())),int(input('target = '))))

'''  
------------------ BINARY SEARCH STEPS -----------------------

1. SET LOW AND HIGH POINTER ==> LOW = 0 , HIGH = len(nums) - 1

2. FIND MID VALUE ==> MID = (LOW + HIGH) // 2

3. COMPARE NUMS[MID] WITH TARGET VALUE:

   CASE 1: NUMS[MID] == TARGET : RETURN MID
   CASE 2: NUMS[MID] < TARGET : LOW = MID + 1
   CASE 3: NUMS[MID] > TARGET : HIGH = MID - 1

4. IF TARGET IS NOT IN A LIST THEN  ( RETURN -1 )

NOTES : IT'S ONLY WORK WHEN LIST/ARRAY IS SORTED. IT IS NOT WORK ON UNSORTED ARRAY OR A LIST....

TIME COMPLEXITY : O(log n)
SPACE COMPLEXITY: O(1)

'''