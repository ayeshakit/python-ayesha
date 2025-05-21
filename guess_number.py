# Guess the Number Game (while loop):
# Consider a random number between 1 and 10. 
# Let user guess until correct. Give hints: “Too high” or “Too low”.


random_num=7
attempt=4
while attempt>0:
 user_input=int(input("guess the number"))
 if user_input==random_num:
    print("Great!! You won!")
    break
 elif user_input<random_num:
        print("Too low")
        attempt=attempt-1
 else:
        print("Too high")
        attempt=attempt-1
if attempt==0:
     print("sorry")
    