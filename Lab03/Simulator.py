from time import sleep
from Events import Event, Correction, Turbulence
from Plane import Plane
from Threads import Threads


class Simulation:
    def __init__(self, plane, log):
        self.plane = plane
        self.log = log
        self.random_turnulance = Threads(self.plane.add_turbulence, self.log)
        
        self.log.warning('Starting new simulation of plane: {}'.format(self.plane.name))

    def print_hello(self):
        print("hello")

    def start(self):
        print("==========Starting Simulation===========")
        print(" End with: q")
        print(" Correction - : -")
        print(" Correction + : +")
        print(" Add more turbulance: t")
        print("========================================")
        sleep(2)

        self.random_turnulance.start()

        while True:
            key = input("Make move: ")
            if key == 'q':
                self.log.warning('Ending silmulation')
                self.random_turnulance.stop()
                break
            elif key == '-':
                self.plane.handle_events(Correction(-5), self.log)
                print(self.plane)
            elif key == '+':
                self.plane.handle_events(Correction(5), self.log)
                print(self.plane)
            elif key == 't':
                self.plane.handle_events(Turbulence(), self.log)
                print(self.plane)

        
            
        