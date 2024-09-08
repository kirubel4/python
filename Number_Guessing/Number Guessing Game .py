import random
def repeat():
    again = input("do u want to play again type 'yes'.")
    if again == "yes":
        guessing()
def compare():
    if difficulty == "hard":
        count = 5
    elif difficulty == "easy":
        count = 10
    while count != 0:
            print(f"you have {count} remaining chance to guess the number.")
            guess = int(input("make a guess: "))
            if number == guess:
                print(f"you got it!!!, The number was {number}")
                repeat()
                break
            elif number > guess:
                print("too low: make another guess")
                count -= 1
            elif number < guess:
                print("too high: make another guess")
                count -= 1  
    else:
        print(f"you lose: the number was {number}")
        repeat()
def guessing():
    global number
    number = random.randint(1, 100)
    print("<<<<<<<<<<<<<   welcome to the number Guessing Game!!  >>>>>>>>>>>>>>>>>>>")
    print("-->I'm thinking of a number between 1 and 100.")
    global difficulty
    difficulty = input("#choose a difficulty to play the game. type 'easy' or 'hard': ")
    compare()   
guessing()
