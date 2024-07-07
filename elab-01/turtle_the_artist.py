from turtlelab7 import turtle, check


def draw_polygon(n, size):
    for _ in range(n):
        turtle.forward(size)
        turtle.left(180-180*(n-2)/n)


draw_polygon(3, 100)

check()
