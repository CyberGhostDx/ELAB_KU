print("Parse a long paragraph (or text) below, following an ENTER as needed:")

paragraph = ""
words = {}

while 1:
    line = input()
    if not line:
        break
    paragraph += line + " "

paragraph = paragraph.split()

for word in paragraph:
    word = word.lower()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)

k = int(input("Top K rank: "))

top_k = []
k_index = -1

prv_count = 0

for word, count in sorted_words:
    if count == prv_count:
        top_k[k_index].append((word, count))
    if count != prv_count:
        k_index += 1
        if k_index == k:
            break
        top_k.append([(word, count)])
    prv_count = count

for i in top_k:
    print(", ".join([f"{word}: {count}" for word, count in i]))
