# SM64 Practice Script

![SM64Prac](https://i.imgur.com/ZJEirG6.gif)

## Getting Started - Basic (.exe)
(Windows) Download the latest .exe from Releases on the right sidebar, and then run it. If SmartScreen shows a warning about untrusted software, this can be ignored.
## Getting Started - Advanced (.py)
Otherwise, if you want to customize the script, or just cannot run .exes, you can clone the source/download zip. Here is how to run it from scratch:

Download the latest Python version best suited for your OS here, if you don't currently have it installed: https://www.python.org/downloads/

NOTE: The currently implemented hotfix for the pick library for Python 3.12 compatibility, causes the terminal cursor (at least in Windows) to always blink on every menu. If you find this annoying, simply just use Python 3.11.

Next, follow the instructions listed below for your OS. Keep in mind this is assuming that Python is installed in PATH.
#### Windows:
1. Open command prompt (cmd.exe)
2. Enter this exact command: `py -m pip install colorama pick py-getch`
3. Download the script via the .zip source code in releases (or cloning the repo), navigate to the folder it downloaded to, and run 'sm64.py'
#### Linux (NOTE: I haven't tested 0.2.0, it should still work):
1. Open your terminal
2. Enter this exact command: `pip3 install colorama pick py-getch`
3. Download the script via the .zip source code in releases (or cloning the repo), navigate to the folder it downloaded to
4. Change the properties of 'sm64.py' so it can be executed
5. Run the 'sm64.py' script

## Changelog

### Version 0.2.0:
    - (Temp) fix for latest Python 3.12 support, via windows-curses compatibility [wermi/edreamleo on GitHub]
    - Ability to customize routes/weighting through the 'stage.json' file, see info menu choice for more details [Artemis/wermi]
    - Will now display the route alongside the category in the roll result menu (unless 0/1 Star is chosen)
    - Added a toggle for main and bowser stages only [Artemis]
    - Added proper star names, with a notation for the main stage star number
    - Minor weighting fixes, implemented more star combinations and many route variations selectable by default

### Version 0.1.1:
    - Fixed 70 Star related bugs and adjusted weighting
    - Laid out initial idea for routes
    - Changed 120 Star to carpetless and 100c + cannon (until further implementation of the routes feature)

### Version 0.1.0:
    - Created the script! Basic menu, supports all main categories and commonly used operating systems

## Thanks to these people to support/inspiration:
    - wermi (tons of help, and teaching me Python related stuff!)
    - Artemis (implementing new features in Version 0.2)
    - tayyip (continued moral support)
    - !whichstar from SM64 discord, Zombie's random star site, and Usamune random stage per category (inspiration)

## Additional Libraries Used
- https://github.com/tartley/colorama
- https://github.com/wong2/pick
- https://github.com/joeyespo/py-getch
