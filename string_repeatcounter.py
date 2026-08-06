word = input("Enter any word: ")
letter = input ("Enter any letter: ")


for w in word :
    repeat = word.count(letter) 

print("The letter (",letter,") appears", repeat, "times in the word",word)