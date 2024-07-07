Man_res = input("What's the result of Manchester city's match? ")
liver_res = input("What's the result of Liverpool's match? ")

if (Man_res == "won" and liver_res == "lost"):
    print("Manchester city is the champion of Premier League.")
elif (Man_res == "lost" and liver_res == "won"):
    print("Liverpool's is the champion of Premier League.")
elif (Man_res == "won" and liver_res == "won"):
    man_won = int(input("What is the margin that Manchester city won by? "))
    liver_won = int(input("What is the margin that Liverpool won by? "))
    if (man_won > liver_won):
        print("Manchester city is the champion of Premier League.")
    elif (man_won < liver_won):
        print("Liverpool is the champion of Premier League.")
    elif (man_won == liver_won):
        win = input(
            "Which team won the play-off match?(Manchester city/Liverpool) ")
        print(f"{win} is the champion of Premier League.")
