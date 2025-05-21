# Write a Python program that takes a person's age as input and prints out whether 
# they are an infant (0-1),
# toddler (2-3), child (4-12), teenager (13-19), adult (20+). 

age=int(input("How old are you?"))
if age>=0 and age<=1:
    print("infant")
elif age>=2 and age<=3:
    print("toddler")
elif age>=4 and age<=12:
    print("child")
elif age>=13 and age<=19:
    print("teenager")
else:
    print("adult")
