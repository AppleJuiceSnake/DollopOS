#!/usr/bin/python
import subprocess
import os
import sys
import pygame
from time import strftime
from subprocess import Popen, PIPE

aboutopen = "False"
restarted = False
cp2 = Popen(['git', 'rev-list', '--all', '--count'], stdout=PIPE, stderr=PIPE)
while cp2.returncode == None:
    currev = str(int(cp2.communicate()[0]))
if not os.path.exists(os.path.join(os.getcwd(), "logs")):
    os.makedirs(os.path.join(os.getcwd(), "logs"))


def start():
    logg = open(os.path.join(os.getcwd(), "logs", strftime("%Y_%-m_%-d_%-I_%-M_%-S_dollop-os.log")), "w+")
    logg.write("DollopOS is now starting up...")
    print("Current Platform: ", sys.platform)
    print("Current Revision: ", currev)
    print("Pygame Version", pygame.ver)
    logg.write("Platfrom:")
    logg.write(sys.platform)
    logg.write("\n")
    logg.write("Revision:")
    logg.write(currev)
    logg.write("\n")
    logg.write("Pygame Version:")
    logg.write(pygame.ver)
    logg.write("\n")

    process = subprocess.Popen("python main.py booting", shell=True, stdout=subprocess.PIPE)
    while process.returncode == None:
        print(process.communicate()[0])
        if process.communicate()[0] == "Restarting...":
            global restarted
            logg.close()
            restarted = True
            process.kill()
            start()
        logg.write(process.communicate()[0])

    if (process.returncode == 0):
        exit()
    else:
        print(process.returncode)
        from errno import errorcode
        print(errorcode.get(process.returncode))
        exit()


start()
