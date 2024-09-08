import random
from art import logo
from os import system

def repeat():
    again = input("Do you want to play again type 'yes' or press any key. ")
    if again == "yes":
        system('cls')
        guessing()
    else:
        system('cls')

def compare():
    if difficulty == "hard":
        count = 5
    elif difficulty == "easy":
        count = 10
    while count != 0:
            print(f"You have {count} remaining chance to guess the number.")
            guess = int(input("make a guess: "))
            if number == guess:
                print(f"You got it!!!, The number was {number}")
                repeat()
                break
            elif number > guess:
                print("Too low: make another guess")
                count -= 1
            elif number < guess:
                print("Too high: make another guess")
                count -= 1  
    else:
        print(f"You lose: the number was {number}")
        repeat()

def guessing():
    global number
    number = random.randint(1, 100)
    print(logo)
    print("-->I'm thinking of a number between 1 and 100.")
    global difficulty
    difficulty = input("Choose a difficulty to play the game. type 'easy' or 'hard': ")
    compare() 

guessing()
