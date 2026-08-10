from calendar import c


inventory_list=["apple", "bread", "milk", "eggs", "butter"]

while True:
    print("\nMenu:")
    print("(a) Add item yo end of the list")
    print("(b)Insert item to a specific location")
    print("(c)Remove item by name")
    print("(d)View sorted inventory")
    print("(e)quit")

    user_input = input("From the above options choose one: ")

    if user_input == "a":
        item = input("Enter item to add: ")
        inventory_list.append(item)
        print(item, "added at he end of the list")
    
    elif user_input == "b":
        item = input("Enter item to insert")
        position = int(input("Enter position (0 = first): "))
        inventory_list.insert(position,item)
        print(item,"insereted at position", position)

    elif user_input == "c":
        item = input("Enter item to remove:")
        if item in inventory_list:
         inventory_list.remove(item)
         print(item, "successfully removed from the list")
        else:
            print(item, "is not in the list")
    
    elif user_input == "d":
        print("sorted_inventory:",sorted(inventory_list))

    elif user_input == "e":
        print("Goodbye!")
        break
    
    else:
         print("Try again")


    


