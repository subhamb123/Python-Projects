import random
import pygame
pygame.init()

def make_random_word():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    word = []

    for i in range(10):
        word.append(random.choice(alphabet))

    return word


def printable_word(list):
    word = ""
    for letter in list:
        word += letter

    return word


def replace_letters(blank_list, word_letters, guess):

    track = False

    for i in range(len(blank_list)):
        if word_letters[i] == guess and blank_list[i] == "_":

            blank_list[i] = word_letters[i]
            track = True


    return track



word = make_random_word()
blanks = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
guesses = 15
guessed = []


while guesses > 0:

    print("Current word: " + printable_word(blanks))
    print("Guessed Letters: " + str(guessed))

    print()
    print("You have " + str(guesses) + " guesses remaining.")
    letter = input("Guess a letter: ")
    print()

    if not letter in guessed:

        replace_letters(blanks, word, letter)
        guessed.append(letter)

        guesses -= 1

    else:
        print("You already guessed that letter. Try again.")

    if not "_" in blanks:
        print("Wow! You guessed it! Congratulations!")
        break


if guesses == 0:
    print("Sorry, the correct word was: " + printable_word(word))