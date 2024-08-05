from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle is gonna win the race ? Enter a color: ")
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']
y_position = [-70,-40,-10,20,50,80]
all_turtles = []

is_race_on = False
for turtle in range(6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230,y=y_position[turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won the winning turtle is {winning_color}.")
                else:
                    print(f"You've lost the winning turtle is {winning_color}.")
            rand_distance = random.randint(0,10)
            turtle.forward(rand_distance)



screen.exitonclick()