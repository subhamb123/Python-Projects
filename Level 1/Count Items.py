numbers = []
number = 0
while True:
    number = input("Enter numbers (done to stop): ")
    if number == "done":
        break
    else:
        numbers.append(int(number))

num = 0
for odd in numbers:
    if odd%2 == 1:
        num += 1



print("Out of " + str(len(numbers)) + " numbers...")

if num == 1:
    print(str(num) + " is odd.")
else:
    print(str(num) + " are odd.")
