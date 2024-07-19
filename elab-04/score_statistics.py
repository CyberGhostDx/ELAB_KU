scores = []

while 1:
    score = input("Enter score (or just ENTER to end): ")
    if not score:
        break
    scores.append(int(score))

for i, score in enumerate(scores):
    print(f"Student #{i+1} score: {score}")

score_avg = sum(scores) / len(scores)
score_min = min(scores)
score_max = max(scores)

print(f"Average score is {score_avg:.2f}")
print(f"Minimum score is {score_min}")
print(f"Maximum score is {score_max}")
