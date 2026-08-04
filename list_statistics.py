from math import *

number = []

for n in range(0, 8):
    num = float(input("enter a number > "))
    number.append(num)

print("Your entered the number:", number)
print("↪ The biggest number:", max(number))
print("↪ The lowest number:", min(number))
print("↪ The sum of all 8 numbers:", sum(number))
print("↪ The average of all 8 numbers:", sum(number)/8)
print("↪ The ascending order of the list:", sorted(number))


     
    


    