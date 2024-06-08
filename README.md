# FarmJob
Remote Monitoring and Control System for Automatic Fill Reservoir
# Scope of Work
## Objective
To implement a remote monitoring and control system for an automatic fill reservoir using Raspberry Pis, Teltonika 4G/LTE Ethernet Gateways, and a secure VPN connection. The system will include a web-based dashboard for monitoring and control accessible via smartphone and PC.
![NetDiag](images\image.png)
## Components and Hardware
### Raspberry Pi Units
- Two (2) Raspberry Pi units with necessary peripherals (power supplies, SD cards, etc.)
- GPIO connections for float switches and pump relays

### Teltonika 4G/LTE Ethernet Gateways
- Two (2) Teltonika TRB140 gateways for secure internet connectivity
- Configuration of APN settings for mobile network operator

###    Sensors and Relays
- Float switches for high and low water level detection
- Relays for controlling pump operation

### Network Components
- OpenVPN setup for secure communication between devices
- Dynamic DNS (DDNS) configuration for remote access

## Software and Configuration
###    Raspberry Pi Setup
- Installation of Raspberry Pi OS on each unit
- Installation of necessary packages (ssh, python, requests, flask)

### Teltonika TRB140 Gateway Configuration
- Internet connectivity setup
- VPN configuration for secure data transmission

### Dynamic DNS Configuration
- Setup of DDNS service to ensure consistent remote access

## Programming and Integration
### Raspberry Pi Programming
- Python scripts for reservoir RPi (RPi1) to monitor float switches and send data
- Python scripts for pump station RPi (RPi2) to control pump and monitor status

### Dashboard Setup on SSH/HTTP Pi
- Installation of Flask and other required packages
- Development of a web-based dashboard for monitoring and control
- Integration of RESTful APIs for communication between RPis and dashboard

## Testing and Implementation
###    Connectivity Testing
- Verification of VPN tunnel establishment
- DDNS setup and access verification

###    Functionality Testing
- Simulation of float switch activations
- Verification of correct signal transmission and pump control

###    Monitoring and Logging
- Implementation of logging for sensor statuses and control actions
- Ongoing monitoring and troubleshooting

## Deliverables
### Fully Configured Hardware
- Two (2) Raspberry Pi units with connected sensors and relays
- Two (2) Teltonika TRB140 gateways with VPN and DDNS configured

### Python Scripts
- Reservoir monitoring and control scripts
- Pump control and status monitoring scripts

### Web-Based Dashboard
- Accessible via smartphone and PC
- Real-time monitoring and control capabilities

## Access Instructions
1. SSH into Raspberry Pi:

```bash
ssh pi@<raspberry_pi_ip_address>
```

2. Install RPi.GPIO:

```bash
sudo apt update
sudo apt install python3-rpi.gpio python3-pip
```

3. Run Your Python Script:

```bash
python3 ./rPI.py
```
### Documentation
Setup and configuration guides
User manual for the dashboard and system operation

