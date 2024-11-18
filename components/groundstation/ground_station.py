import json
import os
import time

from protocol.jarvis import Jarvis


class GroundStation:
    def __init__(self, storage_path, private_key, public_key):
        self.storage_path = storage_path
        self.jarvis = Jarvis(private_key, public_key)
        os.makedirs(storage_path, exist_ok=True)

    def store_data(self, data):
        """Store data locally in JSON format."""
        timestamp = int(time.time())
        file_name = os.path.join(self.storage_path, f"{timestamp}.json")
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data stored at {file_name}.")

    def trigger_alert(self, data):
        """Trigger alerts for critical situations."""
        if data["smoke_level"] > 70.0 or data["temperature"] > 50.0:
            print(f"🔥 ALERT! Possible fire detected: {data}")

    def receive_data(self, raw_message):
        """Handle incoming data from satellites."""
        try:
            message = self.jarvis.parse_message(raw_message)
            print(f"Ground Station received: {message['message_content']}")
            self.store_data(message["message_content"])
            self.trigger_alert(message["message_content"])
        except Exception as e:
            print(f"Error handling data: {e}")


if __name__ == "__main__":
    ground_station = GroundStation(
        storage_path="./data",
        private_key="../protocol/crypto/private_key.pem",
        public_key="../protocol/crypto/public_key.pem"
    )


    # Simulate receiving data from satellites
    def simulate_satellite_input():
        while True:
            data = {
                "sensor_id": "S1",
                "temperature": 55.2,
                "smoke_level": 80.0,
                "humidity": 40.0
            }
            raw_message = ground_station.jarvis.build_message(
                dest_ip="GS", message=data, message_type="priority"
            )
            ground_station.receive_data(raw_message)
            time.sleep(10)


    simulate_satellite_input()
