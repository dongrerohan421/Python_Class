import turtle

def draw_flower():

    window = turtle.Screen()
    window.bgcolor("Black")

    flower = turtle.Turtle()
    flower.color("Pink")
    flower.speed(10)

    for i in range(18):
        draw_circle(flower)
        flower.right(20)
    flower.right(90)

    flower.color("Green")
    flower.pensize(10)
    draw_line(flower)

    window.exitonclick()

def draw_circle(a_turtle):
    a_turtle.circle(75)

def draw_line(a_turtle):
    a_turtle.forward(300)

draw_flower()
