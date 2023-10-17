# Class for simulating communication with a central server

class Communication:
    def __init__(self, url):
        self.url = url

    def send_data(self, data):
        print(f"Sending data to {self.url}: {data}")

    def receive_data(self):
        print(f"Receiving data from {self.url}")
