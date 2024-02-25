#game runs until correct number is guessed or no attempts remaining
poster = """
 _______                               __   __               _______                  __               
|     __|.--.--.-----.-----.-----.    |  |_|  |--.-----.    |    |  |.--.--.--------.|  |--.-----.----.
|    |  ||  |  |  -__|__ --|__ --|    |   _|     |  -__|    |       ||  |  |        ||  _  |  -__|   _|
|_______||_____|_____|_____|_____|    |____|__|__|_____|    |__|____||_____|__|__|__||_____|_____|__|  
                                                                                                       
"""
import random  #import math to generate randomized number

print(poster)
print("\nWelcome to Guess The Number where luck meets probability\nI shall be choosing a number between 1 - 100 and you have to correctly guess the number")

level = ['easy','medium','hard']
attempts = 0
generatedNum = round(random.random() * 100)
print("\nBefore we start Choose a difficulty level 'easy', 'medium' or 'hard' ")
userLevel = input().lower()#stores the level chosen
guessNum = 0 
def inputNum(): #function to store user input number
    global guessNum
    print("Guess the correct number : ")
    guessNum = int(input())
    if guessNum == generatedNum:
        print("""
   _____                            _        __     __                    _         _ 
  / ____|                          | |       \ \   / /                   (_)       | |
 | |     ___  _ __   __ _ _ __ __ _| |_ ___   \ \_/ /__  _   _  __      ___ _ __   | |
 | |    / _ \| '_ \ / _` | '__/ _` | __/ __|   \   / _ \| | | | \ \ /\ / / | '_ \  | |
 | |___| (_) | | | | (_| | | | (_| | |_\__ \    | | (_) | |_| |  \ V  V /| | | | | |_|
  \_____\___/|_| |_|\__, |_|  \__,_|\__|___/    |_|\___/ \__,_|   \_/\_/ |_|_| |_| (_)
                     __/ |                                                            
                    |___/                                                             """)

def calcAttempt(): #function to calc attempts
    global attempts
    attempts -= 1
    if attempts == 0:
        print("""    
   ____  _       _   _            __     __           _                  _ 
  / __ \| |     | \ | |           \ \   / /          | |                | |
 | |  | | |__   |  \| | ___        \ \_/ /__  _   _  | | ___  ___  ___  | |
 | |  | | '_ \  | . ` |/ _ \        \   / _ \| | | | | |/ _ \/ __|/ _ \ | |
 | |__| | | | | | |\  | (_) |  _     | | (_) | |_| | | | (_) \__ \  __/ |_|
  \____/|_| |_| |_| \_|\___/  ( )    |_|\___/ \__,_| |_|\___/|___/\___| (_)
                              |/                                           
                                                                           
         """)
        return exit
    print(f"You have {attempts} attempts left")
    inputNum()

#fuunction for the main logic of game
def game (userAttempt):
    global attempts
    attempts = userAttempt
    print(f"you have {attempts} attempts")
    inputNum()
    while attempts!=0 and guessNum != generatedNum:
        if guessNum < generatedNum - 10:
            print("The number is too low\n")
            calcAttempt()
            
        elif guessNum < generatedNum :
            print("The number is  low\n")
            calcAttempt()
            
        elif guessNum > generatedNum + 10:
            print("The number is too high\n")
            calcAttempt()
            
        elif guessNum > generatedNum:
            print("The number is high\n")
            calcAttempt()
            
        else:
            print("Congrats!You chose the correct number\nYou win")



if __name__ == '__main__': #main code
    if userLevel == level[0]:
        attempts = 10
        game(attempts)
    elif userLevel == level[1]:
        attempts = 7
        game(attempts)
    else:
        attempts = 5
        game(attempts)