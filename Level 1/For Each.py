foods = ["chicken", "pizza", "burger", "fish"]
for food in foods:
    response = input("Do you like " + food + "? y/n: ")
    if response == "y":
        print("I like that too!")
