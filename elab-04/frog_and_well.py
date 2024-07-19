h = int(input("What is the well's depth? "))
u = int(input("Enter the height the frog can jump up: "))
d = int(input("Enter the height the frog slips down: "))

day = 1
while 1:
    h = h - u
    if u == d and h > 0:
        print("The frog will never escape from the well.")
        break
    if h <= 0:
        print(f"The frog can escape the well on day {day}.")
        break
    print(f"On day {day} the frog leaps to the depth of {h} meters.")
    h = h + d
    print(f"At night he slips down to the depth of {h} meters.")
    day += 1
