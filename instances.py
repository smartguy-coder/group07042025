import pygame

from constants import SCROLL_SPEED, WINDOW_WIDTH
from images_sprites import ground_image


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
