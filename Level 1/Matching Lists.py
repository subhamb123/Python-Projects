items = []
prices = []

print("Welcome to Menu Builder!")
item = ""
while item != "done":
    item = input("Enter an item (or done to end): ")
    if item == "done":
        break
    price = int(input("What is the item's price? "))
    items.append(item)
    prices.append(price)

print()
print("MENU:")

for i in range(len(items)):
    print(str(i+1) + ") " + items[i] + " - $" + str(prices[i]))
