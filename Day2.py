def aVeryLargeSum(array):
    for i in array:
        Sum+=i
    return Sum

n=int(input())
arr=[n for n in input().split()]
print(aVeryLargeSum(arr))
