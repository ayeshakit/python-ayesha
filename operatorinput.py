num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
in_operator=input("enter the operator")
if in_operator=="+":
    res=num1+num2
    print(res)
elif in_operator=="*":
    res=num1*num2
    print(res)
elif in_operator=="-":
    res=num1-num2
    print(res)
else:
    res=num1/num2
    if num2==0:
        print("give a valid number")
    else:
        res=num1/num2
        print(res)
