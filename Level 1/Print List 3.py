items = ["hello", 12, True, 5.9, (0, 0)]

output = ""
count = 0

for item in items:
    output += str(item)
    if count < len(items)-1:
        output += ", "
    count += 1
print(output)
