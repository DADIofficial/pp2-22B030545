import pygame, datetime
pygame.init()

HEIGHT, WIDTH = 1400, 700
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
mickey = pygame.image.load("Mickey clock/mickeyclock.jpg")
right_hand = pygame.image.load("Mickey clock/right_hand.png")
left_hand = pygame.image.load("Mickey clock/left_hand.png")
mickey = pygame.transform.scale(mickey, (mickey.get_width()//2, mickey.get_height()//2))
screen = pygame.display.set_mode((mickey.get_width(), mickey.get_height()))
left_hand_rotate = pygame.transform.rotate(left_hand, -datetime.datetime.now().second*6)
right_hand_rotate = pygame.transform.rotate(right_hand, -datetime.datetime.now().minute*6)
second_now = datetime.datetime.now().second
minute_now = datetime.datetime.now().minute
running = True
while running:
    screen.fill((255, 255, 255))  # RGB - red, green, blue; ( 0 - 255 )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(mickey, (0, 0))
    if datetime.datetime.now().second != second_now:
        left_hand_rotate = pygame.transform.rotate(left_hand, -datetime.datetime.now().second*6)
        second_now = datetime.datetime.now().second
    if datetime.datetime.now().minute != minute_now:
        right_hand_rotate = pygame.transform.rotate(right_hand, -datetime.datetime.now().minute * 6)
        minute_now = datetime.datetime.now().minute
    screen.blit(left_hand_rotate, ((mickey.get_width() - left_hand_rotate.get_width())//2, (mickey.get_height() - left_hand_rotate.get_height())//2))
    screen.blit(right_hand_rotate, ((mickey.get_width()-right_hand_rotate.get_width())//2, (mickey.get_height() - right_hand_rotate.get_height())//2))
    pygame.display.flip()
    clock.tick(60)