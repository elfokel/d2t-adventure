#MAIN ADV FILE
import introroom, hall1, player, monster

intro = raw_input("Adventure starts. Commands:\nCheck, Leave\n>")
if intro.upper() == "CHECK":
	introcheck = raw_input(introroom.check)
	if introcheck.upper() == "LEAVE":
		introleave = raw_input(introroom.leave)
		if introleave.upper() == "RIGHT":
			print hall1.right
			execfile('battle.py')
		if introleave.upper() == "LEFT":
			print hall1.left
		if introleave.upper() == "CONTINUE":
			print hall1.cont
if intro.upper() == "LEAVE":
	introleave = raw_input(introroom.leave)
	if introleave.upper() == "RIGHT":
		print hall1.right
		execfile('battle.py')
	if introleave.upper() == "LEFT":
		print hall1.left
	if introleave.upper() == "CONTINUE":
		print hall1.cont	

