import pygame
import random

if __name__ == '__main__':
    pygame.init()
    size = w, h = 800, 400
    screen = pygame.display.set_mode(size)
    running = True
    x = w // 2
    y = h // 2
    v1 = 0
    v2 = 0
    clock = pygame.time.Clock()
    fps = 60

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    v1 = random.randrange(-80, 80)
                    v2 = random.randrange(-80, 80)
                    x = w // 2
                    y = h // 2

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, pygame.Color('blue'), (x, y), 20)
        x += v1 / fps
        y += v2 / fps
        clock.tick(fps)

        pygame.display.flip()
    pygame.quit()