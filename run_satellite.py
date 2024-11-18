import time
from components.satellites.satellite import Satellite

if __name__ == "__main__":
    satellite = Satellite(
        satellite_id="LEO1",
        linked_ground_station="GS",
        private_key="./protocol/crypto/private_key.pem",
        public_key="./protocol/crypto/public_key.pem",
        satellites=["LEO2", "LEO3"]
    )

    while True:
        data = {
            "sensor_id": "S1",
            "temperature": 35.2,
            "smoke_level": 78.0,
            "humidity": 45.0
        }
        satellite.receive_data(data)
        time.sleep(10)
