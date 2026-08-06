words = [
    "apple", "banana", "cat", "dog", "elephant", "fish", "grape", "hat",
    "ice", "juice", "kite", "lion", "mango", "nest", "orange", "pear",
    "queen", "rose", "sun", "tree", "umbrella", "van", "wolf", "xray",
    "yak", "zebra", "ant", "bear", "cloud", "duck", "eagle", "flower",
    "goat", "house", "island", "jacket", "koala", "lemon", "monkey", "night",
    "ocean", "piano", "quilt", "river", "star", "table", "unicorn", "violet",
    "water", "yellow", "zoo", "airplane", "bottle", "candle", "diamond", "engine",
    "forest", "garden", "honey", "igloo", "jungle", "key", "ladder", "mirror",
    "notebook", "onion", "pencil", "quiz", "rainbow", "shadow", "turtle", "umpire",
    "valley", "whale", "xylophone", "yarn", "zipper", "anchor", "brush", "candy",
    "desert", "eagle", "feather", "guitar", "harbor", "insect", "jewel", "kitten",
    "lantern", "mountain", "needle", "oyster", "parrot", "quicksand", "robot", "snake",
    "tunnel", "urchin", "volcano", "window"
]

position = 0
word_find = input("Enter any word -> ")

while position < len(words):
     if words[position] == word_find:
        print(f" {word_find}, found at position {position}!")
        break
     else:
      position += 1
      
    
    
