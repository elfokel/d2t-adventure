#MAIN ADVENTURE FILE!

import random, battlecheck, player

print "You wake up in room."
start = raw_input("What would you like to do?\nOptions:\n1. Check\n2.Leave\n>")
if start.upper() == "CHECK":
	print "You see the room. You find nothing. You leave the room."
	execfile("battle1.py")
	player.hp = 20
	execfile("battle2.py")
	player.hp = 20
	execfile("battle3.py")