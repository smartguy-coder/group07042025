import pygame

from constants import SCROLL_SPEED, WINDOW_WIDTH
from images_sprites import ground_image, birds_images


class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args, **kwargs):
        self.rect.x -= SCROLL_SPEED
        if self.rect.x <= -WINDOW_WIDTH:
            self.kill()


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.fps = 0
        self.image = birds_images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)

    def update(self, *args, **kwargs):
        self.fps += 1
        if self.fps >= 30:
            self.fps = 0
        self.image = birds_images[self.fps // 10]

