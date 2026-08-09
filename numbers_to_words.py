word_list = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
             "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]

while True:
    num = input("Enter a number between 1 to 19 (or enter 'quit' to stop): ")
    if num == "quit":
     break

    number = int(num)
    word = word_list[number]
    print(number, "->", word)
