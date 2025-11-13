from ti_system import *
from ti_graphics import *
import time
import random

# --- CONFIG ---
WIDTH = 320
HEIGHT = 240
GRID = 10

# Convert grid coords to pixel coords
def px(x):
    return x * GRID

def py(y):
    return y * GRID

# Snake starting position
snake = [(10, 10), (9, 10), (8, 10)]
direction = "RIGHT"

# Generate food
def new_food():
    return (random.randint(0, (WIDTH//GRID)-1),
            random.randint(0, (HEIGHT//GRID)-1))

food = new_food()

# Input from numpad
def get_direction(dir_now):
    key = get_key()
    if key == "8" and dir_now != "DOWN":
        return "UP"
    if key == "2" and dir_now != "UP":
        return "DOWN"
    if key == "4" and dir_now != "RIGHT":
        return "LEFT"
    if key == "6" and dir_now != "LEFT":
        return "RIGHT"
    return dir_now

# Move the snake
def next_pos(pos, d):
    x, y = pos
    if d == "UP":
        y -= 1
    elif d == "DOWN":
        y += 1
    elif d == "LEFT":
        x -= 1
    elif d == "RIGHT":
        x += 1
    return (x, y)

# MAIN LOOP
while True:
    clear_screen()

    # Get direction from keypad
    direction = get_direction(direction)

    # Compute next head position
    head = snake[0]
    new_head = next_pos(head, direction)

    # Collision with walls
    if new_head[0] < 0 or new_head[0] >= WIDTH//GRID or \
       new_head[1] < 0 or new_head[1] >= HEIGHT//GRID:
        draw_text(50, 100, "BRO YOU HIT A WALL 💀", "white")
        show_screen()
        time.sleep(2)
        break

    # Collision with self
    if new_head in snake:
        draw_text(50, 100, "YOU ATE YOURSELF SMH 💀", "white")
        show_screen()
        time.sleep(2)
        break

    # Add new head
    snake.insert(0, new_head)

    # Check food
    if new_head == food:
        food = new_food()
    else:
        snake.pop()

    # Draw snake
    for s in snake:
        fill_rect(px(s[0]), py(s[1]), GRID, GRID, "green")

    # Draw food
    fill_rect(px(food[0]), py(food[1]), GRID, GRID, "red")

    show_screen()
    time.sleep(0.1)
