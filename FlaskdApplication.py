from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    reservoir_status = requests.get('http://rpi1_ip:5000/get_status').json()
    pump_status = requests.get('http://rpi2_ip:5000/get_status').json()
    return render_template('index.html', reservoir_status=reservoir_status, pump_status=pump_status)

@app.route('/control_pump', methods=['POST'])
def control_pump():
    command = request.form['command']
    requests.post('http://rpi2_ip:5000/control_pump', json={'command': command})
    return 'Pump Control Command Sent'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
