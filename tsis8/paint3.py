import pygame

pygame.init()
sc = pygame.display.set_mode((800, 600))
surf = pygame.Surface((700, 600))
buttons = pygame.Surface((100, 210))  # creating a button bar
font = pygame.font.SysFont("Verdana", 15)
cur_color = 'white'  # current color that can be changed
# create command dictionary
commands = {
    'line': [4, 4, 44, 44],
    'rect': [52, 4, 44, 44],
    'circle': [4, 50, 44, 44],
    'eraser': [52, 50, 44, 44]
}


# function to set the panel with buttons
def setsurf():
    surf.fill('black')
    buttons.fill('white')
    pygame.draw.rect(buttons, 'black', (2, 2, 96, 206), 1)
    pygame.draw.aaline(buttons, 'black', (8, 8), (40, 40), 1)
    pygame.draw.rect(buttons, 'black', (58, 10, 32, 32), 1)
    pygame.draw.circle(buttons, 'black', (27, 70), 15, 1)
    pygame.draw.rect(buttons, 'black', (56, 58, 36, 28))
    sc.blit(surf, (0, 0))
    sc.blit(buttons, (700, 0))


# line drawing function
def line(sc, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(sc, color, (x, y), d)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(sc, color, (x, y), d)


# function to draw a rectangle
def rectangle(sc, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.rect(sc, color, (x1, y1, width, height), d)
        else:
            pygame.draw.rect(sc, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pygame.draw.rect(sc, color, (x2, y1, width, height), d)
        else:
            pygame.draw.rect(sc, color, (x2, y2, width, height), d)


# function to draw a circle
def circle(sc, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1 - x2)
    height = abs(y1 - y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.ellipse(sc, color, (x1, y1, width, height), d)
        else:
            pygame.draw.ellipse(sc, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pygame.draw.ellipse(sc, color, (x2, y1, width, height), d)
        else:
            pygame.draw.ellipse(sc, color, (x2, y2, width, height), d)


last_pos = (0, 0)
w = 2
draw_line = False
erase = False
ed = 50

d = {
    'line': True,
    'rect': False,
    'circle': False,
    'eraser': False
}

setsurf()
running = True
while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # change colors on keypress
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                cur_color = 'red'
            if event.key == pygame.K_2:
                cur_color = 'green'
            if event.key == pygame.K_3:
                cur_color = 'blue'
            if event.key == pygame.K_4:
                cur_color = 'white'
                # when you click on the area of a certain button, we change the value of the corresponding command to True in the command dictionary
        if event.type == pygame.MOUSEBUTTONDOWN:
            for k, v in commands.items():
                if v[0] <= pos[0] - 700 <= v[0] + v[2] and v[1] <= pos[1] <= v[1] + v[3]:
                    d[k] = True
                    for i, j in d.items():
                        if i != k:
                            d[i] = False
                    break
        # run the functions of the corresponding commands
        if d['line'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
                pygame.draw.circle(surf, cur_color, pos, w)
                draw_line = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_line = False
            if event.type == pygame.MOUSEMOTION:
                if draw_line:
                    line(surf, last_pos, pos, w, cur_color)
                last_pos = pos
        elif d['rect'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                rectangle(surf, last_pos, pos, w, cur_color)
        elif d['circle'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                circle(surf, last_pos, pos, w, cur_color)
        elif d['eraser'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pos
                pygame.draw.rect(surf, 'black', (x, y, ed, ed))
                erase = True
            if event.type == pygame.MOUSEMOTION:
                if erase:
                    pygame.draw.rect(surf, 'black', (pos[0], pos[1], ed, ed))
            if event.type == pygame.MOUSEBUTTONUP:
                erase = False
    # highlight the selected command with a red frame
    for k, v in d.items():
        if v == True:
            pygame.draw.rect(buttons, 'red', commands[k], 1)
        else:
            pygame.draw.rect(buttons, 'black', commands[k], 1)

    sc.blit(buttons, (700, 0))
    sc.blit(surf, (0, 0))
    c = font.render('Press:', True, 'black')
    buttons.blit(c, (5, 100))
    r = font.render('1 - Red', True, 'black')
    buttons.blit(r, (5, 120))
    g = font.render('2 - Green', True, 'black')
    buttons.blit(g, (5, 140))
    b = font.render('3 - Blue', True, 'black')
    buttons.blit(b, (5, 160))
    y = font.render('4 - White', True, 'black')
    buttons.blit(y, (5, 180))

    pygame.display.update()
pygame.quit()