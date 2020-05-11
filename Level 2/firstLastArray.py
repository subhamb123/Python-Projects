numbers = [7,4,6,2]
firstLast = []
if len(numbers) == 1:
    print(numbers)
else:
    firstLast.append(numbers[0])
    firstLast.append(numbers[len(numbers)-1])
    print(firstLast)
