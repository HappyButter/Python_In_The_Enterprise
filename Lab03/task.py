import logging
from Plane import Plane
from Simulator import Simulation

# creating logger
logger = logging.getLogger("")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(name)-8s %(levelname)-8s %(message)s')

file_handler = logging.FileHandler('simulation_history.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



if __name__ == "__main__": 
    
    boeing = Plane('Starship')

    a = Simulation(boeing, logger)
    a.start()
