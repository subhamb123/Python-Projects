import random

people = []

name = ""


while name != "done":


    name = input("Enter a name or type 'done': ")

    if name == "done":

        break

    people.append(name)


pick = random.randint(0, len(people)-1)

vampire = people[pick]

print()


while len(people) > 1:


    print("Here are the list of people: " + str(people))

    guess = input("Who do you think the vampire is? ")


    if guess == vampire:

        print("Congratulations, you got it!")

        break


    elif guess in people:

        print("You are incorrect.")

        people.remove(guess)

    print()


if len(people) == 1:

    print("You couldn't guess the vampire. The vampire was: " + vampire)
