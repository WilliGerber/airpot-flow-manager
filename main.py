# Abrir o arquivo de texto no modo de leitura

from time import sleep
from create_planes import Planes
import random



airplanes =   []

def createPlanes():
    while True:
        if airplanes.lenght < 10:
            airplanes.append(Planes.createPlane())
        sleep(random.randint(10,20))
        
def increaseWaitingTime():
    while True:
        for airplane in airplanes:
            airplane['waitingTime'] += 1
        sleep(1)
        
while True:
    
    createPlanes()
    increaseWaitingTime()
    
    
