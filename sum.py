# Write a Python program that takes an integer input from the user 
# and calculates the sum of its digits using a while loop.
num=int(input("enter the number"))
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num=num//10
print("the sum of digits",sum)
