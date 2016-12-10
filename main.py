# Planning Ahead for the future, with these modules....
import os
import sys
import pygame

#set up screen
pygame.init()
screen = pygame.display.set_mode((320, 480))
done = False

#Background Image
index = pygame.image.load('res/placeholder.png')
screen.blit(index, (1, 1))
pygame.display.flip()

#Speed Control
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)

#Quitting Control
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    

# a test comment left in the code; should remove
print "Dollop OS Testing Git or Whatevs"
