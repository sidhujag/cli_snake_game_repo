import random
import curses

def main(stdscr):
    # Initial setup
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.border(0)

    # Snake initial position
    snake = [[sh//2, sw//4], [sh//2, sw//4-1], [sh//2, sw//4-2]]
    food = [sh//2, sw//2]
    w.addch(food[0], food[1], curses.ACS_PI)
    score = 0

    # Game logic
    key = curses.KEY_RIGHT
    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        if snake[0][0] in [0, sh-1] or \
           snake[0][1] in [0, sw-1] or \
           snake[0] in snake[1:]:
            msg = "Game Over! Score: {}".format(score)
            w.addstr(sh//2, sw//2-len(msg)//2, msg)
            w.nodelay(0)
            w.getch()
            break

        new_head = [snake[0][0], snake[0][1]]

        # Control mechanism
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        # Collision detection with food
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [random.randint(1, sh-2), random.randint(1, sw-2)]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

curses.wrapper(main)
