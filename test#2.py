t=True

while t==True:
    print("Enter a Number to be Squared")
    again=True
    while again==True:
        num1=float(input("num1 "))
        if(num1>0):
            again=False
            continue
        if(num1==0.0):
            again=False
            continue
    if(num1>0):
        print(str(num1)+"**2="+str(num1**2))
        quit=input("quit??? ")
        if(quit=="y"):
           t=False
           continue
    elif(num1==0):
           t=False
           continue
