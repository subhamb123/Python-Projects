guesses = 6

wrong_letters = []

right_letters = []


word = input("Type a word: ")


print("\n" * 100)

for letter in word:

    right_letters.append("_")

while "_" in right_letters and guesses > 0:

    print("You have guessed: " + str(wrong_letters))

    print("Word: " + str(right_letters))

    print("Guesses remaining: " + str(guesses))

    guess = input("Guess a letter: ")

    print()


    if guess not in wrong_letters and guess not in right_letters:

        found = False


        for i in range(len(word)):

            if word[i] == guess:

                right_letters[i] = guess

                found = True


        if not found:

            guesses -= 1

            wrong_letters.append(guess)

    else:

        print("You guessed that letter already.")


if "_" not in right_letters:

    print("Congratulations, you guessed the word!")

else:
    print("Sorry, you didn't guess it.")  
