gifts = ["four calling birds", "three french hens", "two turtle doves", "a partridge in a pear tree"]

output = ""
count = 0

for gift in gifts:
    if count == len(gifts)-1:
        output += "and "
    output += str(gift)
    if count < len(gifts)-1:
        output += ", "
    count += 1

print(output)
