import random
import time
from protocol.jarvis import Jarvis

# TODO start a server

class Sensor:
    def __init__(self, sensor_id, linked_satellite, private_key, public_key):
        self.sensor_id = sensor_id
        self.linked_satellite = linked_satellite
        self.jarvis = Jarvis(private_key, public_key)

    def generate_data(self):
        """Simulate sensor data."""
        return {
            "sensor_id": self.sensor_id,
            "temperature": random.uniform(20.0, 40.0),
            "smoke_level": random.uniform(0.0, 100.0),
            "humidity": random.uniform(30.0, 70.0),
        }

    def send_data(self):
        """Send data to the linked satellite."""
        data = self.generate_data()
        message = self.jarvis.build_message(self.linked_satellite, data)
        # Simulate sending message over the network
        print(f"Sensor {self.sensor_id} sending data: {data}")


if __name__ == "__main__":
    sensor = Sensor(sensor_id="S1", linked_satellite="LEO1", private_key="../protocol/crypto/private_key.pem",
                    public_key="../protocol/crypto/public_key.pem")
    while True:
        sensor.send_data()
        time.sleep(5)
