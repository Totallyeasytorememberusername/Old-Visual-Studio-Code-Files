import random
from turtle import Turtle


b = Turtle()

b.color('brown')
b.speed(0)
b.begin_fill()
b.circle(500)
b.end_fill()
b.begin_fill()
b.left(90)
b.penup()
b.forward(90)
b.pendown()
b.circle(500)
b.end_fill()
b.color('Red')
b.penup()
b.goto(150,-250)
b.pendown()
style = ('Helvetica', 30,)
b.write('Buttcheek Coding', font=style, align='center')
b.hideturtle()

#it's the logo; a buttcheek.

# print("Welcome to Hangman with GUILLOTINES! This is just the same game but there are some images of a guy trying to avoid getting his head chopped off.     ")
# print("                  __                                                                                                                                 ")
# print(" Hi!             |\ |     Next!                                                                                                                      ")
# print("  \              || |       /                                                                                                                        ")
# print("  ()             |()|_  \()          ________                                                                                                        ")
# print(" /||\          __|__|__  ||\        |Head Bin|                                                                                                       ")
# print("  /\          |||||||||| /\         |________|                                                                                                       ")
# print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
# print("Instructions: You got to protect yourself! This is the Salem With Trials and you are known as one with the gift of the dark arts...                  ")
# print("-----------------------------------------------------------------------------------------------------------------------------------------------------")

# print("                    __                                                                                                                                ")
# print("Who ya kill today? |\ |    Hmmm... It says some witch.                                                                                                ")
# print("     /             || |     /                                                                                                                         ")
# print("  ()               |()|_   ()  _      ________                                                                                                        ")
# print(" /||\            __|__|__ /||\|_|    |Head Bin|                                                                                                       ")
# print("  /\            |||||||||| /\        |________|                                                                                                       ")
# print("------------------------------------------------------------------------------------------------------------------------------------------------------")
# print("Instructions: Guess the word your friend put in.                                                                                                      ")
# print("------------------------------------------------------------------------------------------------------------------------------------------------------")
# print("Executioneer: Next!                                                                                                                                   ")
# print("You: Hi Executioner! Who are you going to kill today?                                                                                                 ")
# print("Executioneer: Hmm... let me check. It says some old 'witch', I think. Lives by another witch's house, ate children, stuff like that. I'm not literate.")
# print("You: But that's me!                                                                                                                                   ")

#A stickman test. On the side is a hanging platform.

print("(c)* Buttcheek Coding AB.")   
print("*(c) stands for 'created by' not 'copyright'.")
print("A Python Test Game")
print("Game2")
input("Loading Game...(Press Enter to Continue)")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("     .    .   ____   .    .   _____  .        .   ____   .    .     ")
print("     |    |  /    \  |\   |  /       |\      /|  /    \  |\   |     ")
print("     |____|  |____|  | \  |  |    _  | \    / |  |____|  | \  |     ")
print("     |    |  |    |  |  \ |  |    |  |  \  /  |  |    |  |  \ |     ")
print("     |    |  |    |  |   \|  \____|  |   \/   |  |    |  |   \|     ")
print("     S             A              L             E             M     ")
input("-----------------------Press Enter to Continue----------------------")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

input("Welcome to the game of Hangman: Salem! You are the 1st player, the one that creates the words.")
User_input = input("So input your word here: ")

if len(User_input) >= 25:
    print("Words with over 25 characters are too large for a casual game.")
    while len(User_input) >= 25:
        User_input = input("So input your NEW word here: ")

#The User Input

print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")

#So the friends that are going to come won't see the answer typed

input("Now get one or more of your friends to come and guess it!")

#A reminder that this game is 2-player.

print("~")
print("~")

input("P.S.: Watch your friends at ALL TIMES to make sure they don't scroll up to see what you have typed.")
input("P.S.S.: Don't even get a cup of water or some food, even if your life depends on it. This is more important.")

#some more reminders; this time to not go anywhere.

u = input("P.P.S.S.:PROMISE ME YOU WON'T! Type it here -----> ")
if u == "I Promise":
    pass 
else:
    while u != "I Promise":
        u = input("PROMISE ME OR ELSE!!! ")         


#The reassurance for me that you will guard that keyword against all costs.

