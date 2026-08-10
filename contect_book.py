names = []
contact_numbers = []
 
while True:
    print("\nMenu:")
    print("(a) Add a contact")
    print("(b) Search for a contact")
    print("(c) Delete a contact")
    print("(d)View sall contacts")
    print("(e)quit")

    user_input = input("Choose any option from the above:")

    if user_input == "a":
       name = input("Enter name: ")
       contact_number= input("Enter contact number: ")
       names.append(name)
       contact_numbers.append(contact_number)
       print(name,"has been successfulyy added!")

    elif user_input == "b":
        name = input("Enter name to search:")
        if name in names:
            position =names.index(name)
            print(name, "-", contact_numbers[position])
        else:
            print(name,"Name not found!")
    elif user_input == "c":
        name = input("Enter name to delete:")
        if name in names:
            positon =names.index(name)
            names.pop(position)
            contact_numbers.pop(position)
            print(name,"has been deleted!")
        else:
            print(name,"not found")

    elif user_input == "d":
        print("Contacts: ")
        for i in range (len(names)):
            print(names[i],"-",contact_numbers[i])
    elif user_input == "e":
     print("Goodbye!")
     break
    else:
        print("Try again!b")
    