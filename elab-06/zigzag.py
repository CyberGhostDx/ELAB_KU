sentence = input("Input sentence: ")
row = int(input("Input row: "))
row = row - 1

zigzag = []
pos_x = 0
pos_y = 0
isBackward = True

for i, x in enumerate(sentence):
    zigzag.append((x, pos_x, pos_y))
    if i % row == 0:
        isBackward = not isBackward
    if isBackward:
        pos_y -= 1
        pos_x += 1
    else:
        pos_y += 1

zigzagSentence = ""

for i in range(row + 1):
    zigzagSentence += "".join([x[0] for x in zigzag if x[2] == i])

print(zigzagSentence)
