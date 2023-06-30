# DESPythonMaker usage example

This repository contains an example of how to use the DESPythonMaker to convert a Supremica file with a synthesized supervisor into a Python project.

1. The file ```setup.py``` install the DESPythonMaker as submodule and configure a virtual environment in the folder ```application\env```.

2. The file ```convert.py``` convert the Supremica file ```application_supremica_supervisor.wmod``` into a Python project in the folder ```application\supervisor```.

3. See ```application\main.py``` for an example of how to use the generated supervisor.

4. The file ```application\handle_event.py``` is an personalization of the DESPythonMaker that handle the events of the supervisor. If you want to use the DESPythonMaker without personalization, you can delete this file and use the default DESPythonMaker located in the folder ```supervisor\Supervisor\handle_event.py```.

    * To do this, you have to change the import in ```application\main.py``` from ```from handle_event import handle_event``` to ```from supervisor import handle_event```.

5. For first use, you have to run ```setup.py``` to install the DESPythonMaker and create the virtual environment and run ```convert.py``` to convert the Supremica file into a Python project.
