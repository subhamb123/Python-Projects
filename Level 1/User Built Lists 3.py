guests = []

guest = ""
while guest != "done":
    guest = input("Enter a guest (enter 'done' to exit)")
    if guest != "done":
        guests.append(guest)



print("Here are your guests:")
index = 0
while index < len(guests):
    print("   -" + guests[index])
    index += 1
print("You'll need to cut any pizza into " + str(len(guests)) + " slices.")
