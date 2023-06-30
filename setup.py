import os
import subprocess


def setup():
    # get script path
    script_path = os.path.dirname(os.path.realpath(__file__))

    env_dir = os.path.join(script_path, 'application/env')

    # Path to a Python interpreter that runs any Python script
    # under the virtualenv /path/to/virtualenv/
    python_bin = os.path.join(env_dir, 'Scripts', 'python.exe')

    # verify if virtual env named 'env' exists
    if not os.path.exists(env_dir):
        print(f"\n--->Virtual env 'application/env' not found in '{script_path}'. \n\t---> Creating virtual env...\n")
        result = subprocess.Popen(['python3', '-m', 'venv', env_dir])
        result.wait()
        if(result.returncode != 0):
            print("\n\t---> Error creating virtual env\n")
            exit(0)
        else:
            print("\n\t---> Virtual env created successfully!\n")
        # install requirements
        print("\n\t---> Installing requirements...\n")
        result = subprocess.Popen([python_bin, '-m', 'pip', 'install', '-r', 'application/requirements.txt'])
        result.wait()
        if(result.returncode != 0):
            print("\n\t---> Error installing requirements!\n")
            exit(0)
        else:
            print("\n\t---> Requirements installed successfully!\n")
    # verify if '../des_python_maker/app/despythonmaker.py' exists
    if not os.path.exists('des_python_maker/app/despythonmaker.py'):
        # update submodule
        print("\n\t---> Updating submodule...\n")
        
        result = subprocess.Popen(['git', 'submodule', 'update', '--init', '--remote', '--merge'])
        result.wait()
        if(result.returncode != 0):
            print("\n\t---> Error updating submodule!\n")
            exit(0)
        else:
            print("\n\t---> Submodule updated successfully!\n")

if __name__ == '__main__':
    setup()
