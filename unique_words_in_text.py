file_name = input("Enter file name: ")
try:
    file = open(file_name)
    common_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","let","day"]
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
    unique_words =[]
    word_count = 0
    for line in file:
        split_line = line.split(" ","\n")
        for word in split_line:
            if word.lower() not in common_words and word.lower() not in punctuations:
                unique_words.append(word)
                word_count +=1
            else:
                continue
    print("number of unique words: " + str(word_count))
    print(f'The words are: {unique_words}')
except:
    print("File cannot be openned\nEnter proper file name")


#D:\\thilak projects\\PycharmProjects\\python programs\\romeo.txt












