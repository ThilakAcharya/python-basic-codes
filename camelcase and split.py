def camelCase(sentence):
    words = [[sentence[0]]]
    for i in sentence[1:]:
        if words[-1][-1].islower() and i.upper():
            words.append(list(i))
        else:
            words[-1].append(i)
    return [''.join(word) for word in words]


sentence = "geeksForGeeks"
print(camelCase(sentence))
