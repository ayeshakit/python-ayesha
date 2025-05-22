# 2. Armstrong Number Checker:
# Write a Python program that takes an integer input from the user and checks if it is an Armstrong number 
# (a number that is equal to the sum of its own digits raised to the power of the number of digits) using a for loop. 
number=int(input("enter the number please!"))
n=len(str(number))
org_num=number

sum=0
while number>0:
    digit=number%10
    sum=sum+digit**n
    number=number//10
  

if sum==org_num:
    print("Armstrong")
else:
    print("not Armstrong")

