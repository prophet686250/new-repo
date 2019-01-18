def plusminus(array):
    pos=neg=zero=0.0
    for i in array:
        if i<0:
            neg=neg+1
        elif i>0:
            pos=pos+1
        else:
            zero=zero+1
    print(round(pos/len(array),6))
    print(round(neg/len(array),6))
    print(round(zero/len(array),6))

n=input()
array=[int(x) for x in input().split()]
plusminus(array)
