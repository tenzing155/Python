import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")

def draw_spirograph(gap_between_circles):
    for i in range(int(360 / gap_between_circles)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + gap_between_circles)
        tim.circle(100)

draw_spirograph(10)




screen = t.Screen()
screen.exitonclick()