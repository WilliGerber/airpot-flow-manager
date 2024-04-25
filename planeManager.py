
from planes import Planes 
import random
from time import sleep

class PlaneManager(object):
    def __init__(self, airplanes):
        self.planes = Planes()
        self.airplanes = airplanes

    def createPlanes(self):
        while True:
            if len(self.airplanes) < 20:
                self.airplanes.append(self.planes.createPlane())
                sleep(random.randint(1, 10))

    def updateElapsedTime(self):
        while True:
            for plane in self.airplanes:
                plane['waiting_time'] += 1
                sleep(1)

    def calculatePriority():
        print("priority")

    def checkLandingStripStatus():
        print("checkLandingStripStatus")