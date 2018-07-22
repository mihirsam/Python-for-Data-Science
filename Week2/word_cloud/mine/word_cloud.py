file = open("98-0.txt", "r")
stopwords = open("stopwords.txt", "r")

word_cloud = {}

for word in file:
    print(word)
