# backend/install_dependencies.py
import subprocess
import sys

def run_command(command):
    """Run a command and return success status"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {command}")
        print(f"Error: {e.stderr}")
        return False

# Installation sequence
commands = [
    "pip install --upgrade pip",
    "pip install numpy==1.26.3",
    "pip install scipy==1.12.0",
    "pip install flask==2.3.3",
    "pip install flask-sqlalchemy==3.0.5",
    "pip install flask-jwt-extended==4.5.3",
    "pip install psycopg2-binary==2.9.7",
    "pip install python-dotenv==1.0.0",
    # Skip heavy ML packages for now
]

print("Installing dependencies in sequence...")
for cmd in commands:
    if not run_command(cmd):
        print(f"Failed at: {cmd}")
        sys.exit(1)

print("✓ Basic dependencies installed successfully!")
print("You can install ML packages later when Rust is configured.")