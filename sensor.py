# Class for simulating sensor

import random
from datetime import datetime

class Sensor:

    def __init__(self, lower_range, upper_range):
        self.lower_range = lower_range
        self.upper_range = upper_range

    # simulation of sensor which returns timestamp and random number between min and max values of sensor
    def read_data(self):
        value = random.uniform(self.lower_range, self.upper_range)
        timestamp = datetime.now()
        return [timestamp, value]