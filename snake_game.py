import turtle
import time
import random

score = 0
highest_score = 0
delay_time = 0.4

wind = turtle.Screen()
wind.title("Snake Game")
wind.bgcolor("#34c9eb")
wind.setup(width=600, height=600)

snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.penup()
snake_head.shape("square")
snake_head.color("brown")
snake_head.goto(0, 0)
snake_head.direction = "stop"

food = turtle.Turtle()
food.penup()
food.shape("circle")
food.color("red")
food.goto(0, 100)

pen = turtle.Turtle()
pen.penup()
pen.color("white")
pen.goto(0, 250)
pen.write(f"Score : {score}   Highest_Score : {highest_score}", align="center", font=("caddr", 20, "bold"))


def go_up():
    snake_head.direction = "up"


def go_down():
    snake_head.direction = "down"


def go_left():
    snake_head.direction = "left"


def go_right():
    snake_head.direction = "right"


def move():
    if snake_head.direction == "up":
        snake_head.sety(snake_head.ycor() + 20)
    elif snake_head.direction == "down":
        snake_head.sety(snake_head.ycor() - 20)
    elif snake_head.direction == "right":
        snake_head.setx(snake_head.xcor() + 20)
    elif snake_head.direction == "left":
        snake_head.setx(snake_head.xcor() - 20)


wind.listen()
wind.onkeypress(go_up, "Up")
wind.onkeypress(go_up, "Down")
wind.onkeypress(go_left, "Left")
wind.onkeypress(go_right, "Right")


while True:
    wind.update()
    time.sleep(delay_time)

    if snake_head.distance(food) < 20:
        food.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))


    move()

