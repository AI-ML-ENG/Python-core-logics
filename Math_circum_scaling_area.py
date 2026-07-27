import math
while True:
    action=input("enter what you want to check")
    if action=="area":
        r=float(input("enter the radius"))
        A=math.pi*r**2
        print(A)
    elif action=="circumference":
        r=float(input("enter the radius"))
        C=2*math.pi*r
        print(C)
    elif action == "scaling":
        r=float(input("enter how many times you want to scale"))
        n=int(input("enter the dimension"))
        s=math.pow(r,n)
        print(s)
    elif action == "":
        action=input("enter something you want to know")
    elif action == "exit":
        break

