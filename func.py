import pygame, time, random

def slide(imagesize, image, timer):
	screen = pygame.display.set_mode((imagesize))
	bg = pygame.image.load(image)
	bgrect = bg.get_rect()
	screen.blit(bg, bgrect)
	pygame.display.flip()
	time.sleep(timer)

def weaponhitlist(n):
	miss = ['miss']
	hit = ['hit']
	result = hit + (miss*(n-1))
	return result

def attack(player, monster, playerhitlist, playerweapon, playerweapondmg):
	randomizer = random.choice(playerhitlist)
	if randomizer == 'hit':
		monster.hp = monster.hp - playerweapondmg 
		print '%s takes %s damage' % (monster.name, str(playerweapondmg))
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
			attack(player, monster, player.hitlist1, player.weapon1, player.weapon1dmg)	
		#####IF PLAYER IS ATTACKING WITH WEAPON 2#####
		if enterweapon.upper() == player.weapon2:
			attack(player, monster, player.hitlist2, player.weapon2, player.weapon2dmg)
	else:
		if player.hp < 1:
			print 'You have died.'
			exit()
		if monster.hp < 1:
			print 'You have defeated %s' % (monster.name)
			player.hp = 20