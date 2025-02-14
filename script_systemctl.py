"""
This script is designed to work with Debian-based distributions such as Ubuntu.
For Red Hat-based distributions (e.g., CentOS, Fedora, RHEL), use 'systemctl' instead of 'service'.
"""

import subprocess
# all services
def all_services():
    try:
        status_output = subprocess.run(['service', '--status-all'], capture_output=True, text=True, check=True)
        print(status_output.stdout)
    except subprocess.CalledProcessError as e:
        print(f'An error occured: {e}')

all_services()

# for active services
def active_services():
    try:
        status_output = subprocess.run(['service', '--status-all'], capture_output=True, text=True, check=True)
        filtred_output = subprocess.run(['grep', r'\[ + \]'], input=status_output.stdout, capture_output=True, text=True, check=True)
        lines_with_services = subprocess.run(['awk', r'{print $4}'], input=filtred_output.stdout, capture_output=True, text=True, check=True)
        print(lines_with_services.stdout)
    except subprocess.CalledProcessError as e:
        print(f'An error occured: {e}')

active_services()

# for inactive services
def inactive_services():
    try:
        status_output = subprocess.run(['service', '--status-all'], capture_output=True, text=True, check=True)
        filtred_output = subprocess.run(['grep', r'\[ - \]'], input=status_output.stdout, capture_output=True, text=True, check=True)
        lines_with_services = subprocess.run(['awk', r'{print $4}'], input=filtred_output.stdout, capture_output=True, text=True, check=True)
        print("To są wszystkie wyłączone usługi na serwerze" + lines_with_services.stdout)
    except subprocess.CalledProcessError as e:
        print(f'An error occured: {e}')

inactive_services()
