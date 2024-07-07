chars = ["a", "b", "c", "d", "e"]
numbers = []


def sd(arr, mean):
    sum_square = 0
    for i in arr:
        sum_square += (i-mean)**2
    return (sum_square/len(arr))**(1/2)


for char in chars:
    numbers.append(float(input(f"Input {char}: ")))

mean = f"{sum(numbers)/len(numbers):.3f}"

print(f"mean: {mean}")
print(f"sd: {sd(numbers,float(mean)):.3f}")
