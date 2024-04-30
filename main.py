from time import sleep
from planes import Planes
import threading
import random
from planeManager import PlaneManager

class StatusManager():
    landingStripBusy = threading.Event()
    free_dock_percentage40 = threading.Event()
    free_dock_percentage0 = threading.Event()
    deadlock = threading.Event()
    
    landingStripBusy.clear()
    free_dock_percentage0.clear()
    free_dock_percentage40.clear()
    deadlock.clear()

status = StatusManager()
airplanes = []
dock_amount = 10
planes = Planes()
planeManager = PlaneManager(airplanes, status, dock_amount)

# Funções para serem executadas em threads separadas
def create_planes_thread():
    planeManager.create_planes()

def update_elapsed_time_thread():
    planeManager.update_elapsedTime()

def check_landing_strip_status_thread():
    planeManager.check_landing_strip_status()

# Iniciar as threads
threads = [
    threading.Thread(target=create_planes_thread),
    threading.Thread(target=update_elapsed_time_thread),
    threading.Thread(target=check_landing_strip_status_thread)
]

for thread in threads:
    thread.start()

while True:
    while not status.deadlock.is_set():
        if status.landingStripBusy.is_set():
            sleep(1)
        elif not status.landingStripBusy.is_set():
            cleared_airplane = planeManager.calculate_priority()
        sleep(1)
        print(  f'landingStripBusy {status.landingStripBusy.is_set()}, '
                f'free_dock_percentage0: {status.free_dock_percentage0.is_set()}, '
                f'free_dock_percentage40: {status.free_dock_percentage40.is_set()} ')
    print('Error: DEADLOCK achieved.')
    