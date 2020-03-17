from nesstools import net1
import random as r

# general variables
stringCount = 6         # how many strings should the guitar have?
T = 8                   # how long should the piece be (in seconds)?

# create a string instrument object with 1 string and write the instrument file
my_inst = net1.Net1Instrument(stringCount)
for string in my_inst.strings:
	string.length = r.uniform(0.5, 1.5)
	string.radius = r.uniform(0.0001, 0.0006)
  


for i in range(5):
	stringA = r.randint(1, stringCount)
	stringB = r.randint(1, stringCount)
	rattleDistance = r.uniform(0.00005, 0.001)
	my_inst.addConnection(stringA, stringB, rattleDistance=rattleDistance)


my_inst.write("ness_files_to_process/net1_tutorial2c_inst.m")

my_score = net1.Net1Score(T, stringCount)    

t = 0
dt = 0.25

while t < T-4:
	stringNum = r.randint(1, stringCount)		# which string to play
	strength = r.uniform(0.25, 2.0)				# how hard to strike/pluck
	pos = r.uniform(0.5, 0.99)					# where to strike/pluck
	eventType = r.randint(0, 1)  				# 0 is strike, 1 is pluck

	# add an event to the score at the current time, with the above settings
	my_score.makeEvent(t, stringNum, strength, pos, eventType)

	# increment the current time
	t += dt
  
my_score.write("ness_files_to_process/net1_tutorial2c_score.m")
