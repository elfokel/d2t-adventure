def battle(playerhp, playeratk1, playeratk2, playeratk1dmg, playeratk2dmg, monstername, monsterhp, monsteratk1, monsteratk2, monsteratk1dmg, monsteratk2dmg):
	import random
	import player
	
	#####DEFINE WHICH WEAPON TO BATTLE WITH#####
	if player.attack2 == "LONGSWORD":
		atk2random = random.choice([playeratk2, "miss"])
	if player.attack2 == "FIRESTICK":
		atk2random = random.choice([playeratk2, "miss", "miss"])
	if player.attack2 == "M16":
		atk2random = random.choice([playeratk2, "miss", "miss", "miss", "miss", "miss", "miss", "miss", "miss", "miss"])
	#####START BATTLE######
	while playerhp >= 1 and monsterhp >= 1:
		enterattack = raw_input("Enter attack\n> ")
		#####COMMAND IS NOT RECOGNIZED#####
		if enterattack.upper() not in [playeratk1 , playeratk2]:
			print "Attack not recognized"
		#####IF PLAYER IS ATTACKING WITH ATTACK 1#####
		if enterattack.upper() == playeratk1:
			randomizer = random.choice([playeratk1, "miss"])
			if randomizer == playeratk1:
				monsterhp = monsterhp - playeratk1dmg
				print "%s takes %s damage" % (monstername, str(playeratk1dmg))
			if randomizer == "miss":
				print "You missed!"
			randomizer = random.choice([monsteratk1, monsteratk2, "miss"])
			if randomizer == monsteratk1:
				playerhp = playerhp - monsteratk1dmg
				print "%s hits you with his %s. You take %s damage." % (monstername, monsteratk1, str(monsteratk1dmg))
			if randomizer == monsteratk2:
				playerhp = playerhp - monsteratk2dmg
				print "%s hits you with his %s. You take %s damage." % (monstername, monsteratk2, str(monsteratk2dmg))
			if randomizer == "miss":
				print "%s didn't hit you" % monstername 
		#####IF PLAYER IS ATTACKING WITH ATTACK 2#####
		if enterattack.upper() == playeratk2:
			if atk2random == playeratk2:
				monsterhp = monsterhp - playeratk2dmg
				print "%s takes %s damage" % (monstername, str(playeratk2dmg))
			if atk2random == "miss":
				print "You missed!"
			randomizer = random.choice([monsteratk1, monsteratk2, "miss"])
			if randomizer == monsteratk1:
				playerhp = playerhp - monsteratk1dmg
				print "%s hits you with his %s. You take %s damage." % (monstername, monsteratk1, str(monsteratk1dmg))
			if randomizer == monsteratk2:
				playerhp = playerhp - monsteratk2dmg
				print "%s hits you with his %s. You take %s damage." % (monstername, monsteratk2, str(monsteratk2dmg))
			if randomizer == "miss":
				print "The monster didn't hit you"
	else:
		if playerhp < 1:
			print "You have died."
			exit()
		if monsterhp < 1:
			print "You have defeated. %s" % (monstername)