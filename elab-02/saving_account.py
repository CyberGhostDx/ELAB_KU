money = float(input("Enter initial amount in Baht: "))
interest_rate = float(input("Enter interest rate in percent: "))
years = [1, 5, 10, 20]

for y in years:
    if y == 1:
        print(
            f"Total amount after {y} year is {money*(1+interest_rate/100)**y:.2f} Baht."
        )
    else:
        print(
            f"Total amount after {y} years is {money*(1+interest_rate/100)**y:.2f} Baht."
        )
