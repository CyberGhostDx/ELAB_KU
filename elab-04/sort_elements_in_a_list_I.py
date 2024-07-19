nums = input("Enter list of tuple: ")
nums_list = nums.split()

tuple_list = [tuple([int(y) for y in x]) for x in nums_list]
sorted_tuble_list = sorted(tuple_list, key=lambda x: x[-1])

print(f"Input list: {tuple_list}")
print(f"Output list: {sorted_tuble_list}")
