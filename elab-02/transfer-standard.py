age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))

def calc(age,income):
    if(age > 60 or age < 15): return "Invalid age."
    if(30000 >= income >= 1):
        return f"Your negative income tax is {income*0.2:.2f} Baht."
    elif 80000 > income > 30000:
        return f"Your negative income tax is {6000-(income-30000)*0.12:.2f} Baht."
    elif income >= 80000:
        return "Invalid income."

print(calc(age,income))
