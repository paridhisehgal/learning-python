secret_num = 7
attempts = 0

while True:
    guess = int(input("Guess the secret number! : "))
    attempts += 1
    if guess == secret_num and attempts ==1 :
        print("\nWohoo!You guessed it right☑️","\nIt took you",attempts,"attempt to win the game🎖️")
    elif guess == secret_num and attempts > 1 :
        print("\nWohoo!You guessed it right☑️","\nIt took you",attempts,"attempts to win the game🎖️")
        break
    elif guess < secret_num:
        print ("Ops,Higher!")
    else:
        print("Ops,lower!")



