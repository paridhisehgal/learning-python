from math import*

side_a = int(input("Enter 1st shorter side 'a': "))
side_b = int(input("Enter 2nd shorter side 'b': "))
side_c = sqrt(pow(side_a, 2 )+ pow(side_b,2))
result = round(side_c ,4)

print  ("The hypotenuse will be:",result)