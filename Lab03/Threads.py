import threading
from time import time
from random import randint


class Threads:
    def __init__(self, function, logger):
        self.function = function
        self.new_thread = threading.Event()
        self.logger = logger

    def start(self):
        thread = threading.Thread(target=self.set_function)
        thread.start()

    def stop(self):
        self.new_thread.set()

    def set_function(self):
        next_time = time() + randint(1,3)
        
        while not self.new_thread.wait(next_time - time()):
            next_time += randint(1,3)
            self.function(self.logger)

