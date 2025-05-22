# Number Reverser: 
# Write a Python program that takes an integer input from the user and prints its reverse using a while loop.
user_input=int(input("enter the number"))
rev_num=0
while user_input>0:
    digit=user_input%10
    rev_num=rev_num*10+digit
    user_input=user_input//10

print("Reverse number is =",rev_num)



