used_letters = []

last_used = "s"


print("RULES")
print("-----")
print("1) Players take turns entering words.")
print("2) The first letter of each player's word must be the same as the last letter of the previous word.")
print("3) If your word ends with a letter that's already been used, you lose!")


while last_used not in used_letters:


    used_letters.append(last_used)


    used = "Used letters: "

    for letter in used_letters:

        used += letter + ", "


    print()

    print(used)


    word = input("Enter a word beginning with " + last_used + ": ")


    last_used = word[len(word)-1]


print()

print("The letter has already been used.")

print("You got " + str(len(used_letters)) + " words!")
