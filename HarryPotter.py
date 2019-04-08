#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:09:38 2018

@author: pc

"""

#!/usr/bin/env python
# coding: utf-8

'''
**********************************************************************************************************************************************************************************            
**********************************************************************************************************************************************************************************

Game Name : 5Ws of Wizarding World !

**********************************************************************************************************************************************************************************
“ “ “

DocString: 

A)	INTRODUCTION

        A very warm welcome to you in Hogwarts – School of Witchcraft and Wizardy! 
                
        It is my pleasure to have you as our student with us. I am Professor Dumbledore, your headmaster. 
        
        I hope you have already visited Diagon Alley to get :
            
            1.	Magic Wand : 
                If you do not have this, please grab a nearby pen or chopstick NOW to mimic the wand. Swing / Swish the wand 3 times to test if the spells work. 
                       
            2.	Textbooks :
                Required for classes in “Potions” and “Defense Against the Dark Arts”
            
            3.	Marauder’s Map: 
                Tracking of all Hogwarts people and properties
           
        In order to be assigned to your Hogwarts house – Gryffindor/Ravenclaw/Hufflepuff/Slytherin , you need to play the orientation game which has 3 stages.
        
            1. Magical Powers
            2. Wizard Training
            3. How good a wizard am I? 
        
        
        Off you go now!
        
    

“ “ “
**********************************************************************************************************************************************************************************
'''


import numpy as np

from PIL import Image, ImageFilter

import colorama
from colorama import Fore

import random

import os
import glob

import time




# start game

def start_game():
#     """ To start game. """
    key = ''
    while(key.lower() != 's'):
        key = input(">Press 's' to begin...")
    return True


def get_integer_input(question):
# """ To convert input into integer """
    while True:
        try:
            integer_input = int(input (question))
            return integer_input
        except:
            print ("ERROR - Please enter a valid integer value!")

# Pre-Orientation
            
# Make sure student has the magic wand.

def wand_available(name) :
#     """ Check if student has the magic wand """   
    
    print ('\n\n\n{}, do you have your magic wand?'.format(name))
    while True :
        wand_available = input('> Please input Y or N:  ').upper()

        if wand_available == 'Y':
            print ('\nGreat! You are ready to proceed...')
            break
        elif wand_available == 'N':
            print ('\nThis is not a good start {}, you are not following instructions. Please get a wand – either a pen or a chopstick equivalent. If not, you will have 1 detention class next week in the Dungeons.'.format(name))
            break
        else:
            print( ' ERROR. Please input Y or N.')
#     input('<Press Enter>')


# Make sure student has some background on the Harry Potter series. 
    
def HP_knowledge(name):
#     """ Check how much knowledge student has about the Harry Potter series. """
    
    print('\nMoving forward, on a scale of 1 to 5, how much do you know about the Harry Potter series?')
#     HP_know = int(input (' > Please enter answer on scale of 1 (smallest) to 5 (biggest): \n'))
    
    while True:
        HP_know = get_integer_input(' > Please enter answer on scale of 1 (smallest) to 5 (biggest): \n')
        if HP_know in [1,2,3] :
            print ( '\nSince you are new , here is some additional information  to prepare you for the tasks ahead: ')
            time.sleep(2)
            print ('*' * 50)
            print ('\n*Hogwarts is a school that students attend to learn magic! \n\n*Good guys: Most Hogwarts students and professors. Specifically, Harry Potter and his good friends Hermoine and Ron. \n\n*Bad guys: Voldemort, who is a serial killer, and his supporters.')  
            print ('*' * 50)
            time.sleep(2)
            break
        elif HP_know in [4,5] :
            print ('*' * 50) 
            print ('\nSince you are familiar, no additional information for you. Proceed on.')
            time.sleep(2)
            break
    
    input ('< Press Enter to Continue: >')
    print ('\nNow that you are all set {}, your magical journey of 3 stages begins! Swing your wand 3 times for the good luck spell "JiaYou!".'.format(name))
    print (' \n\t*1. Magical Powers \n\t*2. Wizard Training \n\t*3. How good a wizard am I?')
    input ('< Press Enter to Continue: >')
    

    
### Stage 1 - Magical Powers


def get_input_option(black_lake):
#     """ Get input from student on the move he/she would like to make .  """
    
    if 'hagrid' in black_lake[0]:
        departing, arriving = black_lake[0], black_lake[1]
    else:
        departing, arriving = black_lake[1], black_lake[0]

    while True:
        option = input (">Your option to move a creature or Hagrid : ")
        print('\n\n')
        if option.lower() in departing:
            return option
        elif option.lower() in arriving:
            print ('\nOnly Hagrid can move the creature! Move either Hagrid or a creature from another side')
        else:
            print ('\nPlease enter valid option from {}'.format(departing))

def print_black_lake_layout(black_lake):
#      """ Printing the layout. """
     
    left_side, right_side = black_lake
    if len(left_side)==0:
        left_side = '{}'
    if len(right_side)==0:
        right_side = '{}'
    print ('\n{}    | BLACK LAKE |    {}'.format(left_side, right_side))

def check_safe(black_lake, departing):
#      """ Safety check of all creatures. """
     
    if 'dragon' in departing and 'tarantula' in departing:
        print_black_lake_layout(black_lake)
        print ('\n\n\nOops... Dragon ate Tarantula... Yum! Yum! ... You lost but will allow you to proceed to next stage')
        return False
    if 'tarantula' in departing and 'owl' in departing:
        print_black_lake_layout(black_lake)
        print ('\n\n\nOops... Tarantula ate Owl... Yum! Yum! ... You lost but will allow you to proceed to next stage')
        return False
    return True

def cross(black_lake):
#      """ Hagrid's movements. """
     
    if 'hagrid' in black_lake[0]:
        departing, arriving = black_lake[0], black_lake[1]
    else:
        departing, arriving = black_lake[1], black_lake[0]
        
    departing.remove('hagrid')
    arriving.add('hagrid')
    
    safe = check_safe(black_lake, departing)
    
    return black_lake, safe

