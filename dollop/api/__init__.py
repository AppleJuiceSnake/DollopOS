#API BEGINS!
import os
import pygame
import bluetooth
print "Incomplete!~"

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def display_text(text,size,xloc,yloc):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (xloc,yloc)
    gameDisplay.blit(TextSurf, TextRect)
