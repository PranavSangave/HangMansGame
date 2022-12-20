"""
Algorithm:
-----------------
1.Show Welcome Screen
2.Take Player Name
3.Take Difficulty Level
3.1 Set chances as per difficulty level.
4.Start Game
5.Show Blank Underscores
6.Show Message to Guess the word
7.Take Letter or #
8.If letter is present in original word, then again show underscores but with filled letter.
9.If user gives #, then take a word from user and compare with original word.
10.Show score board.
11.Ask to play again or not.
12.If yes,then play again.
13.If not, then exit.
"""
from colorama import Fore
import time
import random
import subprocess as sp

#List of words as per difficulty levels
easy_word_list = ["cat","mango","chalk","banana","dog","parrot","lion"]

medium_word_list = ["cooler","laptop","stand","python","stadium"]

hard_word_list = ["elephant","zebronics","jaguar","apostrophy","politics"]

hint_list = {
                # easy hints
                "cat":"A cute small animal, it will drink your all milk when your not at home.",
                "mango":"The king of fruits",
                "chalk":"You ate it in school, its a pen of all teachers",
                "banana":"A fruit we eat after peeling",
                "dog":"The most common pet",
                "parrot":"The bird who loves to eat chilies",
                "lion":"The king of Forest",

                # medium hints
                "cooler": "The machine useful in Summer",
                "laptop": "The most important machine your life, if you are CS student",
                "stand": "A normal metal piece without it you bike will not stands.",
                "python": "In which language Pranav wrote this program",
                "stadium": "Favourite place of cricket fans",

                # hard hints
                "elephant":"A huge vegterian animal",
                "zebronics":"A company which created a gaming keyboards and mouses",
                "jaguar":"A TATA owned luxery car compamy",
                "politics":"A dirty game, played by uneducated peoples",
                "apostrophy":" (') "
            }

while True:
    randomWord = None
    randomHint = None
    chances = None
    raw_str = []
    temp_str = ""

    #Printing Welcome Screen
    print(Fore.GREEN+"\n==========================================")
    print(Fore.GREEN+"=============="+Fore.CYAN +" HangMans Game "+Fore.GREEN+"=============")
    print(Fore.GREEN+"==========================================")

    #Taking PLayers name
    player_name = input(Fore.WHITE+"Enter Player's Name: ")

    #Showing Difficulty Manual
    while(True):
        print(Fore.CYAN+player_name,"please select game difficulty")
        print("1.Easy")
        print("2.Medium")
        print("3.Hard")
        difficulty_level = int(input("Enter Your Choice Here: "))

        if(difficulty_level != 1 and difficulty_level != 2 and difficulty_level != 3):
            print(Fore.RED+"Please Select Valid Option !")

        if(difficulty_level==1):
            time.sleep(1.0)
            print(Fore.MAGENTA+"Ohh, Noob Player Ah ! Good Luck...")
            time.sleep(1.0)
            print(Fore.GREEN+"You'll get 20 chances to guess the word.")
            time.sleep(1.0)
            break
        elif(difficulty_level==2):
            time.sleep(1.0)
            print(Fore.MAGENTA+"Good Courage ! Good Luck...")
            time.sleep(1.0)
            print(Fore.GREEN + "You'll get 15 chances to guess the word.")
            time.sleep(1.0)
            break
        elif(difficulty_level==3):
            time.sleep(1.0)
            print(Fore.MAGENTA+"Ohh, Pro Player Ah? Well, Good Luck !")
            time.sleep(1.0)
            print(Fore.GREEN + "You'll get 10 chances to guess the word.")
            time.sleep(1.0)
            break

    if difficulty_level == 1:
        randomWord = random.choice(easy_word_list)
        chances = 20
    elif difficulty_level == 2:
        randomWord = random.choice(medium_word_list)
        chances = 15
    elif difficulty_level == 3:
        randomWord = random.choice(hard_word_list)
        chances = 10
    randomHint = hint_list[randomWord]

    def isLetterPresent(g_letter):
        flag = 0
        for i in range(len(randomWord)):
            # print("\n\nPresenting isLetterPresent Body...")
            # print("Value of i = ", randomWord[i])
            if randomWord[i] == g_letter:
                flag = 1
                break
        if flag == 1:
            return True
        else:
            return False

    def listDeveloper(g_letter):
        global raw_str
        for i in range(len(randomWord)):
            if randomWord[i] == g_letter:
                raw_str[i] = randomWord[i]

    def stringDeveloper():
        global raw_str
        temp_str = ""
        for i in range(len(raw_str)):
            temp_str = temp_str + raw_str[i] + " "
        return temp_str

    def gameInit():
        global raw_str
        for i in range(len(randomWord)):
            raw_str.append("_")
            print(Fore.CYAN+"_", end=" ")
        print(Fore.CYAN + "\nHint: "+randomHint)

        cha = 1
        while cha <= chances:
            ter_flag = 0
            #checking that word have _ or not
            for i in range(len(raw_str)):
                if raw_str[i] == '_':
                    ter_flag = 1
            if ter_flag == 0:
                print()
                print(Fore.BLUE+"Hurrayyy "+player_name+" You Won The Game!")
                break
            print(Fore.MAGENTA+"\nChance No. ",cha)
            guess_letter = input(Fore.GREEN+"Guess the letter: ")
            if isLetterPresent(guess_letter) == True:
                print(Fore.GREEN+"Great Guess! ")
                listDeveloper(guess_letter)
                print(Fore.CYAN + stringDeveloper())
                continue
            else:
                print(Fore.RED + "One Chance Wasted! ")
            cha = cha + 1

        if(cha >= chances):
            print(Fore.CYAN+"\nBetter Luck Next Time!!!")

    gameInit()
    print(Fore.RED + "\nWant to play again? (y/n)")
    play_again = input("Provide Your Choice Here: ")
    if play_again == 'y':
        continue
    else:
        break

print("Thank You! ")