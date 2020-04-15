same = False
a = [1,2,3]
b = [1,3]
if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    same = True

if same:
    print(same)
