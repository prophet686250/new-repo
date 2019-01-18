n=int(input())
arr=list(map(int, input().strip().split()))
print(*reversed(arr))

# OR
#print(' '.join(map(str, reversed(arr))))
"""where join() takes a seperator as an arguement and joins the elements
of array in reversed() order which have been already mapped by the map() function"""
