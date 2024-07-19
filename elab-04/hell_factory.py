a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

product = {"A": a, "B": b, "C": c}

product = sorted(product.items(), key=lambda x: x[1], reverse=True)
product = [[x, y] for x, y in product]

product_num = [int(x[1]) for x in product]
product_zero = [x for x in product_num if x == 0]


while len(product_zero) != 2:
    product[0][1] -= 1
    product[1][1] -= 1
    product[2][1] += 1

    product = sorted(product, key=lambda x: x[1], reverse=True)
    product_num = [x[1] for x in product]
    product_zero = [x for x in product_num if x == 0]

print(product[0][0])
