def sum_list(num_list):
    if len(num_list) == 0:
        return 0
    total = 0
    for num in num_list:
        total += num
    return total

nums = []
val = ""

while val != "done":
    val = input("Enter a number or done: ")

    print()
    if val == "done":
        break

    nums.append(float(val))
    amount = sum_list(nums)
    print("Current Total: " + str(amount))



print()
amount = sum_list(nums)
print("FINAL TOTAL: " + str(amount))
sum_list(nums)

