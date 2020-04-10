import random
import pygame
pygame.init()
words = []
word = ""
sentence = ""
count = 0
while word != "done":
    word = input("Enter a word (Type \"done\" to quit): ")
    if word != "done":
        words.append(word)

print()
print("Here are your words")
print("-------------------")
for i in range(len(words)):
    print(words[i])

print()
print("Here are your random sentences")
print("------------------------------")    
for i in range(len(words)):
    count = 0
    sentence = "Sentence " + str(i+1) + ": "
    while count < len(words):
        sentence += words[random.randint(0, len(words)-1)] + " "
        count+=1
    
    print(sentence)
