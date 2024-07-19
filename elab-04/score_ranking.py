scores = []

while 1:
    score = input("Enter score (or just ENTER to end): ")
    if not score:
        break
    scores.append(int(score))

scores.sort(reverse=True)

for i, score in enumerate(scores):
    print(f"Rank #{i+1}: {score}")
