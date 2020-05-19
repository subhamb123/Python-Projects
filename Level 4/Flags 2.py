import pygame
pygame.init()
def totals(num_list):                                   

    total = 0
    for num in num_list:
        total += num

    avg = total / len(num_list)

    print("FINAL TOTAL: " + str(total))
    print("FINAL AVERAGE: " + str(avg))

    print()


values = []
new_val = ""

while new_val != "done":
    new_val = input("Enter a value to add (enter done to finish): ")

    if new_val == "done":
        break
    else:
        values.append(int(new_val))

        print("CURRENT TOTAL: " + str(sum(values)))
                                          


totals(values)