import pygame
import random

from constants import WINDOW_HEIGHT, WINDOW_WIDTH, SCROLL_SPEED
from images_sprites import skyline_image, bottom_pipe_image, top_pipe_image
from instances import Ground, Bird, Pipe
from utils import quit_game
from dynamic_state import score

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

font = pygame.font.SysFont('Segoe', 30)

def main():
    ground_group = pygame.sprite.Group()
    ground_group.add(Ground(x=0, y=500))

    bird_group = pygame.sprite.GroupSingle()
    bird_group.add(Bird())

    pipe_group = pygame.sprite.Group()
    pipe_timer = 0

    while True:
        quit_game()
        window.fill(color=(20, 50, 20))
        window.blit(skyline_image, dest=(0, 0))

        bird_group.draw(window)
        user_input = pygame.key.get_pressed()
        bird_group.update(user_input)

        pipe_group.draw(window)
        pipe_group.update()
        if pipe_timer <= 0:
            x_top = WINDOW_WIDTH
            x_bottom = WINDOW_WIDTH
            y_top = random.randint(-600, -480)
            y_bottom = y_top + random.randint(90, 130) + bottom_pipe_image.get_height()
            pipe_group.add(Pipe(x=x_top, y=y_top, image=top_pipe_image, pipe_type='top'))
            pipe_group.add(Pipe(x=x_bottom, y=y_bottom, image=bottom_pipe_image, pipe_type='bottom'))

            pipe_timer = random.randint(180, 250)
        pipe_timer -= SCROLL_SPEED

        if len(ground_group) <= 2:
            ground_group.add(Ground(x=WINDOW_WIDTH, y=500))
        ground_group.draw(window)
        ground_group.update()

        score_text = font.render(f'Score: {score["score"]}', True, pygame.Color(220, 220, 220))
        window.blit(score_text, (20, 20))

        clock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
