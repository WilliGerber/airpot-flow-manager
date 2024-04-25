from time import sleep
import random
import datetime

class Planes(object):
    
    def __init__(self):
        pass
        
    def randomUrgency(self):
        number = random.randint(1, 100)
        limit_1 = 75
        limit_2 = limit_1 + 24
        if number <= limit_1:
            return 1
        elif number <= limit_2:
            return 2
        else:
            return 3
            
    def choose_takeoff_or_landing(self):
        number = random.randint(1, 2)

        if number == 1:
            return "Takeoff"
        else:
            return "Landing"
            
    def createPlane(self):
        return {
            'code': random.randint(1000, 99999),
            'arrival_time': datetime.datetime.now(),
            'waiting_time': 0,
            'urgency': self.randomUrgency(),
            'type': self.choose_takeoff_or_landing(),
            'status': False
        }

