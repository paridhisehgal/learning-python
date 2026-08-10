shopping_list = []
while True:
    print("\nMenu:")
    print("(a)Add an item:")
    print("(b)Remove an iten")
    print("(c)View the list")
    print("(d)Quit")
 
    user_input = input("\nChoose any option from a to d ->")
    
    if user_input == "a":
        item = input("Add any item of your choice: ")
        shopping_list.append(item)
        print(item,"successfully added to the list!")
    
    elif user_input == "b":
        item = input("Enter any item to remove: ")
        shopping_list.append(item)
        print(item, "successfully removed from the list!")
     
    elif user_input == "c":
        print("shopping list:", shopping_list)

    elif user_input == "d":
        print("Happy shopping, goodbye!")
        break
     
    else:
        print("Please try again!")
