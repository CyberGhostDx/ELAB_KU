amount = float(input("Enter buying amount: "))

if amount >= 3000:
    print(f"Amount due after discount is {amount*0.85:.2f} baht.")
elif amount >= 1000 and amount < 3000:
    print(f"Amount due after discount is {amount*0.9:.2f} baht.")
else:
    print(f"Amount due after discount is {amount} baht.")
