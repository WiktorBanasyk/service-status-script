#This script is for RedHat
import subprocess

def all_services():
    try:
        status_output = subprocess.run(['systemctl', '--list-units', '--type=service', '--all'],
            capture_output=True,
            text=True,
            check=True
        )
        print(status_output)
    except subprocess.CalledProcessError as e:
        print(f'An error occued')
all_services()