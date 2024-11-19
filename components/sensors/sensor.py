import time
import json
from protocol.jarvis import Jarvis
import random


class Sensor:
    def __init__(self, receive_port=33000, send_port=34000, adjacency_list_file="./discovery/adjacency_list.json"):
        self.jarvis = Jarvis(
            receive_port=receive_port,
            send_port=send_port,
            adjacency_list_file=adjacency_list_file,
        )
        self.local_ip = self.jarvis.local_ip
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        """Retrieve neighbors from the adjacency list."""
        return self.jarvis.adjacency_list.get(self.local_ip, {})

    def generate_data(self):
        """Simulate data generation."""
        return {
            "sensor_id": self.local_ip,
            "temperature": random.uniform(20, 50),  # Random temperature
            "smoke_level": random.uniform(10, 100),  # Random smoke level
            "humidity": random.uniform(20, 80)  # Random humidity
        }

    def send_data(self):
        """Send data to the nearest neighbor."""
        if not self.neighbors:
            print(f"No neighbors found for sensor {self.local_ip}. Data transmission skipped.")
            return

        data = self.generate_data()
        print(f"Sensor {self.local_ip} generated data: {data}")

        # Select the ground station among all neighbors
        next_hop = max(self.neighbors, key=self.neighbors.get)
        print(f"Sensor {self.local_ip} sending data to next hop: {next_hop}")

        self.jarvis.send_message(dest_ip=next_hop, message=data)

    def handle_message(self, data):
        """Handle incoming messages, such as ACKs."""
        message = self.jarvis.parse_message(data)
        print(f"Sensor {self.local_ip} received message: {message['message_content']}")

        # Handle ACK message
        if message["message_type"] == "ACK":
            print(f"Sensor {self.local_ip} received ACK for message ID: {message['message_id']}")

    def start_receiver(self):
        """Start the sensor's receiver to handle incoming messages."""
        self.jarvis.start_receiver()

    def start(self):
        """Start both sending data and receiving messages."""
        # Start the receiver in a separate thread
        import threading
        threading.Thread(target=self.start_receiver, daemon=True).start()

        # Periodically send data
        while True:
            self.send_data()
            time.sleep(5)
