
#!/bin/bash
# Web Tier User Data Script
# NOTE: For production, pre-bake this into an AMI instead of running at boot

dnf install -y httpd php
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-TUCLFO-3-17940/4-lab-vpc-web-server/s3/lab-app.zip
unzip lab-app.zip -d /var/www/html/
systemctl enable httpd
systemctl start httpd

