'''
import os
os.system('python3 -m venv venv')
os.system('pip install -r requirements.txt')
os.system('python main.py')
os.system('cmd /c start chrome http://localhost:5555')

os.system('pause')
'''

import subprocess
import time
com=[]
com.append("python3 -m venv venv")
com.append('pip install -r requirements.txt')
com.append('python main.py')
com.append('cmd /c start chrome http://localhost:5555')
for i in range(len(com)):
    subprocess.Popen(com[i], shell=True)
    time.sleep(1)
