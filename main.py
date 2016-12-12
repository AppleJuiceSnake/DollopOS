#!/usr/bin/python
# Planning Ahead for the future, with these modules....

import os
import sys
import getopt
import pygame
# The entire Dollop System, plus an api!
import dollop

#Constants
fullscr = False

#Set up screen
pygame.init()
scrsize = (dollop.scr_width, dollop.scr_height)
if not dollop.fullscr:
    screen = pygame.display.set_mode(scrsize)
else:
    screen = pygame.display.set_mode(scrsize, pygame.FULLSCREEN)

#Window Title
pygame.display.set_caption('DollopOS OpenAlpha 1')

#Background Image, and various other screen elements
screen.blit(dollop.bg, (1, 1))
screen.blit(dollop.tskbar, (0,440))
screen.blit(dollop.logo, (288,448))
screen.blit(dollop.menu, (0,440))
screen.blit(dollop.label, (50, 440))
pygame.display.flip()
dollop.mainLoop()

