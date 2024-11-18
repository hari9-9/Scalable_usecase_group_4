import time
import json
from components.sensors.sensor import Sensor


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


if __name__ == "__main__":
    config = load_config()
    sensors = []

    # Create sensor instances dynamically
    for sensor_id, satellite in config["sensors"].items():
        sensors.append(Sensor(
            sensor_id=sensor_id,
            linked_satellite=satellite,
            private_key="./protocol/crypto/private_key.pem",
            public_key="./protocol/crypto/public_key.pem"
        ))

    # Simulate sensor data generation and transmission
    while True:
        for sensor in sensors:
            sensor.send_data()
        time.sleep(5)
