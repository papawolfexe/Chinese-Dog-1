import pygame
from dataclasses import dataclass


@dataclass
class MoveDirs:
    up = 0
    down = 1
    left = 2
    right = 3


class GameObject:
    def __init__(
            self,
            game_window: pygame.Surface,
            image_path, pos: tuple[float, float],
            size: tuple[float, float],
            default_speed: float,
            center_positioning: bool = False
    ) -> None:

        self.game_window = game_window
        self.image_path = image_path
        self.pos = pos
        self.size = size
        self.default_speed = default_speed
        self.center_positioning = center_positioning

        self.img = pygame.image.load(self.image_path).convert()

        self.rect = self.img.get_rect()
        self.rect.size = self.size

        if not self.center_positioning:
            self.rect.topleft = self.pos
        else:
            self.rect.center = self.pos

        self.img = pygame.transform.scale(self.img, self.rect.size)

        self.game_window.blit(self.img, self.rect.topleft)

    def draw(self):
        self.game_window.blit(self.img, self.rect.topleft)

    def move(self, direction: MoveDirs, speed: int = None):
        if speed is None:
            speed = self.default_speed
        if direction == MoveDirs.up:
            self.rect = self.rect.move(0, -1 * speed)
        elif direction == MoveDirs.down:
            self.rect = self.rect.move(0, 1 * speed)
        elif direction == MoveDirs.left:
            self.rect = self.rect.move(-1 * speed, 0)
        elif direction == MoveDirs.right:
            self.rect = self.rect.move(1 * speed, 0)
