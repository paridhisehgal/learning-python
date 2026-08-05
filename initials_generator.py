full_name = input("Enter your full name -> ")
separated_name = full_name.split()

first_letter = []

for name in separated_name:
      first_letter.append(name[0].upper())
      
initials =".".join (first_letter)
print ("Your inititals:-","\n#", initials)

    
    


