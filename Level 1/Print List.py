elements = ["fire", "earth", "air", "water", "magnesium", "carbon"]

output = ""
count = 0

for element in elements:
    output += str(element)
    if count < len(elements)-1:
        output += ", "
    count += 1

print(output)
