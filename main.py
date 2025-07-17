import pygame

from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from images_sprites import skyline_image
from instances import Ground, Bird
from utils import quit_game

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))


def main():
    ground_group = pygame.sprite.Group()
    ground_group.add(Ground(x=0, y=500))

    bird_group = pygame.sprite.GroupSingle()
    bird_group.add(Bird())

    while True:
        quit_game()
        window.fill(color=(20, 50, 20))
        window.blit(skyline_image, dest=(0, 0))

        if len(ground_group) <= 2:
            ground_group.add(Ground(x=WINDOW_WIDTH, y=500))
        ground_group.draw(window)
        ground_group.update()

        bird_group.draw(window)
        bird_group.update()

        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
