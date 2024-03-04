# SM64 Practice Script (very barebones!)

![SM64Prac](https://i.imgur.com/90A65mj.gif)

## Getting Started - Basic (.exe)
Download the latest .exe from Releases, and then run it (Windows required).

## Getting Started - Advanced (.py)
Otherwise, if you want to edit the script (e.g. fine tuning the weighting of the stars to your specific needs), or are using a different operating system, you can find the Python script itself within the provided .zip folder. I will provide steps below on how to run it this way from scratch.

#### NOTE: This script doesn't work with Python 3.12+ (as of March 3rd 2024).
Download the Python 3.11.6 version best suited for your OS here, if you don't currently have it installed: https://www.python.org/downloads/release/python-3116/

Next, follow the instructions listed below for your OS.
#### Windows:
1. Open command prompt (cmd.exe)
2. Enter this exact command (assuming that Python is in PATH): "py -m pip install colorama pick py-getch"
3. Download the 'sm64.py' script, and navigate to the folder
4. Run the 'sm64.py' script
#### Linux:
1. Open your terminal
2. Enter this exact command: "pip3 install colorama pick py-getch"
3. Download the 'sm64.py' script, navigate to the folder where it was downloaded
4. Change the properties of the sm64.py script file so it can be executed
5. Run the 'sm64.py' script

Non-default libraries used on GitHub:

- https://github.com/tartley/colorama
- https://github.com/wong2/pick
- https://github.com/joeyespo/py-getch
