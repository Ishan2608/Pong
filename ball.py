from turtle import Turtle

COLOR = "white"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self, x_bounce, y_bounce):
        if y_bounce:
            self.y_move *= -1
        elif x_bounce:
            self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1


