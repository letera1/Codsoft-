from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
INITIAL_SPEED = 250  # Initial speed of the snake
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "yellow"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinate = [x, y]
        self.shape = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    global direction, SPEED

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Check for collision with the boundaries of the game window
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        game_over()
        return

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinate[0] and y == food.coordinate[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete(food.shape)
        food = Food()
        # Gradually increase SPEED based on score
        SPEED = max(50, INITIAL_SPEED - (score * 2))  # Increase the speed incrementally based on score
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    direction = new_direction


def on_key_press(e):
    directions = ["up", "down", "left", "right"]
    key = e.keysym.lower()
    if key in directions:
        if (key == "up" and direction != "down") or \
                (key == "down" and direction != "up") or \
                (key == "left" and direction != "right") or \
                (key == "right" and direction != "left"):
            change_direction(key)


def game_over():
    global SPEED
    SPEED = 0
    canvas.create_text(GAME_WIDTH / 2, GAME_HEIGHT / 2, text="Game Over!", font=("Helvetica", 36), fill="white",
                       anchor="center")


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'
label = Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

snake = Snake()
food = Food()
SPEED = INITIAL_SPEED  # Set initial speed
next_turn(snake, food)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind("<KeyPress>", on_key_press)
window.mainloop()
