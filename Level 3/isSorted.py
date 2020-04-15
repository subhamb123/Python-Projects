switch = True
    sorted = True
    while switch:
        floats = [16.1, 12.3, 22.2, 14.4]
        if len(floats) == 1:
            break
        for number in range(0, len(floats)-1):
            if floats[number] > floats[number+1]:
                sorted = False
                switch = False
        switch = False
    if sorted:
        print("The list is sorted.")
    else:
        print("The list isn't sorted.")
