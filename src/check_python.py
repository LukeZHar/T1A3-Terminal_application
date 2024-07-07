import subprocess

def check_python(command):
    try:
        # Execute the command to check the Python version
        result = subprocess.run([command, '--version'], capture_output=True, text=True)
        
        # If the command is successful, print the Python version
        if result.returncode == 0:
            print(f"{command} is installed.")
            print(f"Version: {result.stdout.strip()}")
            return True
        else:
            return False
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    if not check_python('python'):
        if not check_python('python3'):
            print("Python is not installed.")