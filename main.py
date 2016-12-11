# Planning Ahead for the future, with these modules....
import os
import sys
import pygame
import initp

#set up screen
pygame.init()
screen = pygame.display.set_mode((320, 480))

#Background Image
index = pygame.image.load('res/placeholder.png')
screen.blit(index, (1, 1))
pygame.display.flip()


screen.blit(initp.logo, (20,20))
mainLoop()
