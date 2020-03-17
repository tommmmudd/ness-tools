from nesstools import net1
import random as r  			# for randomising events


# general variables
stringCount = 1         # how many strings should the guitar have?
T = 3                   # how long should the piece be (in seconds)?

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 3 strings
my_inst = net1.Net1Instrument(stringCount)

# write the instrument file as a NESS-compatible text file
my_inst.write("ness_files_to_process/test_instrument.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (stringCount)
my_score = net1.Net1Score(T, stringCount)    
my_score.makeEvent(0.1)

# export the score as a NESS-compatible score file
my_score.write("ness_files_to_process/test_score.m")



