week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

miles_per_day = []


for day in week:

    miles = input("How many miles did you walk on " + day + "? ")

    miles_per_day.append(float(miles))


total_miles = 0

total_calories = 0


for miles in miles_per_day:

    total_miles += miles

    total_calories += miles * 70


avg_miles = total_miles / len(week)

avg_cal = total_calories / len(week)


print()

print("Fitness stats")

print("-------------")


print("Total Miles: " + str(total_miles))

print("Total Calories: " + str(total_calories))

print("Average Miles: " + str(avg_miles))

print("Average Calories: " + str(avg_cal))
