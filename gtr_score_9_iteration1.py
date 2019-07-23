from nesstools import guitar
import random as r 			# use the random module for randomised events

#________________________________________
# General variables
# note that we don't need to define the score duration, T, here, as that will be determined by the tab
numberOfStrings = 3         # how many strings should the guitar have?
T = 30

#________________________________________
#_____CREATE THE SCORE FILE______________

my_score = guitar.GuitarScore(T, numberOfStrings)

# start from time=1 second
time = 1		# our current time variable that we will increase until we hit our maximum

while time < T-6:
	# this sets up a WHILE LOOP - all the indented code below is looped 
	# the loop stops when our cumulative time variable, t, gets to 6 seconds from the end of the score
	# (the -6 is so that we have time for the final events to ring out)

	# for each iteration, we'll add an event on a particular string
	# here we use the random module to create a random integer between 1 and numberOfStrings for our string number
	string = r.randint(1, numberOfStrings)

	# generate a random fret each time between 0 and 12
	fret = r.randint(0, 12)

	# we'll use the playFret function from tutorial 3:
	my_score.playFret	(string, time, fret)

	# we increase our current time by a quarter of a second and go around the loop again
	time += 0.25


# Once the whileloop is finished, export the score as a NESS-compatible score file
my_score.write("ness_files_to_process/gtr_score_9_iteration1.m")



#____________________________________________________________
# CREATE THE INSTRUMENT FILE

# create a string instrument object with 6 strings.
my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.defaultGuitar() # default steel strings
my_guitar.write("ness_files_to_process/gtr_instrument_9_iteration1.m")