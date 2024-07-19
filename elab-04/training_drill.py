d = int(input("Distance from starting point(m.): "))

x = 0
pos = []


while 1:
    if d == 0:
        print(0)
        print("Buzz moved 0 set(s)")
        break
    if x < d:
        x += 5
        pos.append(str(x))
        x -= 2
        pos.append(str(x))
        if x == d:
            print(" ".join(pos))
            print(f"Buzz moved {len(pos)//2} set(s)")
            break
    else:
        x -= 4
        pos.append(str(x))
        x += 3
        pos.append(str(x))
        if x == d:
            print(" ".join(pos))
            print(f"Buzz moved {len(pos)//2} set(s)")
            break
