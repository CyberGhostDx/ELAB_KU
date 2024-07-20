w = float(input("Weight: "))
h = float(input("Height: "))


def cal(bmi):
    if bmi >= 30:
        return "You're in the obese range."
    if bmi >= 25:
        return "You're in the overweight range."
    if bmi >= 18.6:
        return "You're in the healthy weight range."
    else:
        return "You're in the underweight range."


bmi = w / (h / 100) ** 2

print(f"Your BMI is {bmi:.1f} {cal(bmi)}")
