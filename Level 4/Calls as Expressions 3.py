def get_age(birth_year):

    now = 2018
    age = now - birth_year
    return age



total_age = 0

siblings = int(input("How many siblings do you have? "))
for i in range(siblings):
    date = int(input("Enter a birth year sibling " + str(i + 1) + ": "))

    total_age += get_age(date)

date = int(input("What year were you born? "))

my_age = get_age(date)
total_age += my_age

avg_age = total_age / (siblings + 1)
print("The average age of you and your siblings is: " + str(avg_age))