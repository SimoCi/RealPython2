import sys
from random import choice

import pdb

random1 = [1,2,3,4,5,6,7,8,9,10,11,12]
random2 = [1,2,3,4,5,6,7,8,9,10,11,12]

while True:
	pdb.set_trace()
	print "To exit this game type 'exit'"
	answer = raw_input("What is {} times {}?".format(choice(random2), choice(random1)))

	product = int(choice(random2)*choice(random1))

	# exit
	if answer == "exit":
		print "Now exiting game!"
		sys.exit()

	# very bad example : instead, you might want to match a given number by 
	# multiplicating two random integers
	# I supposed user always entered the right answer for a required multiplication
	# finally, I understood the man's goal: write a little app to test your
	# knowledge of 'tabelline'

	# determine if number is correct
	# elif answer == choice(random2)*choice(random1):
	elif answer == product:
		print "Correct!"
	else:
		print "Wrong!"