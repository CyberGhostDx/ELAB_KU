age = int(input("Enter your age : "))


def cal(y):
    if y >= 60:
        return "Senior Adult"
    if y >= 19:
        return "Adult"
    if y >= 13:
        return "Adolescence"
    return "Child"


print(f"You are {cal(age)}.")
