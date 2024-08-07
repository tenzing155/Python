from turtle import Turtle,Screen

tim = Turtle()

def trinagle():
    tim.color("purple")
    for i in range(3):
        tim.forward(100)
        tim.right(120)
trinagle()

def sqaure():
    tim.color("green")
    for i in range(4):
        tim.forward(100)
        tim.right(90)
sqaure()

def pentagon():
    tim.color("red")
    for i in range(5):
        tim.forward(100)
        tim.right(72)
pentagon()

def hexagon():
    tim.color("blue")
    for i in range(6):
        tim.forward(100)
        tim.right(60)
hexagon()

def heptagon():
    tim.color("grey")
    for i in range(7):
        tim.forward(100)
        tim.right(51.42)
heptagon()

def octagon():
    tim.color("dark blue")
    for i in range(8):
        tim.forward(100)
        tim.right(45)
octagon()
   
def nonagon():
    tim.color("pink")
    for i in range(9):
        tim.forward(100)
        tim.right(40)
nonagon()

def decagon():
    tim.color("orange")
    for i in range(10):
        tim.forward(100)
        tim.right(36)
decagon()



screen = Screen()
screen.mainloop()