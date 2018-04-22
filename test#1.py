t=True

while t==True:
    num1=float(input("num1 "))
    num2=float(input("num2 "))
    typeofop=input("what kind of operation??? +,-,*,/ ")
    if  typeofop=="+":
       print(str(num1)+" + "+str(num2)+" = "+str(num1+num2))
    elif  typeofop=="-":
        print(str(num1)+" - "+str(num2)+" = "+str(num1-num2))
    elif  typeofop=="*":
        print(str(num1)+" * "+str(num2)+" = "+str(num1*num2))
    elif  typeofop=="/":
        print(str(num1)+" / "+str(num2)+" = "+str(num1/num2))

    quit=input("quit??? ")
    if(quit=="y"):
      t=False
      continue
