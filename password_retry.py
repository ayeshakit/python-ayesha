# Password Retry System (while loop) :
# Predefined password. 
# Let user try until correct or after 3 failed attempts show "Account locked" 

password="ayesha"
attempt=3
while attempt>0:
 user_input=input("enter your password")
 if user_input==password:
    print("login suncessful")
    break
 else:
    print("failed")
    attempt=attempt-1