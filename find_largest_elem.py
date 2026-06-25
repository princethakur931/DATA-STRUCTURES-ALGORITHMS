# find the third largest element from an array

l = list(map(int,input('list = ').split()))

def third_largest(list):
    n = len(list)
    first=second=third=float('-inf')
    for i in range(n):
        if list[i]>first:
            third = second
            second = first
            first = list[i]

        if first>list[i]>second:
            third = second
            second = list[i]

        if second>list[i]>third:
            third = list[i]

    return third

print(third_largest(l))