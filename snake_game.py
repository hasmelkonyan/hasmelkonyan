import turtle
import time
import random

highest_score = 0
delay_time = 0.4
snake_body = []

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
pen.color("black")
pen.goto(0, 250)


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
    if snake_head.direction == "down":
        snake_head.sety(snake_head.ycor() - 20)
    if snake_head.direction == "right":
        snake_head.setx(snake_head.xcor() + 20)
    if snake_head.direction == "left":
        snake_head.setx(snake_head.xcor() - 20)


wind.listen()
wind.onkeypress(go_up, "Up")
wind.onkeypress(go_up, "Down")
wind.onkeypress(go_left, "Left")
wind.onkeypress(go_right, "Right")


def play():
    score = 0
    global highest_score
    while True:
        wind.update()
        pen.write(f"Score : {score}   Highest_Score : {highest_score}", align="center", font=("caddr", 20, "bold"))
        if snake_head.distance(food) < 20:
            food.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))
            tail = turtle.Turtle()
            tail.color("brown")
            tail.shape("square")
            tail.penup()
            tail.speed(0)
            snake_body.append(tail)
            score += 1

        for i in range(len(snake_body) - 1, -1, -1):
            if i > 0:
                snake_body[i].goto(snake_body[i - 1].xcor(), snake_body[i - 1].ycor())
            else:
                snake_body[0].goto(snake_head.xcor(), snake_head.ycor())
        if snake_head.xcor() > 280 or snake_head.xcor() < -280 or snake_head.ycor() > 280 or snake_head.ycor() < -280:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_body.clear()
            food.goto(0, 100)
            if highest_score < score:
                highest_score = score
                snake_head.direction = "stop"
            play()

        for each in snake_body:
            if each.dictance(snake_head) < 20:
                time.sleep(1)
                snake_head.goto(0, 0)
                snake_body.clear()
                food.goto(0, 100)
                if highest_score < score:
                    highest_score = score
                    snake_head.direction = "stop"
            play()


        move()
        time.sleep(delay_time)



play()


