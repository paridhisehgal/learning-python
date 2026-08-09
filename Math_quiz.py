print("\nHere's a Math Quiz for you!")
intro = input("\nEnter 'yes' to start ->")
import random

score_count = 0
for i in range(5):
    num1 =random.randint(1,20)
    num2 =random.randint(1,20)
    correct_answer = num1+ num2
    user_ans =int(input(f"\nwhat is {num1} + {num2}? ->1"))
    if user_ans == correct_answer:
        score_count = score_count +1
        
print ("You scored", score_count, "out of 5!")
    