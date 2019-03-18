from nesstools import guitar


#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 6 strings
my_guitar = guitar.StringInstrument(2)

# set it up as a default steel string guitar
my_guitar.defaultGuitar()

# export the instrument as a NESS-compatible instrument file
my_guitar.write("basic_guitar.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(60, 2)       

my_score.plucks.append( [] )
# explort the score as a NESS-compatible score file
my_score.write("solo_score.m")


def tabToScore(tabString):
