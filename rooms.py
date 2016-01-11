class Room:
	def enter(self):
		print "You shouldn't be entering a generic room.  Shame on you."
		exit(0)
		
class R1(Room):
	def enter(self):
		print "\nYou have entered room 1."
		print "There is a door on your right and a door on your left."
		print "Which do you take?"
		while True:
			door_choice = raw_input("right or left? > ")
			if door_choice == "right":
				r2 = R2()
				r2.enter()
				break
			elif door_choice == "left":
				r3 = R3()
				r3.enter()
				break
			else:
				print "Please choose 'right' or 'left'"
				door_choice = raw_input("right or left? > ")

class R2(Room):
	def enter(self):
		print "\nYou have entered room 2."
		print "There is a door behind you and a door in front of you."
		print "Which do you take?"
		while True:
			door_choice = raw_input("behind or in front? > ")
			if door_choice == "behind":
				r1 = R1()
				r1.enter()
				break
			elif door_choice == "in front":
				r4 = R4()
				r4.enter()
				break
			else:
				print "Please choose 'in front' or 'behind'"
				door_choice = raw_input("in front or behind? > ")

class R3(Room):
	def enter(self):
		print "\nYou have entered room 3."
		print "There is a door above you and a door behind you."
		print "which do you take?"
		while True:
			door_choice = raw_input("above or behind? > ")
			if door_choice == "behind":
				r1 = R1()
				r1.enter()
				break
			elif door_choice == "above":
				r5 = R5()
				r5.enter()
				break
			else:
				print "Please chooise 'in front' or 'behind'"
				door_choice = raw_input()

class R4(Room):
	def enter(self):
		print "\nYou have entered room 4."
		print "There is nowhere else to go.  You are trapped in a maze for all eternity."
		print "You realize this sequence of rooms is merely the echo chamber of your own mind."
		print "Do you fall into despair?"
		despr = raw_input("yes or no? > ")
		if despr == "yes":
			print "Your will has betrayed you."
			print "gg"
		else:
			print "You have overcome the meaninglessness of your surroundings."
			print "Nice!"
		exit(0)
			
class R5(Room):
	def enter(self):
		print "\nYou have ascended into the zone of higher learning."
		print "Everything you knew before fades into distant memory as you confront a transcendent reality."
		print "Nice."
		exit(0)
		