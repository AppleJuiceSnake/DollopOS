#!/usr/bin/python
# Planning Ahead for the future, with these modules....

import os
import sys
import getopt
import pygame
# The entire Dollop System, plus an api!
from dollop import *

#Set up screen
pygame.init()
scrsize = (dollop.scr_width, dollop.scr_height)
if not dollop.fullscr:
    screen = pygame.display.set_mode(scrsize)
else:
    screen = pygame.display.set_mode(scrsize, pygame.FULLSCREEN)

#Background Image
screen.blit(dollop.bg, (1, 1))
screen.blit(dollop.logo, (20,20))
pygame.display.flip()
dollop.mainLoop()
