# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 204, 204)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
BROWN = (51, 25, 0)
BAIGE = (255, 229, 204)
HICKORY = (81, 59, 48)
HOUSE = (140, 102, 85)
WINDOW = (255, 223, 168)
YELLOW = (255, 221, 0)
GREY = (204, 204, 204)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])

def draw_snowman(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y-80, 80, 80])
    pygame.draw.ellipse(screen, WHITE, [x+10, y-130, 60, 60])
    pygame.draw.ellipse(screen, WHITE, [x+20, y-160, 40, 40])
    pygame.draw.ellipse(screen, BLACK, [x+30, y-150, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [x+45, y-150, 5, 5])
    pygame.draw.polygon(screen, ORANGE, [[x+40, y-142], [x+40, y-135], [x+50, y-140]])

def draw_tree(x, y):
    pygame.draw.rect(screen, BROWN, [x, y-250, 40, 260])
    pygame.draw.ellipse(screen, GREEN, [x-60, y-400, 160, 160])

def draw_house(x, y):
    pygame.draw.rect(screen, HOUSE, [x+420, y-200, 200, 200])
    pygame.draw.rect(screen, HOUSE, [x+560, y-300, 40, 80])
    pygame.draw.polygon(screen, HICKORY, [[x+380, y-200], [x+660, y-200], [x+520, y-300]])
    pygame.draw.rect(screen, BLACK, [x+520, y-100, 50, 100])
    pygame.draw.rect(screen, WINDOW, [x+450, y-170, 50, 50])



    
'''making snow'''
rain = []
for n in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    r = random.randrange(1, 5)
    rain.append([x, y, r, r])

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now '''
    '''for s in rain'''
    for r in rain:
        r[1] += 2
        r[0] -= 1
        
        if r[1] > 500:
                r[0] = random.randrange(000, 1000)
                r[1] = random.randrange(-200, 0)

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLUE)
    pygame.draw.rect(screen, WHITE, [0, 500, 800, 100])
    
    ''' cloud ''' 
    y = 50
    for x in range(300, 700, 50):
        draw_cloud(x, y)

    ''' snowman '''
    y = 510
    for x in range(20, 800, 305):
        draw_snowman(x, y)

    ''' trees '''
    y = 500
    for x in range(160, 500, 800):
        draw_tree(x, y)

    ''' houses '''
    y = 500
    for x in range(0, 500, 800):
        draw_house(x, y)

    ''' fence '''
    y = 475
    for x in range(5, 800, 30):
        post = [[x+5, y], [x+10, y+40], [x, y+40], [x, y+5]]
        pygame.draw.polygon(screen, WINDOW, post)

    pygame.draw.rect(screen, WINDOW, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WINDOW, [0, y+30, 800, 5])







    for r in rain:
        pygame.draw.ellipse(screen, WHITE, r)




    # pygame.draw.line(screen, GREEN, [300, 40], [100,500], 5)
    # pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300])
    # pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    # pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    # pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
