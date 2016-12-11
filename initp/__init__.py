import pygame

logo = pygame.image.load('../res/initp')


#Speed Control
clock = pygame.time.Clock()
defaultSpeed = 60
currentSpeed = defaultSpeed
def setspeed(speed):
    try:
        speed += 0
        currentSpeed = speed
    except TypeError:
        print "HEY! THE SPEED IN setspeed() IS SUPPOSED TO BE A NUMBER!"

#Main Loop
def mainLoop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    pygame.display.flip()
    clock.tick(defaultSpeed)
