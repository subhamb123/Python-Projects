import random


birds = ["parrot", "owl", "toucan"]

adj = ["red-throated", "black-winged"]

boasts = ["with my eyes closed", "from across a crowded forest"]

q = ""


while q != "quit":

    q = input("Enter a title or type 'quit'")

    if q == "quit":
        break

    index = random.randint(0, len(birds)-1)

    bird_choice = birds[index]


    index = random.randint(0, len(adj)-1) 

    adj_choice = adj[index]


    index = random.randint(0, len(boasts)-1) 

    boast_choice = boasts[index]


    print("Well, I spotted a " + adj_choice + " " + bird_choice + " " + boast_choice + "!")

    print()
