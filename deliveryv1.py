import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

background = pygame.image.load('C:/Users/jphoe/Documents/Deliversoon/deliverbackground2.png')


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


        screen.fill((255,255,255))

        screen.blit(background, (0, 0))

        draw_text('DeliverSoon', font, (255, 255, 255), screen, 200, 20)

        mx, my = pygame.mouse.get_pos()

        #Text formatting
        #draw_text('Texthere', font, (255,255,255), screen, x, y)
        #Note it doesn't like apostrophes, write it is instead of it's

        draw_text('You are a full time delivery driver with £500 rent due on Sunday.', font, (255, 255, 255), screen, 50, 50)
        draw_text('Do you have what it takes to pay the bill?', font, (255, 255, 255), screen, 50, 75)
        draw_text('Start', font, (255, 255, 255), screen, 50, 100)

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
        screen.blit(background, (0, 0))
        draw_text('In this game you will be asked multiple questions to represent decisions', font, (255, 255, 255), screen, 40, 20)
        draw_text('delivery drivers make every day. Good luck!', font, (255, 255, 255), screen, 40, 40)

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
        screen.blit(background, (0, 0))
        draw_text('It is early Monday morning, and you get a notification on your phone.', font, (255, 255, 255), screen, 40, 20)
        draw_text('"Breakfast wrap devilery". A customer wants a breakfast wrap', font, (255,255,255), screen, 40, 40)
        draw_text('Delivered to their workplace. Accept?', font, (255,255,255), screen, 40, 60)

        mx, my = pygame.mouse.get_pos()

        draw_text('Accept', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        draw_text('Decline', font, (255, 255, 255), screen, 50, 180)
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
        screen.blit(background, (0, 0))
        draw_text('You accept the job, and drive to the restaurant and the desired', font, (255, 255, 255), screen, 40, 20)
        draw_text('workplace, and wait outside as requested. After 5 minutes the', font, (255, 255, 255), screen, 40, 40)
        draw_text('customer has not appeared, what do you do?', font, (255, 255, 255), screen, 40, 60)

        mx, my = pygame.mouse.get_pos()

        draw_text('Wait another 5 minutes', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        draw_text('Call the customer', font, (255, 255, 255), screen, 50, 180)
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
        screen.blit(background, (0, 0))
        draw_text('You made no money this morning.', font, (255, 255, 255), screen, 200, 20)
        draw_text('You need to choose your perfect delivery vehicle. Choosing a bike', font, (255, 255, 255), screen, 40, 40)
        draw_text('is fast but a car will keep the food for longer, but required fuel.', font, (255, 255, 255), screen, 40, 60)

        mx, my = pygame.mouse.get_pos()

        draw_text('Choose the car', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        draw_text('Choose the bike', font, (255, 255, 255), screen, 50, 180)
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
        screen.blit(background, (0, 0))
        draw_text('After waiting a further 5 minutes, you have no choice but to', font, (255, 255, 255), screen, 40, 20)
        draw_text('call the customer. After this, they come down and collect their food.', font, (255, 255, 255), screen, 40, 40)
        draw_text('Job complete! You recieved no tip, as the food was cold.', font, (255, 255, 255), screen, 40, 60)

        mx, my = pygame.mouse.get_pos()

        draw_text('Continue', font, (255, 255, 255), screen, 50, 80)
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
        screen.blit(background, (0, 0))
        draw_text('You chose to ring the customer, and they appear to collect their', font, (255, 255, 255), screen, 40, 20)
        draw_text('food, thanking you for stopping it getting cold.', font, (255, 255, 255), screen, 40, 40)
        draw_text('Job complete! You recieved a £5 tip', font, (255, 255, 255), screen, 40, 60)
        mx, my = pygame.mouse.get_pos()

        draw_text('Continue', font, (255, 255, 255), screen, 50, 80)
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
        screen.blit(background, (0, 0))
        draw_text('You earned some money this morning, and now need to choose your', font, (255, 255, 255), screen, 40, 20)
        draw_text('perfect delivery vehicle. The bike is fast, but the car will keep', font, (255, 255, 255), screen, 40, 40)
        draw_text('food warm longer at the cost of higher expenses.', font, (255, 255, 255), screen, 40, 60)

        mx, my = pygame.mouse.get_pos()

        draw_text('Choose the car', font, (255, 255, 255), screen, 50, 80)
        button_1 = pygame.Rect(50, 100, 200, 50)
        draw_text('Choose the bike', font, (255, 255, 255), screen, 50, 180)
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
        screen.blit(background, (0, 0))
        draw_text('You have chosen the car.', font, (255, 255, 255), screen, 40, 20)
        draw_text('The car allows you to keep food warmer for longer', font, (255, 255, 255), screen, 40, 40)
        draw_text('The car costs £25 a week in insurance.', font, (255, 255, 255), screen, 40, 60)

        mx, my = pygame.mouse.get_pos()

        draw_text('Restart', font, (255, 255, 255), screen, 50, 80)
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

def screen7b():
    click = False
    while True:


        screen.fill((0,0,0))
        screen.blit(background, (0, 0))
        draw_text('You have chosen the bike.', font, (255, 255, 255), screen, 40, 20)
        draw_text('The bike allows you to pick up and drop off food faster', font, (255, 255, 255), screen, 40, 40)
        draw_text('The car costs £15 a week in insurance.', font, (255, 255, 255), screen, 40, 60)

        mx, my = pygame.mouse.get_pos()

        draw_text('Restart', font, (255, 255, 255), screen, 50, 80)
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
