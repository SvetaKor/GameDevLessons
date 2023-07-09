import pygame


def draw(screen: pygame.Surface):
    font = pygame.font.Font('C://WINDOWS//Fonts//segoeuil.ttf', 36)
    text = font.render('Hello!', True, (12, 34, 56))
    text_x = w // 2 - text.get_width() // 2
    text_y = h // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    pygame.draw.circle(screen, (253, 78, 24), (w//2, h//4), 70, 8)


if __name__ == '__main__':
    pygame.init()
    size = w, h = 600, 600
    screen = pygame.display.set_mode(size)
    color = pygame.Color(25, 60, 10)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] + 20, hsv[3])
    screen.fill(color)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
