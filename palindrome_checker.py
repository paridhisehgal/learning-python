word = input("enter a word >")
word_reverse = word[::-1]

if word == word_reverse:
    print("the word", word, "is a palindrome!")
else:
    print ("the word", word, "is not a pallindrome!")
