import turtle
import time
import random

highest_score = 0

# window for the game
wind = turtle.Screen()
wind.title("Snake Game")
wind.bgcolor("#34c9eb")
wind.setup(width=600, height=600)

# the head of the snake
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.penup()
snake_head.shape("square")
snake_head.color("brown")
snake_head.goto(0, 0)
snake_head.direction = "stop"


def create_food():
    """this function creates food on the window randomly
    """

    food = turtle.Turtle()
    food.penup()
    food.shape("circle")
    food.color("red")
    food.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))
    return food


def create_tail():
    """this function creates tail for the snake if it eats the food
    """

    tail = turtle.Turtle()
    tail.shape("square")
    tail.color("brown")
    tail.penup()
    tail.speed(0)
    return tail


# for type anything on the game window
pen = turtle.Turtle()
pen.penup()
pen.color("black")
pen.goto(0, 250)


def go_up():

    """changes the direction of the snake's head upwards
    """

    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():

    """changes the direction of the snake's head downwards
    """

    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left():

    """changes the direction of the snake's head to the left
    """

    if snake_head.direction != "right":
        snake_head.direction = "left"


def go_right():

    """changes the direction of the snake's head to the right
    """

    if snake_head.direction != "left":
        snake_head.direction = "right"


def move():

    """moves the snake in a given direction
    """

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


def is_game_over(head, lst):

    """game end conditions
    """

    if head.xcor() < -290 or head.xcor() > 290 or head.ycor() < -290 or head.ycor() > 290:
        return True
    for each in lst:
        if each.distance(head) < 20:
            return True
    return False


def play():
    global highest_score
    score = 0
    delay_time = 0.4
    snake_body = []
    food = create_food()
    while True:
        wind.update()
        if not is_game_over(snake_head, snake_body):
            pen.clear()
            pen.write(f"Score : {score}   Highest Score : {highest_score}", align="center", font=("caddr", 20, "bold"))

            if snake_head.distance(food) < 20:
                snake_body.append(create_tail())
                score += 1
                create_food()

            if score > 0 and score % 10 == 0 and delay_time > 0:
                delay_time -= 0.1

            for i in range(len(snake_body) - 1, -1, -1):
                if i > 0:
                    snake_body[i].goto(snake_body[i - 1].xcor(), snake_body[i - 1].ycor())
                else:
                    snake_body[0].goto(snake_head.xcor(), snake_head.ycor())
        else:
            if highest_score < score:
                highest_score = score
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_body.clear()
            snake_head.direction = "Stop"
            pen.clear()
            pen.write(f"Score : {score}   Highest Score : {highest_score}", align="center", font=("caddr", 20, "bold"))
            play()

        move()
        time.sleep(delay_time)


play()
