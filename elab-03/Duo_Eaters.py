def eat(S, P, G):
    paun = S // P
    gane = S % P // G
    dog = S % P % G
    return (paun, gane, dog)


starting = int(input("Input starting food (S): "))
paun = int(input("Input Paun's eating rate (P): "))
gane = int(input("Input Gane's eating rate (G): "))

e = eat(starting, paun, gane)

print(f"Paun eats {e[0]} time(s)")
print(f"Gane eats {e[1]} time(s)")
print(f"Remaining {e[2]} for dog")