def cross_n_move_creature(black_lake, creature):
#      """ Creature movements with Hagrid. """
     
    if 'hagrid' in black_lake[0]:
        departing, arriving = black_lake[0], black_lake[1]
    else:
        departing, arriving = black_lake[1], black_lake[0]
        
    departing.remove('hagrid')
    
    if creature in departing:
        departing.remove(creature)
        arriving.add(creature)
        
    arriving.add('hagrid')
    
    safe = check_safe(black_lake, departing)
    
    return black_lake, safe

    
def Magical_Powers (name) :
#      """ Student to solve this challenge. """
    print(Fore.MAGENTA + '\n\nLoading Stage 1: Magical Powers.......\n')
    print(Fore.BLACK)
    time.sleep(2)
    
    
    print('*'*50) 
    print ('\nWelcome to Magical Powers, {}! \n'.format(name))
    print ('\nAim: To help Professor Hagrid safely get 3 creatures (Dragon, Tarantula, Owl) across the Black Lake.')
    print ('\nRules: \n\t- Professor Hagrid must be sailing the boat. \n\t- At any time, Professor Hagrid can only take one creature with him on the boat. \n\t- Not Safe: Dragon and Tarantula together as the dragon eats the tarantula. \n\t- Not Safe: Tarantula and Owl together as the tarantula eats the owl. \n\t- All creatures are safe when Professor Hagrid is present.\n')     
    print('*'*50)  
    input('<Press Enter to Continue>')
    print('\nWho would you put on the boat to cross the Black Lake? Select one creature or Hagrid. \n\n- Continue selecting one creature or Hagrid every time till all have safely crossed Black Lake. You have maximum 20 moves.\n\n')
    input('<Press Enter to Continue>')
    
    left_side = {'hagrid', 'dragon', 'tarantula', 'owl'}
    right_side = set([])
    black_lake = (left_side, right_side)
    
    count = 0
    
    while True:
        if count > 20:
            print ('\nYou took too long. The creatures have escaped ...')
        
        if len(black_lake[1]) == 4:
            print ('\n Congrats! Hagrid is very pleased with your help :) ')
            return True
            
        print_black_lake_layout(black_lake)
        time.sleep(1)
        
        option = get_input_option(black_lake).lower()
        
        if option == 'hagrid':
            black_lake, safe = cross(black_lake)
        else:
            black_lake, safe = cross_n_move_creature(black_lake, option)

        if not safe:
            return False

        count += 1
        





# Stage 2 - Wizard Training : 2 questions to test your magical knowledge. 

def Wizard_Training_A (name) :
#     """ Student to solve 1 riddle"""
    print(Fore.MAGENTA + '\n\nLoading Stage 2A: Wizard Training A.......\n')
    print(Fore.BLACK)
    time.sleep(2)
    
    print('*'*50)
    print ('\nWelcome to Wizard Training A, {}! \n'.format(name))
    print ('\nAim: Solve a riddle.')
    print ('\nRules:\n\t- You have maximum 3 tries.')
    print('*'*50)
    input('<Press Enter to Continue>')
    #time.sleep(5)
    
    print ('\nQuestion : What boy wizard magically grew a beard each night?')
        
    count = 0
    
    while True:
        if count != 0 and count < 3:
            print ('\nSorry, that is not correct! Please try again.')
            
        if count == 3:
            print ('\nNope, that is not right! Oh No! Oops you used up all your 3 tries! Too bad. But you can get a secret entry to continue...')
            return False
            
        riddle_guess = input ('>Your answer : ')
        
        if riddle_guess.lower() == 'hairy potter' :
            print('\nCongratulations! That is correct! You have a great sense of humour - like me :) \n')
            return True

        count += 1
        
