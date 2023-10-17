# Class for connecting sensor, data processor, and communication classes together

from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication

class Device:
    def __init__(self, sensor, data_processor, communication):
        self.sensor = sensor
        self.data_processor = data_processor
        self.communication = communication
        self.data = []

    def get_data(self, data_size):
        try:
            for _ in range(data_size):
                self.data.append(self.sensor.read_data())
        except Exception as e:
            print(f"Error getting data: {e}")

    def process_data(self):
        try:
            avg = self.data_processor.get_average(self.data)
            min_value = self.data_processor.get_min_value(self.data)
            max_value = self.data_processor.get_max_value(self.data)
            med = self.data_processor.get_median(self.data)
            return avg, min_value, max_value, med
        except Exception as e:
            print(f"Error processing data: {e}")

    def send_data_to_server(self, data):
        try:
            self.communication.send_data(data)
        except Exception as e:
            print(f"Error sending data to server: {e}")

    def receive_data_from_server(self):
        try:
            self.communication.receive_data()
        except Exception as e:
            print(f"Error receiving data from server: {e}")