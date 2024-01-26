import random
import curses

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor
sh, sw = stdscr.getmaxyx()  # Get the width and height of the screen
w = curses.newwin(sh, sw, 0, 0)  # Create a new window using the screen height and width
w.keypad(1)
w.timeout(100)  # Refresh the screen every 100 milliseconds

# Create the snake's initial position
snk_x = sw//4
snk_y = sh//2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Create the food's initial position
food = [sh//2, sw//2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# Initial direction the snake moves towards
key = curses.KEY_RIGHT

# Game logic
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Check if snake has hit the border or itself
    if snake[0][0] in [0, sh] or \
        snake[0][1]  in [0, sw] or \
        snake[0] in snake[1:]:
        curses.endwin()
        quit()

    # Determine the new head of the snake
    new_head = [snake[0][0], snake[0][1]]

    # Move the snake
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert the new head of the snake
    snake.insert(0, new_head)

    # Check if snake got the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
import random
import curses

def create_food(snake, box):
    food = None
    while food is None:
        food = [random.randint(box[0][0]+1, box[1][0]-1), random.randint(box[0][1]+1, box[1][1]-1)]
        if food in snake:
            food = None
    return food

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3, sw-3]]
    stdscr.box()

    snake = [[sh//2, sw//2 + 1], [sh//2, sw//2], [sh//2, sw//2 - 1]]
    direction = curses.KEY_RIGHT
    for y, x in snake:
        stdscr.addch(y, x, '#')

    food = create_food(snake, box)
    stdscr.addch(food[0], food[1], '*')

    score = 0

    while True:
        next_key = stdscr.getch()
        if next_key == -1:
            key = direction
        else:
            key = next_key

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]:
            direction = key

        head = [snake[0][0], snake[0][1]]

        if direction == curses.KEY_RIGHT:
            head[1] += 1
        if direction == curses.KEY_LEFT:
            head[1] -= 1
        if direction == curses.KEY_DOWN:
            head[0] += 1
        if direction == curses.KEY_UP:
            head[0] -= 1

        snake.insert(0, head)

        if snake[0] == food:
            score += 1
            food = create_food(snake, box)
            stdscr.addch(food[0], food[1], '*')
        else:
            stdscr.addch(snake[-1][0], snake[-1][1], ' ')
            snake.pop()

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1]  in [box[0][1], box[1][1]] or
            snake[0] in snake[1:]):
            break

        stdscr.addch(snake[0][0], snake[0][1], '#')

    stdscr.addstr(sh//2, sw//2 - len("Game Over!")//2, "Game Over!")
    stdscr.nodelay(0)
    stdscr.getch()

    stdscr.addstr(sh//2 + 1, sw//2 - len(f"Final Score: {score}")//2, f"Final Score: {score}")
    stdscr.getch()

curses.wrapper(main)
import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT
score = 0

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or \
        snake[0][1]  in [0, sw] or \
        snake[0] in snake[1:]:
        curses.endwin()
        quit()
    
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')
    
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
