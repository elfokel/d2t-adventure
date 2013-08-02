import random
import player, monster1, monster2, monster3

def weaponhitlist(n):
	miss = ['miss']
	hit = ['hit']
	result = hit + (miss*(n-1))
	return result

def playerattack1(player, monster):
	randomizer = random.choice(player.hitlist1)
	if randomizer == 'hit':
		monster.hp = monster.hp - player.weapon1dmg 
		print '%s takes %s damage' % (monster.name, str(player.weapon1dmg))
	if randomizer == 'miss':
		print 'You missed!'
	randomizer = random.choice([monster.hitlist])
	if randomizer == 'hit1':
		player.hp = player.hp - monster.weapon1dmg
		print '%s hits you with his %s. You take %s damage.' % (monster.name, monster.weapon1, str(monster.weapon1dmg))
	if randomizer == 'hit2':
		player.hp = player.hp - monster.weapon2dmg
		print '%s hits you with his %s. You take %s damage.' % (monster.name, monster.weapon2, str(monster.weapon2dmg))
	if randomizer == 'miss':
		print '%s did not hit you' % monster.name 

def playerattack2(player, monster):
	randomizer = random.choice(player.hitlist2)
	if randomizer == 'hit':
		monster.hp = monster.hp - player.weapon2dmg 
		print '%s takes %s damage' % (monster.name, str(player.weapon2dmg))
	if randomizer == 'miss':
		print 'You missed!'
	randomizer = random.choice(monster.hitlist)
	if randomizer == 'hit1':
		player.hp = player.hp - monster.weapon1dmg
		print '%s hits you with his %s. You take %s damage.' % (monster.name, monster.weapon1, str(monster.weapon1dmg))
	if randomizer == 'hit2':
		player.hp = player.hp - monster.weapon2dmg
		print '%s hits you with his %s. You take %s damage.' % (monster.name, monster.weapon2, str(monster.weapon2dmg))
	if randomizer == 'miss':
		print '%s did not hit you' % monster.name 


def battle(player, monster):
	#####START BATTLE######
	while player.hp >= 1 and monster.hp >= 1:
		enterweapon = raw_input('Enter weapon\n> ')
		#####COMMAND IS NOT RECOGNIZED#####
		if enterweapon.upper() not in [player.weapon1 , player.weapon2]:
			print 'Weapon not recognized'
		#####IF PLAYER IS ATTACKING WITH WEAPON 1#####
		if enterweapon.upper() == player.weapon1:
			playerattack1(player, monster)	
		#####IF PLAYER IS ATTACKING WITH WEAPON 2#####
		if enterweapon.upper() == player.weapon2:
			playerattack2(player, monster)
	else:
		if player.hp < 1:
			print 'You have died.'
			exit()
		if monster.hp < 1:
			print 'You have defeated %s' % (monster.name)
			player.hp = 20

