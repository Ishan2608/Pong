from turtle import Turtle
import random

FONT = ("Courier", 52, "normal")
ALIGNMENT = 'center'
COLOR = "white"
COLOR_LIST = ['light blue', 'royal blue', 'light steel blue', 'steel blue',
              'light cyan', 'light sky blue', 'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink', 'medium sea green', 'khaki']


class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(10)
        self.color(random.choice(COLOR_LIST))
        self.text_display()

    def text_display(self):
        self.clear()
        self.dashed_line()
        self.goto(0, -30)
        self.write(f"Pong Game", align=ALIGNMENT, font=FONT)
        self.goto(0, 0)
        self.draw_circle()

    def dashed_line(self):
        self.penup()
        self.goto(0, -290)
        self.setheading(90)
        while self.ycor() < 290:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.setheading(0)

    def draw_circle(self):
        self.goto(0, -200)
        self.pendown()
        self.circle(200)
        self.penup()

    def change_color(self):
        self.color(random.choice(COLOR_LIST))
        self.text_display()
