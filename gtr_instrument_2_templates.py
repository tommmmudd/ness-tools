from nesstools import guitar


#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object
my_guitar = guitar.StringInstrument()

my_guitar.defaultBass()			# a 4 string bass: EADG

# other default instruments:
# defaultGuitar()  		   - will NOT set a new stringCount, but adapts to the amount currently defined
# brightGuitar()           - a 6 string guitar with a brighter tone
# defaultBass()			   - a 4 string bass: EADG
# bass6String()			   - a 6 string bass: EADGBE
# defaultGuitarAndBass()   - a 10 string combined instrument: 6 regular guitar strings and 4 regular bass strings
# earthGuitar()            - a 6 string guitar tuned to AEADF#B
# dadgadGuitar()           - a 6 string guitar tuned to: DADGAD
# lowGuitar()              - a 6 string guitar with longer strings, resulting in a lower register. The strings are still more-or-less in tune with each other
# randomGuitar()           - a 6 string guitar with lots of parameters randomised (won't be in regular tuning!)
# randomGlassGuitar()      - a 6 string randomised guitar with thicker strings that give a bar-like glassy sound. NOTE: can lead to some large DC offsets, so you will likely need to download each string output wav separately and add a DC blocker to each file.

# set our local stringCount variable according to the number in the instrument definition
stringCount = my_guitar.stringCount		# stringCount = 4 in our case, for the bass

# export the file as a format compatible instrument file for the NESS model
my_guitar.write("ness_files_to_process/inst_2_defaultBass.m")




#________________________________________
#_____CREATE THE SCORE FILE______________

# in order to test our instrument file, we create a quick score file that will play all the strings from 1 to [stringCount]
T = 9                      # how long should the piece be (in seconds)?

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, stringCount)       

# create a variable that represents the indexes of all strings
allStrings = [a+1 for a in range(stringCount)]		# creates a list like [1, 2, 3, 4, 5, 6] - a value for each string

my_score.pluck(allStrings, 	0.2)		# pluck all six strings at time 0.2 at fret 0

my_score.playFret(allStrings, 1, 0)		# set all fingers to 0th fret
my_score.playFret(allStrings, 3, 5, 2)	# move all fingers to 5th fret over 2 seconds
		
my_score.pluck(allStrings, 	4)		# pluck all six strings at time 0.2 at fret 0

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_2_score.m")



