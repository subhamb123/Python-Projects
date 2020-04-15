numbers = [3, 5, 2, 1, 92, 38, 3, 14, 5, 73, 5]
print("Here is the list: " + str(numbers))
target = int(input("Enter a number to check how many of that number is in the list: "))
count = 0
for number in numbers:
    if number == target:
        count += 1
if count == 1:
    print("There is " + str(count) + " occurance of your number in the list.")
else:
    print("There are " + str(count) + " occurances of your number in the list.")
