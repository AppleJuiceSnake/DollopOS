# Planning Ahead for the future, with these modules....
import os
import sys
import pygame

#set up screen
pygame.init()
screen = pygame.display.set_mode((320, 480))
done = False

index = pygame.image.load('placeholder.png')
screen.blit(index, (1, 1))
pygame.display.flip()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    


# a test comment left in the code; should remove
print "Dollop OS Testing Git or Whatevs"
