word = input("enter a word >")
word_reverse = word[::-1]

if word == word_reverse:
    print("The word", word, "is a palindrome!")
else:
    print ("The word", word, "is not a palindrome!")
