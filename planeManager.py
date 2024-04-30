
from planes import Planes 
import random
from time import sleep

class PlaneManager(object):
    def __init__(self, airplanes, status, dock_ammount):
        self.planes = Planes()
        self.airplanes = airplanes
        self.status = status
        self.dock_ammount = dock_ammount
        self.airplanes_with_status = []

    def create_planes(self):
        while True:
            if len(self.airplanes) < 20:
                self.airplanes.append(self.planes.createPlane())
                sleep(random.randint(1, 10))
                print('Airplane created')

    def update_elapsedTime(self):
        while True:
            for plane in self.airplanes:
                plane['waiting_time'] += 1
                sleep(1)

    def calculate_priority(self):
        # P (prioridade) = T (tempo de espera) x U (peso urgencia) x TDL (taxa docas livres)
        airplanes_to_priorize = self.airplanes
        if list(filter(lambda plane: plane['urgency'] == 5, self.airplanes)):
            airplanes_to_priorize = list(filter(lambda plane: plane['urgency'] == 5, self.airplanes))
            for plane in airplanes_to_priorize:
                plane['priority'] = plane['waiting_time']
        elif self.status.free_dock_percentage0.is_set():
            airplanes_to_priorize = list(filter(lambda plane: plane['type'] == 'Takeoff', self.airplanes))
            for plane in airplanes_to_priorize:
                plane['priority'] = plane['waiting_time']*plane['urgency']
        else:
            for plane in airplanes_to_priorize:           
                if self.status.free_dock_percentage40.is_set() and plane['type'] == 'Takeoff':
                    tdl = 3
                else:
                    tdl = 2
                plane['priority'] = plane['waiting_time']*plane['urgency']*tdl
        if airplanes_to_priorize:
            authorized_plane = sorted(airplanes_to_priorize, key=lambda plane: plane['priority'], reverse=True)[0]
        
        for plane in self.airplanes:
            if plane['code'] == authorized_plane['code']:
                plane['status'] = True
        print(authorized_plane)
        return authorized_plane


    def check_landing_strip_status(self):
        while True:
            self.airplanes_with_status = list(filter(lambda plane: plane['status'] == True, self.airplanes))
            if len(self.airplanes_with_status) == 1:
                self.status.landingStripBusy.set()
                print('landingStripBusy seted')
                sleep(random.randint(10, 20))
                self.clear_airplane_status()
            elif len(self.airplanes_with_status) > 1:
                self.status.deadlock.set()
            else:
                self.status.landingStripBusy.clear()
                print('landingStripBusy cleared')
            print('aqui')
            sleep(1)
        
    def clear_airplane_status(self):
        if self.status.deadlock.is_set():
            pass
        else:
            for plane in self.airplanes:
                if plane['code'] == self.airplanes_with_status[0]['code']:
                    self.airplanes.remove(plane)
                    print(f'Removed plane: {plane["code"]}')


    def calculate_free_dock_percentage(self):
        while True:
            airplanes_to_takeoff = list(filter(lambda plane: plane['type'] == 'Takeoff', self.airplanes))
            if len(airplanes_to_takeoff) == self.dock_ammount:
                self.status.free_dock_percentage0.set()
                self.status.free_dock_percentage40.clear()
                print('free_dock_percentage0 seted')
            elif len(airplanes_to_takeoff)/self.dock_ammount < 60:
                self.status.free_dock_percentage40.set()
                self.status.free_dock_percentage0.clear()
                print('free_dock_percentage40 seted')
            else:
                self.status.free_dock_percentage40.clear()
                self.status.free_dock_percentage0.clear()
                print('free_dock_percentage cleared')

