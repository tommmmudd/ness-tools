from nesstools import guitar

numberOfStrings = 2         # how many strings should the guitar have?
T = 10                      # how long should the piece be (in seconds)?

#________________________________________
#_____CREATE THE INSTRUMENT FILE_________

# create a string instrument object with 6 strings
my_guitar = guitar.StringInstrument(numberOfStrings)

# set it up as a default steel string guitar
my_guitar.defaultGuitar()

# export the instrument as a NESS-compatible instrument file
my_guitar.write("basic_guitar.m")


#________________________________________
#_____CREATE THE SCORE FILE_________

# Create a score object, specifying the total duration (T) and the string count (numberOfStrings)
my_score = guitar.GuitarScore(T, numberOfStrings)       


#tabFile = "multiline_fugue_short.txt"
#tabFile = "single_line.txt"
s1 = "|-5-6-5-3-1-3-1-3-|"
s2 = "|-0-----7-8-6-5-3-|"
tabFile = [s1, s2]


#tabFile = "7steps"
my_score.tabToScore(tabFile, numberOfStrings, 1)
# explort the score as a NESS-compatible score file
my_score.write("example3_score.m")