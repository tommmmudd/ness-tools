from nesstools import guitar
import random as r 			# import the random module as "r"
	
numberOfStrings = 1         # how many strings should the guitar have?
T = 15                      # how long should the piece be (in seconds)?

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 6 strings and write it to a file
my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.write("ness_files_to_process/EXPERIMENT2_long_frets_guitar.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, numberOfStrings)       

# Add score events (plucks and finger placements) using a built in function
t = 0.1                     # events start at 1 second
timeStep = 0.5				# half a second between events
iterationCount = 0			# a variable for counting the iterations

# iterate through the score incrementally in time
# when our time variable t gets to 6 seconds from the end of the score, the iteration loop stops
while t < T-6:	

	# choose a new fret and glideTime randomly	
	newFret = r.randint(0, 17)				# note that the random functions rely on the random module being imported as r (see top of file)

	# very short finger movement time
	glideTime = 0.001
	# but 20% chance of a slower 1/4 second movement
	if (r.random() < 0.2):
		glideTime = 0.25

	# add this finger movement to the score file
	my_score.playFret (1, t,   newFret,    glideTime)

	# every third iteration, add a pluck
	if iterationCount%3 == 0:
		my_score.pluck (1, t, 0.75, 0.001, 0.3)

	# count our iterations
	iterationCount += 1
	# increment the time by a fixed amount
	t += timeStep


# export the final score
my_score.write("ness_files_to_process/EXPERIMENT2_score.m")