def Wizard_Training_B (name) :
#     """Student to solve another riddle"""
    print(Fore.MAGENTA + '\n\nLoading Stage 2B: Wizard Training B.......\n')
    print(Fore.BLACK)
    time.sleep(2)
    
    print('*'*50)
    print ('\nWelcome to Wizard Training B, {}! \n'.format(name))
    print ('\nAim: Identify what/who is shown in the image.')
    print ('\nRules:\n\t- You have maximum 3 tries.')
    print('*'*50)
    input('<Press Enter to Continue>')
        
    #time.sleep(5)
    
    print ('\nQuestion : Name one of the characters you see in the image below.')
    time.sleep(1)
    
    
    image = Image.open('./snape_sirius.jpg')
    display (image)
    
    count = 0
    
    while True:
        if count != 0 and count < 3:
            print ('\nSorry, that is not correct! Please try again. A hint is their names begin with the alphabet S.')
        
        if count == 3:
            print ('\nSorry :( \n\n\t\t\t ************* \n\t\t\t --GAME OVER-- \n\t\t\t ************* \n\nBased on your performance, you have been assigned to Slytherin house.\n\n\t\t\t*** Congratulations !!! *** \n\nLook forward to seeing you around in the Hogwarts castle, {}!'.format(name))
            return False
        
        riddle_guess = input ('>Your answer : ')
        
        if riddle_guess.lower() in ['snape' , 'sirius']:
            print('\nCongratulations! That is correct!')
            print ('\n\n\n\t\t\t ************* \n\t\t\t --GAME OVER-- \n\t\t\t ************* \n\nBased on your performance, you have been assigned to Ravenclaw house.\n\n\t\t\t*** Congratulations !!! *** \n\nLook forward to seeing you around in the Hogwarts castle, {}!'.format(name))
            return True
        
        count += 1






### Stage 3 - How Good A Wizard Am I ? 

def build_ques_ans():
#     """ Game is in the form of Who Wants To Be A Millionare. One image question will be asked from a random list of images , with 4 random options. If student does not know the answer, he/she can use the 2 Lifelines available. """
    
    
    f_img = glob.glob('./options/*.jpg')
    f_img = [os.path.basename(x) for x in f_img]
    sel_img = random.choice(f_img)
    
    question = "Identify the character in this image: "
    correct_answer = [os.path.splitext(sel_img)[0]]
        
    f_img_n = [os.path.splitext(x)[0] for x in f_img if x is not sel_img]
    
    answer_options = correct_answer + random.sample(set(f_img_n), 3)
    
    return (question, answer_options, correct_answer[0])



def show_question(ques):
#     """ Prints question """
    
    print (ques)
    
    
def show_image(f_p, blur_factor):
#      """ Shows image with blur """
     
    basewidth = 320
    raw_image = Image.open(f_p)
    wpercent = (basewidth / float(raw_image.size[0]))
    hsize = int((float(raw_image.size[1]) * float(wpercent)))
    raw_image = raw_image.resize((basewidth, hsize), Image.ANTIALIAS)
    box = (15,15, 500, 500)
    ic = raw_image.crop(box)
    for i in range(blur_factor):  # with the BLUR filter, you can blur a few times to get the effect you're seeking
        ic = ic.filter(ImageFilter.BLUR)
        raw_image.paste(ic, box)
    
    display(raw_image)
    
    
def get_input_choice(possible_choices):
#      """ Get student input """
     
    while True:
        choice = input ('>\nEnter your choice: ')
        if choice in possible_choices:
            return choice
        print ('\nPlease enter a valid choice from  -->  {}'.format(possible_choices))
        
        
def show_options(choices, options, ll_choices, ll_options):
#      """ Showing all the options? """
     
    print ('\nOptions : \n')
    for i in range(len(choices)):
        print (choices[i] + ' :  ' + options[i])
    print ('\nLifelines Available : \n')
    for i in range(len(ll_choices)):
        print (ll_choices[i] + ': ' + ll_options[i])
    
    return (get_input_choice(choices + ll_choices))


def do_fi_fi(choices, options, ans):
#      """ Lifeline activated for 50-50. 2 wrong answers will be eliminated. """
     
    options_idx = [x for x in range(len(choices))]
    options_idx.remove(options.index(ans))
    fi_fi = sorted([options.index(ans), random.sample(set(options_idx),1)[0]])

    choices_fi_fi = [choices[idx] for idx in fi_fi]
    options_fi_fi = [options[idx] for idx in fi_fi]
    
    return (choices_fi_fi, options_fi_fi)


