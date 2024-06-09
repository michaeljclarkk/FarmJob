import RPi.GPIO as GPIO
from flask import Flask, request, jsonify

# GPIO Pins for the pump relay and fault detection
PUMP_RELAY_PIN = 17
PUMP_FAULT_PIN = 27

# Set up the GPIO mode and pin configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_RELAY_PIN, GPIO.OUT)
GPIO.setup(PUMP_FAULT_PIN, GPIO.IN)

# Initialize Flask application
app = Flask(__name__)

@app.route('/control_pump', methods=['POST'])
def control_pump():
    """
    Endpoint to control the pump based on received commands.
    Expects a JSON payload with a 'command' key having value 'start' or 'stop'.
    """
    data = request.json
    if data['command'] == 'start':
        GPIO.output(PUMP_RELAY_PIN, GPIO.HIGH)  # Start the pump
    elif data['command'] == 'stop':
        GPIO.output(PUMP_RELAY_PIN, GPIO.LOW)   # Stop the pump
    return "Pump Control Updated", 200

@app.route('/get_status', methods=['GET'])
def get_status():
    """
    Endpoint to get the current status of the pump.
    Returns the pump fault status as JSON.
    """
    fault_status = GPIO.input(PUMP_FAULT_PIN)
    return jsonify({'pump_fault': fault_status})

if __name__ == '__main__':
    # Run the Flask app on port 5000, accessible to other devices in the network
    app.run(host='0.0.0.0', port=5000)
