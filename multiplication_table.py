num = int(input("Enter a number -> "))
range_limit = int(input("Enter another number -> "))
print("The multiplication table for" , num ,"upto", range_limit ,"is: ")

for n in range (1, range_limit+1):
    print( num , "*" , n ,"=",num * n)