def play_Good_wizard(name):
#      """ How Good a WIzard am I?  """
     
    question, answer_options, correct_answer = build_ques_ans()
    choices = ['A', 'B', 'C', 'D']
    ll_choices = ['L1', 'L2']
    ll_options = ['50-50', 'de-blur']
    
    blur_factor = 100
    
    while True:
        print ('\n******************************\n')
        show_question(question)  
        show_image('./options/'+correct_answer+'.jpg', blur_factor)
        in_choice = show_options(choices, answer_options, ll_choices, ll_options)
        
        if in_choice in choices:
            
            if in_choice != choices[answer_options.index(correct_answer)]:
                print ('\nWrong Answer :(')
                print ('\nSorry :( \n\n\t\t\t ************* \n\t\t\t --GAME OVER-- \n\t\t\t ************* \n\nBased on your performance, you have been assigned to Hufflepuff house.\n\n\t\t\t*** Congratulations !!! *** \n\nLook forward to seeing you around in the Hogwarts castle, {}!'.format(name))
                return False
            
            if in_choice == choices[answer_options.index(correct_answer)]:
                print ('\nGreat job!')
                print ('\n\n\n\t\t\t ************* \n\t\t\t --GAME OVER-- \n\t\t\t ************* \n\nBased on your performance, you have been assigned to Gryffindor house.\n\n\t\t\t*** Congratulations !!! *** \n\nLook forward to seeing you around in the Hogwarts castle, {}!'.format(name))
                return True

        if in_choice in ll_choices:
            ll = ll_choices.index(in_choice)
            del[ll_options[ll_choices.index(in_choice)]]
            ll_choices.remove(in_choice)
            
            if in_choice == 'L1':
                print ('\n50-50 lifeline activated... eliminating 2 wrong choices...\n')
                time.sleep(2)
                choices_fi_fi, options_fi_fi = do_fi_fi(choices, answer_options, correct_answer)
                choices = choices_fi_fi
                answer_options = options_fi_fi
            
            if in_choice == 'L2':
                print ('\nde-blur lifeline activated... de-blurring the image...\n')
                time.sleep(2)
                blur_factor = 2
                

                
def Good_wizard (name):
#      """ To start test on How Good a Wizard am I? """
    print(Fore.MAGENTA + '\n\nLoading Stage 3: How Good a wizard am I?.......\n')
    print(Fore.BLACK)
    time.sleep(2)
    
    print('*'*50)
    print (' \nWelcome to the test "How Good A Wizard am I?", {}! \n'.format(name))
    print ('\nAim: Identify the person shown in the image.')
    print ('\nRules:\n\t- You will be given 4 options to choose from. \n\t- If you are stuck, you have 2 lifelines. \n\t\t~ Lifeline 1: "50-50" : 2 of the wrong answers will be eliminated.\n\t\t~ Lifeline 2: Image will be de-blurred.\n')    
    print('*'*50)
    input('<Press Enter to Continue>')
               
#    time.sleep(10)
     
    Good_wizard_result = play_Good_wizard(name)


def do_restart():
    while True:
        get_last_choice = get_integer_input('\n>Your choice 1 or 2: ')
        
        if get_last_choice == 1:
            return True

        if get_last_choice == 2 :
            return False

### Main Game Code

def PLAY_GAME():
    
    if (start_game()):
        print ("Starting game...")
        time.sleep(1)

        print (Fore.MAGENTA + '\nWelcome to Hogwarts! I hope you have a magical journey ahead!')
        print(Fore.BLACK)

        name = input('Please enter your name: ')
        print ('\nAs your headmaster, I need to do some pre-orientation checks.... :') 
        wand_available (name) 
        time.sleep(2)
        HP_knowledge (name) 
        time.sleep(3)

        
        
        while True:
            Magical_Powers_result = Magical_Powers(name)   # stage 1
            time.sleep(1)
            if Magical_Powers_result :
                Good_wizard_result = Good_wizard (name)   # stage 3
                break
            else:
                Wizard_Training_A_result = Wizard_Training_A(name)   # stage 2a
                
                if Wizard_Training_A_result:
                    Good_wizard_result = Good_wizard (name)   # stage 3
                    break
                    
                else:
                    print('\nYou have an option here. Do you want to: \n\n\t 1: Go back to Stage 1 - Magical Powers to try your luck again at getting Hagrid and his creatures across the Blake Lake? \n\n\t 2: Proceed to Training B? ')
                    
                    restart = do_restart()
                    if restart:
                        print('You are going back to Magical Powers.')
                        time.sleep(.5)
                        continue
                    else:
                        print('You are proceeding to Wizard Training B.')
                        Wizard_Training_B (name)
                        break
                    
                    
                
PLAY_GAME()