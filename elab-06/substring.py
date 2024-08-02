text = input("Text: ")
substr = input("Substring: ")

newStr = ""

i = 0

while i < len(text):
    isSub = False
    if text[i] == substr[0]:
        for j in range(1, len(substr)):
            if i + j > len(text) - 1:
                isSub = False
                break
            if text[i + j] != substr[j]:
                isSub = False
                break
            isSub = True
    if isSub:
        newStr += f"[{substr}]"
        i += len(substr) - 1
    else:
        newStr += text[i]
    i += 1


if newStr == text:
    newStr = ""
    i = 0
    while i < len(text):
        diff = 0
        dummy = ""
        if text[i] == substr[0]:
            dummy += "[" + text[i]
            for j in range(1, len(substr)):
                if i + j > len(text) - 1:
                    break
                if text[i + j] != substr[j]:
                    diff += 1
                    dummy += "?"
                    continue
                dummy += substr[j]
            dummy += "]"
        if 0 < diff <= 1:
            newStr += dummy
            i += len(substr) - 1
        else:
            newStr += text[i]
            dummy = ""
            diff = 0
        i += 1

print(newStr)
