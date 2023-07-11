import pygame

pygame.init()
size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
r = 0
g = 0
b = 0
o = 0

running = True

screen2 = pygame.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 0, 0
drawing = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            screen2.blit(screen, (0, 0))
            drawing = False
            x1, y1, w, h = 0, 0, 0, 0
        if event.type == pygame.MOUSEMOTION:
            w, h = event.pos[0] - x1, event.pos[1] - y1
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                screen.fill((0, 0, 0))
                screen2.fill((0, 0, 0))
            if event.unicode == 'r':
                r = 255
                g = 0
                b = 0
            if event.unicode == 'g':
                r = 0
                g = 255
                b = 0
            if event.unicode == 'b':
                r = 0
                g = 0
                b = 255
            if event.unicode == 'y':
                r = 255
                g = 255
                b = 0
            if event.unicode == 'k':
                o = 1
            if event.unicode == 'c':
                o = 2

    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    if drawing and o == 1:
        pygame.draw.rect(screen, (r, g, b), ((x1, y1), (w, h)), 5)
    if drawing and o == 2:
        pygame.draw.circle(screen, (r, g, b), (x1, y1), w * 2, 5)

    pygame.display.flip()
pygame.quit()