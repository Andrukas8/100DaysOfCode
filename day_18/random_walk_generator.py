from turtle import Turtle, Screen
import random

SIDE = 50
WIDTH = 3
STEPS = 100

tim = Turtle()

screen = Screen()
screen.colormode(255)


def random_walk():
    """
    Generates random walk curve with random colors, and direction
    """
    for i in range(1, STEPS):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        turn = random.choice(["L", "R"])
        direction = random.choice(["F", "B"])
        angle = random.choice([90, 270, 45, 135, 225, 315])

        tim.color(r, g, b)
        tim.width(WIDTH)

        if turn == "L":
            tim.left(angle)
        else:
            tim.right(angle)

        if direction == "F":
            tim.forward(SIDE)
        else:
            tim.backward(SIDE)


def main():

    random_walk()

    screen.exitonclick()


if __name__ == "__main__":
    main()
