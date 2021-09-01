"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def check_string (number):
    
    while True:
        try :
            number = int(number)
            guess = number
            return guess
            break   
        except ValueError:
            number = input ("please choose a number , and only a number , between 1 and 10   ")
            continue 
    return number    


def check_number(number):  
    while True:
        try: 
            if number >= 11 or number <= 0:
                print ("woah woah woah...\nYou picked a number outside the paramiters! Not cool...")
                number = int (input("Try again ...  "))
                continue
            else:
                in_range = number
                break
        except ValueError:
            number = int (input ("please choose a number , not a word...  "))
            continue   
    return int(in_range)


def start_game(high_score):
    attempts = 1
    answer = random.randint(1,10)
    high_score = high_score 
    print ("Hello! And welcome to the Number Guessing Game!")
    print (f"The current high score is {high_score}...\nThink you can beat it?")
    guess = input("To begin , Guess a random number from 1 to 10!!!!!")
    

      
    while True:
        guess = check_string(guess)   
        guess = check_number(guess)
        
        if guess < answer :
            check_number(int(guess))
            attempts = attempts + 1
            print ("Bummer, your guess was wrong! **psst ... the correct answer is higher!...***")
            guess = input ("Try again!...  ")
        elif guess > answer :
            check_number(int(guess))
            attempts = attempts + 1
            print ("Aww shucks, your guess was wrong! *cough* ...try guessing lower ...*cough**cough*") 
            guess = input ("Try again!...  ")
        elif guess == answer:
            print ("WOW!! YOUR ANSWER IS CORRECT! \n GOOD JOB!!")
            print (f"It took you only ... {attempts} attempts to get the correct answer.")
            print ("...GAME\n...OVER")
            if attempts < high_score:
                high_score = attempts
            break

    response = input("...That is ...\nUnless you want to play again ? (yes/no)?")
    if response.lower() == "yes":
        print ("AWESOME!!!\n ...STARTING NEW GAME NOW!!!...")
        start_game(high_score)
    else:
        print ("OK...\nThanks for playing!")

high_score = 1000
start_game(high_score)