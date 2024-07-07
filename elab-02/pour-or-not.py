minutes = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
is_rain = input("Is it raining (y/n)? ")


day = minutes // 1440
hour = minutes % 1440 

if hour >= 720:
    day += 1

if is_rain.lower() == "y":
    is_rain = True
else:
    is_rain = False

print(f">>> {day} days before due.")

if day > 5:
    print(">>> I will not do the assignment.")
elif 5 >= day >= 2:
    if temp > 40 or (temp > 25 and is_rain):
        print(">>> I will not do the assignment.")
    else:
        print(">>> I will do the assignment.")
else:
    print(">>> I will do the assignment.")
