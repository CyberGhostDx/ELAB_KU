text = input("Enter text: ")
step = int(input("Enter step: "))

alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypt = ""

for i in text:
    if not i.isalpha():
        encrypt += i
        continue
    if i.islower():
        encrypt += alphabet[(alphabet.index(i.lower()) + step) % 26]
    else:
        encrypt += alphabet[(alphabet.index(i.lower()) + step) % 26].upper()

print(encrypt)
