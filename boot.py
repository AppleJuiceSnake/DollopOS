import subprocess
import os
from time import strftime
logg = open(os.path.join("logs",strftime("%Y_%-m_%-d_%-I_%-M_%-S_dollop-os.log"),), "w")
process = subprocess.Popen("python main.py", shell=True, stdout=subprocess.PIPE)
while process.returncode == None:
    logg.write(process.communicate()[0])
exit()
