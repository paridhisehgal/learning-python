
num_list = []
for i in range(1,11):
    num = float(input("Enter a number -> "))
    num_list.append(num)

print("\n", num_list)

positives = 0
negatives = 0
zeroes = 0

for i in num_list:
    if i > 0 :
     positives += 1

    elif i < 0:
     negatives += 1

    else:
        zeroes += 1

print ("\nThe list contains:" ,"\n","positive numbers =" ,positives, "\n", "negative numbers =", negatives, "\n", "number 0 = ", zeroes)

from math import* 
for i in num_list :
    floor_value = floor(i)
    ceil_value = ceil(i)
    absolute_value = (abs(i))

    print("\nNumber","[",i,"]")
    print("↪ absolute value =", absolute_value)
    print("↪ ceil value =", ceil_value)
    print("↪ floor value =", floor_value)
    












     






    

