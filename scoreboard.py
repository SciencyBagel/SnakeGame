from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 22, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # read from high score from file
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())

        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        # check if user got high score
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
