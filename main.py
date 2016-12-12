#!/usr/bin/python
# Planning Ahead for the future, with these modules....

import os
import sys
import getopt
import pygame
# The entire Dollop System, plus an api!
from dollop import *

#Constants
logo = pygame.image.load('res/logo.png')
bg = pygame.image.load('res/placeholder.png')
menu = pygame.image.load('res/menu.png')
scr_width = 320
scr_height = 480
fullscr = False

#Set up screen
pygame.init()
scrsize = (scr_width, scr_height)
if not fullscr:
    screen = pygame.display.set_mode(scrsize)
else:
    screen = pygame.display.set_mode(scrsize, pygame.FULLSCREEN)

#Background Image
screen.blit(dollop.bg, (1, 1))
screen.blit(dollop.logo, (20,20))
screen.blit(menu, (320,1)
pygame.display.flip()
dollop.mainLoop()
