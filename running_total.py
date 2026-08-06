count = 0
total = 0

while True:
    number = (input("Keep entering your number or type 'done' to finish: "))
    if number == "done":
        break
    elif number != "done":
       finish = float(number)
       total = total + finish
       count = count + 1
       print("running total:", total)

print("The final total is ->", total)
print("The total numbers enetred are:",count)
     
