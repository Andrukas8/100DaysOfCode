from turtle import Turtle, Screen
import random

SIDE = 100
tim = Turtle()

screen = Screen()
screen.colormode(255)


def build_figures(sides):
    """
    Generates poligons from triangle to whatever number of
    sides is provided as an argument. Every poligon has its random color.
    """
    for i in range(3, sides + 1):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        tim.color(r, g, b)
        for _ in range(1, i + 1):
            tim.forward(SIDE)
            tim.right(360 / i)


def main():

    # Move the Turtle to a more convenient position:
    tim.penup()
    tim.goto(-50, 300)
    tim.pendown()

    build_figures(10)

    screen.exitonclick()


if __name__ == "__main__":
    main()
