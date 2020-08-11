import pygame
import backend as bk

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
light_blue = (158, 158, 255)

scheme_count = 1

dW = 670
dH = 190

clear_icon = pygame.image.load('icon.png')

cDisplay = pygame.display.set_mode((dW, dH), pygame.RESIZABLE)
pygame.display.set_caption('Live Coronavirus Updates')
pygame.display.set_icon(clear_icon)


def text_objects(text, font, c):  # render the text
    text_surface = font.render(text, True, c)
    return text_surface, text_surface.get_rect()


def message_display(text, size, color=(0, 0, 0), coordinates=(cDisplay.get_width() // 2, cDisplay.get_height() // 2)):
    large_text = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (coordinates[0], coordinates[1])
    cDisplay.blit(text_surf, text_rect)


def print_total(color):
    global cDisplay
    message_display('Global Cases: ' + bk.cases(), 40, color, (cDisplay.get_width()//2, cDisplay.get_height()//2 - 50))
    message_display('Global Deaths: ' + bk.deaths(), 40, color, (cDisplay.get_width()//2, cDisplay.get_height()//2))
    message_display('Global Recoveries: ' + bk.recoveries(), 40, color, (cDisplay.get_width()//2, cDisplay.get_height()//2 + 50))


def update():  # the loop that draw and puts the text and data on the screen
    global light_blue
    global white
    global black
    global scheme_count
    global cDisplay
    data_start = True
    scheme_count = 1
    color_back = white
    color_txt = black
    while data_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    scheme_count += 1
                    if scheme_count == 4:
                        scheme_count = 1
            elif event.type == pygame.VIDEORESIZE:
                cDisplay = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if scheme_count == 1:
            color_back = white
            color_txt = black
        elif scheme_count == 2:
            color_back = black
            color_txt = white
        elif scheme_count == 3:
            color_back = light_blue
            color_txt = black

        cDisplay.fill(color_back)
        print_total(color_txt)

        pygame.display.flip()


update()