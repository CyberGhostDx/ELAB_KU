scores = []


def std_s(samples):
    mean = sum(samples) / len(samples)
    sst = sum([(sample - mean) ** 2 for sample in samples])
    return (sst / (len(samples) - 1)) ** 0.5


def calc_grade(score, mean, sd):
    if score >= mean + 1.5 * sd:
        return "A"
    if mean + sd <= score < mean + 1.5 * sd:
        return "B+"
    if mean + 0.5 * sd <= score < mean + sd:
        return "B"
    if mean <= score < mean + 0.5 * sd:
        return "C+"
    if mean - 0.5 * sd <= score < mean:
        return "C"
    if mean - sd <= score < mean - 0.5 * sd:
        return "D+"
    if mean - 1.5 * sd <= score < mean - sd:
        return "D"
    return "F"


while 1:
    score = input("Enter score (or just ENTER to end): ")
    if not score:
        break
    scores.append(int(score))

avg = sum(scores) / len(scores)
sd = std_s(scores)

score_reports = [(score, calc_grade(score, avg, sd)) for score in scores]

print(f"Average score is {avg:.2f}")
print(f"Standard deviation is {sd:.2f}")
for i, (score, grade) in enumerate(score_reports):
    print(f"Student #{i+1} score: {score} grade: {grade}")
