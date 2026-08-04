from math import *
num = int(input("enter a positive number: "))

while num < 0:
    num = int(input("enter a positive number: "))
    


result1 =int(sqrt (num))
result2 = int(num ** 2)
result3 = int(num ** 3)
print ("square root:" , abs(result1))
print ("square:" , abs(result2))
print ("cube:" , abs(result3))


    