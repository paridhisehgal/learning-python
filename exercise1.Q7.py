sentence = input("enter a sentence: ")
vowels = ["a" , "e", "i" , "o"  , "u"]

count = 0
for v in vowels :
    count += sentence.lower().count(v)

print (count)