print("~")
print("~")

i = input("Have you brought your friend yet? ")
if i == "Yes":
    pass
else:
    input("Well, then do it!")
    input("And don't say any of that 'Bghiegage' or 'Irrnfcuiehjfied' stuff. I realy hate it when you do that.")

#The final confirmation you brought your friends over.

print("~")
print("~")

input("Guess the number now!")
input("I mean to your friend that you brought over.")
input("He's here now? Good! I- wait, look behind you!")
x = input("Have you done it yet? ")
if x == "Yes":
    print("So you figured out it was a trick...")
else:
    print("Well, do it now!")

#A trick/comedic section.

print("~")
print("~")

input("Ok. Serious time now.")

#To remind you to be serious.

stars = len(User_input) * "*"
stars_list = []

for letter in stars:
    stars_list.append(letter)




word_not_guessed = True

#The section for showing the length of the word that needs to be guessed

#Missed_Letters = ""

Pigs = 10


while word_not_guessed:
    index = 0
    count = 0
    #print("Previous incorrect guesses:", previous_guesses)
    print("Lives: ", Pigs)
    if Pigs <= 0:
        input("Ye died. (Press Enter to Continue)")
        break
    print("Current phrase: ", "".join(stars_list))
    TMZ = input("Guess a typeable/emoji: ")
    if TMZ == "/GetHint":
       random_index = random.randrange(0, len(User_input))
       User_input = list(User_input)
       hint_letter = User_input[random_index]
       TMZ = hint_letter
       User_input = "".join(User_input)
            
    # if TMZ == "/kill.Computer_program 'hangman'":
    #     input("Converting...")
    #     b = Turtle()

    #     b.color('brown')
    #     b.speed(0)
    #     b.begin_fill()
    #     b.circle(500)
    #     b.end_fill()
    #     b.begin_fill()
    #     b.left(90)
    #     b.penup()
    #     b.forward(90)
    #     b.pendown()
    #     b.circle(500)
    #     b.end_fill()
    #     b.color('Red')
    #     b.penup()
    #     b.goto(150,-250)
    #     b.pendown()
    #     style = ('Helvetica', 30,)
    #     b.write('Buttcheek Coding', font=style, align='center')
    #     b.hideturtle()

        # input("Welcome to the game 'Happy Unicorn Ponies'!")
        # input("The game is simple.")
        # input("You state your answoor too daa quest...")
        # input("Power 10%. Battery Saver Mode On. All code applications automatically turned off. Speeding to end of earlier game.")
        # words_not_guessed = False

#Section 5

    Apple_Pen_pg2 = []

    previous_guesses = []

    # to check correct answers
    for letter in User_input:
        if letter in TMZ:
            stars_list[index] = letter

        index += 1
    index = 0
    for letter in User_input:
        #global leter
        leter = letter
        if letter in TMZ:
            if letter not in Apple_Pen_pg2:
                stars_list[index] = letter
                Pigs = Pigs + 1
        index += 1
    
    # to check wrong answers


    Apple_Pen_pg2 += leter
    for letters in TMZ:
        if letters not in User_input:
            if letters not in previous_guesses:
                previous_guesses += letters
                Pigs = Pigs - 1
    for ZUES in stars_list:
       if ZUES == "*": 
           count = count + 1

    if count == 0:
        word_not_guessed = False
        input("Congrats, you guessed the whole thing without all your body parts falling off!")

print("~")
print("~")

(
#Needed Addition: We need to add some more stuff to make this a game.
#Addition: Add pictures and sentences with each choice ~IN PROGRESS.
)

























#Apple_Pen_pg2 has never existed as a variable therefore the computer cannot read it. It has disappeared into thin air.

#Fix Lives Program


# #Future Challenge: Create a turtle that can show you the Minecraft (C) Logo.

# Traceback (most recent call last):
#   File "c:/Users/Sylvan Student/Desktop/Old-Visual-Studio-Code-Files/Hangman.py", line 332, in <module>
#     stars_list[index] = letter
# IndexError: list assignment index out of range

#Latest Update:
#Added Title Screen
#Changed What was it? Oh yeah the Time of interest from Rule of Terror to Salem Witch Trials
#Put extra credits in beginning of game