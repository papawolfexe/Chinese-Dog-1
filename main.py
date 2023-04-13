import pygame
from dataclasses import dataclass
from GameObject import GameObject, MoveDirs


@dataclass
class StartVars:
    X, Y = 600, 600
    fps = 60
    clock = pygame.time.Clock()


# Init all Modules
pygame.init()

# Window init
window = pygame.display.set_mode((StartVars.X, StartVars.Y))
glorious_leader = pygame.image.load("zie_zie_ping_公鸡.jpg").convert()
pygame.display.set_icon(glorious_leader)
pygame.display.set_caption("这 事物")

# Music init
pygame.mixer.music.load("MAO_ZEDONG_DRIP.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1, start=1.5)

# Social Credit Counter
social_credit = counter, text = 0, 'Social Credit: +0'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)


def key_press_handler(keys):
    if keys[pygame.K_UP]:
        bruh.move(MoveDirs.up)
    if keys[pygame.K_DOWN]:
        bruh.move(MoveDirs.down)
    if keys[pygame.K_LEFT]:
        bruh.move(MoveDirs.left)
    if keys[pygame.K_RIGHT]:
        bruh.move(MoveDirs.right)


# Game loop
bruh = GameObject(window, r"./Bruh.png", (300, 300), (144, 144), 5, True)

while True:
    window.fill((0, 0, 0))  # Replace with background game object
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.USEREVENT:
            counter += 1
            text = str('Social Credit: +' + str(counter)).rjust(3)
    key_press_handler(pygame.key.get_pressed())

    bruh.draw()
    window.blit(font.render(text, True, "white"), (32, 48))

    pygame.display.flip()
    StartVars.clock.tick(StartVars.fps)
