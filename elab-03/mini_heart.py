import math


def MiniHeart(l):
    return l * l + math.pi * (l / 2) ** 2


L = float(input("Please enter the value of L: "))
print(f"Area is {MiniHeart(L):.4f}")
