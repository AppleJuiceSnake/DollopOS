# modules,modules,modules
import os
import sys
import getopt
import pygame
import ConfigParser
import io
import subprocess
from time import sleep
from ConfigParser import SafeConfigParser
from time import localtime, strftime
# Current revision from commit count
from subprocess import Popen, PIPE
cp2 = Popen(['git', 'rev-list', '--all', '--count'], stdout=PIPE,stderr=PIPE)
while cp2.returncode == None:
    currev = str(int(cp2.communicate()[0]))


#Constants
aboutopen = 'False'
aboutopened = False
menuopen = True
fullscr = False
started = False
time = strftime("%I:%M", localtime())
curstate = ""
# Assets
parser = SafeConfigParser()
parser.read('settings/display.ini')

bgsetting =  parser.get('Background', 'image')
bsetting =  parser.get('Background', 'image')
scr_widths = parser.get('Resoultion', 'width')
scr_heights = parser.get('Resoultion', 'Height')
scr_width = int(scr_widths)
scr_height = int(scr_heights)

parser.read("settings/installed.ini")

instlab = "programs are installed"
installeds = parser.get('Programs', 'amount')
installed = int(installeds)
pe = parser.get('Programs', 'image')
perror = pygame.image.load(pe)
p1 = parser.get('Programs', 'p1')
p1image = parser.get('Programs', 'p1image')
aboutopen = parser.get("Programs", 'aboutopen')

action = ''
confopen = False
print bgsetting , 'is currenlty set as the background'
rotate = pygame.image.load('res/rotate.png')
cover = pygame.image.load('res/cover.png')
warning = pygame.image.load('res/warning.png')
sdicon = pygame.image.load('res/shutdown_icon.png')
ab = pygame.image.load('res/about.png')
abtb = pygame.image.load('res/about_tb_icon.png')
dbtb = pygame.image.load('res/desktop_tb_icon.png')
mtb = pygame.image.load('res/menu_tb_icon.png')
respring = pygame.image.load('res/restart_icon.png')
restart = pygame.image.load('res/restart.png')
logo = pygame.image.load('res/logo.png')
bg = pygame.image.load(bsetting)
sd = pygame.image.load('res/shut_down.png')
tskbar = pygame.image.load('res/taskbar.png')
menu = pygame.image.load('res/menu_icon.png')
close = pygame.image.load('res/close_icon.png')
# Set up pygame
pygame.init()
pygame.font.init()
scrsize = (scr_width, scr_height)
if not fullscr:
    screen = pygame.display.set_mode(scrsize)
else:
    screen = pygame.display.set_mode(scrsize, pygame.FULLSCREEN)
# Text Functions 
def text_objects(text,color, font):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
def display_text(text,color,size,xloc,yloc):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text,color,largeText)
    TextRect.topleft = (xloc,yloc)
    screen.blit(TextSurf, TextRect)

start = pygame.image.load('res/start.png')
screen.blit(start, (0,0))
pygame.display.flip()

# Load it back up for landscape mode
parser.read('settings/display.ini')
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
    global aboutopened
    if menuopen:
        curstate = "Menu"
        #Set up the background for the menu before drawing absolutly anything else.
        pygame.draw.rect(screen, gray,(0,280,200,160))
        screen.blit(pygame.transform.flip(menu,False,True), (0,440))
        screen.blit(tskbar, (0,0))
        if aboutopened:
            screen.blit(close, (280,0))
        if not aboutopened:
            screen.blit(sdicon, (280,0))
        screen.blit(respring, (240,0))
        display_text(instlab, black, 15, 20, 285)
        display_text(installeds, black, 15, 0, 285)
        if installed == 0:
            screen.blit(perror, (70,320))
        if installed == 1:
            display_text(p1, black, 15,1,305)
            screen.blit(close, (1,325))
        display_text("Menu", black, 35, 50, 0)
        screen.blit(mtb, (0,0))
        menuopen = False
        pygame.display.flip()
        menuopen = False
        display_text(installed,black,11,0,380)
    else:

        screen.blit(bg, (1, 1))
        screen.blit(tskbar, (0, 440))
        screen.blit(tskbar, (0, 0))
        if aboutopened:
            screen.blit(close, (280,0))
        if not aboutopened:
            screen.blit(sdicon, (280,0))
        screen.blit(logo, (288, 448))
        screen.blit(menu, (0, 440))
        screen.blit(respring, (240,0))
        screen.blit(rotate, (240,440))
        display_text("Desktop", black, 35, 50, 0)
        screen.blit(dbtb, (0,0))
        display_text(time, black, 35, 50, 440)
        menuopen = True
        pygame.display.flip()

