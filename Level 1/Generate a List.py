import random


player_number = int(input("How many players are there? "))
players = []

for i in range(player_number):
    players.append("Player " + str(i))


print()
print("Here is your random order:")
while len(players) > 0:
    index = random.randint(0, len(players) - 1)
    print(players[index])
    players.remove(players[index])
