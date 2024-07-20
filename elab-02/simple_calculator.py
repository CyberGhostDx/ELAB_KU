x = float(input("x: "))
operator = input("Operator: ")
y = float(input("y: "))

if operator == "+":
    print(int(x + y))
elif operator == "-":
    print(int(x - y))
elif operator == "*":
    print(int(x * y))
elif operator == "/":
    print(f"{x/y:.2f}")
elif operator == "%":
    print(int(x % y))
else:
    print("Unknown Operator")
