flavors = ["Black Raspberry", "Butterscotch", "Chocolate", "Coconut", "Coffee", "Cookie Dough", "Ketchup", "Lavender", "Mango", "Mint Chip", "Strawberry", "Vanilla"]
favorites = []
count = 0

while count < 5:

    print("Flavors to choose from: ")
    index = 0
    while index < len(flavors):
        print("   -" + flavors[index])
        index += 1

    favorite = input("What is your favorite flavor? ")
    favorites.append(favorite)
    if favorite in flavors:
        flavors.remove(favorite)


    count += 1

print()
print("Your Flavor Rankings:")
index = 0
while index < len(favorites):
    print(str(index + 1) + ". " + favorites[index])
    index += 1
