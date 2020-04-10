ingredients = ["tomato", "chicken", "bun", "lettuce", "onion", "ketchup"]

first = []
second = []

player1 = True


while len(ingredients) > 0:


    remaining = "The remaining ingredients are: "

    for ingredient in ingredients:
        remaining += ingredient + ", "
        

    print("Remaining ingredients: " + remaining)


    if player1:
        choice = input("Choose an ingredient from the list: ")

        if choice in ingredients:
            ingredients.remove(choice)
            first.append(choice)


    else:
        choice = input("Choose an ingredient from the list: ")

        if choice in ingredients:
            ingredients.remove(choice)
            second.append(choice)




    player1 = not player1

    print()


print("Your Sandwiches")
print("---------------")


san1 = "Player 1's sandwich: "

for ingredient in first:
    san1 += ingredient + ", "
    

print(san1)


san2 = "Player 2's sandwich: "

for ingredient in second:
    san2 += ingredient + ", "


print(san2)
