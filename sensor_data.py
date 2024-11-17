import time
import numpy as np
from unittest.mock import MagicMock
import requests

# Mock SMBus and MLX90640 for Windows compatibility
SMBus = MagicMock()
MLX90640 = MagicMock()

# Configuration
SENSOR_ADDRESSES = [0x33, 0x34, 0x35]  # Simulated I2C addresses
TEMPERATURE_THRESHOLD = 70.0  # Fire detection threshold in Celsius
ALERT_URL = "http://ground_station/api/fire-alert"  # Replace with your API endpoint
SENSOR_LOCATIONS = [
    {"latitude": 52.12345, "longitude": -8.98765},
    {"latitude": 52.22345, "longitude": -8.88765},
    {"latitude": 52.32345, "longitude": -8.78765},
]


# Simulated MLX90640 sensor behavior
def initialize_mocked_sensors(sensor_addresses):
    sensors = []
    for address in sensor_addresses:
        mock_sensor = MagicMock()
        
        # Simulate data with a realistic temperature distribution
        def generate_mock_data():
            # Start with ambient temperature (e.g., 25°C) and add random noise
            temp_grid = np.random.normal(25, 5, (24, 32))  # Mean = 25°C, std deviation = 5°C
            # Introduce a hotspot with a small probability
            if np.random.rand() > 0.8:  # 20% chance of a hotspot
                hotspot_x = np.random.randint(0, 24)
                hotspot_y = np.random.randint(0, 32)
                temp_grid[hotspot_x, hotspot_y] = np.random.uniform(70, 100)  # Simulate a fire
            return temp_grid
        
        # Mock the get_frame method with realistic data generation
        mock_sensor.get_frame = MagicMock(side_effect=generate_mock_data)
        sensors.append(mock_sensor)
    print("Thermal sensors initialized.")
    return sensors




# Simulated thermal data collection
def get_temperature_data(sensor):
    try:
        return sensor.get_frame()  # Simulate data from sensor
    except Exception as e:
        print(f"Error reading thermal data: {e}")
        return None

# Mock alert system
def send_alert(temperature, location, sensor_id):
    data = {
        "sensor_id": sensor_id,
        "temperature": f"{temperature:.2f} °C",
        "location": location,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    try:
        # Simulate sending data (prints instead of an actual request)
        print(f"Simulated Alert Sent: {data}")
    except Exception as e:
        print(f"Error sending alert for Sensor {sensor_id}: {e}")

# Main function
def main():
    sensors = initialize_mocked_sensors(SENSOR_ADDRESSES)
    while True:
        for idx, sensor in enumerate(sensors):
            temperature_data = get_temperature_data(sensor)
            if temperature_data is not None:
                max_temperature = np.max(temperature_data)  # Get max temperature
                print(f"Sensor {idx} - Max Temperature: {max_temperature:.2f} °C")

                # Check for fire conditions
                if max_temperature >= TEMPERATURE_THRESHOLD:
                    print(f"Fire detected by Sensor {idx}! Sending alert...")
                    send_alert(max_temperature, SENSOR_LOCATIONS[idx], idx)
        print('\n')
        time.sleep(5)  # Delay between readings

if __name__ == "__main__":
    main()