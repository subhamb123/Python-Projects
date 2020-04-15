same = False
sameFirstLast=[1, 2, 1] 
if len(sameFirstLast) == 1:
    same = True
elif len(sameFirstLast) > 1 and sameFirstLast[0] == sameFirstLast[len(sameFirstLast)-1]:
    same = True
    
if same:
    print(same)
