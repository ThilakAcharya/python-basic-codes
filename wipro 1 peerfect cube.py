def PerfectCube(n,arr):
    lst = []
    for i in arr:
        for j in range(2,100000):
            if pow(j,3) == i:
                lst.append(j)

    return len(lst)
n = int(input("n: "))
arr = list(map(int,input("array number: ").split()))
lst = PerfectCube(n,arr)
print(lst)
