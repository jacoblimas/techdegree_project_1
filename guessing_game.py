"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

random_number = random.randint(1,10)

def start_game():
    print("\n------------------------------------\nWelcome to the Number Guessing Game!\n------------------------------------\n")

    name = input("Enter your name: ")
    print("Hello, {}, welcome to the guessing game. I am thinking of a number between 1 and 10.".format(name))
    play_game = input("Do you want to play: Enter (Yes/No): ")
    
    attempts = 0
    while play_game.lower() == "yes":
        attempts +=1
        try:
            guess = int(input("Please enter a number 1 - 10: "))
            if guess <= 0:
                raise ValueError("Choose number 1 - 10: ")
        except ValueError as err:
            print("Not a valid number.".format(err))
        else: 
            
            if guess > random_number:
                print("It's Lower")
            elif guess < random_number:
                print("It's Higher")
            else:
                print("GOT IT. The total amount of attempts is: {}. \nGAME HAS ENDED".format(attempts))
                break
    
                
            
            
        
    

    
    
    
# Kick off the program by calling the start_game function.
start_game()