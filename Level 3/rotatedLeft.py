numbers = [5, 11, 9, 22]
rotatedLeft = []
for i in range(1,len(numbers)):
    rotatedLeft.append(numbers[i])

rotatedLeft.append(numbers[0])
print(rotatedLeft)
