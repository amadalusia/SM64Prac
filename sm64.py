#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
#import ctypes
#ctypes.windll.kernel32.SetConsoleTitleW("SM64 Practice Script")
import random
from getch import getch, pause
from patchedpick import pick
from colorama import init, Fore, Back, Style

#Clears text on Windows/Linux/MacOS.
def clear():
	if os.name == 'nt':
		_ = os.system('cls')
	else:
		_ = os.system('clear')

#This function is the key used by sort() below, to sort the results by the order you would encounter them in a run, depending on the chosen category. i is the index number, for example lakitu skip would be 0.
def stage_order(course):
	course_order_master_list= ['MISC - Lakitu Skip', 'MISC - LBLJ', 'BoB - Island Hop', 'BoB - Bomb Clip', 'WF - Cannonless', 'WF - Owlless', 'WF - 100 + Reds', 'WF - Wild Blue', 'WF - Whomp King', 'WF - Tower', 'MISC - Aquarium', 'JRB - Ship Clip', 'JRB - 100 + Reds', 'JRB - Cannon', 'JRB - Cave', 'JRB - Jet Stream', 'JRB - Eel', 'MISC - PSS U21', 'MISC - PSS Box', 'MISC - Wing Cap Stage', 'BitDW - Reds', 'BitDW - Stage', 'MISC - SBLJ', 'MISC - Bowser 1 Fight', 'BoB - Big Bob-omb on the Summit', 'BoB - Footrace with Koopa the Quick', 'BoB - Shoot to the Island in the Sky', 'BoB - Secrets', 'BoB - 100 + Reds', 'CCM - Reds', 'CCM - Wallkicks', 'CCM - Lil Penguin', 'CCM - Slide', 'CCM - 100 + Slide', 'CCM - 100 + Race', 'CCM - Snowman', 'MISC - MIPS 1', 'SSL - Secrets', 'SSL - Pillarless', 'SSL - Topless', 'SSL - Talons', 'SSL - Reds', 'SSL - 100 + Secrets', 'SSL - Pyramid', 'HMC - 100 + Reds', 'HMC - Box TJ', 'HMC - Toxic Maze', 'HMC - Emergency Exit', 'HMC - Switch', 'HMC - Rolling Rocks', 'MISC - Metal Stage', 'LLL - Reds', 'LLL - Cage TJWK', 'LLL - Wingcap', 'LLL - Lava Boost', 'LLL - Elevator', 'LLL - Bully', 'LLL - Bullies', 'LLL - 100 + Volcano', 'MISC - MIPS 2', 'MISC - Vanish Stage', 'BBH - Ghost Hunt', 'BBH - Merry Go Round', 'BBH - 100 + Reds', 'BBH - Eyeball', 'BBH - Balcony', 'BBH - Books', 'MISC - MIPS Clip', 'DDD - 100 + Reds', 'DDD - Chests', 'DDD - Bowsers Sub', 'DDD - Manta', 'DDD - Jet Stream', 'DDD - Vanish', 'BitFS - Reds', 'BitFS - Stage', 'MISC - Bowser 2 Fight', 'WDW - 100 + Secrets', 'WDW - Vanish', 'WDW - 100 + Reds', 'WDW - Secrets', 'WDW - Elevator', 'WDW - Top Town', 'WDW - Arrow Lifts', 'THI - 100 + Reds', 'THI - Secrets', 'THI - Wiggler', 'THI - Mountain', 'THI - Plants', 'THI - Koopa', 'TTM - Mountain', 'TTM - Monkey', 'TTM - Waterfall', 'TTM - Box Jump', 'TTM - 100 + Reds', 'TTM - Reds', 'TTM - Breeze', 'SL - 100 + Reds', 'SL - Snowman Head', 'SL - Igloo', 'SL - Pond Box', 'SL - Deep Freeze', 'SL - Ice Bully', 'MISC - Stairs BLJs', 'MISC - Cloud Stage', 'TTC - 100 + Thwomp', 'TTC - Pendulums', 'TTC - Cage', 'TTC - Hand', 'TTC - Bars', 'TTC - Reds', 'RR - Carpetless', 'RR - Lakitu Bounce', 'RR - 100 + Cannon', 'RR - Reds', 'RR - Tricky Triangles', 'RR - Swingin Breeze', 'BitS - Reds', 'BitS - Stage', 'MISC - Bowser 3 Fight']
	try:
		i = course_order_master_list.index(course)
	except:
		i = -1
	return i

