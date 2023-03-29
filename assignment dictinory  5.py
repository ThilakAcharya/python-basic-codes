file_name = input("Enter File name: ")
try:
    file = open(file_name)
    domains = {}
    for line in file:
        if line.startswith('From') and not line.startswith('From:'):
            split_line = line.split(" ")
            user,domain = split_line[1].split("@")
            if domain not in domains:
                domains[domain] = 1
            else:
                domains[domain] += 1
    print(domains)
except:
    print("File cannot be opened\n Enter proper name.")

#D:\\thilak projects\\PycharmProjects\\mbox-short.txt
