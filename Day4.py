def Weird(num):
    if num % 2!=0:
        print("Weird")
    else:
        if num<=5 & num>=2:
            print("Not Weird")
        elif num<=20 & num>=6:
            print("Weird")
        else:
            print("Not Weird")

num=int(input())
Weird(num)
