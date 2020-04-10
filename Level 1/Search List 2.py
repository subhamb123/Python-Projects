import random

numbers = []
while len(numbers) < 8:
    number = random.randint(-100, 100)
    numbers.append(number)
print("Here are some numbers: " + str(numbers))

print("These are the positive ones:")

for number in numbers:
    if number > 0:
        print(number)
