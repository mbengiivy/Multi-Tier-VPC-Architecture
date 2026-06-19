
#!/bin/bash
# App Tier Setup Script
# Run this when building the app tier AMI

# Install dependencies
dnf install -y python3-pip
pip3 install flask pymysql

# Create app directory
mkdir -p /opt/app-tier

# Copy app.py to /opt/app-tier/
# Then run: sudo python3 /opt/app-tier/app.py

