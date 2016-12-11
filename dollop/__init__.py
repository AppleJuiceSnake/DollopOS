import pygame
import api

#Constants
logo = pygame.image.load('res/logo.png')
bg = pygame.image.load('res/placeholder.png')
scr_width = 320
scr_height = 480
fullscr = False

#Speed Control
clock = pygame.time.Clock()
defaultSpeed = 60
currentSpeed = defaultSpeed
def setSpeed(speed):
    try:
        speed += 0
        currentSpeed = speed
    except TypeError:
        print "HEY! THE SPEED IN setSpeed() IS SUPPOSED TO BE A NUMBER!"

def getSpeed():
    return currentSpeed
#Main Loop
def mainLoop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    api.message_display()
    pygame.display.flip()
    clock.tick(currentSpeed)
