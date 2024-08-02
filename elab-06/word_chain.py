text = input("Text: ").split()

chains = 1
max_count = 0
current_count = 0

for i in range(0, len(text) - 1):
    diff = 0
    for j in range(len(text[i])):
        if text[i][j] != text[i + 1][j]:
            diff += 1
    if diff > 2:
        chains += 1
        current_count = 0
    current_count += 1
    if current_count > max_count:
        max_count = current_count

print(f"{chains} Chain(s). Maximum length is {max_count} word(s).")
