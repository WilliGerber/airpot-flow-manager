from time import sleep
from planes import Planes
import threading
import random

planes = Planes()

airplanes = []

def createPlanes():
    while True:
        if len(airplanes) < 20:
            airplanes.append(planes.createPlane())
            sleep(random.randint(1, 10))

def updateElapsedTime():
    while True:
        for plane in airplanes:
            plane['waiting_time'] += 1
            sleep(1)

threading.Thread(target=createPlanes).start()
threading.Thread(target=updateElapsedTime).start()

while True:
    print(airplanes)
    sleep(1)