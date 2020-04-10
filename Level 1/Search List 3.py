sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

print("Here is a sentence:")
output = ""
for word in sentence:
    output += word + " "
print(output)
print()


find = input("Please enter a word to find: ")


found = False
for word in sentence:
    if word == find:
        found = True
        break

if found:
    print("That word is in the sentence.")
else:
    print("That word is not found.")
