from battlefun import battlefunc
import player, monster1, monster2, monster3


print "You wake up in room."
playername = raw_input("What's your name? ")
playername = player.name
start = raw_input("What would you like to do?\nOptions:\n1. Check\n2. Leave\n> ")
if start.upper() == "CHECK":
	print "You inspect the room. You find nothing. You leave the room."


###MONSTER 1 BATTLE#####
battlefunc(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster1.monsternam, monster1.hp, monster1.attack1, monster1.attack2, monster1.attack1dmg, monster1.attack2dmg)

###MONSTER 2 BATTLE####
battlefunc(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster2.monsternam, monster2.hp, monster2.attack1, monster2.attack2, monster2.attack1dmg, monster2.attack2dmg)

###MONSTER 3 BATTLE####
battlefunc(player.hp, player.attack1, player.attack2, player.attack1dmg, player.attack1dmg, monster3.monsternam, monster3.hp, monster3.attack1, monster3.attack2, monster3.attack1dmg, monster3.attack2dmg)