import threading
import time
from protocol.jarvis import Jarvis


class Satellite:
    def __init__(self, satellite_id, linked_ground_station, private_key, public_key, satellites=[]):
        self.satellite_id = satellite_id
        self.linked_ground_station = linked_ground_station
        self.satellites = satellites  # List of other satellites to broadcast data to
        self.jarvis = Jarvis(private_key, public_key)

    def receive_data(self, data):
        """Receive data from sensors."""
        print(f"Satellite {self.satellite_id} received data: {data}")
        self.broadcast_to_satellites(data)
        self.forward_to_ground_station(data)

    def broadcast_to_satellites(self, data):
        """Broadcast data to other satellites."""
        print(f"Satellite {self.satellite_id} broadcasting data to satellites.")
        for satellite in self.satellites:
            message = self.jarvis.build_message(satellite, data, message_type="broadcast")
            print(f"Broadcasted to {satellite}: {message[:50]}...")  # Simulating broadcast

    def forward_to_ground_station(self, data):
        """Forward data to the ground station."""
        print(f"Satellite {self.satellite_id} forwarding data to Ground Station.")
        message = self.jarvis.build_message(self.linked_ground_station, data, message_type="priority")
        print(f"Forwarded to Ground Station: {message[:50]}...")  # Simulating forward


if __name__ == "__main__":
    satellite = Satellite(
        satellite_id="LEO1",
        linked_ground_station="GS",
        private_key="../protocol/crypto/private_key.pem",
        public_key="../protocol/crypto/public_key.pem",
        satellites=["LEO2", "LEO3"]
    )


    # Simulate incoming data from sensors
    def simulate_sensor_input():
        while True:
            data = {
                "sensor_id": "S1",
                "temperature": 35.2,
                "smoke_level": 78.0,
                "humidity": 45.0
            }
            satellite.receive_data(data)
            time.sleep(10)


    threading.Thread(target=simulate_sensor_input, daemon=True).start()

    while True:
        time.sleep(1)
