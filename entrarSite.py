import shutil
# import os
import subprocess
# import webbrowser
from time import sleep

chromeCaminho = shutil.which("google-chrome")

# os.system(chromeCaminho)

#===================abir o chrome em um site==================
# subprocess.Popen([chromeCaminho , "https://www.quotex.com"])
# webbrowser.open('https://www.google.com')

site = input("Digite o site que quer entrar: ")
site = site.replace("https://" , "").replace(".com" , "")

sleep(0.3)
subprocess.Popen([chromeCaminho , f"https://{site}.com"])