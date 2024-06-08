import RPi.GPIO as GPIO
import requests
import time

HIGH_LEVEL_PIN = 17
LOW_LEVEL_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(HIGH_LEVEL_PIN, GPIO.IN)
GPIO.setup(LOW_LEVEL_PIN, GPIO.IN)

def send_signal(url, data):
    requests.post(url, json=data)

while True:
    high_level = GPIO.input(HIGH_LEVEL_PIN)
    low_level = GPIO.input(LOW_LEVEL_PIN)
    
    data = {
        'high_level': high_level,
        'low_level': low_level
    }
    send_signal("http://ssh_http_pi_ip:5000/update_status", data)
    time.sleep(5)
