resseruct = 0
hand_grenade = 0
day = 0
binoculars = 0
water = 0
food = 0
axe = 0
axe_durability = 100
treechop = 0
tree_barks = treechop
pickaxe = 0
pick_durability = 100
bricks = 0
HP = 100

if HP == 0:
	print("You have 0 HP left, You died game over.")

if axe_durability == 0:
	axe = axe - 1
	print("Your axe broke and now you cant use it.")

name = str(input("Enter your name :- "))

answer = input(
	"You are on a dirt road would you like to go left, or right ?..").lower()

if answer == "left":
	print("You come to a river. You can walk around it or swim across. Type walk to walk or swim to swim")
	answer = str(input("Enter your answer here :-"))
	
	if answer == "swim":
		print("You came across a hungry crocodile who ate you. You lose.")
		quit()
	
	elif answer == "walk":
		print("You were walking and came across an abandoned village. Would you like to explore it or go towards an ugly witch approaching you ?")
		answer = str(input("Enter witch for witch and village for village:- "))
		
		if answer == "witch":
			print("The witch gave you powers and now you can resseruct yourself 1 time")
			print("ressurect + 1")
			resseruct = resseruct + 1
			print("You now head to the village and a swarm of zombies attack you. Would you like to find shelter or find a weapon ?")
			answer = input("Enter weapon for weapon and shelter for shelter :-")
			
			if answer == "weapon":
				print("You found a hand grenade. You put it in your pouch")
				print("Hand grenade + 1")
				hand_grenade = hand_grenade + 1
				print("You find a watchtower and a boat. Where would you like to go ?")
				answer = input("Enter watchtower for watchtower and boat for boat:-")
				
				if answer == "watchtower":
					print("You enter the watchtower and lock the door.")
					print("While locking the door you see that you are bleeding and have lost 7 HP. You apply a bandaid but it doesn't help you recover your HP")
					HP = HP -7
					print("You climb up the watch tower and notice that every zombie in the village are gethered outside looking up towards you and are able to do nothing about it.")
					print("Would you like to use this as an opportunity to use the handgrenade or save it later and flash light at them so they run away ?")
					answer = input("Enter grenade for hand grenade and light for flash light :-")
					
					if answer == "grenade":
						print("You threw the grenade down and all the zombies died.")
						hand_grenade = hand_grenade - 1
						print("You have",hand_grenade,"hand grenades left")
						print("You decide to sleep after a terrifying and tiring day.")
						print("You wake up the next day")
						day = day + 1
						print("It is day",day)
						print("You explore the lighthouse and find some binoculars and a water bottle with some food")
						binoculars = binoculars + 1
						water = water + 1
						food = food + 1
						print("You leave the lighthouse and hop onto the boat to exit the haunting village of the damned.")
						print("You can see a cold terrestrial yet unpopulated land and a savanah village which was filled with people.")
						print("You decide to go to the village but u start feeling hungry")
						print("Would you like to go to the village first or eat some food.")
						answer = input("Enter village for village and food for food :-")
						
					if answer == "village":
						print("You go towards the village hunger deprived and fall unconcious on the land.")
						print("You wake up at the house of a villager and they treat you really good and for free.")
						print("You thank them and ask them for a permission to build your which they very kindly and happpily give.")
						print("You are offered a temperory house until you make yours, wich you graciously accept.")
						print("You have to make a house hence you head to the jungle with an axe(durability = 100) the toolsmith gave you.")
						print("The durability of an axe decreases everytime you use it by 5")
						print("You see a lot of trees at north, wet concrete by the river at east and large bamboo plants at south.")
						print("For chopping trees enter north, for collecting concrete enter east and for collecting some strong and large bamboos enter south")
						answer = input("Enter your answer :- ")
						
						if answer == "north":
							print("You head north...")
							treechop = int(input("How many trees would you like to chop down :-"))
							axe_durability = axe_durability - (treechop * 5)
							print("You received",treechop,"barks of trees")
							print("The durability of your axe is",axe_durability)
							
						elif answer == "east":
							print("You head East...")
							
							if pickaxe == 0:
								print("You remember that you need a pickaxe to break large chunks of concrete.")
								print("You dint have a pickaxe.")
								print("Would you like to go north, collect some wood and craft a pickaxe, or go somewhere else ?")
								print("Type wood for pickaxe, north to go north, and east to head east")
								answer = input("Enter your choice:-")
								
								if answer == "north":
									print("You head north...")
									treechop = int(input("How many trees would you like to chop down :-"))
									axe_durability = axe_durability - (treechop * 5)
									print("You received",treechop,"barks of trees")
									print("The durability of your axe is",axe_durability)
							
							else:
								print("You broke down large chunk of wet concrete and got smaller bricks")
								pick_durability = pick_durability - 10
								print("bricks + 50")
								bricks = bricks + 50
								
						elif answer == "south":
							print("You head south...")
							print("You see big bamboos and attempt to to break it. You get 70 bamboos but when you were breaking them, ine of them fell on your head and you lost 12 HP")
							HP = HP - 12
							
						print("You head back to the village")
						print("This is all I could think of for now. I hope you enjoyed the game. Thank You")
									
					elif answer == "food":
						print("You open packed food")
						food = food - 1
						print("The smell of food attracts pirrahnas which eat the boat and you with it.")
						print("Atleast someone satisfied their hunger but you died all hungry. Game over. You lose")
						quit()
								
					elif answer == "flashlight":
						print("You make the zombies run away for the night.")
						print("The next day morning you forget about them and get out of the lighthouse.")
						print("Ofcouse, the zombies ate you.")
						
				elif answer == "boat":
					print("You ride on the boat but the fast swimming zombies catch up to you and eat  you. You lose. The end")
					quit()
			
			elif answer == "shelter":
				print("You quickly run inside an abondoned house. Unfortunately The ceiling decides to drop on you. You die a horrific death where the zombie are making an unsatisfactory meal out of your tiny brain.")
				quit()
		
		elif answer == "village":
			print("Some zombies are coming running after you for your brain would you like to search for a weapon or go towards the witch for shelter ?")
			answer = input("Enter witch for witch and weapon for weapon")
			
			if answer == "witch":
				print("The witch tried to help you before the entered the village of the damned. but you ignored her")
				print("She is now angry with you and has cursed you.")
				print("You are dying a torcherous pain. You lose game over.")
				quit()
			
			elif answer == "weapon":
				print("You go searching for a weapon but a zombie gets to you and pins you down.")
				print("The zombie had an non-satisfying dinner, feasting at your brain so he threw your remains into the fire.")
				print("You lose")
			quit()

# elif answer == "right":
# 	
# else:
# 	print("Not a valid option...")