import random
import curses

screen = curses.initscr()
curses.curs_set(0)
screen_hight, screen_width = screen.getmaxyx()
window = curses.newwin(screen_hight, screen_width, 0, 0)
window.keypad(1)
window.timeout(100)

snake_x = screen_width // 4
snake_y = screen_hight // 2

snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

food = [snake_y // 2, snake_x // 2]
window.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key
    
    head_y, head_x = snake[0][0], snake[0][1]
    if head_y >= screen_hight - 1 or head_y <= 0 or head_x >= screen_width - 1 or head_x <= 0 or snake[0] in snake[1:]:
        curses.endwin()
        quit()
        
    new_head = [snake[0][0], snake[0][1]]
    
    if key == curses.KEY_DOWN:
        new_head[0] += 1    
    elif key == curses.KEY_UP:
        new_head[0] -= 1    
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1    
    elif key == curses.KEY_LEFT:
        new_head[1] -= 1
        
    snake.insert(0, new_head)
    
    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, screen_hight - 2),
                random.randint(1, screen_width - 2)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tall = snake.pop()
        window.addch(tall[0], tall[1], " ")
        
    
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)