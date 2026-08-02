rad = float(input("Enter radius of a circle: "))

from math import*
circumference = 2 * pi * rad
area = pi * pow(rad,2)
result1= round(circumference,10)
result2 = round(area,50)


print("Circumference:", result1)
print("Area:", result2)