#Roll to choose the course/star, handle multiple rolls (max 10), go back to the main menu, and handle any input errors.
def course_roll(course_list, category, weight_list):
	while(1):
		print(Fore.BLUE + "-" * 43)
		print(Fore.GREEN + "Type 'r' to roll (returns 1 result).")
		print("Type 'r2'-'r10' to return multiple results.")
		print(Fore.MAGENTA + "Type 'm' to go back to category selection." + Style.RESET_ALL)
		user_response = input("")
		user_response_firstchar = user_response[:1]
		clear()
		if user_response_firstchar == 'r':
			number_of_rolls = user_response[1:]
			try:
				number_of_rolls = int(number_of_rolls)
				number_of_rolls = min(number_of_rolls, 10)
				number_of_rolls = max(number_of_rolls, 1)
			except:
				number_of_rolls = 1
			generated_courses = []
			#Math is here, this is a random selection that is weighted, and then checks against the generated course list to prevent duplicates. See the above defined stage_order function for how the sorting is handled.
			while len(generated_courses) < number_of_rolls:
				generated_choice = random.choices(course_list, weight_list, k=1)
				generated_choice = generated_choice[0]
				if generated_choice not in generated_courses:
					generated_courses.append(generated_choice)
				generated_courses.sort(key=stage_order)
			print("Category:")
			print(Fore.YELLOW + category)
			print(Fore.WHITE + "Results:")
			for course_result in generated_courses:
				print(Fore.CYAN + course_result + Style.RESET_ALL) 
		elif user_response == 'm':
			break
		else:
			print("Category:")
			print(Fore.YELLOW + category)
			print(Fore.WHITE + "Results:")
			print(Fore.RED + "Error: Unknown input." + Style.RESET_ALL)

#Menu is from the imported pick library. 
title = ("Select a main category, or option to continue.")
options = ["120 Star","70 Star","16 Star","1 Star","0 Star","Routes (completely unfinished feature)","About","Quit"]
while(1):
	clear()
	option, index = pick(options, title, indicator='>>')
 
#TODO: determine route based stuff like LBLJ, stage order, etc.
	if option == "120 Star":
		weight_list_120_star = [1, 2, 3, 3, 8, 2, 3, 4, 1, 6, 9, 5, 3, 2, 2, 1, 1, 2, 6, 1, 5, 2, 5, 6, 9, 1, 9, 6, 2, 9, 10, 1, 10, 5, 7, 2, 4, 2, 4, 2, 3, 4, 3, 3, 8, 2, 7, 6, 5, 2, 2, 5, 2, 8, 5, 9, 4, 3, 2, 10, 4, 3, 9, 1, 3, 5, 3, 3, 9, 7, 5, 5, 1, 9, 6, 4, 5, 1, 2, 6, 8, 6, 2, 7, 2, 8, 6, 7, 3, 1, 1, 5, 10, 4, 3, 2, 4, 5, 10, 8, 8, 5, 5, 2, 9, 3]
		course_list_120_star = ['MISC - Lakitu Skip', 'BoB - Bomb Clip', 'WF - Cannonless', 'WF - Owlless', 'WF - 100 + Reds', 'WF - Wild Blue', 'WF - Whomp King', 'WF - Tower', 'MISC - Aquarium', 'JRB - Ship Clip', 'JRB - 100 + Reds', 'JRB - Cannon', 'JRB - Cave', 'JRB - Jet Stream', 'JRB - Eel', 'MISC - PSS U21', 'MISC - PSS Box', 'MISC - Wing Cap Stage', 'BitDW - Reds', 'MISC - Bowser 1 Fight', 'BoB - Big Bob-omb on the Summit', 'BoB - Footrace with Koopa the Quick', 'BoB - Shoot to the Island in the Sky', 'BoB - Secrets', 'BoB - 100 + Reds', 'MISC - MIPS 1', 'SSL - Pillarless', 'SSL - Topless', 'SSL - Talons', 'SSL - Reds', 'SSL - 100 + Secrets', 'SSL - Pyramid', 'HMC - 100 + Reds', 'HMC - Box TJ', 'HMC - Toxic Maze', 'HMC - Emergency Exit', 'HMC - Switch', 'HMC - Rolling Rocks', 'MISC - Metal Stage', 'LLL - Reds', 'LLL - Wingcap', 'LLL - Elevator', 'LLL - Bully', 'LLL - Bullies', 'LLL - 100 + Volcano', 'MISC - MIPS 2', 'MISC - Vanish Stage', 'CCM - Reds', 'CCM - Wallkicks', 'CCM - Lil Penguin', 'CCM - Slide', 'CCM - 100 + Race', 'CCM - Snowman', 'BBH - Ghost Hunt', 'BBH - Merry Go Round', 'BBH - 100 + Reds', 'BBH - Eyeball', 'BBH - Balcony', 'BBH - Books', 'DDD - 100 + Reds', 'DDD - Chests', 'DDD - Bowsers Sub', 'BitFS - Reds', 'MISC - Bowser 2 Fight', 'DDD - Manta', 'DDD - Jet Stream', 'DDD - Vanish', 'WDW - Vanish', 'WDW - 100 + Reds', 'WDW - Secrets', 'WDW - Elevator', 'WDW - Top Town', 'WDW - Arrow Lifts', 'THI - 100 + Reds', 'THI - Secrets', 'THI - Wiggler', 'THI - Mountain', 'THI - Plants', 'THI - Koopa', 'TTM - Mountain', 'TTM - Monkey', 'TTM - Waterfall', 'TTM - Box Jump', 'TTM - 100 + Reds', 'TTM - Breeze', 'SL - 100 + Reds', 'SL - Snowman Head', 'SL - Igloo', 'SL - Pond Box', 'SL - Deep Freeze', 'SL - Ice Bully', 'MISC - Cloud Stage', 'TTC - 100 + Thwomp', 'TTC - Pendulums', 'TTC - Cage', 'TTC - Hand', 'TTC - Bars', 'TTC - Reds', 'RR - Carpetless', 'RR - Lakitu Bounce', 'RR - 100 + Cannon', 'RR - Reds', 'RR - Tricky Triangles', 'RR - Swingin Breeze', 'BitS - Reds', 'MISC - Bowser 3 Fight']
		course_roll(category=option, course_list=course_list_120_star, weight_list=weight_list_120_star)

