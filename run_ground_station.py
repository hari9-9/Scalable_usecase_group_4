import time
from components.groundstation.ground_station import GroundStation

if __name__ == "__main__":
    ground_station = GroundStation(
        storage_path="./data",
        private_key="./protocol/crypto/private_key.pem",
        public_key="./protocol/crypto/public_key.pem"
    )

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
