# Temperature Converter: Write a Python program that takes a temperature
# input in Celsius and converts it to Fahrenheit if the temperature is above 0°C,
# or to Kelvin if the temperature is below 0°C.

n=int(input("enter temperature please!!"))
if n>0:
    f=((9*n)/5)+32
    print("temperature in Fahrenheit",f)
else:
    kelvin = n + 273.15
    print("temperature in kelvin",kelvin)
