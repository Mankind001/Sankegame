from turtle import Turtle


class Createsnake:
    def __init__(self):
        self.initial_snake_length=3
        self.p = []
        self.e=0


    def initial_snake(self):
        for i in range(self.initial_snake_length):
            b = Turtle(shape='square')
            b.color("white")
            self.p.append(b)
        for i in self.p:
            i.penup()
            i.goto(-self.e, 0)
            self.e += 20
        self.p[0].color("red")
        return self.p

def create_wall():
    line = Turtle()
    line.shape("square")
    line.color("grey")
    line.penup()
    line.goto(400, 400)
    line.pendown()
    line.pensize(20)
    line.goto(400, -400)
    line.goto(-400, -400)
    line.goto(-400, 400)
    line.goto(400, 400)
    line.hideturtle()