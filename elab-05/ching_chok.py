lucky = int(input("Enter lucky number : "))
n = int(input("Enter amount of candidates : "))
id_list = []
id_r = []

for i in range(n):
    id = input(f"Enter ID card number {i+1}: ")
    id_list.append(int(id))
    id_r.append(id.replace(str(lucky), ""))

pair = min(enumerate(id_r), key=lambda x: len(x[1]))
max_num = len(str(id_list[pair[0]])) - len(pair[1])

winner = list(
    filter(
        lambda x: len(str(x)) - len(str(x).replace(str(lucky), "")) == max_num, id_list
    )
)

print(f"Winner: {max(winner)}")
