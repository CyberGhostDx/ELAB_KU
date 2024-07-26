word = input("Enter a string: ")

vowels = "aeiou"

unique_vowels = []
unique_consonants = []

for char in word:
    char = char.lower()
    if not char.isalpha():
        continue
    if char in vowels and not char in unique_vowels:
        unique_vowels.append(char)
    elif not char in unique_consonants and not char in vowels:
        unique_consonants.append(char)

print(f"Unique vowels:  {unique_vowels}")
print(f"Unique consonants:  {unique_consonants}")
