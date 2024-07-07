m = int(input("How long have Buzz played ?: "))

hour = m // 60

if m % 60 > 20:
    hour += 1
price = hour*900

if (4 > hour >= 2):
    price = hour*900*0.9
elif hour == 4:
    price = hour*900*0.8
elif hour >= 5:
    price = hour*900*0.7
