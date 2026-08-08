sentence = input("Enter any sentence: ")
words = sentence.split()

print("Total number of characters :",len(sentence))
print("Total number of words in a sentence:",len(words))

sentence_count = sentence.count(".") + sentence.count("!") + sentence.count("?")
print("Total number of sentences:", sentence_count)

longest_word = ""
for word in words:
    if len(word) >len(longest_word):
        longest_word = word
    
print("The longest_word in a sentence :", longest_word)




