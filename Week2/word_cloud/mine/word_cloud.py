file = open("98-0.txt","r")
stopword = open("stopwords.txt", "r")

stopwords = []
for word in stopword:
    stopwords.append(word.strip("\n"))

word_cloud = {}
for word in file:
    words = []
    words = word.split(' ')

    for i in range(0, len(words)):
        if words[i] not in word_cloud.keys():
            if words[i] not in stopwords:
                word_cloud[words[i]] = 1
            else:
                pass
        else:
            word_cloud[words[i]] += 1


result = sorted(word_cloud.items(), key=lambda x: x[1], reverse = True)

print("Word_Cloud: \n")

i = 0
for key, value in result:
    print(key, ":", value)
    i += 1
    if i > 10:
        break
    else:
        pass
