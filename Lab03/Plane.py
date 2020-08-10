from time import sleep
import random

class Plane:
    def __init__(self, name):
        self.orientation = 0
        self.name = name
        self.rate_of_correction = 5
        self.value = self.gauss_generator(1,1000)

    def __str__(self):
        return "Actual orientation is: {}".format(self.orientation) 


    def gauss_generator(self, start, end):
        current = start 
        while current < end:
            yield random.gauss(0, 2*self.rate_of_correction)
            current += 1


    def print_and_logg(self, logger, name):
        print("tilt = {:3.6f}".format(self.orientation))
        logger.info("Function: {} | tilt = {:3.6f}".format(name, self.orientation))


    def apply_correction(self, logger, correction):
        self.orientation += correction
        self.print_and_logg(logger, "apply_correction")


    def add_turbulence(self, logger):
        self.orientation += next(self.value)
        self.print_and_logg(logger, "add_turbulence")


    def handle_events(self, event, logger):
        if event.type == 'C':
            self.apply_correction(logger, event.get_step)
        elif event.type == 'T':
            self.add_turbulence(logger)



