import subprocess
from setup import setup

input_file = 'application_supremica_supervisor.wmod'

output_dir = 'application/supervisor'

setup()

result = subprocess.Popen(['python3', 'des_python_maker/app/despythonmaker.py', '-i', input_file, '-o', output_dir])
result.wait()
if(result.returncode != 0):
    print("\n--->Error running des_python_maker!\n")
    exit(0)
else:
    print("\n--->des_python_maker executed successfully!\n")
