police_distance = 0
criminal_distance = 100
n = 0
while 1:
    d = int(input("Input distance: "))
    n += 1
    police_distance += d
    criminal_distance += 2**n
    print(f"Police distance: {police_distance}")
    print(f"Criminal distance: {criminal_distance}")
    if police_distance >= criminal_distance:
        print("Caught him!")
        break
