import pygame
from sys import exit

from utils import quit_game

pygame.init()
clock = pygame.time.Clock()

window_height = 720
window_width = 550
window = pygame.display.set_mode(size=(window_width, window_height))


def main():
    while True:
        quit_game()
        window.fill(color=(20, 50, 20))

        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
