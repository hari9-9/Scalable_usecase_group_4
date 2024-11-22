import threading
from components.sensors.sensor import Sensor


def start_sensor_instance(sensor_id, receive_port, send_port):
    """Start a single sensor instance."""
    print(f"Starting Sensor {sensor_id} on ports {receive_port} (receive) and {send_port} (send)...")
    sensor = Sensor(
        receive_port=receive_port,
        send_port=send_port,
        adjacency_list_file="./protocol/discovery/adjacency_list.json"
    )
    sensor.start()


if __name__ == "__main__":
    sensors_config = [{"sensor_id": "S1", "receive_port": 33000, "send_port": 34000}]

    # Start each sensor in its own thread
    threads = []
    for config in sensors_config:
        thread = threading.Thread(
            target=start_sensor_instance,
            args=(config["sensor_id"], config["receive_port"], config["send_port"]),
            daemon=True
        )
        threads.append(thread)
        thread.start()

    # Keep the main thread alive to allow sensors to run
    for thread in threads:
        thread.join()
