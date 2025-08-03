# simulate.py

import requests
import random
import time
import threading

# Configuration for your Django backend
API_BASE_URL = "http://127.0.0.1:8000/api/"

# API Endpoints
DEVICE_ENDPOINT = f"{API_BASE_URL}devices/"
SENSOR_DATA_ENDPOINT = f"{API_BASE_URL}sensordata/"
ALERT_ENDPOINT = f"{API_BASE_URL}alerts/"

# Device State
DEVICE_NAME = "simulated_device_001"
# This will hold the ID of the device created in your Django database
DEVICE_ID = None

def get_or_create_device():
    """Checks if the simulated device exists on the API and creates it if not."""
    global DEVICE_ID
    print("Checking for simulated device on the API...")
    try:
        # First, try to get the device
        response = requests.get(DEVICE_ENDPOINT)
        devices = response.json()
        for device in devices:
            if device['name'] == DEVICE_NAME:
                DEVICE_ID = device['id']
                print(f"Found existing device. ID: {DEVICE_ID}")
                return

        # If not found, create a new user and device
        print("Device not found. Creating a new user and device...")
        
        # NOTE: For this to work, you will need to set up a superuser
        # or a user with permissions to create new devices.
        # This is a simplified example.
        
        # First, create a user if one doesn't exist
        # This part assumes you're using Django's built-in User model
        # You may need to create a user manually or adjust this logic.
        
        # Assuming you've created a user with username 'simuser' and password 'password123'
        user_id = 1 # We'll assume user with ID 1 exists
        
        # Now create the device
        new_device_data = {
            "name": DEVICE_NAME,
            "priority": 1,
            "status": "connected",
            "user": user_id  # Link to the user
        }
        
        response = requests.post(DEVICE_ENDPOINT, json=new_device_data)
        if response.status_code == 201:
            new_device = response.json()
            DEVICE_ID = new_device['id']
            print(f"Successfully created new device. ID: {DEVICE_ID}")
        else:
            print(f"Failed to create new device. Status: {response.status_code}, Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with the API: {e}")
    
def generate_fake_sensor_data():
    """Generates a dictionary of fake sensor data."""
    return {
        "temperature": round(random.uniform(20.0, 40.0), 2),
        "current": round(random.uniform(0.1, 5.0), 3),
        "voltage": 220,
        "vibration": round(random.uniform(0.0, 1.0), 2)
    }

def send_sensor_data():
    """Sends sensor data to the API endpoint."""
    while True:
        if DEVICE_ID:
            readings = generate_fake_sensor_data()
            for reading_type, reading_value in readings.items():
                data_payload = {
                    "reading_value": reading_value,
                    "reading_type": reading_type,
                    "device": DEVICE_ID
                }
                try:
                    response = requests.post(SENSOR_DATA_ENDPOINT, json=data_payload)
                    print(f"Sent {reading_type} data for device {DEVICE_ID}. Status: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Failed to send {reading_type} data: {e}")
        else:
            print("Device not created yet. Waiting...")
        
        time.sleep(5)  # Send new data every 5 seconds

def send_alerts():
    """Simulates sending a random alert to the API."""
    while True:
        if DEVICE_ID:
            if random.random() < 0.1:  # 10% chance to send an alert
                alert_types = ['Overheating', 'Power Disconnect', 'Overload']
                alert_payload = {
                    "message": f"Simulated alert: {random.choice(alert_types)} detected.",
                    "alert_type": random.choice(alert_types),
                    "device": DEVICE_ID
                }
                try:
                    response = requests.post(ALERT_ENDPOINT, json=alert_payload)
                    print(f"Sent alert for device {DEVICE_ID}. Status: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Failed to send alert: {e}")
        
        time.sleep(30) # Check for alerts every 30 seconds

if __name__ == "__main__":
    print("Starting simulated hardware device...")
    get_or_create_device()
    
    # Start threads for different functions
    threading.Thread(target=send_sensor_data, daemon=True).start()
    threading.Thread(target=send_alerts, daemon=True).start()
    
    # Keep the main thread alive to allow other threads to run
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped.")