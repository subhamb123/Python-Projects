pets = []
pet = ""
while pet != "done":
    pet = input("Enter the pets you have (done to finish): ")
    if pet != "done":
        pets.append(pet)

dog = False
for pet in pets:
    if pet == "dog":
        dog = True
        break

print("Here are your pets:")
print(pets)

if dog:
    print("The dog was found.")
else:
    print("The dog wasn't found.")
