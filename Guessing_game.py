from webbrowser import Konqueror


secret_word = "Clock it"
guess = " "
guess_count = 0
guess_limit = 5
out_of_guesses = False

while secret_word != guess and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("enter guess word: ")
        guess_count +=1
    
    else:
        out_of_guesses = True

if out_of_guesses:
        print ("Reached guess limit, you lose!")

else:
     print("You win!")



