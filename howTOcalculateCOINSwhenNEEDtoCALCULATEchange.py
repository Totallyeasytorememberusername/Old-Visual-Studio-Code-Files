change = int(input("How much change do you need to give back? "))
total = 0
quarter = 25
dime = 10
nickel = 5
penny = 1
quarter_counter = 0
dime_counter = 0
nickel_counter = 0
penny_counter = 0

while change != total:
	if change > total - 25:
		total += quarter
		quarter_counter += 1
	
	elif change > total - 10:
		total += dime
		dime_counter += 1
	
	elif change > total - 5:	
		total += nickel
		nickel_counter += 1

	elif change > total - 1:	
		total += penny
		penny_counter += 1

	if total == change:
		break

print("quarters: ", quarter_counter)
print("dimes: ", dime_counter)
print("nickels: ", nickel_counter)
print("pennies: ", penny_counter)

#Problem: It seems like that when the number needed calculations for strays out of multiples of quarters already there and needs another, then it does not work.
#Wanted Additions: Sometimes change could go over $1. We need bills.
#Wanted Additions: When doing the above, the ones that are not needed still read '0'. We need to cancel those.
#NO QUESTIONS(HIGHLIGHT WHEN NO QUESTIONS)
#OK(HIGHLIGHT FOR OK)
#BYE(HIGHLIGHT FOR BYE)
#MWAH HA HA HA HA(HIGHLIGHT FOR MWAH HA HA HA HA)
#LOADING(HIGHLIGHT FOR LOADING)