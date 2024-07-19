def DrawRat():
    s = '__QQ\n()">\n'
    print(s)


def DrawHunter():
    s = " O\n/|\ \n/ \ \n"
    print(s)


def DrawLion():
    s = " /\_/\ \n( o.o )\n > ^ <\n"
    print(s)


def check_draw(c):
    if c == 1:
        DrawRat()
    if c == 2:
        DrawHunter()
    if c == 3:
        DrawLion()


def check_winner(c1, c2):
    if c1 == 1 and c2 == 2:
        return True
    elif c1 == 2 and c2 == 3:
        return True
    elif c1 == 3 and c2 == 1:
        return True
    elif c1 == c2:
        return "draw"
    return False


p1 = input("Player1 name: ")
p2 = input("Player2 name: ")

p1_score = 0
p2_score = 0

print("\nRound 1!")
print(f"{p1} 0 / {p2} 0")

p1_choice = int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
p2_choice = int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))

print("\n" + p1)
check_draw(p1_choice)

print("VS\n")

print(p2)
check_draw(p2_choice)

if check_winner(p1_choice, p2_choice) and check_winner(p1_choice, p2_choice) != "draw":
    p1_score += 1
elif check_winner(p1_choice, p2_choice) != "draw":
    p2_score += 1

# round 2

print("Round 2!")
print(f"{p1} {p1_score} / {p2} {p2_score}")

p1_choice = int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
p2_choice = int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))

print("\n" + p1)
check_draw(p1_choice)

print("VS\n")

print(p2)
check_draw(p2_choice)

if check_winner(p1_choice, p2_choice) and check_winner(p1_choice, p2_choice) != "draw":
    p1_score += 1
elif check_winner(p1_choice, p2_choice) != "draw":
    p2_score += 1

if p1_score == 2 and p2_score == 0:
    print(f"{p1} {p1_score} / {p2} {p2_score}")
    print(p1, "win!")
elif p1_score == 0 and p2_score == 2:
    print(f"{p1} {p1_score} / {p2} {p2_score}")
    print(p2, "win!")
else:
    # round 3

    print("Round 3!")
    print(f"{p1} {p1_score} / {p2} {p2_score}")
    p1_choice = int(input(f"{p1}'s choice (1/rat, 2/hunter and 3/lion): "))
    p2_choice = int(input(f"{p2}'s choice (1/rat, 2/hunter and 3/lion): "))

    print("\n" + p1)
    check_draw(p1_choice)

    print("VS\n")

    print(p2)
    check_draw(p2_choice)

    if (
        check_winner(p1_choice, p2_choice)
        and check_winner(p1_choice, p2_choice) != "draw"
    ):
        p1_score += 1
    elif check_winner(p1_choice, p2_choice) != "draw":
        p2_score += 1

    print(f"{p1} {p1_score} / {p2} {p2_score}")
    if p1_score == p2_score:
        print("Draw!")
    elif p1_score > p2_score:
        print(p1, "win!")
    else:
        print(p2, "win!")
