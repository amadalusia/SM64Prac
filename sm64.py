#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import random
from patchedpick import pick
from getch import getch, pause
from colorama import init, Fore, Back, Style
import stagedata
#import ctypes
#ctypes.windll.kernel32.SetConsoleTitleW("SM64 Practice Script")

# Opens 'stage.json', which is used for the course master list, weighting, and routes.
# Uses internal database as a fallback and dumps it to file if not present.
def load_stage_json():
    path = 'stage.json'
    try:
        with open(path, 'r') as f:
            stage_json = json.load(f)
    except:
        stage_json = json.loads(stagedata.json)
        if not os.path.isfile(path):
            try:
                with open('stage.json', 'w') as f:
                    f.write(json.dumps(stage_json, indent=4))
            except:
                pass
    return stage_json

# Clears text on Windows/Linux/MacOS.
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# This function causes the results to be sorted by the master list, rather than random. 'i' is the index number, for example lakitu skip would be 0.
# TODO: Make this sort by chosen route rather than by the master list, and describe the bottom two blocks below that were written by Artemis.
def stage_order(course):
    try:
        i = list(stage_json["course-master-list"].keys()).index(course)
    except:
        i = -1
    return i

def route_choice(category):
    category_options = list(stage_json[category].keys())
    while(1):
        option, index = pick(category_options, "Select a route:", indicator='>>')
        return option

def get_refined(category, route):
    temp_stage = stage_json[category][route]
    temp_weight = []
    x = [temp_stage, temp_weight]
    for i in temp_stage:
        temp_weight.append(stage_json["course-master-list"][i])
    return x

# Roll to choose the course/star, handle multiple rolls (max 10), go back to the main menu, and handle any input errors.
def course_roll(course_list, category, weight_list):
    while(1):
        print(Fore.BLUE + "-" * 64)
        print(Fore.GREEN + "Type 'r' to roll (returns 1 result).")
        print("Type 'r2'-'r10' to return multiple results.")
        print(Fore.MAGENTA + "Type 'm' to go back to category selection." + Style.RESET_ALL)
        user_response = input("")
        user_response_firstchar = user_response[:1]
        clear()
        if user_response_firstchar == 'r':
            number_of_rolls = user_response[1:]

# If misc_option is disabled, this will appropriately remove all MISC tasks from the list.
            if misc_option:
                new_course_list = course_list
                new_weight_list = weight_list
            else:
                new_course_list = []
                new_weight_list = []
                j = 0
                for i in course_list:
                    if "MISC" not in i:
                        new_course_list.append(i)
                        new_weight_list.append(weight_list[j])
                    j += 1

# This will make sure the max is not above the amount of valid entries in `course_list`.
            try:
                number_of_rolls = int(number_of_rolls)
                number_of_rolls = min(number_of_rolls, 10)
                number_of_rolls = max(number_of_rolls, 1)
                number_of_rolls = min(number_of_rolls, len(new_course_list))
            except:
                number_of_rolls = 1
            generated_courses = []

# The roll math is here, containing a random selection that is weighted, and then checks against the generated course list to prevent duplicates. See the above defined stage_order function for how the sorting is handled. This also doesn't display the route if the chosen category is 0/1 Star.
            while len(generated_courses) < number_of_rolls:
                generated_choice = random.choices(new_course_list, new_weight_list, k=1)
                generated_choice = generated_choice[0]
                if generated_choice not in generated_courses:
                    generated_courses.append(generated_choice)
                generated_courses.sort(key=stage_order)
            print("Category [Route]:")
            if len(list(stage_json[category])) > 1:
                print(Fore.YELLOW + category + " [" + route + "]")
            else:
                print(Fore.YELLOW + category)
            print(Fore.WHITE + "Results:")
            for course_result in generated_courses:
                print(Fore.CYAN + course_result + Style.RESET_ALL) 
        elif user_response == 'm':
            break
        else:
            print("Category [Route]:")
            if len(list(stage_json[category])) > 1:
                print(Fore.YELLOW + category + " [" + route + "]")
            else:
                print(Fore.YELLOW + category)
            print(Fore.WHITE + "Results:")
            print(Fore.RED + "Error: Unknown input." + Style.RESET_ALL)

# Menu is from the imported pick library. 
title = ("Select a main category, or other menu option to continue.")
options = ["120 Star", "70 Star", "16 Star", "1 Star", "0 Star", "Main & Bowser Stages Only - Enabled", "Routes & Weighting Modification Info", "About", "Quit"]
misc_option = False

while(1):
    clear()
    stage_json = load_stage_json()
    option, index = pick(options, title, indicator='>>')

# Checks if the selected option is one of the main categories, and then presents the different route choices (if they exist)
    if " Star" in option:
        if len(stage_json[option].keys()) > 1:
            route = route_choice(option)
        else:
            route = list(stage_json[option].keys())[0]
        stage = get_refined(option, route)
        course_roll(category=option, course_list=stage[0], weight_list=stage[1])
