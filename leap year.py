'''a = True
while a == True:
    year = int(input("Year: "))'''
for year in range(1800,2025):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print(" leap year{}".format(year))
    else:
        print("not leap year{}".format(year))

    '''status = input("to exit enter exit: ")
    if status.lower() == "exit":
        a = False'''
