import turtle
from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
turtle.colormode(255)


def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple

def make_a_square():
    for i in range (1,5):
        muf.forward(100)
        muf.left(90)


def make_a_dashed_square():
    is_finished = False
    while not is_finished:
        for i in range (4):
            for _ in range (10):
                muf.forward(10)
                muf.up()
                muf.forward(10)
                muf.down()
            muf.left(90)
        is_finished = True


def draw_multiple_shapes():
    angle = 360
    for i in range(3, 11):
        muf.color(random.choice(colours))
        for k in range(i):
            turn_angle = angle / i
            muf.right(turn_angle)
            muf.forward(100)


def draw_spirograph(desired_degree):
    """ Set the desired tilting angle of each circles in order to create your own unique spirograph """
    muf.speed("fastest")
    for _ in range(int(360/desired_degree)):
        muf.color(random_color_generator())
        muf.circle(100)
        muf.left(desired_degree)


def random_walk():
    possibilities = [0, 90, 180, 270]
    muf.pensize(5)
    muf.hideturtle()
    muf.speed("fast")
    for _ in range(500):
        muf.color(random_color_generator())
        muf.forward(20)
        muf.setheading(random.choice(possibilities))



muf = Turtle()
muf.shape("turtle")
muf.color("red")
# make_a_square()

# make_a_dashed_square()

# draw_multiple_shapes()

random_walk()

# draw_spirograph(5)










screen = Screen()
screen.exitonclick()
