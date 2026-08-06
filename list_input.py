numbers_list =[]

for x in range (0,5):
    num = int(input("\nEnter a number -> "))
    numbers_list.append(num)

print ("\n",numbers_list)
print("\nThe above list in reverse order will be:","\n",numbers_list[::-1])