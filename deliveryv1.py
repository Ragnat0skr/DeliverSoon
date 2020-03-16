import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)


font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def titlescreen():
    click = False
    while True:


        screen.fill((0,0,0))
        draw_text('DeliverSoon', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text('Start', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click == True:
                        screen1a()

        pygame.draw.rect(screen, (255, 0, 0), button_1)


         #click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def screen1a():
    click = False
    while True:


        screen.fill((0,0,0))
        draw_text('Screen 1a', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text('Move on', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click == True:
                        screen2a()

        pygame.draw.rect(screen, (255, 0, 0), button_1)


         #click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def screen2a():
    click = False
    while True:

        screen.fill((0,0,0))
        draw_text('Screen 2a Question', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text('Answer A', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        draw_text('Answer B', font, (255, 255, 255), screen, 50, 180)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                        screen3a()
        if button_2.collidepoint((mx, my)):
            if click:
                        screen3b()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def screen3a():
    click = False
    while True:

        screen.fill((0,0,0))
        draw_text('Screen 3a Question', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text('Answer A', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        draw_text('Answer B', font, (255, 255, 255), screen, 50, 180)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                        screen4a()
        if button_2.collidepoint((mx, my)):
            if click:
                        screen4b()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def screen3b():
    click = False
    while True:

        screen.fill((0,0,0))
        draw_text('Screen 3b Question', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text('Answer A', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        draw_text('Answer B', font, (255, 255, 255), screen, 50, 180)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                        screen7a()
        if button_2.collidepoint((mx, my)):
            if click:
                        screen7b()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def screen4a():
    click = False
    while True:


        screen.fill((0,0,0))
        draw_text('Screen 4a', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text('Move on', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click == True:
                        screen6a()

        pygame.draw.rect(screen, (255, 0, 0), button_1)


         #click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def screen4b():
    click = False
    while True:


        screen.fill((0,0,0))
        draw_text('Screen 4b', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text('Move on', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click == True:
                        screen6a()

        pygame.draw.rect(screen, (255, 0, 0), button_1)


         #click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def screen6a():
    click = False
    while True:

        screen.fill((0,0,0))
        draw_text('Screen 6a Question', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text('Answer A', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        draw_text('Answer B', font, (255, 255, 255), screen, 50, 180)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                        screen7a()
        if button_2.collidepoint((mx, my)):
            if click:
                        screen7b()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def screen7a():
    click = False
    while True:


        screen.fill((0,0,0))
        draw_text('You have reached 7a', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text('Start', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click == True:
                        screen1()

        pygame.draw.rect(screen, (255, 0, 0), button_1)


         #click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def screen7b():
    click = False
    while True:


        screen.fill((0,0,0))
        draw_text('You have reached 7b', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        draw_text('Start', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click == True:
                        screen1a()

        pygame.draw.rect(screen, (255, 0, 0), button_1)


         #click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


titlescreen()
