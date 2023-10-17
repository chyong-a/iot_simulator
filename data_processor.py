# Class for processing and performing basic analytics on the data

import statistics

class DataProcessor:

    @staticmethod
    def get_average(data):
        values = []
        for timestamp, value in data:
            values.append(value)
        return statistics.mean(values)

    @staticmethod
    def get_min_value(data):
        #return min(data, key=lambda x: x[1])[1]
        values = []
        for timestamp, value in data:
            values.append(value)
        return min(values)

    @staticmethod
    def get_max_value(data):
        #return max(data, key=lambda x: x[1])[1]
        values = []
        for timestamp, value in data:
            values.append(value)
        return max(values)
    
    @staticmethod
    def get_median(data):
        #return statistics.mean(data, key=lambda x: x[1])[1]
        values = []
        for timestamp, value in data:
            values.append(value)
        return statistics.median(values)
