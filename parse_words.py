with open("wordlist.txt", "r") as file:
    words = file.readlines()
    
filtered_words = map(lambda x: x.replace("\u200b", ""), words)

word_dict = {}

for line in filtered_words:
    word = line[:5]
    diff = line[5:]
    diff_fixed = diff.rstrip("\n")
    word_dict[word] = diff_fixed

print(word_dict)
