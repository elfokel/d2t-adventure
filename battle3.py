import player
import monster3
import random

print "BATTLE TEST\n------------------\nAttacks: %s and %s" % (player.attack1, player.attack2)


while player.hp >= 1 and monster3.hp >= 1:
	enterattack = raw_input("Enter attack\n>")
	if enterattack.upper() not in [player.attack1 , player.attack2]:
		print "Attack not recognized"
	if enterattack.upper() == player.attack1:
		randomizer = random.choice([player.attack1, player.miss])
		if randomizer == player.attack1:
			monster3.hp = monster3.hp - player.attack1dmg
			print "The monster takes %s damage" % str(player.attack1dmg)
		if randomizer == player.miss:
			print "You missed!"
		randomizer = random.choice([monster3.attack1, monster3.attack2, monster3.miss])
		if randomizer == monster3.attack1:
			player.hp = player.hp - monster3.attack1dmg
			print "The monster hits you with his %s. You take %s damage." % (monster3.attack1, str(monster3.attack1dmg))
		if randomizer == monster3.attack2:
			player.hp = player.hp - monster3.attack2dmg
			print "The monster hits you with his %s. You take %s damage." % (monster3.attack2, str(monster3.attack2dmg))
		if randomizer == monster3.miss:
			print "The monster didn't hit you"
	if enterattack.upper() == player.attack2:
		randomizer = random.choice([player.attack2, player.miss])
		if randomizer == player.attack2:
			monster3.hp = monster3.hp - player.attack2dmg
			print "The monster takes %s damage" % str(player.attack2dmg)
		if randomizer == player.miss:
			print "You missed!"
		randomizer = random.choice([monster3.attack1, monster3.attack2, monster3.miss])
		if randomizer == monster3.attack1:
			player.hp = player.hp - monster3.attack1dmg
			print "The monster hits you with his %s. You take %s damage." % (monster3.attack1, str(monster3.attack1dmg))
		if randomizer == monster3.attack2:
			player.hp = player.hp - monster3.attack2dmg
			print "The monster hits you with his %s. You take %s damage." % (monster3.attack2, str(monster3.attack2dmg))
		if randomizer == monster3.miss:
			print "The monster didn't hit you"
else:
	if player.hp < 1:
		print "You have died"
	if monster3.hp < 1:
		print "You have defeated the monster"