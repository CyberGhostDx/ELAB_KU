p1 = input("Player1 name: ")
p2 = input("Player2 name: ")

p1_score = 0
p2_score = 0
print()

rat = '__QQ\n()">\n    '.split("\n")
hunter = " O \n/|\\\n/ \\".split("\n")
lion = " /\ /\ \n( o.o )\n > ^ < ".split("\n")

choice = [rat, hunter, lion]


def vs(c1, c2):
    for i in range(3):
        if i == 1:
            print(c1[i] + "  VS  " + c2[i])
            continue
        if c1[i] == "    " and c2[i] == "    ":
            continue
        print(c1[i] + " " * 6 + c2[i])


def check_win(s1, s2):
    if s1 == s2:
        return "d"
    if s1 == 1 and s2 == 2:
        return "s1"
    elif s1 == 2 and s2 == 3:
        return "s1"
    elif s1 == 3 and s2 == 1:
        return "s1"
    return "s2"


for i in range(5):
    print(f"Round {i+1}!")
    print(f"{p1} {p1_score} / {p2} {p2_score}")
    p1_choice = int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
    p2_choice = int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))
    vs(choice[p1_choice - 1], choice[p2_choice - 1])
    print()
    win = check_win(p1_choice, p2_choice)
    if win == "s1":
        p1_score += 1
    elif win == "s2":
        p2_score += 1
    if p1_score == 3 or p2_score == 3:
        print(f"{p1} {p1_score} / {p2} {p2_score}")
        if p1_score == 3:
            print(f"{p1} win!")
        else:
            print(f"{p2} win!")
        break
else:
    print(f"{p1} {p1_score} / {p2} {p2_score}")
    if p1_score == p2_score:
        print("Draw!")
    elif p1_score > p2_score:
        print(f"{p1} win!")
    else:
        print(f"{p2} win!")
