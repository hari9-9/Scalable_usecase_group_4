import time
import json
from components.satellites.satellite import Satellite


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


if __name__ == "__main__":
    config = load_config()
    satellites = []

    # Create satellite instances dynamically
    for satellite_id, connections in config["satellites"].items():
        satellites.append(Satellite(
            satellite_id=satellite_id,
            linked_ground_station=config["ground_station"],
            private_key="./protocol/crypto/private_key.pem",
            public_key="./protocol/crypto/public_key.pem",
            satellites=connections
        ))

    # Simulate satellite operations
    while True:
        for satellite in satellites:
            data = {
                "sensor_id": "S1",  # Example data for simulation
                "temperature": 35.2,
                "smoke_level": 78.0,
                "humidity": 45.0
            }
            satellite.receive_data(data)
        time.sleep(10)
