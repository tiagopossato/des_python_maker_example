import subprocess
from setup import setup

input_file = 'pick_and_place_basic.wmod'

output_dir = 'application/supervisor'

setup()

result = subprocess.Popen(['python3', 'C:\Users\tiago\Documents\des_python_maker\app\despythonmaker.py', '-i', input_file, '-o', output_dir])
result.wait()
if(result.returncode != 0):
    print("\n--->Error running des_python_maker!\n")
    exit(0)
else:
    print("\n--->des_python_maker executed successfully!\n")