# Toggles the flag for main and bowser stages only
    if "Main & Bowser Stages Only - " in option:
        if option == "Main & Bowser Stages Only - Disabled":
            options[5] = "Main & Bowser Stages Only - Enabled"
            misc_option = False
        else:
            options[5] = "Main & Bowser Stages Only - Disabled"
            misc_option = True

# Script routes modification tutorial section, pause is from imported getch library.
    if option == "Routes & Weighting Modification Info":
        print(Fore.CYAN + "Routes & Weighting Modification Info")
        print(Fore.RED + "\nNOTE: This is currently not possible with the .exe, however nearly all star and route variations are included by default." + Fore.WHITE + "\n\nIn order to do this you will need to use the .py script (as outlined on the GitHub page).") 
        print("\nTo create or edit routes, or change the default weighting, you will need to modify the '" + Fore.GREEN + "stage.json" + Style.RESET_ALL + "' file. This file can be easily opened and modified inside of Notepad or any other text editor.")
        print("\nInside this file, you will find the '" + Fore.MAGENTA + "course-master-list" + Style.RESET_ALL + "', then the categories, with routes being nested inside. While making any changes, this exact formatting must be maintained in order for it to work. When making changes that involve swapping stars, you must use the " + Fore.BLUE + "EXACT" + Fore.WHITE + " star names from the '" + Fore.MAGENTA + "course-master-list" + Style.RESET_ALL + "'.")
        print("\nOnce you've finished making changes, save the '" + Fore.GREEN + "stage.json" + Style.RESET_ALL + "' file, and then relaunch the script.")
        print(Fore.YELLOW + "\nLIMITATION: Sorting of results isn't implemented fully. Results are only sorting based on the 'course-master-list', rather than the chosen route. That list is based on the normal 120 Star LBLJ route, so regardless of your route structure, it won't sort all the results in the intended order. You could also update the 'course-master-list' order alongside the route, but keep in mind that will effect all the categories. This is something I plan to fix, along with easier editing via .xlsx spreadsheets.")
        print("\nExample: 70 Star is always going to show HMC results before DDD, regardless of choosing HMC late route." + Style.RESET_ALL)
        pause('\nPress any key to continue.')
        clear()

# Script about section, pause is from imported getch library.
    if option == "About":
        print(Fore.YELLOW + "SM64 Practice Script maintained by Kyman (@Kym4n)")
        print(Fore.CYAN + "Current Version: 0.2.0-04-15-2024.")
        print(Fore.GREEN + "0.2.0 Changelog (see GitHub for full history):")
        print(Fore.WHITE + "\n- (Temp) fix for latest Python 3.12 support, via windows-curses compatibility [wermi/edreamleo on GitHub]")
        print("- Ability to customize routes/weighting through the 'stage.json' file, see info menu choice for more details [Artemis]")
        print("- Will now display the route alongside the category in the roll result menu (unless 0/1 Star is chosen)")
        print("- Added a toggle for main and bowser stages only [Artemis]")
        print("- Added proper star names, with a notation for the main stage star number")
        print("- Minor weighting fixes, implemented more star combinations and many route variations selectable by default")
        print(Fore.MAGENTA + "\nThanks to these people for contributions/inspiration:"+ Style.RESET_ALL)
        print("- wermi (tons of help throughout, and teaching me important Python related stuff!)")
        print("- Artemis (implementing various new features in Version 0.2.0)")
        print("- tayyip (continued moral support)")
        print("- !whichstar command from SM64 discord, Zombie's random star webapp, Usamune random stage per category (inspiration)")
        pause('\nPress any key to continue.')
        clear()

# Quit option, pause is from imported getch library.
    if option == "Quit":
        print(Fore.YELLOW + "Thank you so much for-a running my script." + Style.RESET_ALL)
        pause('Press any key to exit.')
        clear()
        quit()

# Script Ideas / Roadmap:
# -> Implement better ordering of results based on chosen route, rather than master list
# -> More sane stage.json or .xlsx, where routes reference index stuff (this file does not need to be 3200 lines)
# -> For 70 star, provide option for your choices from the pool of: toxic maze, wigglers red coins, pyramid puzzle (currently just providing all by default)
# -> Condense route selections by providing sub menus
# -> Ability to remember the last selected route if you go back to main menu and then back to same category via pick default_index, or have it just save the first one you chose and skip the menu after and then have some sort of reset all routes toggle on the main menu 
# -> Implement menu glitch related stuff for each category, or at least have a sub menu that is just a full resource for it
# -> Auto roll every x mins i.e. a10 and you do 10 mins on each result
# -> Implement presets for RTA vs consistency practice, goals given change base on selection
# -> Implement scaling for users pbs, prompts to enter pb, goal star times balanced to your level, "estimated good practice under xx.xx 5x"
# -> Implement being able to pull from the spreadsheet the records and ideal run times (with vid links too?)
# -> Tracking of your best and average time?
# -> Formatting things to look better