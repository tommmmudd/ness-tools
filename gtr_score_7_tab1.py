from nesstools import guitar

#________________________________________
# General variables
# note that we don't need to define the score duration, T, here, as that will be determined by the tab
numberOfStrings = 6         # how many strings should the guitar have?


#________________________________________
#_____CREATE THE SCORE FILE_________

# Note that because we are using tab to create the score, the initial T is arbitrary, as it will be determined later, 
# but a value for T still needs to be specified (0 in this example)
my_score = guitar.GuitarScore(0, numberOfStrings)       

# specify the tab file as a list of strings, one element for each string
# here, each string is set up as s1, s2, ... s6, where s1 is the thicker E string and s6 us the thinnest string

s6 = "|-0------0--2--3-3-----|"
s5 = "|-0-----0-------3------|"
s4 = "|-0----0---------4-----|"
s3 = "|-2---2-----------5----|"
s2 = "|-2--2-----------5-----|"
s1 = "|-0-0----------3---3---|"
# collate the strings into a list
tab = [s1, s2, s3, s4, s5, s6]

# specify the playback rate for this tab.
# where a value of 1 is 1/8 of a second per unit, 2 is 1/16 of a second per unit, 0.5 is 1/4 of a second per unit, etc
rate = 0.5

# convert the tab to score information in the my_score object, specifying the number of strings and the rate
my_score.tabToScore(tab, numberOfStrings, rate)

# explort the score as a NESS-compatible score file
my_score.write("ness_files_to_process/gtr_score_7_tab1.m")



#____________________________________________________________
# Create a score from a file input
# make sure you download this txt file first and move it to this directory:
# https://www.classtab.org/bach_js_bwv0578_fugue_in_gm_little_fugue.txt

tabFile = "tab/bach_js_bwv0578_fugue_in_gm_little_fugue.txt"

tabFile_score = guitar.GuitarScore(0, numberOfStrings)
tabFile_score.tabToScore(tabFile, numberOfStrings, 1.0)

tabFile_score.write("ness_files_to_process/gtr_score_7_tabFile.m")

#____________________________________________________________
# CREATE THE INSTRUMENT FILE

# create a string instrument object with 6 strings.
my_guitar = guitar.StringInstrument(numberOfStrings)
my_guitar.defaultGuitar() # default steel strings
my_guitar.write("ness_files_to_process/gtr_instrument_7_tab1.m")