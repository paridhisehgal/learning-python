VOWEL_REPLACEMENT = {
    "a": "e",
    "e": "i",
    "i": "o",
    "o": "u",
    "u": "a"
}

VOWELS = ['a', 'e', 'i', 'o', 'u']

message = input("Enter any message: ")
formatted_message = ""

for character in message:
    if character in VOWELS:
        formatted_message += VOWEL_REPLACEMENT[character]
    else:
        formatted_message += character

print("message: ", message)
print("formatted message: ", formatted_message)
