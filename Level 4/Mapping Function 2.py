import random


def greet(num, name):
    if num == 1:
        return "What's up " + name + "?"
    elif num == 2:
        return "How's it going " + name + "?"
    elif num == 3:
        return "What can I do for you " + name + "?"
    elif num == 4:
        return "Welcome " + name
    elif num == 5:
        return "Hello " + name
    else:
        return "Enter a valid input!"

name = input("What is your name? ")

done = ""
while done != "done":

    done = input("Type a number 1 - 5 or done: ")
    if done == "done":
        break

    greeting = greet(int(done), name)

    print(greeting)
    print()