#TODO: determine route based stuff like island hop, double pless, hmc late/early, ttc 100 sl reds thi reds etc.
	if option == "70 Star":
		weight_list_70_star = [1, 3, 2, 3, 3, 8, 2, 3, 4, 1, 1, 2, 7, 1, 6, 3, 5, 4, 2, 1, 9, 7, 2, 1, 2, 4, 8, 5, 4, 4, 6, 4, 5, 10, 1, 8, 6, 6, 1, 8, 6, 1, 7, 7, 2, 8, 2, 8, 4, 1, 1, 1, 6, 2, 5, 2, 9, 7, 6, 3, 10, 6, 5, 4, 6, 5, 8, 3]
		course_list_70_star = ['MISC - Lakitu Skip', 'BoB - Island Hop', 'BoB - Bomb Clip', 'WF - Cannonless', 'WF - Owlless', 'WF - 100 + Reds', 'WF - Wild Blue', 'WF - Whomp King', 'WF - Tower', 'MISC - PSS U21', 'MISC - PSS Box', 'MISC - Wing Cap Stage', 'BitDW - Reds', 'MISC - Bowser 1 Fight', 'CCM - Wallkicks', 'CCM - Lil Penguin', 'CCM - 100 + Slide', 'BBH - Balcony', 'BBH - Books', 'MISC - MIPS 1', 'SSL - Secrets', 'SSL - Pillarless', 'SSL - Talons', 'SSL - Pyramid', 'LLL - Reds', 'LLL - Wingcap', 'LLL - Lava Boost', 'LLL - Elevator', 'LLL - Bully', 'LLL - Bullies', 'DDD - Chests', 'DDD - Bowsers Sub', 'DDD - Manta', 'BitFS - Reds', 'MISC - Bowser 2 Fight', 'WDW - 100 + Secrets', 'WDW - Elevator', 'WDW - Top Town', 'WDW - Arrow Lifts', 'THI - Secrets', 'THI - Mountain', 'THI - Plants', 'TTM - Waterfall', 'TTM - Mountain', 'TTM - Box Jump', 'TTM - Reds', 'TTM - Breeze', 'SL - Snowman Head', 'SL - Pond Box', 'SL - Deep Freeze', 'SL - Ice Bully', 'MISC - MIPS 2 + Toad', 'HMC - Box TJ', 'HMC - Emergency Exit', 'HMC - Switch', 'HMC - Rolling Rocks', 'RR - Lakitu Bounce', 'RR - Reds', 'RR - Tricky Triangles', 'RR - Swingin Breeze', 'TTC - 100 + Thwomp', 'TTC - Pendulums', 'TTC - Cage', 'TTC - Hand', 'TTC - Bars', 'TTC - Reds', 'BitS - Stage', 'MISC - Bowser 3 Fight']
		course_roll(category=option, course_list=course_list_70_star, weight_list=weight_list_70_star)

