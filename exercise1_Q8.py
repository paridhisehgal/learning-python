
sentence = input("Enter a sentence: ")
words = sentence.split()

result = ""
for w in words:
    result += "" +w[0].upper()+ w[1: ]+ " "
      
print(result.strip())

print(sentence.upper())
print(sentence.lower())

