groceries = []
option = ""
while option != "done":
    option = input("Enter 'add' to add groceries, 'remove' to remove groceries, 'replace' to replace a grocery item with another, 'show' to reveal grocery list, or 'done' to exit program: ")
    if option == "done":
        print("Here is your final grocery list: " + str(groceries))
        break
    elif option == "add":
        groceries.append(input("Enter an item: "))
        print("Here is your current grocery list: " + str(groceries))
    elif option == "remove":
        remove = input("Enter an item: ")
        if remove in groceries:
            groceries.remove(remove)
            print("Here is your current grocery list: " + str(groceries))
        else:
            print("Item not in grocery list.")
            print("Here is your current grocery list: " + str(groceries))
    elif option == "show":
        print("Here is your current grocery list: " + str(groceries))
    elif option == "replace":
        replace = input("Enter an item to replace: ")
        if replace in groceries:
            item = input("Enter replacement item: ")
            groceries[groceries.index(replace)] = item
            print("Here is your current grocery list: " + str(groceries))
        else:
            print("Item not in grocery list.")
            print("Here is your current grocery list: " + str(groceries))
