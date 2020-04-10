animals = []

animal = ""
while animal != "done":
    animal = input("Enter an animal (enter 'done' to exit)")
    if animal != "done":
        animals.append(animal)



cage = "+===============+"
index = 0
print("ZOO MAP:")
print(cage)
while index < len(animals):
    row = "| " + animals[index]
    spaces = 14 - len(animals[index])
    while spaces > 0:
        row += " "
        spaces -= 1
    row += "|"
    print(row)
    print(cage)
    index += 1
