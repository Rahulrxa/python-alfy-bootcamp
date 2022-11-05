import turtle

display = turtle.Screen()
turtle = turtle.Turtle()

turtle.color('black')
turtle.pensize(1)
turtle.shape("arrow")
turtle.speed(5)


def rectangle(edge):
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)


def triangle(edge):
    turtle.right(60)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)

def ears():
    turtle.circle(30)
    turtle.circle(20)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.circle(30)
    turtle.circle(20)

def eyes():
    turtle.penup()
    turtle.setpos(20, -40)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()
    turtle.circle(10)

rectangle(100)
ears()
eyes()

turtle.penup()
turtle.setpos(50, -45)
turtle.pendown()

triangle(15)

turtle.penup()
turtle.setpos(30, -75)
turtle.pendown()
turtle.right(120)
turtle.circle(25, 120)

#Hide arrow
turtle.hideturtle()

#Wait for user to close the display
display.mainloop()
