from nesstools import guitar

stringCount = 4

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object
my_guitar = guitar.StringInstrument(stringCount)
# set all four strings to be low E strings with the 
my_guitar.setRegularString(0, 0)
my_guitar.setRegularString(1, 0)
my_guitar.setRegularString(2, 0)
my_guitar.setRegularString(3, 0)

# Changing some of the other string properties:
# lowDecay, highDecay

# REMEMBER THAT THE highDecay MUST BE LESS THAN THE lowDecay!

# 1st string settings
my_guitar.strings[0].lowDecay = 2      # very short decay times - the string will sound muted
my_guitar.strings[0].highDecay = 1
my_guitar.strings[0].outputPos = 0.95	# pickup position is very close to the bridge

# 2nd string settings
my_guitar.strings[1].lowDecay = 5      # short decay times - the string will sound muted
my_guitar.strings[1].highDecay = 2      
my_guitar.strings[1].outputPos = 0.87   # pickup position is quite close to the bridge

# 3rd string settings
my_guitar.strings[2].lowDecay = 15      # default decay times
my_guitar.strings[2].highDecay = 5
my_guitar.strings[2].outputPos = 0.72   # pickup position is nearer 19th fret

# 4th string settings
my_guitar.strings[3].lowDecay = 70      # long decay times
my_guitar.strings[3].highDecay = 25
my_guitar.strings[3].outputPos = 0.5   # pickup position is at 12th fret!

# export the file as a format compatible instrument file for the NESS model
my_guitar.write("ness_files_to_process/inst_5_instrument.m")




#________________________________________
#_____CREATE THE SCORE FILE______________

# in order to test our instrument file, we create a quick score file that will play all the strings from 1 to [stringCount]
T = 40                      # how long should the piece be (in seconds)?

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, stringCount)       

# pluck string 1 a few times
my_score.pluck(1, 0.1)
my_score.pluck(1, 0.5)
my_score.pluck(1, 1.5)

# wait a bit, then pluck string 2 a few times
my_score.pluck(2, 4.1)
my_score.pluck(2, 4.5)
my_score.pluck(2, 5.5)

# wait a bit, then pluck string 3 a few times
my_score.pluck(3, 8.1)
my_score.pluck(3, 8.5)
my_score.pluck(3, 9.5)

# wait a bit, then pluck string 3 a few times
my_score.pluck(4, 15.1)
my_score.pluck(4, 15.5)
my_score.pluck(4, 16.5)

# export the score as a NESS-compatible score file
my_score.write("ness_files_to_process/inst_5_score.m")