# Class for displaying the collected sensor data and analytics results
import logging

class Dashboard:
    def display_data(self, data):
        logging.info("Displaying sensor data...")
        print("Timestamp\t\t\tSensor data")
        print("--------------------------------------------")
        for timestamp, value in data:
            print(f"{timestamp}\t{value:.2f}")

    def display_analytics(self, analytics):
        avg, min_value, max_value, med = analytics
        logging.info("Displaying analytic results...")
        print("Analytic results")
        print("--------------------------------------------")
        print(f"Average: {avg:.2f}")
        print(f"Minimum: {min_value:.2f}")
        print(f"Maximum: {max_value:.2f}")
        print(f"Median: {med:.2f}")
