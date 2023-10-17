import random
from datetime import datetime
from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from device import Device
from dashboard import Dashboard

def main():

    # initialization of classes
    sensor = Sensor(0, 100)
    data_processor = DataProcessor()
    communication = Communication("https://central-server.example.com")
    device = Device(sensor, data_processor, communication)
    dashboard = Dashboard()

    # collecting of 10 samples of data
    device.get_data(10)

    # getting average, min, max and median of collected data
    processed_data = device.process_data()

    # communication with a server
    device.send_data_to_server(processed_data)
    device.receive_data_from_server()

    # display of data
    dashboard.display_data(device.data)
    print("\n")
    dashboard.display_analytics(processed_data)

# check if the current module is run as the main program or as imported module
if __name__ == "__main__":
    main()