# Write a Python program that takes a person's height (in meters) 
# and weight (in kilograms) as input and calculates their Body Mass Index (BMI).
# Print out their BMI and a message indicating whether they are underweight (<18.5), normal (18.5-24.9), 
# overweight (25-29.9), or obese (>=30). 
weight=float(input("enter your weight in kg!"))
height=float(input("enter your height in meter "))
bmi=weight/(height**2)
if bmi<18.5:
    print("under weight")
elif bmi>=18.5 and bmi<=24.9:
    print("normal")
elif bmi>=25 and bmi<=29.9:
    print("overweight")
else:
    print("obese")
