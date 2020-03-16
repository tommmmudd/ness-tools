from nesstools import net1
import random as r  			# for randomising events


# general variables
stringCount = 3         # how many strings should the guitar have?
T = 8                      # how long should the piece be (in seconds)?

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 3 strings
my_inst = net1.Net1Instrument(stringCount)

# add a connection between string 1 and 2, using the default connection parameters
my_inst.addConnection(1, 2)

# write the instrument file as a NESS-compatible text file
my_inst.write("ness_files_to_process/net1_tutorial_inst.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (stringCount)
my_score = net1.Net1Score(T, stringCount)    

t = 0
dt = 0.25					# interval between events

while t < T-4:
	stringNum = r.randint(1, stringCount)		# which string to play
	strength = r.uniform(0.5, 2.0)				# how hard to strike/pluck
	pos = r.uniform(0.5, 0.9)					# where to strike/pluck
	eventType = r.randint(0, 1)  				# 0 is strike, 1 is pluck

	# add an event to the score at the current time, with the above settings
	my_score.makeEvent(t, stringNum, strength, pos, eventType)

	# increment the current time
	t += dt


# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/net1_tutorial_score.m")



