
import random
from turtle import Turtle, Screen
from tkinter import messagebox

from score import Score


scoreboard = Score(-240, 360, 0)
class Hello:
    current_direction = 0
    score = -1
    time_delay = 0.1
    u = True

    @staticmethod
    def common_func(p, food):

        if not Hello.u:
            return

        prev_positions = []
        for seg in p:
            prev_positions.append((seg.xcor(), seg.ycor()))


        p[0].setheading(Hello.current_direction)
        p[0].forward(20)


        for i in range(1, len(p)):
            # p[i].goto(prev_positions[i-1])
            new_x, new_y = prev_positions[i - 1]
            p[i].penup()
            p[i].color("darkgreen")
            p[i].goto(new_x, new_y)


        if p[0].distance(food) < 15:
            Hello.handle_food_collision(p, food)


        Hello.check_wall_collision(p[0])
        # Hello.check_body_collision(p)

    @staticmethod
    def handle_food_collision(p, food):
        food.hideturtle()
        Hello.score += 1
        Hello.update_speed()
        food.goto(random.randint(-380, 380), random.randint(-380, 380))
        food.showturtle()
        scoreboard.increase()

        p.append(Turtle(shape='square'))

    @staticmethod
    def update_speed():
        if Hello.score < 5:
            Hello.time_delay = 0.1
        elif Hello.score < 10:
            Hello.time_delay = 0.085
        elif Hello.score < 15:
            Hello.time_delay = 0.065
        elif Hello.score < 20:
            Hello.time_delay = 0.045
        else:
            Hello.time_delay = 0.030


    @staticmethod
    def check_wall_collision(head):
        if abs(head.xcor()) >= 390 or abs(head.ycor()) >= 390:
            Hello.game_over()


    @staticmethod
    def game_over():
        scoreboard.highscore_update()
        Hello.u = False
        Screen().update()
        messagebox.showinfo("Game Over", f"Score: {Hello.score+1}")

