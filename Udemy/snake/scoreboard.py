from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.update_scoreboard()
        self.hideturtle()

    
    def update_scoreboard(self):
        self.write(f"Score : {self.score}" ,align="center", font=("Arial", 24, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score == self.score

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!" ,align="center", font=("Arial", 24, "normal"))