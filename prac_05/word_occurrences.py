text = input("Text: ")
words = text.split()

word_to_count = {}
for word in words:
    word = word.lower()
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

for word, count in sorted(word_to_count.items()):
    print(f"{word} : {count}")
