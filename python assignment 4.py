file = open("D:\\thilak projects\\PycharmProjects\\mbox-short.txt")
list1 = []
domain_file = {}
count =0
for line in file:
    if line.startswith('From') and not line.startswith('From:'):
        split_at_space = list(line.split(" "))
        print(split_at_space[1])
        user,domain = split_at_space[1].split("@")
        if domain not in domain_file:
            domain_file[domain] += 1
        count += 1
print(f'Total number of mails: {count}')
print(domain_file)
