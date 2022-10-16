import subprocess
import time
import os
com=[]
com.append("python3 -m venv venv")
com.append('pip install -r requirements.txt')
com.append('python main.py')
com.append('cmd /c start chrome http://localhost:5555')
for i in range(len(com)):
    subprocess.Popen(com[i], shell=True)
    time.sleep(1)

os.system('pause')
