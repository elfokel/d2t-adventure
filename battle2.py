import player
import monster2
import random

print "BATTLE 2\n------------------\nAttacks: %s and %s" % (player.attack1, player.attack2)


while player.hp >= 1 and monster2.hp >= 1:
	enterattack = raw_input("Enter attack\n>")
	if enterattack.upper() not in [player.attack1 , player.attack2]:
		print "Attack not recognized"
	if enterattack.upper() == player.attack1:
		randomizer = random.choice([player.attack1, player.miss])
		if randomizer == player.attack1:
			monster2.hp = monster2.hp - player.attack1dmg
			print "The monster takes %s damage" % str(player.attack1dmg)
		if randomizer == player.miss:
			print "You missed!"
		randomizer = random.choice([monster2.attack1, monster2.attack2, monster2.miss])
		if randomizer == monster2.attack1:
			player.hp = player.hp - monster2.attack1dmg
			print "The monster hits you with his %s. You take %s damage." % (monster2.attack1, str(monster2.attack1dmg))
		if randomizer == monster2.attack2:
			player.hp = player.hp - monster2.attack2dmg
			print "The monster hits you with his %s. You take %s damage." % (monster2.attack2, str(monster2.attack2dmg))
		if randomizer == monster2.miss:
			print "The monster didn't hit you"
	if enterattack.upper() == player.attack2:
		randomizer = random.choice([player.attack2, player.miss])
		if randomizer == player.attack2:
			monster2.hp = monster2.hp - player.attack2dmg
			print "The monster takes %s damage" % str(player.attack2dmg)
		if randomizer == player.miss:
			print "You missed!"
		randomizer = random.choice([monster2.attack1, monster2.attack2, monster2.miss])
		if randomizer == monster2.attack1:
			player.hp = player.hp - monster2.attack1dmg
			print "The monster hits you with his %s. You take %s damage." % (monster2.attack1, str(monster2.attack1dmg))
		if randomizer == monster2.attack2:
			player.hp = player.hp - monster2.attack2dmg
			print "The monster hits you with his %s. You take %s damage." % (monster2.attack2, str(monster2.attack2dmg))
		if randomizer == monster2.miss:
			print "The monster didn't hit you"
else:
	if player.hp < 1:
		print "You have died"
	if monster2.hp < 1:
		print "You have defeated the monster"