from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Udemy\snake\data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.update_scoreboard()
        self.hideturtle()

    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}" ,align="center", font=("Arial", 24, "normal"))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Udemy\snake\data.txt","w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    