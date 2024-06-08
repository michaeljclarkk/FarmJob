import RPi.GPIO as GPIO
from flask import Flask, request

PUMP_RELAY_PIN = 17
PUMP_FAULT_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_RELAY_PIN, GPIO.OUT)
GPIO.setup(PUMP_FAULT_PIN, GPIO.IN)

app = Flask(__name__)

@app.route('/control_pump', methods=['POST'])
def control_pump():
    data = request.json
    if data['command'] == 'start':
        GPIO.output(PUMP_RELAY_PIN, GPIO.HIGH)
    else:
        GPIO.output(PUMP_RELAY_PIN, GPIO.LOW)
    return "Pump Control Updated", 200

@app.route('/get_status', methods=['GET'])
def get_status():
    fault_status = GPIO.input(PUMP_FAULT_PIN)
    return {'pump_fault': fault_status}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
