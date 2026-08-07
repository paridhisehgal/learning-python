words_list = []
cleaned_list = []

for i in range (1 , 11):
    word = input ("Enter a word: ")
    words_list.append(word)
    if word not in cleaned_list:
     cleaned_list.append(word)

print("\n➡️ original list ->", words_list)
print("\n➡️ your cleaned_list -> ", cleaned_list)

    
