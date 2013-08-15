from func import battle, weaponhitlist, slide
import player, monster1, monster2, monster3
import random, pygame, time

#pygame.init()
#slide([800, 600], "images/slide1.png", 1)
#slide([800, 600], "images/slide2.png", 1)
#pygame.quit()

#Adventure starts here

print "A long time ago stuff happened!"
time.sleep(3)
print "Then stuff happened after that"
time.sleep(3)
print "Now this stuff will happen"
time.sleep(3)

print 'Adventure starts!'
#playername = raw_input('What is your name? ')
#playername = player.name
start = raw_input('You wake up in a room. What would you like to do?\nOptions:\n1. Check\n2. Leave\n> ')

while start.upper() not in ('CHECK', 'LEAVE'):
	print 'Command not recognized!'
	start = raw_input('What would you like to do?\nOptions:\n1. Check\n2. Leave\n> ')
else:
	if start.upper() == 'CHECK':
		weapon = raw_input('You have found some weapons!. You may only pick one since you are too much of a weakling to carry two.\n1. Longsword - Damage: 3, Hit Chance: 50%\n2. Firestick - Damage: 5, Hit Chance: 33%\n3. M16 - Damage: 10, Hit Chance: 10%\n> ')
		while weapon not in ['1', '2', '3']:
			print 'That is not one of the weapons!'
			weapon = raw_input('You have found some weapons!. You may only pick one since you are too much of a weakling to carry two.\n1. Longsword - Damage: 3, Hit Chance: 50%\n2. Firestick - Damage: 5, Hit Chance: 33%\n3. M16 - Damage: 10, Hit Chance: 10%\n> ')
		if weapon.upper() == '1':
			player.weapon2 = 'LONGSWORD'
			player.weapon2dmg = 3
			player.hitlist2 = weaponhitlist(2)
		if weapon.upper() == '2':
			player.weapon2 = 'FIRESTICK'
			player.weapon2dmg = 5
			player.hitlist2 = weaponhitlist(5)
		if weapon.upper() == '3':
			player.weapon2 = 'M16'
			player.weapon2dmg = 10
			player.hitlist2 = weaponhitlist(10)	  

	########## MONSTER BATTLE SELECTION ############
		monsters = [monster1, monster2, monster3]
		while monsters:
			monster = random.choice(monsters)
			battle(player, monster)
			monsters.remove(monster)

	if start.upper() == 'LEAVE':
		print 'You leave the room.'
	########## MONSTER BATTLE SELECTION ############	
		monsters = [monster1, monster2, monster3]
		while monsters:
			monster = random.choice(monsters)
			print monster.name
			battle(player, monster)
			monsters.remove(monster)
			print monsters