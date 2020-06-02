import random
import pygame
pygame.init()

def syllable():
    a = ["ab", "ak", "ad", "ach", "af", "ag", "al", "am", "an", "ap", "ar", "as", "at", "ath", "av", "aw", "ax"]
    e = ["eb", "ed", "ef", "eg", "el", "em", "en", "ep", "ers", "ert", "erth", "erv"]
    i = ["ib", "ick", "if", "ig", "ill", "im", "in", "is", "it", "ix"]
    o = ["ob", "od", "off", "of", "og", "om", "on", "or", "ot", "oth", "ost", "ox", "orb"]

    lists = [a, e, i, o]

    list = lists[random.randint(0, len(lists) - 1)]
    letters = list[random.randint(0, len(list) - 1)]
    return letters


def letter(cap):
    letters = ["b", "br", "bl", "k", "kr", "kl", "d", "dr", "f", "fl", "g", "gr", "gl", "h", "m", "n", "p", "pr", "pl", "r", "s", "t", "tr"]
    caps = ["B", "Br", "Bl", "K", "Kr", "Kl", "D", "Dr", "F", "Fl", "G", "Gr", "Gl", "H", "M", "N", "P", "Pr", "Pl", "R", "S", "T", "Tr"]

    if cap:
        final_letter = caps[random.randint(0, len(caps) - 1)]
    else:
        final_letter = letters[random.randint(0, len(letters) - 1)]

    return final_letter


done = ""
while done != "done":

    done = input("Press enter for a new random name (or type done) ")

    """start_letter = letter(True)                         
    syll1 = syllable()
    next_letter = letter(False)
    syll2 = syllable()"""

    word = letter(True) + syllable() + letter(False) + syllable()   
    print()
    print(word)