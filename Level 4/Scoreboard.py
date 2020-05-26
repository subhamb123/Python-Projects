def print_min_max(all_scores, all_players, which_score):


    if len(all_scores) == 0:

        print("No scores yet entered")

        return


    min = all_scores[0]

    max = all_scores[0]

    min_person = all_players[0]

    max_person = all_players[0]


    for i in range(len(all_scores)):

        score = all_scores[i]

        if score < min:

            min = score

            min_person = all_players[i]

        if score > max:

            max = score

            max_person = all_players[i]



    if which_score == "min" or which_score == "both":

        print("LOWEST SCORE: " + min_person + ", with " + str(min))

    if which_score == "max" or which_score == "both":

        print("HIGHEST SCORE: " + max_person + ", with " + str(max))



def print_scores(all_scores, all_players):


    if len(all_scores) == 0:

        print("No scores yet entered")

        return


    print("ALL SCORES")

    print("--------------------------")

    for i in range(len(all_scores)):

        print(all_players[i] + ": " + str(all_scores[i]))


def print_summary(all_scores, all_players):

    print("SCORE SUMMARY")

    print("--------------------------")

    print("TOTAL NUMBER OF SCORES: " + str(len(all_scores)))

    print_min_max(all_scores, all_players, "both")



names = []

scores = []



done = False
while not done:



    print()
    print("---- MENU ----")
    print("What would you like to do?")
    print("   1: Enter a new player & score")
    print("   2: Get the current highest score")
    print("   3: Get the current lowest score")
    print("   4: Print all scores")
    print("   5: Print a full summary")
    print("   0: Quit")
    user_choice = input()
    print()

    if user_choice == "0":
        done = True


    elif user_choice == "1":

        name = input("Enter a player name: ")

        score = input("Enter a player score: ")

        names.append(name)

        scores.append(score)



    elif user_choice == "2":

        print_min_max(scores, names, "max")

    elif user_choice == "3":

        print_min_max(scores, names, "min")

    elif user_choice == "4":

        print_scores(scores, names)

    elif user_choice == "5":

        print_summary(scores, names)

    else:
        print("I'm sorry, that was not a valid choice")