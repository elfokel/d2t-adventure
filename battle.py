import player
import monster
import random

print "BATTLE TEST\n------------------\nAttacks: %s and %s" % (player.attack1, player.attack2)


while player.hp >= 1 and monster.hp >= 1:
	enterattack = raw_input("Enter attack\n>")
	if enterattack.upper() not in [player.attack1 , player.attack2]:
		print "Attack not recognized"
	if enterattack.upper() == player.attack1:
		randomizer = random.choice([player.attack1, player.miss])
		if randomizer == player.attack1:
			monster.hp = monster.hp - player.attack1dmg
			print "The monster takes %s damage" % str(player.attack1dmg)
		if randomizer == player.miss:
			print "You missed!"
		randomizer = random.choice([monster.attack1, monster.attack2, monster.miss])
		if randomizer == monster.attack1:
			player.hp = player.hp - monster.attack1dmg
			print "The monster hits you with his %s. You take %s damage." % (monster.attack1, str(monster.attack1dmg))
		if randomizer == monster.attack2:
			player.hp = player.hp - monster.attack2dmg
			print "The monster hits you with his %s. You take %s damage." % (monster.attack2, str(monster.attack2dmg))
		if randomizer == monster.miss:
			print "The monster didn't hit you"
	if enterattack.upper() == player.attack2:
		randomizer = random.choice([player.attack2, player.miss])
		if randomizer == player.attack2:
			monster.hp = monster.hp - player.attack2dmg
			print "The monster takes %s damage" % str(player.attack2dmg)
		if randomizer == player.miss:
			print "You missed!"
		randomizer = random.choice([monster.attack1, monster.attack2, monster.miss])
		if randomizer == monster.attack1:
			player.hp = player.hp - monster.attack1dmg
			print "The monster hits you with his %s. You take %s damage." % (monster.attack1, str(monster.attack1dmg))
		if randomizer == monster.attack2:
			player.hp = player.hp - monster.attack2dmg
			print "The monster hits you with his %s. You take %s damage." % (monster.attack2, str(monster.attack2dmg))
		if randomizer == monster.miss:
			print "The monster didn't hit you"
else:
	if player.hp < 1:
		print "You have died"
	if monster.hp < 1:
		print "You have defeated the monster"