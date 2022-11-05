import turtle

turtle = turtle.Turtle()

turtle.color('black')
turtle.pensize(1)
turtle.shape("arrow")
turtle.speed(5)


def triangle(edge):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(60)


triangle(100)
triangle(100)
triangle(100)
triangle(100)
triangle(100)
triangle(100)