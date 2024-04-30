from time import sleep
from planes import Planes
import threading
import random
from planeManager import PlaneManager

class statusManager():
    landingStripBusy = threading.Event()
    free_dock_percentage40 = threading.Event()
    free_dock_percentage0 = threading.Event()
    deadlock = threading.Event()
    
    landingStripBusy.clear()
    free_dock_percentage0.clear()
    free_dock_percentage40.clear()
    deadlock.clear()

status = statusManager()
airplanes = []
dock_ammount = 10
planes = Planes()
planeManager = PlaneManager(airplanes, status, dock_ammount)


threading.Thread(target=planeManager.create_planes).start()
threading.Thread(target=planeManager.update_elapsedTime).start()
threading.Thread(target=planeManager.check_landing_strip_status).start()

while True:
    while not status.deadlock.is_set():
        while status.landingStripBusy.is_set():
            sleep(1)
        if not status.landingStripBusy.is_set():
            cleared_airplane = planeManager.calculate_priority()
        sleep(1)
        print(  f'landingStripBusy {status.landingStripBusy.is_set()}, '
                f'free_dock_percentage0: {status.free_dock_percentage0.is_set()}, '
                f'free_dock_percentage40 {status.free_dock_percentage40.is_set()}, ')
    print('Error: DEADLOCK achieved. Review Code')