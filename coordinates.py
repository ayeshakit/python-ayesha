# Write a Python program that takes the coordinates (x, y)
# of a point as input and prints out which quadrant it belongs to (1st, 2nd, 3rd, or
# 4th).
x=int(input("value for x"))
y=int(input("value for y"))
if (x>0 and y>0):
    print("first quadrant")
elif(x<0 and y<0):
    print("3rd quadrant")
elif(x>0 and y<0):
    print("4th quadrant")
elif (x == 0 and y == 0):
    print("The point is at the origin")
elif x == 0:
    print("The point is on the Y-axis")
elif y == 0:
    print("The point is on the X-axis")
else:
    print("2nd quadrant")