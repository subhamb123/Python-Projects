count = 0

movies = ["Star Wars", "Pirates of the Caribbean", "The Matrix"]
ratings = []

for movie in movies:
    rating = int(input("Rate " + movie + " from 1 to 10: "))
    ratings.append(rating)

while count < len(movies):
    print("You rated " + str(movies[count]) + " a " + str(ratings[count]) + ".")
    count += 1

lowest = 10
highest = 0

for rating in ratings:
    if rating < lowest:
        lowest = rating
    elif rating > highest:
        highest = rating

print("Your Rankings")
print("-------------")
print("You rated " + str(movies[ratings.index(lowest)]) + " the lowest with a rating of " + str(lowest) + ".")
print("You rated " + str(movies[ratings.index(highest)]) + " the highest with a rating of " + str(highest) + ".")
