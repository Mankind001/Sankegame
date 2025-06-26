from turtle import Screen,Turtle
from creating_snake import Createsnake, create_wall
from the_logic import Hello
from key_directions import Positioning
import time
import random
def food_func():
    food.goto(random.randint(-380, 380), random.randint(-380, 380))
    food.showturtle()

# def game_over():
#     Hello.u = False
#     screen.bye()
#     print(f"Game Over! Final Score: {Hello.score}")

screen = Screen()
screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(width=800, height=800)
screen.tracer(0)

# Create snake
snake_creator = Createsnake()
p = snake_creator.initial_snake()
create_wall()

# Initialize food
food = Turtle()
food.shape("circle")
food.color("blue")
food.shapesize(0.5, 0.5)
food.penup()
food.hideturtle()


screen.listen()
screen.onkey(Positioning.up, "Up")
screen.onkey(Positioning.down, "Down")
screen.onkey(Positioning.right, "Right")
screen.onkey(Positioning.left, "Left")



food_func()

# Main game loop
while Hello.u:

    screen.update()
    Hello.common_func(p, food)
    time.sleep(Hello.time_delay)

screen.exitonclick()