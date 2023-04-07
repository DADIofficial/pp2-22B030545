import random, time, datetime

import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40

#If 3 seconds pass, the food will disappear
WHITE = (255, 255, 255)
#Speed down
PINK = (255, 192, 203)
#Speed up
ORANGE = (255, 69, 0)
clock = pygame.time.Clock()

#fonts
font = pygame.font.SysFont("Verdana", 120)
font_small = pygame.font.SysFont("Verdana", 80)
font_micro = pygame.font.SysFont("Verdana", 50)
game_over = font.render("Game Over", True, RED)
SPEED_UP = font_small.render("SPEED UP", True, ORANGE)
SPEED_DOWN = font_small.render("SPEED DOWN", True, PINK)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        head = self.body[0]
        otherhead = self.body[1]
        k = True
        for idx in range(len(self.body) - 1, 0, -1):
            #Head turns red on impact
            if self.body[idx - 1].x == self.body[0].x + dx and self.body[idx - 1].y == self.body[0].y + dy and (dx != 0 or dy != 0):
                k = False
                pygame.draw.rect(
                    SCREEN,
                    RED,
                    pygame.Rect(
                        head.x * BLOCK_SIZE,
                        head.y * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                    ))
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        # [Point(0, 1), Point(2, 5), Point(5, 9)]
        # [Point(0, 0), Point(0, 1), Point(2, 5)]
        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > WIDTH // BLOCK_SIZE - 1 or self.body[0].x < 0 or self.body[0].y < 0 or self.body[0].y > HEIGHT // BLOCK_SIZE - 1:
            k = False
            pygame.draw.rect(
                SCREEN,
                RED,
                pygame.Rect(
                    otherhead.x * BLOCK_SIZE,
                    otherhead.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                ))

        return(k)

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True


def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self, food_color):
        pygame.draw.rect(
            SCREEN,
            food_color,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


def main():
    num_level = 1
    num_food = 0
    score_num_food = font_micro.render(str(num_food), True, GREEN)
    speed = 4
    food_color = GREEN
    secondthen = datetime.datetime.now().second

    # Creating levels with a new loop within a loop
    pygame.display.set_caption("Level" + str(num_level))
    running = True
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0
    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, 1
                elif event.key == pygame.K_RIGHT:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT:
                    dx, dy = -1, 0
        #Special event for WHITE
        if food_color == WHITE and secondthen + 3 == datetime.datetime.now().second:
            food_color = random.choice([GREEN, WHITE, ORANGE, PINK])
            secondthen = datetime.datetime.now().second

            while True:
                food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                if (food.location.x, food.location.y) not in snake.body:
                    break

        snake.draw()
        food.draw(food_color)
        draw_grid()
        SCREEN.blit(score_num_food, (WIDTH - 80, 40))

        if snake.check_collision(food):
            #Special event for other color
            if food_color == ORANGE:
                speed += 4
                num_food += 2
                SCREEN.blit(SPEED_UP, (50, 250))
                pygame.display.update()
                time.sleep(1)
            if food_color == PINK:
                speed = max(4, speed-4)
                SCREEN.blit(SPEED_DOWN, (50, 250))
                pygame.display.update()
                time.sleep(1)
            if food_color == WHITE:
                num_food += 4
            num_food += 1
            #New color for food_color
            food_color = random.choice([GREEN, WHITE, ORANGE, PINK])

            score_num_food = font_micro.render(str(num_food), True, GREEN)
            secondthen = datetime.datetime.now().second

            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )

            # To prevent food from falling on the snake
            while True:
                food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                if (food.location.x, food.location.y) not in snake.body:
                    break

        if snake.move(dx, dy) == False:
            SCREEN.blit(game_over, (50, 250))
            pygame.display.flip()
            time.sleep(2)
            running = False
        pygame.display.flip()
        clock.tick(speed)


if __name__ == '__main__':
    main()