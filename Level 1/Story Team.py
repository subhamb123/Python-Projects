num_players = int(input("Number of players: "))

words = []


current_word = ""

while current_word != "The end.":

    for i in range(num_players):

        print()


        print("Player " + str(i+1) + ", it is your turn.")

        current_word = input("Input a new word or input 'The end.': ")

        words.append(current_word)


        if current_word == "The end.":

            break


story = ""

for word in words:

    story += word + " "


print()

print(story)
