acronym = ""

word = ""
while word != "done":
    word = input("Please enter a word: ")

    if word != "done":
        acronym += word[0]


print("These words make the acronym:")
print(acronym)
