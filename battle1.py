import player
import monster1
import random

print "BATTLE 1\n------------------\nAttacks: %s and %s" % (player.attack1, player.attack2)


while player.hp >= 1 and monster1.hp >= 1:
	enterattack = raw_input("Enter attack\n>")
	if enterattack.upper() not in [player.attack1 , player.attack2]:
		print "Attack not recognized"
	if enterattack.upper() == player.attack1:
		randomizer = random.choice([player.attack1, player.miss])
		if randomizer == player.attack1:
			monster1.hp = monster1.hp - player.attack1dmg
			print "The monster takes %s damage" % str(player.attack1dmg)
		if randomizer == player.miss:
			print "You missed!"
		randomizer = random.choice([monster1.attack1, monster1.attack2, monster1.miss])
		if randomizer == monster1.attack1:
			player.hp = player.hp - monster1.attack1dmg
			print "The monster hits you with his %s. You take %s damage." % (monster1.attack1, str(monster1.attack1dmg))
		if randomizer == monster1.attack2:
			player.hp = player.hp - monster1.attack2dmg
			print "The monster hits you with his %s. You take %s damage." % (monster1.attack2, str(monster1.attack2dmg))
		if randomizer == monster1.miss:
			print "The monster didn't hit you"
	if enterattack.upper() == player.attack2:
		randomizer = random.choice([player.attack2, player.miss])
		if randomizer == player.attack2:
			monster1.hp = monster1.hp - player.attack2dmg
			print "The monster takes %s damage" % str(player.attack2dmg)
		if randomizer == player.miss:
			print "You missed!"
		randomizer = random.choice([monster1.attack1, monster1.attack2, monster1.miss])
		if randomizer == monster1.attack1:
			player.hp = player.hp - monster1.attack1dmg
			print "The monster hits you with his %s. You take %s damage." % (monster1.attack1, str(monster1.attack1dmg))
		if randomizer == monster1.attack2:
			player.hp = player.hp - monster1.attack2dmg
			print "The monster hits you with his %s. You take %s damage." % (monster1.attack2, str(monster1.attack2dmg))
		if randomizer == monster1.miss:
			print "The monster didn't hit you"
else:
	if player.hp < 1:
		print "You have died"
	if monster1.hp < 1:
		print "You have defeated the monster"