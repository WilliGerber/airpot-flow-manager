from time import sleep
from planes import Planes
import threading
import random
from planeManager import PlaneManager

airplanes = []
planes = Planes()
planeManager = PlaneManager(airplanes)

threading.Thread(target=planeManager.createPlanes).start()
threading.Thread(target=planeManager.updateElapsedTime).start()

while True:
    print(airplanes)
    sleep(1)