#MAIN ADVENTURE FILE

import random, battlecheck

print "You wake up in room."
start = raw_input("What would you like to do?\nOptions:\n1. Check\n2.Leave\n>")
if start.upper() == "CHECK":
	print "You see the room. You find nothing. You leave the room."
	ranroom = random.choice([battlecheck.battle1, battlecheck.battle2, battlecheck.battle3])
	if ranroom == battlecheck.battle1:
		execfile("battle1.py")
	if ranroom == battlecheck.battle2:
		execfile("battle2.py")
	if ranroom == battlecheck.battle3:
		execfile("battle3.py")