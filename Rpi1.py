import RPi.GPIO as GPIO
import requests
import time

# GPIO Pins for high and low water level float switches
HIGH_LEVEL_PIN = 17
LOW_LEVEL_PIN = 27

# Set up the GPIO mode and pin configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup(HIGH_LEVEL_PIN, GPIO.IN)
GPIO.setup(LOW_LEVEL_PIN, GPIO.IN)

def send_signal(url, data):
    """
    Function to send data to a specified URL using HTTP POST request.
    Args:
        url (str): The endpoint to send data to.
        data (dict): The data payload to send.
    """
    try:
        requests.post(url, json=data)
    except Exception as e:
        print(f"Error sending data: {e}")

# Main loop to constantly monitor the water levels
while True:
    # Read the state of the float switches
    high_level = GPIO.input(HIGH_LEVEL_PIN)
    low_level = GPIO.input(LOW_LEVEL_PIN)
    
    # Prepare the data payload
    data = {
        'high_level': high_level,
        'low_level': low_level
    }
    
    # Send the data to the SSH/HTTP Pi
    send_signal("http://ssh_http_pi_ip:5000/update_status", data)
    
    # Wait for 5 seconds before the next reading
    time.sleep(5)
