for i in range(5, 0, -1):
        print("-"*i, end = '')
        for j in range(11-(i*2)):
            print(str(11-(i*2)), end = '')
        print("-"*i)
