# Planning Ahead for the future, with these modules....
import os
import sys
import getopt
import pygame
from time import localtime, strftime
# Current revision from commit count
from subprocess import Popen, PIPE
cp2 = Popen(['git', 'rev-list', '--all', '--count'], stdout=PIPE,stderr=PIPE)
while cp2.returncode == None:
    currev = str(int(cp2.communicate()[0]))
# Constants

logo = pygame.image.load('res/logo.png')
bg = pygame.image.load('res/placeholder.png')
tskbar = pygame.image.load('res/taskbar.png')
menu = pygame.image.load('res/menu_icon.png')
close = pygame.image.load('res/close_icon.png')
scr_width = 320
scr_height = 480
fullscr = False
menuopen = False
time = strftime("%I:%M", localtime())
curstate = ""
# Set up pygame
pygame.init()
pygame.font.init()
scrsize = (scr_width, scr_height)
if not fullscr:
    screen = pygame.display.set_mode(scrsize)
else:
    screen = pygame.display.set_mode(scrsize, pygame.FULLSCREEN)
# Text Functions 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def display_text(text,size,xloc,yloc):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.topleft = (xloc,yloc)
    screen.blit(TextSurf, TextRect)
# To add more colors, go to www.colorschemer.com/online.html or another color palette
# with the ability to see the RGB values. Then fork the Github Repo and modify 
# this area and johnnyw3 or I will decide on whether your changes are acceptable.
# Colors
black = (0,0,0)
white = (255,255,255)
brown = (100,42,42)
gray = (128,128,128)
darkdarkred = (64,0,0)
rhubarb = (128,0,0)
red = (255,0,0)
redorange = (255,64,0)
orange = (255,128,0)
orangeyellow = (255,192,0)
yellow = (255,255,0)
limegreen = (192,255,0)
screengreen = (128,255,0)
lightgreen = (64,255,0)
green = (0,255,0)
mehgreen = (0,255,64)
greenblue = (0,255,128)
aqua = (0,255,192)
lightblue = (0,255,255)
turquoise = (0,192,255)
teal = (0,128,255)
lightdarkblue = (0,64,255)
blue = (0,0,255)
darkblue = (64,0,255)
purple = (128,0,255)
violet = (192,0,255)
magenta = (255,0,255)
darklightmagenta = (255,0,192)
pink = (255,0,128)
lightred = (255,0,64)
# Image Functions
def menu_opener():
    global menuopen
    if menuopen:
        curstate = "Menu"
        screen.blit(pygame.transform.flip(menu,False,True), (0,440))
        screen.blit(tskbar, (0,0))
        screen.blit(close, (280,0))
        menuopen = False
        pygame.display.flip()
    else:
        display_text("Desktop", 35, 0, 0)
        screen.blit(menu, (0,440))
        menuopen = True
        pygame.display.flip()
# Speed Control
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
# Window Title
pygame.display.set_caption('DollopOS Rev ' + str(int(currev)))
# Main Loop
# Always define variables that need to stay set from the loop, outside the loop.
# Curstates are: "" "Menu"
def mainLoop():
    global time
    global curstate
    while True:
        if curstate == "":
            menuopen = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] < 40:
                        if mouse[0] > 0:
                            if mouse[1] < 480:
                                if mouse[1] > 440:
                                    #State stuff goes here
                                    curstate = "Menu"
                                    menu_opener()
                    #Temporary quit stuffs for convenience
                    if mouse[0] > 280:
                        if mouse[1] < 40:
                            pygame.quit()
                            quit()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if not time == strftime("%I:%M", localtime()):
                time = strftime("%I:%M", localtime())
                font = pygame.font.SysFont("comicsansms", 55)
                label = font.render(time, True, black)
                screen.blit(tskbar, (0,0))
                screen.blit(label, (50,440))
                screen.blit(close, (280,0))
            display_text("Desktop",35,0,0)
            pygame.display.flip()
            clock.tick(currentSpeed)
            pygame.draw.rect(screen, red,(550,450,100,50))
        else:
            if curstate == "Menu":
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        if mouse[0] < 40:
                            if mouse[0] > 0:
                                if mouse[1] < 480:
                                    if mouse[1] > 440:
                                        # State stuff goes here
                                        curstate = "Menu"
                                        menu_opener()
                        # Temporary quit stuffs for convenience
                        if mouse[0] > 280:
                            if mouse[1] < 40:
                                pygame.quit()
                                quit()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                display_text("Menu", 35, 0,0)
                screen.blit(close, (280, 0))
def startup():
    screen.blit(bg, (1, 1))
    screen.blit(tskbar, (0,440))
    screen.blit(tskbar, (0,0))
    screen.blit(close, (280,0))
    screen.blit(logo, (288,448))
    screen.blit(menu, (0,440))
    font = pygame.font.SysFont("comicsansms", 55)
    label = font.render(time, True, black)
    screen.blit(label, (50, 440))
    pygame.display.flip()
    # Create stuff to log
    print "Current Platform: ", sys.platform
    print "Current Revision: ", currev
    print "Pygame Version", pygame.ver
    mainLoop()
startup()

