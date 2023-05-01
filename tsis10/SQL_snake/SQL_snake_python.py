import random, time
import pygame
import json, psycopg2
from tsis10.PhoneBook.config import params

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (125, 125, 125)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

#fonts
font = pygame.font.SysFont("Verdana", 120)
font_small = pygame.font.SysFont("Verdana", 80)
font_micro = pygame.font.SysFont("Verdana", 50)
game_over = font.render("Game Over", True, RED)
completed = font_small.render("Level Completed", True, GREEN)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __json__(self):
        return {'x': self.x, 'y': self.y}


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x= 10,
                y= 10,
            ),
            Point(
                x=11,
                y=10,
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
        if dx != 0 or dy != 0:
            for idx in range(len(self.body) - 1, 0, -1):
                # Head turns red on impact
                if self.body[idx - 1].x == self.body[0].x + dx and self.body[idx - 1].y == self.body[0].y + dy and (
                        dx != 0 or dy != 0):
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

            if self.body[0].x > WIDTH // BLOCK_SIZE - 1 or self.body[0].x < 0 or self.body[0].y < 0 or self.body[
                0].y > HEIGHT // BLOCK_SIZE - 1:
                k = False

            return (k)

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

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

def draw_Blocks(x, y):
    pygame.draw.rect(
        SCREEN,
        GREY,
        pygame.Rect(
            x * BLOCK_SIZE,
            y * BLOCK_SIZE,
            BLOCK_SIZE,
            BLOCK_SIZE,
        )
    )

def main():
    level_complited = True
    num_level = 1
    num_food = 0
    snake = Snake()
    name = input("Name: ")
    db = psycopg2.connect(**params)
    current = db.cursor()
    current.execute("SELECT COUNT(*) FROM user_snake WHERE user_name=%s", (name,))
    count = current.fetchone()[0]
    if count > 0:
        print("Running the last save")
        with open(name + '.json', 'r') as f:
            data = f.read()
            save_snake = json.loads(data)
            if save_snake[0] == True:
                snake.body = [Point(d['x'], d['y']) for d in save_snake[1]]
                num_level = save_snake[2] // 8 + 1
                num_food = save_snake[2]
    else:
        print("This user was adding")
        current.execute("INSERT INTO user_snake VALUES (%s, %s)", (name, 0))
        db.commit()
        save_result = [False, [p.__json__() for p in snake.body], 0]
        with open(name + '.json', 'w') as f:
            json.dump(save_result, f)

    score_num_food = font_micro.render(str(num_food), True, GREEN)
    b = 0

    # Creating levels with a new loop within a loop
    while  level_complited:
        pygame.display.set_caption("Level" + str(num_level))
        running = True
        dx, dy = 0, 0
        food_eaten = num_food % 8
        blocks = [ ]
        food = Food(5, 5)

        with open("wall" + str(num_level - 1) + ".txt") as wall:
            for i in range(0, 20):
                k = wall.readline()
                for j in range(0, 20):
                    if k[j] == "#":
                        blocks.append([i, j])

        while running:
            SCREEN.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    level_complited = False
                    running = False
                    with open(name + '.json', 'w') as f:
                        json.dump([True, [p.__json__() for p in snake.body], num_food], f)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        dx, dy = 0, -1
                    elif event.key == pygame.K_DOWN:
                        dx, dy = 0, 1
                    elif event.key == pygame.K_RIGHT:
                        dx, dy = 1, 0
                    elif event.key == pygame.K_LEFT:
                        dx, dy = -1, 0

            if snake.check_collision(food):
                food_eaten += 1
                num_food += 1
                score_num_food = font_micro.render(str(num_food), True, GREEN)
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
                # To prevent food from falling on the snake
                while True:
                    food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                    food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                    if [food.location.x, food.location.y] not in snake.body and [food.location.x, food.location.y] not in blocks:
                        break
            snake.draw()
            food.draw()
            for i in blocks:
                draw_Blocks(i[0], i[1])
            draw_grid()
            SCREEN.blit(score_num_food, (WIDTH-80, 40))

            if snake.move(dx, dy) == False or [snake.body[0].x, snake.body[0].y] in blocks:
                pygame.draw.rect(
                    SCREEN,
                    RED,
                    pygame.Rect(
                        snake.body[1].x * BLOCK_SIZE,
                        snake.body[1].y * BLOCK_SIZE,
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                    )
                )
                SCREEN.blit(game_over, (50, 250))
                pygame.display.flip()
                time.sleep(2)
                running = False
                level_complited = False

                current.execute("SELECT score FROM user_snake WHERE user_name=%s", (name,))
                if current.fetchone()[0] < num_food:
                    current.execute("UPDATE user_snake SET score=%s WHERE user_name=%s", (num_food, name))

                save_result = [False, [p.__json__() for p in snake.body], 0]
                with open(name + '.json', 'w') as f:
                    json.dump(save_result, f)

            if food_eaten == 8:
                num_level += 1
                SCREEN.blit(completed, (50, 250))
                pygame.display.flip()
                time.sleep(2)
                running = False
                b += 1
            pygame.display.flip()
            clock.tick(5 * num_level)
        snake = Snake()
    db.commit()
    current.close()
    db.close()


if __name__ == '__main__':
    main()