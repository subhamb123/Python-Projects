names = ["x", "y", "z"]
found = False


search = input("Search a name in the class: ")
for name in names:
    if search == name:
        found = not found
        break
if found:
    print("The student is in class.")
else:
    print("The student isn't in class.")
