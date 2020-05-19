import random
import pygame
pygame.init()

def print_summary(all_names, all_foods):
    print()
    print("PLAYER CHOICES: ")
    print_favs(all_names, all_foods)
    
    print()
    print("FOOD SCORES: ")
    print_scores(all_foods)
    
    print()
    print("MOST POPULAR FOOD: ")
    print_winner(all_foods)
    
def print_favs(names, foods):
    for i in range(len(names)):
        print(names[i] + ": " + foods[i])


def print_scores(foods):
    unique_food_list = []
    food_scores = []

    for i in range(len(foods)):
        if not (foods[i] in unique_food_list):
            unique_food_list.append(foods[i])
            food_scores.append(1)
        else:
            position = unique_food_list.index(foods[i])
            food_scores[position] += 1

    for i in range(len(unique_food_list)):
        print(unique_food_list[i] + ": " + str(food_scores[i]))


def print_winner(foods):
    unique_food_list = []
    food_scores = []

    for i in range(len(foods)):
        if not (foods[i] in unique_food_list):
            unique_food_list.append(foods[i])
            food_scores.append(1)
        else:
            position = unique_food_list.index(foods[i])
            food_scores[position] += 1

    max_score = 0
    most_popular = ""
    for i in range(len(food_scores)):
        if food_scores[i] > max_score:
            max_score = food_scores[i]
            most_popular = unique_food_list[i]

    print(most_popular)


all_names = []
all_foods = []
name = ""

while name != "done":

    name = input("Is another person voting? (enter name or done): ")
    if name == "done":
        break

    food = input("What is your favorite food, " + name + "? ")
    all_names.append(name)
    all_foods.append(food)
    print()

print_summary(all_names, all_foods)