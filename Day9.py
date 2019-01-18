n=int(input())
d={}
for i in range(n):
    text=input().split()
    d[text[0]]=text[1]
flag=1
while flag:
    line=input()
    if d.get(line)==None:
        print("Not found")
    else:
        print(line,end='')
        print('=', end='')
        print(d.get(line))
        
#this code runs for infinity. find a solution so that it stops working after user stops entering input
