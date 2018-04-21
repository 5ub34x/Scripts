#!/usr/bin/python

# Twitter: @5ub34x

from fabric.api import run
from fabric.operations import sudo

# pip install fabric

# Name this file fabfile.py
# Run the following command to execute:
# fab -i <key.pem> -u ubuntu -H <SSH IP> Redirector

def Redirector():
	# Update system
	run("sudo apt update")
	run("sudo apt dist-upgrade -y")

	# Remove text from authorized_keys
	run("sudo sed -i -n 's/^.*0\" //p' /root/.ssh/authorized_keys")

	# Add GatewayPorts yes to SSH Configuration
	sudo('echo "GatewayPorts yes" >> /etc/ssh/sshd_config')

	# Restart the SSH service
	run("sudo service ssh restart")
