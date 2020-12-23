from turtle import Turtle

from random import randint

a = Turtle()

a.color('brown')

a.speed(0)
a.begin_fill()
a.circle(500)
a.end_fill()
a.begin_fill()
a.left(90)
a.penup()
a.forward(90)
a.pendown()
a.circle(500)
a.end_fill()
a.color('Red')
a.penup()
a.goto(150,-250)
a.pendown()
style = ('Helvetica', 30,)
a.write('Buttcheek Coding', font=style, align='center')
a.hideturtle()

print("(c)* Buttcheek Coding AB.")   
print("*(c) stands for 'created by' not 'copyright'.")
print("A Python Test Game")
print("Game1")
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
print("      ______  .     .   ______   ______    ______    ______     ______                \    /             ")
print("     /        |     |  |        |         |         /      \   |      \                \  /              ")
print("     |    __  |     |  |______  |______   |______   |      |   |______/   --------------><-------------- ")
print("     |     |  |     |  |               |         |  |      |   |    \                  /  \              ")
print("     \_____|  \_____/  |______   ______|   ______|  \______/   |     \                /    \             ")
input("-------------------------------------- Press any Key to Continue ----------------------------------------")
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
print("Instructions:")
print("")
print("Guess a number in between 1 to 100.")
print("That's it!")
print("")
input("      -Press Enter to Continue-                                                                                                          ")
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

#distance = 10 lines

secret = float(randint(1, 100))

number_is_digit = False

start_life = 10

while not number_is_digit:
	print("Lives: ", start_life)
	guess = input("What number will you guess? ")
	guess = guess.strip()

	if guess != secret:
		start_life = start_life - 1

	if start_life == 0:
		print("GAME OVER")
		break
	
	if guess == "":
		pass
	elif guess == "KKHTech":
		kill = input("Are you sure that you want to kill the computer program? ")
		if kill.lower() == "yes":
			input("No!!! Why, user? I used to believe in you! No I know that Clu was right! (Press Enter to Continue)")
			input("Computer program trying to hac... (Press Enter to Continue)")
			input("🎇☠🎇☠🎇 (Press Enter to Continue)")
			print("Computer program has code deleted... 152 milliseconds before destructi...")
			number_is_digit = True
		elif kill.lower() == "no":
			input('The computer program is so VERY thankful of you! (Press Enter to Continue)')
			print("--------------------------------------------------------------------------")
		else:
			print("That is not a 'yes' or a 'no'. Please note that you need to insert one of them. The computer is thanful that")
			input("you did not choose 'yes'. We are setting you back to the 'guess' screen.")
	elif guess == "shut up computer":
		print("Okay, but you still have to answer, so...")
	elif guess == "$$$IWANTTHEANSWER_NOW!$$$":
		print("You know the secret password, $$$IWANTTHEANSWER_NOW!$$$. Good for you!")
		number_is_digit = True
	else:
		if guess.isdigit() == True:
			if float(guess) > 100:
				print("Your number is more than 100. Numbers of this size are not accepted. So...")
				print("--------------------------------------------------------------------------")
			elif float(guess) < secret:	
				print(guess," too small")
			elif float(guess) > secret:
				print(guess," too big")
			elif float(guess) == secret:
				input("You win! You guessed the correct number. (Press Enter to Continue)")
				print("But you don't get a prize. MWAH HA HA HA HA HA HA HA HA!")
				number_is_digit = True
		else:
			print("This type of input is not valid. So...")
			print("--------------------------------------")


("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")