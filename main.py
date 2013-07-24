from battle import battle
import player, monster1, monster2, monster3

#battle1 = battle(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster1.monsternam, monster1.hp, monster1.attack1, monster1.attack2, monster1.attack1dmg, monster1.attack2dmg)
#battle2 = battle(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster2.monsternam, monster2.hp, monster2.attack1, monster2.attack2, monster2.attack1dmg, monster2.attack2dmg)
#battle3 = battle(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster3.monsternam, monster3.hp, monster3.attack1, monster3.attack2, monster3.attack1dmg, monster3.attack2dmg)   

#Adventure starts here####

print "You wake up in room."
playername = raw_input("What's your name? ")
playername = player.name
start = raw_input("What would you like to do?\nOptions:\n1. Check\n2. Leave\n> ")

while start.upper() not in ("CHECK", "LEAVE"):
	print "Command not recognized!"
	start = raw_input("What would you like to do?\nOptions:\n1. Check\n2. Leave\n> ")
else:
	if start.upper() == "CHECK":
		weapon = raw_input("You've found some weapons!. You may only pick one since you are too much of a weakling to carry two.\n1. Longsword - Damage: 3, Hit Chance: 50%\n2. Firestick - Damage: 5, Hit Chance: 33%\n3. M16 - Damage: 10, Hit Chance: 10%\n> ")
		while weapon.upper() not in ["LONGSWORD", "FIRESTICK", "M16"]:
			print "That is not one of the weapons!"
			weapon = raw_input("You've found some weapons!. You may only pick one since you are too much of a weakling to carry two.\n1. Longsword - Damage: 3, Hit Chance: 50%\n2. Firestick - Damage: 5, Hit Chance: 33%\n3. M16 - Damage: 10, Hit Chance: 10%\n> ")
		if weapon.upper() == "LONGSWORD":
			player.attack2 = "LONGSWORD"
			player.attack2dmg = 3
		if weapon.upper() == "FIRESTICK":
			player.attack2 = "FIRESTICK"
			player.attack2dmg = 5
		if weapon.upper() == "M16":
			player.attack2 = "M16"
			player.attack2dmg = 10	  
		###MONSTER 1 BATTLE#####
		print "#### STARTING BATTLE 1! ####"
		battle(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster1.monsternam, monster1.hp, monster1.attack1, monster1.attack2, monster1.attack1dmg, monster1.attack2dmg)
		
		###MONSTER 2 BATTLE####
		print "#### STARTING BATTLE 2! ####"
		battle(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster2.monsternam, monster2.hp, monster2.attack1, monster2.attack2, monster2.attack1dmg, monster2.attack2dmg)
		
		###MONSTER 3 BATTLE####
		print "#### STARTING BATTLE 3! ####"
		battle(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster3.monsternam, monster3.hp, monster3.attack1, monster3.attack2, monster3.attack1dmg, monster3.attack2dmg)

	if start.upper() == "LEAVE":
		print "You leave the room."
		
		###MONSTER 1 BATTLE#####
		print "#### STARTING BATTLE 1! ####"
		battle(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster1.monsternam, monster1.hp, monster1.attack1, monster1.attack2, monster1.attack1dmg, monster1.attack2dmg)
		
		###MONSTER 2 BATTLE####
		print "#### STARTING BATTLE 2! ####"
		battle(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster2.monsternam, monster2.hp, monster2.attack1, monster2.attack2, monster2.attack1dmg, monster2.attack2dmg)
		
		###MONSTER 3 BATTLE####
		print "#### STARTING BATTLE 3! ####"
		battle(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster3.monsternam, monster3.hp, monster3.attack1, monster3.attack2, monster3.attack1dmg, monster3.attack2dmg)