import random


animals = ["tiger", "dog", "lizard", "hedgehog", "ferret"]

option = random.randint(0, len(animals)-1)

print("Your pet is a " + animals[option])
