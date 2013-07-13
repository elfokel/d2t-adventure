# MAIN ADVENTURE FILE!

import random, player

# Adventure Starts
print "You wake up in room."
start = raw_input("What would you like to do?\nOptions:\n1. Check\n2. Leave\n>")
if start.upper() == "CHECK":
	print "You see the room. You find nothing. You leave the room."

# Random Boss Selection
	boss1 = "1"
	boss2 = "2"
	boss3 = "3"
	randomboss = random.choice([boss1, boss2, boss3])
	while randomboss == "1":
		execfile("battle1.py")
		boss1 = "0"
		player.hp = 20
	while randomboss == "2":
		execfile("battle2.py")
		player.hp = 20
		boss2 = "0"
	while randomboss == "3":
		execfile("battle3.py")
		player.hp = 20
		boss3 = "0"