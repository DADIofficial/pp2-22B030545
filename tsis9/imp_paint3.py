import pygame

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
buttons_bar = pygame.Surface((200, 700))
font = pygame.font.SysFont("Verdana", 15)
button_position = {
    'line': [4, 4, 44, 44],
    'rect': [52, 4, 44, 44],
    'circle': [4, 50, 44, 44],
    'eraser': [52, 50, 44, 44]
}

def submaterials():

    pygame.draw.rect(buttons_bar, BLACK, (2, 2, 96, 206), 1)
    pygame.draw.aaline(buttons_bar, BLACK, (8, 8), (40, 40), 1)
    pygame.draw.rect(buttons_bar, BLACK, (58, 10, 32, 32), 1)
    pygame.draw.circle(buttons_bar, BLACK, (27, 70), 15, 1)
    pygame.draw.rect(buttons_bar, BLACK, (56, 58, 36, 28))
    c = font.render('Press:', True, 'black')
    buttons_bar.blit(c, (5, 100))
    r = font.render('1 - Red', True, 'black')
    buttons_bar.blit(r, (5, 120))
    g = font.render('2 - Green', True, 'black')
    buttons_bar.blit(g, (5, 140))
    b = font.render('3 - Blue', True, 'black')
    buttons_bar.blit(b, (5, 160))
    y = font.render('4 - White', True, 'black')
    buttons_bar.blit(y, (5, 180))
    SCREEN.blit(buttons_bar, (700, 0))


# Point = collections.namedtuple('Point', ['x', 'y'])

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return


class Button(GameObject):
    def __init__(self, x1, x2, y1, y2, button_pressed):
        self.x1, self.x2, self.y1, self.y2, self.button_pressed = x1, x2, y1, y2, button_pressed
        self.rect = pygame.draw.rect(
            buttons_bar,
            'red' if self.button_pressed else BLACK,
            (
                self.x1,
                self.x2,
                self.y1,
                self.y2,
            )
        )

    def draw(self):
        pygame.draw.rect(
            buttons_bar,
            'red' if self.button_pressed else 'black',
            (
                self.x1,
                self.x2,
                self.y1,
                self.y2,
            ),
            1
        )

    def update(self, current_pos):
        pass


class Pen(GameObject):
    def __init__(self, *args, **kwargs):  # Pen(1, 2, 3, a=4) =>
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
                width=5
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))  # (x, y) Point((x, y)) => Point(x, y)

class Eraser(GameObject):
    def __init__(self, *args, **kwargs):  # Pen(1, 2, 3, a=4) =>
        self.points: list[Point, ...] = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            next_point = self.points[idx + 1]
            pygame.draw.line(
                SCREEN,
                BLACK,
                start_pos=(point.x, point.y),  # self.points[idx]
                end_pos=(next_point.x, next_point.y),
                width=20
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))  # (x, y) Point((x, y)) => Point(x, y)

class Rectangle(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
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
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

class Ellipse(GameObject):
    def __init__(self, start_pos, *args, **kwargs): # Rectangle(start_pos=1); Pen(start_pos=1)
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
            width=5,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos


def main():
    running = True
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen  # current_shape()
    current_color = WHITE
    line_button = Button(4, 4, 44, 44, True)
    rec_button =  Button(52, 4, 44, 44, False)
    cir_button = Button(4, 50, 44, 44, False)
    eraser_button = Button(52, 50, 44, 44, False)
    buttons = [
        line_button, rec_button, cir_button, eraser_button
    ]
    objects = []

    while running:
        SCREEN.fill(BLACK)
        buttons_bar.fill('white')
        for obj in buttons:
            obj.draw()
        for obj in objects:
            obj.draw()
        submaterials()


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
                    for obj in buttons:
                        obj.button_pressed = False
                    rec_button.button_pressed = True

                    # current_shape = button.connected_shape
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
                else:
                    active_obj = current_shape(start_pos=event.pos)
                    objects.append(active_obj)
                    active_obj.color = current_color

            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=event.pos)


            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object
        clock.tick(30)
        pygame.display.flip()




if __name__ == '__main__':
    main()