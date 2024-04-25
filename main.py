from time import sleep
from create_planes import Planes
import random
import threading

planes = Planes()
airplanes =   []

def createPlanes():
    while True:
        if len(airplanes) < 10:
            airplanes.append(planes.createPlane())
        sleep(random.randint(10,20))
        
def increaseWaitingTime():
    while True:
        for airplane in airplanes:
            airplane['waiting_time'] += 1
        sleep(1)
        
while True:
    threading.Thread(target=createPlanes).start()
    threading.Thread(target=increaseWaitingTime).start()
    
    print(airplanes)
    
    sleep(1)
