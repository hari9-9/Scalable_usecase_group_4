import time
from components.sensors.sensor import Sensor

if __name__ == "__main__":
    sensor = Sensor(
        sensor_id="S1",
        linked_satellite="LEO1",
        private_key="./protocol/crypto/private_key.pem",
        public_key="./protocol/crypto/public_key.pem"
    )

    while True:
        sensor.send_data()
        time.sleep(5)
