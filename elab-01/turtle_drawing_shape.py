from turtlelab4 import turtle, check


def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


def draw_triangle(size):
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)


draw_square(100)
draw_triangle(200)
