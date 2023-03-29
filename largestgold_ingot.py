G = 7
B = 1
H =1
L = list(map(int,input("l: ").rstrip().split()))
c = 0
for i in L:
    if i >=3:
        c+=i
        print(i)
    else:
        break
print(c)
