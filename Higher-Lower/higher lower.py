import random
from data import data
from art import logo, vs
from os import system

def chance_1():
    Random_numbers = random.randint(0,len(data)-1)
    return Random_numbers

def chance_2():
    Random_numbers2 = random.randint(0,len(data)-1)
    return Random_numbers2

def fuction():
    total = 0
    x = chance_1()
    y = chance_2()
    z = True

    while z:
        if x == y:
            x = chance_1()
            y = chance_2()

        compare = print(f"compare A: {data[x]['name']}, {data[x]['description']} from {data[x]['country']}.")
        print(vs)
        compare2 = print(f"compare B: {data[y]['name']}, {data[y]['description']} from {data[y]['country']}.")
        answer = input("\nwho has more follower? Type 'A' or 'B': ").capitalize()

        if data[x]['follower_count'] > data[y]['follower_count'] and answer == "A":
            x = chance_1()
            total +=1
            y = chance_2()
            system("cls")
        elif data[x]['follower_count'] < data[y]['follower_count'] and answer == "A":
            z = False
            system("cls")
            break
        elif data[x]['follower_count'] < data[y]['follower_count'] and answer == "B":
            total +=1
            x = y
            y = chance_2()
            system("cls")
        elif data[x]['follower_count'] > data[y]['follower_count'] and answer == "B":
            z = False
            system("cls")
            break
    print(logo)
    print(f"you lose: your final score is {total}")
    ask  = input("Do you want to play Higher Lower again, type 'yes' to play or 'no' to skip: ").lower()

    if ask ==  "no":
         z = False
    elif ask == "yes":
        system("cls")
        print(logo)
        fuction()

    else:
        print("wrong input")
        
ask  = input("Do you want to play Higher Lower, type 'yes' to play or 'no' to skip: "'\n').lower()

if ask == "yes":
    print(logo)
    fuction()
elif ask == "no":
    print("thank you for playing")
else:
    print("wrong input")
    