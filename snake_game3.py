import curses
import time
from curses import textpad
import random


def direction(direct, new_direct):
    if new_direct == curses.KEY_RIGHT and direct != curses.KEY_LEFT or \
            new_direct == curses.KEY_LEFT and direct != curses.KEY_RIGHT or \
            new_direct == curses.KEY_DOWN and direct != curses.KEY_UP or \
            new_direct == curses.KEY_UP and direct != curses.KEY_DOWN:
        direct = new_direct
    return direct


def snake_move(direct, snake):
    for i in range(1, len(snake)):
        snake[i] = snake[i - 1]
        if direct == curses.KEY_RIGHT:
            snake[0] = [snake[0][0], snake[0][1] + 1]
        elif direct == curses.KEY_LEFT:
            snake[0] = [snake[0][0], snake[0][1] - 1]
        elif direct == curses.KEY_UP:
            snake[0] = [snake[0][0] - 1, snake[0][1]]
        elif direct == curses.KEY_DOWN:
            snake[0] = [snake[0][0] + 1, snake[0][1]]
    return snake


def create_head(snake, direct):
    new_head = [None, None]
    if direct == curses.KEY_RIGHT:
        new_head = [snake[0][0], snake[0][1] + 1]
    elif direct == curses.KEY_LEFT:
        new_head = [snake[0][0], snake[0][1] - 1]
    elif direct == curses.KEY_DOWN:
        new_head = [snake[0][0] + 1, snake[0][1]]
    elif direct == curses.KEY_UP:
        new_head = [snake[0][0] - 1, snake[0][1]]
    return new_head


def new_food(height, width, snake):
    n_food = (random.randint(1, height - 2), random.randint(1, width - 2))
    while n_food in snake:
        n_food = (random.randint(1, height - 2), random.randint(1, width - 2))
    return n_food


def is_game_over(width, height, snake):
    if snake[0][0] == 0 or snake[0][0] == height - 1 or \
            snake[0][1] == 0 or snake[0][1] == width - 1:
        return True
    if snake[0] in snake[1:]:
        return True
    return False


def play(std_scr):
    curses.curs_set(0)
    std_scr.nodelay(1)
    delay = 300
    std_scr.timeout(delay)
    height, width = std_scr.getmaxyx()
    score, highest_score = 0, 0
    snake = [[10, 5], [10, 4]]
    food = [10, 30]
    direct = curses.KEY_RIGHT
    std_scr.addstr(2, 2, f"score: {score} Highest score: {highest_score}")

    while not is_game_over(width, height, snake):
        std_scr.refresh()
        new_direct = std_scr.getch()
        direct = direction(direct, new_direct)
        snake = snake_move(direct, snake)
        std_scr.addstr(food[0], food[1], "f")

        if snake[0] == food:
            std_scr.refresh()
            score += 1
            std_scr.addstr(2, 2, f"score: {score} Highest score: {highest_score}")
            food = new_food(height, width, snake)
            std_scr.addstr(food[0], food[1], "f")
            snake.append(create_head(snake, direct))
            std_scr.timeout(delay)

        std_scr.clear()
        std_scr.addstr(food[0], food[1], "f")
        std_scr.addstr(1, 2, f"score: {score} Highest score: {highest_score}")
        for sn in snake:
            std_scr.addstr(sn[0], sn[1], "s")
        std_scr.refresh()


curses.wrapper(play)
