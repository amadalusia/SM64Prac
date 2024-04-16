# SM64 Practice Script

![SM64Prac](https://i.imgur.com/90A65mj.gif)

## Getting Started - Basic (.exe)
(Windows) Download the latest .exe from Releases on the right sidebar, and then run it. If SmartScreen shows a warning about untrusted software, this can be ignored. Keep in mind that .exe versions of this script currently have the weighting and star choice per category hard locked, but now comes with basically every variation preloaded into it.
## Getting Started - Advanced (.py)
Otherwise, if you want to customize the routes, weighting, the script, or just cannot run .exes, you can find the Python script itself included with each release. You can also use the 'sm64.py' file that will recieve commits between releases. The steps below are based on the file being named this, but it doesn't matter. Here is how to run it from scratch:

Download the latest Python version best suited for your OS here, if you don't currently have it installed: https://www.python.org/downloads/

Next, follow the instructions listed below for your OS. Keep in mind this is assuming that Python is installed in PATH.
#### Windows:
1. Open command prompt (cmd.exe)
2. Enter this exact command: `py -m pip install colorama pick py-getch`
3. Download the 'sm64.py' script, and navigate to the folder it downloaded to
4. Run the 'sm64.py' script
#### Linux:
1. Open your terminal
2. Enter this exact command: `pip3 install colorama pick py-getch`
3. Download the 'sm64.py' script, and navigate to the folder it downloaded to
4. Change the properties of the 'sm64.py' so it can be executed
5. Run the 'sm64.py' script

## Changelog

### Version 0.2.0:
    - (Temp) fix for latest Python 3.12 support, via windows-curses compatibility [wermi/edreamleo on GitHub]
    - Ability to customize routes/weighting through the 'stage.json' file, see info menu choice for more details [Artemis]
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
