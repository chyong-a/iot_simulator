import sys
import os

# Adding the parent directory of the current file to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest

from communication import Communication
from dashboard import Dashboard
from data_processor import DataProcessor
from device import Device
from sensor import Sensor

class TestIoTDevice(unittest.TestCase):

    def setUp(self):
        print("\nSet Up")
        self.sensor = Sensor(0, 100)
        self.data_processor = DataProcessor()
        self.communication = Communication("https://central-server.example.com")
        self.device = Device(self.sensor, self.data_processor, self.communication)
        self.dashboard = Dashboard()
        
    def tearDown(self):
        print("\nTear Down")
    
    def test_get_data(self):
        self.device.get_data(10)
        self.assertEqual(len(self.device.data), 10)

    def test_get_average(self):
        data = [(1, 10), (2, 20), (3, 30)]
        expected_average = 20
        self.assertEqual(self.data_processor.get_average(data), expected_average)

    def test_get_min_value(self):
        data = [(1, 10), (2, 20), (3, 30)]
        expected_min = 10
        self.assertEqual(self.data_processor.get_min_value(data), expected_min)

    def test_get_max_value(self):
        data = [(1, 10), (2, 20), (3, 30)]
        expected_max = 30
        self.assertEqual(self.data_processor.get_max_value(data), expected_max)
    
    def test_get_median(self):
        data = [(1, 10), (2, 20), (3, 10)]
        expected_median = 10
        self.assertEqual(self.data_processor.get_median(data), expected_median)

    def test_process_data(self):
        self.device.get_data(10)
        processed_data = self.device.process_data()
        self.assertIsNotNone(processed_data)
        self.assertIsInstance(processed_data, tuple)

    def test_send_data_to_server(self):
        processed_data = (50, 10, 90)
        self.device.send_data_to_server(processed_data)

    def test_receive_data_from_server(self):
        self.device.receive_data_from_server()

    def test_display_data(self):
        self.device.get_data(10)
        with self.assertLogs() as logs:
            self.dashboard.display_data(self.device.data)
        self.assertIn("Displaying sensor data...", logs.output[0])

    def test_display_analytics(self):
        processed_data = (50, 10, 90, 60)
        with self.assertLogs() as logs:
            self.dashboard.display_analytics(processed_data)
        self.assertIn("Displaying analytic results...", logs.output[0])
    

if __name__ == '__main__':
    unittest.main()