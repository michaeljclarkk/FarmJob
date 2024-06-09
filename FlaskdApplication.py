from flask import Flask, render_template, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Simulated reservoir and pump status
reservoir_status = {
    'high_level': False,
    'low_level': False
}

pump_status = {
    'pump_fault': False
}

@app.route('/')
def index():
    """
    Route for the main dashboard page.
    Renders the index.html template with reservoir and pump status.
    """
    return render_template('index.html', reservoir_status=reservoir_status, pump_status=pump_status)

@app.route('/update_status', methods=['POST'])
def update_status():
    """
    Endpoint to update the reservoir status.
    Receives data from the Reservoir Pi and updates the status.
    """
    global reservoir_status
    data = request.json
    reservoir_status['high_level'] = data.get('high_level')
    reservoir_status['low_level'] = data.get('low_level')
    return 'Status updated', 200

@app.route('/control_pump', methods=['POST'])
def control_pump():
    """
    Endpoint to control the pump.
    Receives commands from the web interface to start or stop the pump.
    """
    data = request.form
    command = data.get('command')
    # Simulate pump control
    if command == 'start':
        pump_status['pump_fault'] = False  # Reset fault on start
    return 'Pump control updated', 200

if __name__ == '__main__':
    # Run the Flask app on port 5000, accessible to other devices in the network
    app.run(host='0.0.0.0', port=5000)