def about():
    global aboutopened
    aboutopen = "True"
    aboutopened = True
    curstate = "Menu"
    screen.blit(cover, (0,0))
    screen.blit(ab, (0,0))
    screen.blit(tskbar, (0, 440))
    screen.blit(tskbar, (0, 0))
    if aboutopened:
        screen.blit(close, (280,0))
    if not aboutopened:
        screen.blit(sdicon, (280,0))
    screen.blit(logo, (288, 448))
    screen.blit(menu, (0, 440))
    screen.blit(respring, (240,0))
    screen.blit(rotate, (240,440))
    display_text(time, black, 35, 50, 440)
    screen.blit(abtb, (0,0))
    display_text("About", black, 35, 50, 0)
    display_text('About DollopOS', white, 30, 40, 80)
    display_text('Use this area to put some sogan...', white, 15, 35, 125)
    display_text('Current Revision:', white, 30, 0, 150)
    display_text('DollopOS is licenced under GPL 3.0', white, 15, 35, 390)
    display_text('AppleJuiceSnake, 2016-2017', white, 13, 60, 410)
    display_text(currev, white, 30, 260, 150)
    pygame.display.flip()

def areyousure():
    global event
    global time
    global aboutopened
    global confopen
    global curstate
    global action
    curstate = ""
    screen.blit(cover,(0, 0))
    screen.blit(tskbar, (0, 440))
    screen.blit(tskbar, (0, 0))
    if aboutopened:
        screen.blit(close, (280,0))
    if not aboutopened:
        screen.blit(sdicon, (280,0))
    if curstate == "Menu":
        display_text("Warning", black, 35, 50, 0)
    screen.blit(logo, (288, 448))
    screen.blit(menu, (0, 440))
    screen.blit(respring, (240,0))
    screen.blit(rotate, (240,440))
    display_text(time, black, 35, 50, 440)
    screen.blit(warning, (0,0))
    display_text('Are you sure you want to', white, 15, 30, 125)
    display_text('?', white, 15, 290, 125)
    display_text(action, white, 15, 210, 125)
    pygame.draw.rect(screen, teal,(20,220,90,50))
    pygame.draw.rect(screen, teal,(200,220,90,50))
    display_text('Yes', white, 35, 40, 220)
    display_text('No', white, 35, 220, 220)
    pygame.display.flip()
    confopen = True
    mainLoop()

   


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
    global aboutopened
    global event
    global menuopen
    global confopen
    global action
    while True:
        if curstate == "":
            menuopen = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if mouse[0] < 280:
                        if mouse[0] > 240:
                            if mouse[1] < 40:
                                if mouse[1] > 0:
                                    action = "Restart"
                                    areyousure()
                    if mouse[0] < 80:
                        if mouse[0] > 0:
                            if mouse[1] < 280:
                                if mouse[1] > 220:
                                    if confopen:
                                        if action == "Shut Down":
                                            screen.blit(sd, (0,0))
                                            pygame.display.flip()
                                            #Shutdown Scripts Here!
                                            pygame.quit()
                                            quit()
                                        if action == "Restart":
                                            screen.blit(restart, (0,0))
                                            pygame.display.flip()
                                            #Put Restart scripts here since 'print "restart"'
                                            #basically makes a call to the boot.py
                                            #to restart the script/system
                                            print "Restarting..."
                                    if not confopen:
                                        mainLoop()
                    if mouse[0] < 320:
                        if mouse[0] > 220:
                            if mouse[1] < 280:
                                if mouse[1] > 220:
                                    if confopen:
                                        confopen = False
                                        startup()
                                    if not confopen:
                                        mainLoop()
                    if mouse[0] > 280:
                        if mouse[1] < 40:
                            if aboutopened:
                                aboutopened = False
                                startup()
                            action = 'Shut Down'
                            areyousure()
                    if mouse[0] < 40:
                        if mouse[0] > 0:
                            if mouse[1] < 480:
                                if mouse[1] > 440:
                                    #State stuff goes here
                                    curstate = "Menu"
                                    menu_opener()
                    if mouse[0] < 320:
                        if mouse[0] > 280:
                            if mouse[1] < 480:
                                if mouse[1] > 440:
                                    #State stuff goes here
                                    curstate = "Menu"
                                    about()
                    #Temporary quit stuffs for convenience
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if not time == strftime("%I:%M", localtime()):
                time = strftime("%I:%M", localtime())
                display_text(time, black, 35, 50, 440)
            display_text("Desktop",black,35,50,0)
            screen.blit(dbtb, (0,0))
            pygame.display.flip()
            clock.tick(currentSpeed)
            pygame.draw.rect(screen, red,(550,450,100,50))
        else:
            if curstate == "Menu":
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        if mouse[0] < 80:
                            if mouse[0] > 0:
                                if mouse[1] < 280:
                                    if mouse[1] > 220:
                                        if confopen:
                                            if action == "Shut Down":
                                                screen.blit(sd, (0,0))
                                                pygame.display.flip()
                                                #Shutdown Scripts Here! 
                                                #Make it wait here -Atmatm6
                                                pygame.time.wait(5000)
                                                pygame.quit()
                                                quit()
                                            if action == "Restart":
                                                screen.blit(restart, (0,0))
                                                pygame.display.flip()
                                                print "Restarting..."
                                                execfile('boot.py')
                                                #Put scripts to be ran on shutdown here
                                                pygame.quit()
                                                quit()
                                        if not confopen:
                                            mainLoop()
                        if mouse[0] < 280:
                            if mouse[0] > 240:
                                if mouse[1] < 40:
                                    if mouse[1] > 0:
                                        action = "Restart"
                                        areyousure()
                        if mouse[0] < 320:
                            if mouse[0] > 280:
                                if mouse[1] < 480:
                                    if mouse[1] > 440:
                                        #State stuff goes here
                                        curstate = "Menu"
                                        about()
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
                                if not menuopen:
                                    if aboutopened:
                                        aboutopened = False
                                        startup()
                                    action = "Shut Down"
                                    areyousure()
                                if menuopen:
                                    if aboutopened:
                                        aboutopened = False
                                        startup()
                                    action = "Shut Down"
                                    areyousure()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if not time == strftime("%I:%M", localtime()):
            time = strftime("%I:%M", localtime())
            display_text(time,black,35,50,440)
        pygame.display.flip()
        clock.tick(currentSpeed)

def startup():
    global aboutopened
    landen = parser.get('Landscape', 'enabled')
    if landen == "True":
        #Put landscape screen settings here
        print "landen is on..."
    if landen == "False":
        screen.blit(bg, (1, 1))
        screen.blit(tskbar, (0,440))
        screen.blit(tskbar, (0,0))
        if aboutopened:
            screen.blit(close, (280,0))
        if not aboutopened:
            screen.blit(sdicon, (280,0))
        screen.blit(logo, (288,448))
        screen.blit(menu, (0,440))
        screen.blit(respring, (240,0))
        screen.blit(rotate, (240,440))
        screen.blit(dbtb, (0,0))
        display_text(time,black,35,50,440)
        pygame.display.flip()
    # Create stuff to log
    print "Current Platform: ", sys.platform
    print "Current Revision: ", currev
    print "Pygame Version", pygame.ver
    mainLoop()


# Changing to landccape mode
# parser.set('landscape', 'enabled', 'True')
startup()
