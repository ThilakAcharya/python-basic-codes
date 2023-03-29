file_name = input("Enter File name: ")
try:
    file = open(file_name)
    days = {}
    for line in file:
        if line.startswith('From') and not line.startswith('From:'):
            split_line = line.split(" ")
            day = split_line[2]
            if day not in days:
                days[day] = 1
            else:
                days[day] += 1
    print(days)
except:
    print("File cannot be opened\n Enter proper name.")

#D:\\thilak projects\\PycharmProjects\\mbox-short.txt
