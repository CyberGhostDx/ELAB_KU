str1 = eval(input("String set1: "))
str2 = eval(input("String set2: "))

alphabet = "abcdefghijklmnopqrstuvwxyz"

concatenated_words = []

for word1 in str1:
    for word2 in str2:
        concate_word = word1 + word2
        check_char = alphabet
        for char in concate_word:
            check_char = check_char.replace(char, "")
        if len(check_char) == 0:
            concatenated_words.append(concate_word)

print(f"Output: {len(concatenated_words)}")
print("The total complete pairs that are forming are: ")
for word in concatenated_words:
    print(" " + word)