#TODO: determine route based stuff like LBLJ vs no LBLJ, different star choices
	if option == "16 Star":
		weight_list_16_star = [1, 2, 6, 2, 3, 4, 2, 5, 3, 1, 2, 4, 5, 3, 4, 2, 3, 5, 5, 6, 2, 3, 6, 3]
		course_list_16_star = ['MISC - Lakitu Skip', 'MISC - LBLJ', 'BitDW - Reds', 'MISC - Bowser 1 Fight', 'WF - Cannonless', 'WF - Owlless', 'WF - Wild Blue', 'SSL - Pillarless', 'SSL - Talons', 'SSL - Pyramid', 'LLL - Reds', 'LLL - Cage TJWK', 'LLL - Lava Boost', 'LLL - Bully', 'HMC - Box TJ', 'HMC - Emergency Exit', 'HMC - Rolling Rocks', 'MISC - MIPS Clip', 'DDD - Bowsers Sub', 'BitFS - Stage', 'MISC - Bowser 2 Fight', 'MISC - Stairs BLJs', 'BitS - Stage', 'MISC - Bowser 3 Fight']
		course_roll(category=option, course_list=course_list_16_star, weight_list=weight_list_16_star)

	if option == "1 Star":
		weight_list_1_star = [1, 3, 8, 2, 7, 8, 10, 2, 5, 10, 4]
		course_list_1_star = ['MISC - Lakitu Skip', 'MISC - LBLJ', 'BitDW - Stage', 'MISC - Bowser 1 Fight', 'MISC - SBLJ', 'DDD - Bowsers Sub', 'BitFS - Stage', 'MISC - Bowser 2 Fight', 'MISC - Stairs BLJs', 'BitS - Stage', 'MISC - Bowser 3 Fight']
		course_roll(category=option, course_list=course_list_1_star, weight_list=weight_list_1_star)

	if option == "0 Star":
		weight_list_0_star = [1, 3, 8, 2, 7, 10, 2, 5, 10, 4]
		course_list_0_star = ['MISC - Lakitu Skip', 'MISC - LBLJ', 'BitDW - Stage', 'MISC - Bowser 1 Fight', 'MISC - SBLJ', 'BitFS - Stage', 'MISC - Bowser 2 Fight', 'MISC - Stairs BLJs', 'BitS - Stage', 'MISC - Bowser 3 Fight']
		course_roll(category=option, course_list=course_list_0_star, weight_list=weight_list_0_star)

#Script routes section (this is completely unfinished), pause is from imported getch library.
	if option == "Routes (completely unfinished feature)":
		pause('120 Star:\nStage:	Star <Count>:	Menu Direction:\nBowser in the Dark World	Red Coins <1>	.\nWhomps Fortress\n\nPress any key to continue.')
		clear()

#Script about section, pause is from imported getch library.
	if option == "About":
		pause('SM64 Practice Script maintained by Kyman (@Kym4n)\n\nCurrent Version: 0.1.1 beta-03-03-2024\n\nChange Log:\n\nVersion 0.1.1:\n- Fixed 70 Star related bugs and adjusted weighting\n- Laid out initial idea for Routes section\n- Changed 120 Star to carpetless and 100c + cannon (until further implementation of the Routes feature)\n\nVersion 0.1:\n- Created the script! Basic menu, supports all main categories and commonly used operating systems\n\nThanks to these people to support/inspiration:\n- wermi (for help/teaching me Python related stuff!)\n- tayyip (for continued moral support)\n- !whichstar command from SM64 discord\n- Zombie (random star webapp)\n- Usamune (random stage per category function)\n\nPress any key to continue.')
		clear()

#Quit option, pause is from imported getch library.
	if option == "Quit":
		pause('Thank you so much for-a running my script. Press any key.')
		clear()
		quit()

# Script Future Ideas:
# -> format look of text better
# -> flag for strings beginning with 'MISC' to be part of roll results (default to disable them)
# -> implement menus for picking route stuff, way to save settings?
# -> auto roll every x mins i.e. a10 and you do 10 mins on each star
# -> implement presets for RTA vs consistency practice, goals given change base on selection
# -> implement scaling for users pbs, prompts to enter pb, goal star times balanced to your level, "estimated good practice under xx.xx 5x"
# -> implement being able to pull from the spreadsheet the records and ideal run times (with vid links too?)
# -> tracking of your best and average time?
# -> implement routing/menu glitch related stuff for each category, access this from Routes menu option? <- WIP
