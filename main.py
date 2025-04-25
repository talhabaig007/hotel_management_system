# main.py
import subprocess

# Function to launch the login system
def launch_login_system():
    try:
        subprocess.Popen(["python", "login.py"])  # Redirect to login.py
    except Exception as e:
        print(f"Error launching login system: {e}")

# Launch the login system when main.py is executed
if __name__ == "__main__":
    launch_login_system()
