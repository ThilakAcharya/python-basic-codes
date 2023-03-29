file_name = input("Enter File name: ")
try:
    file = open(file_name)
    mails = {}
    for line in file:
        if line.startswith('From') and not line.startswith('From:'):
            split_line = line.split(" ")
            mail_id = split_line[1]
            if mail_id not in mails:
                mails[mail_id] = 1
            else:
                mails[mail_id] += 1
    max_value = max(mails, key=mails.get)
    print(max_value,mails[max_value]                                                    )
except:
    print("File cannot be opened\n Enter proper name.")

#D:\\thilak projects\\PycharmProjects\\mbox-short.txt
