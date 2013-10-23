from func import battle, weaponhitlist, slide
import player, monster1, monster2, monster3
import random, pygame, time

pygame.init()
slide([800, 600], "images/slide1.png", 1)
slide([800, 600], "images/slide2.png", 1)
pygame.quit()

#Adventure starts here

print "A long time ago stuff happened!"
time.sleep(3)
print "Then stuff happened after that"
time.sleep(3)
print "Now this stuff will happen"
time.sleep(3)

print 'Adventure starts!'
player.name = raw_input('What is your name? ')
start = raw_input('You wake up in a room. What would you like to do?\nOptions:\n1. Check\n2. Leave\n> ')

while start.upper() not in ('CHECK', 'LEAVE'):
	print 'Command not recognized!'
	start = raw_input('>')
else:
	if start.upper() == 'CHECK':
		print 'You have found some weapons!. Pick only one since you are too much of a weakling to carry two.'
		weapon = raw_input('\n-------------------------------------------\n-  Weapon    -   Damage  -    Hit Chance  -\n-------------------------------------------\n- Longsword  -     3     -       50%      -\n- Firestaff  -     5     -       33%      -\n-    M16     -    10     -       10%      -\n-------------------------------------------\n\nEnter weapon name to pick it up.\n>')
		while weapon.upper() not in ['LONGSWORD', 'FIRESTAFF', 'M16']:
			print 'That is not a weapon! Try again.'
			weapon = raw_input('>')
		if weapon.upper() == 'LONGSWORD':
			player.weapon2 = 'LONGSWORD'
			player.weapon2dmg = 3
			player.hitlist2 = weaponhitlist(2)
		if weapon.upper() == 'FIRESTAFF':
			player.weapon2 = 'FIRESTAFF'
			player.weapon2dmg = 5
			player.hitlist2 = weaponhitlist(5)
		if weapon.upper() == 'M16':
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