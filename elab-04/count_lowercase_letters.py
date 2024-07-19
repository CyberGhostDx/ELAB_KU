words = input("Enter list of words: ")

print(sum([1 for x in words if x.islower()]))
