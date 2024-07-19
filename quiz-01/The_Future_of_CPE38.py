survey = input("ผลการสำรวจ: ")
survey = survey.split()
survey = [int(x) for x in survey]

h = max(survey)


def getStone(h):
    if h <= 0:
        return " "
    if h >= 9:
        return "x"
    if h >= 5:
        return "="
    return "o"


def draw_map(survey, h):
    for i in range(1, h + 1):
        current_h = h - i
        for i in range(len(survey)):
            if survey[i] >= current_h:
                print(getStone(survey[i] - current_h), end="")
            else:
                print(" ", end="")
        print()


def draw_flag(survey, h):
    max_length = len(survey)
    spacing = survey.index(h)
    print(" " * spacing + "+-------+"[: max_length - spacing])
    print(" " * spacing + "| CPE38 |"[: max_length - spacing])
    print(" " * spacing + "+-------+"[: max_length - spacing])
    print(" " * spacing + "|")
    print(" " * spacing + "|")
    print(" " * spacing + "|")


print("แผนที่:")
draw_map(survey, h)
print("อาจารย์โตโต้เดินทางไปปักธงที่จุดยอดสูงสุด:")
draw_flag(survey, h)
draw_map(survey, h)
