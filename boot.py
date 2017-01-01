#!/usr/bin/python
import subprocess
import os
from time import strftime
if not os.path.exists(os.path.join(os.getcwd(), "logs")):
    os.makedirs(os.path.join(os.getcwd(), "logs"))
def start():
    logg = open(os.path.join(os.getcwd(),"logs",strftime("%Y_%-m_%-d_%-I_%-M_%-S_dollop-os.log"),), "w+")
    process = subprocess.Popen("python main.py", shell=True, stdout=subprocess.PIPE)
    while process.returncode == None:
        if process.communicate()[0] == "restart":
            start()
        logg.write(process.communicate()[0])
    if (process.returncode == 0):
        exit()
    else:
        print process.returncode
        from errno import errorcode
        print errorcode.get(process.returncode)
        exit()