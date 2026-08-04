sent = input("Enter a sentence > ")
words = sent.split()

print (words)

used_words = []
for word in words:
    if word not in used_words:
        word_count = words.count(word)
        used_words.append(word)
        print("The word", word, "appears", word_count, "times")

    
  



