import pygame

from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
buttons_bar = pygame.Surface((200, 700))

# color
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(150, 150, 150)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)

# font
font = pygame.font.SysFont("Papyrus", 15)
font_size = pygame.font.SysFont("Papyrus", 25)

def submaterials(size):
    buttons_bar.fill((GREY))
    pygame.draw.rect(buttons_bar, BLACK, (2, 2, 96, 335), 1)  # rect for bar
    pygame.draw.aaline(buttons_bar, BLACK, (8, 8), (40, 40), 1)  # line for line
    pygame.draw.rect(buttons_bar, BLACK, (58, 15, 32, 20), 1)  # rect for rect
    pygame.draw.circle(buttons_bar, BLACK, (27, 70), 15, 1)  # circ for circ
    pygame.draw.rect(buttons_bar, BLACK, (56, 58, 36, 28))  # rect for eraser
    pygame.draw.rect(buttons_bar, BLACK, (10, 103, 32, 32), 1)  # rect for square
    pygame.draw.polygon(buttons_bar, BLACK, [[56, 117], [74, 100], [92, 117], [74, 134]], 1) # polygon for rhombus
    pygame.draw.polygon(buttons_bar, BLACK, [[10, 145], [10, 180], [40, 180]], 1) # polygon for right
    pygame.draw.polygon(buttons_bar, BLACK, [[74, 145], [56, 180], [92, 180]], 1)

    c = font.render('Press:', True, BLACK)
    buttons_bar.blit(c, (30, 192))
    r = font.render('1 - Red', True, RED)
    buttons_bar.blit(r, (25, 212))
    g = font.render('2 - Green', True, GREEN)
    buttons_bar.blit(g, (20, 232))
    b = font.render('3 - Blue', True, BLUE)
    buttons_bar.blit(b, (23, 252))
    y = font.render('4 - White', True, WHITE)
    buttons_bar.blit(y, (20, 272))
    size_in_font = font.render('SIZE:', True, BLACK)
    buttons_bar.blit(size_in_font, (5, 302))
    size_in_font = font_size.render(str(size), True, BLACK)
    buttons_bar.blit(size_in_font, (55, 294))


# Point = collections.namedtuple('Point', ['x', 'y'])

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def __init__(self):
        self.size = 15
        return
    def draw(self):
        return

    def update(self, current_pos):
        return


class Button(GameObject):
    def __init__(self, x1, y1, x2, y2, button_pressed):
        super().__init__()
        self.x1, self.x2, self.y1, self.y2, self.button_pressed = x1, x2, y1, y2, button_pressed
        self.rect = pygame.draw.rect(
            buttons_bar,
            RED if self.button_pressed else BLACK,
            (
                self.x1,
                self.y1,
                self.x2,
                self.y2,
            )
        )

    def draw(self):
        pygame.draw.rect(
            buttons_bar,
            RED if self.button_pressed else BLACK,
            (
                self.x1,
                self.y1,
                self.x2,
                self.y2,
            ),
            1
        )

    def update(self, current_pos):
        pass


class Pen(GameObject):
    def __init__(self, *args, **kwargs):  # Pen(1, 2, 3, a=4) =>
        super().__init__()
        self.points: list[Point, ...] = []  # [(x1, y1), (x2, y2)]
        self.color = WHITE

    def draw(self):

        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                self.color,
                start_pos=(point.x, point.y),  # self.points[idx]
                end_pos=(next_point.x, next_point.y),
                width = max(1, self.size)
            )
            if point.x > 0 and point.y > 0:
                pygame.draw.circle(
                    SCREEN,
                    self.color,
                    (point.x, point.y),  # self.points[idx]
                    self.size // 2
                )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))  # (x, y) Point((x, y)) => Point(x, y)


class Eraser(GameObject):
    def __init__(self, *args, **kwargs):  # Pen(1, 2, 3, a=4) =>
        super().__init__()
        self.points: list[Point, ...] = []  # [(x1, y1), (x2, y2)]

    def draw(self):

        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                BLACK,
                start_pos=(point.x, point.y),  # self.points[idx]
                end_pos=(next_point.x, next_point.y),
                width = max(1, self.size)
            )
            if point.x > 0 and point.y > 0:
                pygame.draw.circle(
                    SCREEN,
                    BLACK,
                    (point.x, point.y),  # self.points[idx]
                    self.size // 2
                )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))  # (x, y) Point((x, y)) => Point(x, y)


class Rectangle(GameObject):
    def __init__(self, start_pos):  # Rectangle(start_pos=1); Pen(start_pos=1)
        super().__init__()
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = WHITE

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            SCREEN,
            self.color,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


