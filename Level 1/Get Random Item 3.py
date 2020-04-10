import random
animals = ["lion", "horse", "dog", "bird", "human", "bat", "cat", "goat"]

head_index = random.randint(0, len(animals)-1)
head = animals[head_index]

body_index = random.randint(0, len(animals)-1)
body = animals[body_index]


print("The " + head + body + " is a mythical creature.")
print("It has the head of a " + head + " and the body of a " + body + ".")
