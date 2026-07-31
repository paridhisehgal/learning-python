word = input( "Enter a word: ")
number = int(input("Enter a number: "))
result = ""

for i in range (number):
    if i == 0:
        result += word
    else:
        result += f' {word}'

print("result is: " + result)