class Square(GameObject):
    def __init__(self, start_pos):  # Rectangle(start_pos=1); Pen(start_pos=1)
        super().__init__()
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = WHITE

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        size = (min(end_pos_x - start_pos_x, end_pos_y - start_pos_y))
        if self.start_pos.x > self.end_pos.x:
            start_pos_x = end_pos_x - size
        if self.start_pos.y > self.end_pos.y:
            start_pos_y = end_pos_y - size

        pygame.draw.rect(
            SCREEN,
            self.color,
            (
                start_pos_x,
                start_pos_y,
                size,
                size,
            ),
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Rhombus(GameObject):
    def __init__(self, start_pos):  # Rectangle(start_pos=1); Pen(start_pos=1)
        super().__init__()
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = WHITE

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)


        pygame.draw.polygon(
            SCREEN,
            self.color,
            [
                [start_pos_x, (start_pos_y + end_pos_y)/2],
                [(start_pos_x + end_pos_x)/2, start_pos_y],
                [end_pos_x, (start_pos_y + end_pos_y)/2],
                [(start_pos_x + end_pos_x)/2, end_pos_y]
            ],
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Right_trian(GameObject):
    def __init__(self, start_pos):  # Rectangle(start_pos=1); Pen(start_pos=1)
        super().__init__()
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = WHITE

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)



        pygame.draw.polygon(
            SCREEN,
            self.color,
            [
                [end_pos_x if (self.start_pos.x > self.end_pos.x and self.start_pos.y < self.end_pos.y) else start_pos_x, start_pos_y],
                [end_pos_x, start_pos_y] if (self.start_pos.x > self.end_pos.x and self.start_pos.y > self.end_pos.y) else [start_pos_x, end_pos_y],
                [end_pos_x, start_pos_y if (self.start_pos.x < self.end_pos.x and self.start_pos.y > self.end_pos.y) else end_pos_y]
                #3 conditon where point change
            ],
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Equ_trian(GameObject):
    def __init__(self, start_pos):  # Rectangle(start_pos=1); Pen(start_pos=1)
        super().__init__()
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = WHITE

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)



        pygame.draw.polygon(
            SCREEN,
            self.color,
            [
                [start_pos_x, start_pos_y] if (self.start_pos.y < self.end_pos.y) else [start_pos_x, end_pos_y],
                [end_pos_x, start_pos_y] if (self.start_pos.y < self.end_pos.y) else [end_pos_x, end_pos_y],
                [(start_pos_x + end_pos_x)/2, (start_pos_y + ((3**0.5)*(end_pos_x - start_pos_x))//2) if self.start_pos.y < self.end_pos.y else (end_pos_y - ((3**0.5)*(end_pos_x - start_pos_x))//2)]
                #3 conditon where point change
            ],
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Ellipse(GameObject):
    def __init__(self, start_pos):  # Rectangle(start_pos=1); Pen(start_pos=1)
        super().__init__()
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.color = WHITE

    def draw(self):
        start_pos_x = min(self.start_pos.x, self.end_pos.x)  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos.y, self.end_pos.y)

        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.ellipse(
            SCREEN,
            self.color,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=self.size,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


def main():
    running = True
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen  # current_shape()
    current_color = WHITE
    current_size = 15

    line_button = Button(4, 4, 44, 44, True)
    rec_button = Button(52, 4, 44, 44, False)
    cir_button = Button(4, 50, 44, 44, False)
    eraser_button = Button(52, 50, 44, 44, False)
    square_button = Button(4, 96, 44, 44, False)
    rhombus_button = Button(52, 96, 44, 44, False)
    right_tri_button = Button(4, 142, 44, 44, False)
    equ_tri_button = Button(52, 142, 44, 44, False)
    buttons = [
        line_button, rec_button, cir_button, eraser_button, square_button, rhombus_button, right_tri_button, equ_tri_button
    ]

    objects = []

    while running:
        SCREEN.fill(BLACK)
        buttons_bar.fill('white')
        submaterials(current_size)
        for obj in objects:
            obj.draw()
        for obj in buttons:
            obj.draw()
        SCREEN.blit(buttons_bar, (700, 0))

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            current_size += 1
        elif pressed_keys[K_DOWN]:
            current_size = max(0, current_size - 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_color = RED

                elif event.key == pygame.K_2:
                    current_color = GREEN

                elif event.key == pygame.K_3:
                    current_color = BLUE

                elif event.key == pygame.K_4:
                    current_color = WHITE

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rec_button.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    current_shape = Rectangle
                    # color of button
                    for obj in buttons:
                        obj.button_pressed = False
                    rec_button.button_pressed = True

                elif line_button.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    line_button.button_pressed = True
                    current_shape = Pen

                elif eraser_button.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    eraser_button.button_pressed = True
                    current_shape = Eraser

                elif cir_button.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    cir_button.button_pressed = True
                    current_shape = Ellipse

                elif square_button.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    square_button.button_pressed = True
                    current_shape = Square

                elif rhombus_button.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    rhombus_button.button_pressed = True
                    current_shape = Rhombus

                elif right_tri_button.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    right_tri_button.button_pressed = True
                    current_shape = Right_trian

                elif equ_tri_button.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    equ_tri_button.button_pressed = True
                    current_shape = Equ_trian

                else:
                    active_obj = current_shape(start_pos=event.pos)
                    objects.append(active_obj)
                    active_obj.color = current_color
                    active_obj.size = current_size

            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object
        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
    main()