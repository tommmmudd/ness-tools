# NESS FUNCTIONS!!
from . import brass
import random as r

# fr MIDI strings
from midiutil.MidiFile import MIDIFile
import midi

# BRASS


#SCALE CREATOR
modes = [["major", "ionian"], ["dorian"], ["phygian"], ["lydian"], ["mixolydian"], ["minor", "aeolian"], ["locrian"]]
keys = { # ensure a conversion to lowercase first
        "c" : 0,
        "c#" : 1,
        "d" : 2,
        "d#" : 3,
        "e" : 4,
        "f" : 5,
        "f#" : 6,
        "g" : 7,
        "g#" : 8,
        "a" : 9,
        "a#" : 10,
        "b" : 11,
        "db" : 1,
        "eb" : 3,
        "gb" : 6,
        "ab" : 8,
        "bb" : 10
}

# Major
stringFretsEThick = [0, 2, 4, 5, 7, 9, 10, 12, 14, 16, 17, 19]
stringFretsA      = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19]
stringFretsD      = [0, 2, 4, 6, 7, 9, 11, 12, 14, 16, 18, 19]
stringFretsG      = [1, 2, 4, 6, 7, 9, 11, 13, 14, 16, 18, 19]
stringFretsB      = [0, 2, 3, 5, 7, 9, 10, 12, 14, 15, 17, 19]
stringFretsEThin  = [0, 2, 4, 6, 7, 9, 10, 12, 14, 16, 17, 19]
fretsFMinor = [stringFretsEThick, stringFretsA, stringFretsD, stringFretsG, stringFretsB, stringFretsEThin]

# Minor
stringFretsEThick = [0, 2, 3, 5, 7, 8, 10, 12, 14, 15, 17, 19]
stringFretsA      = [0, 2, 3, 5, 7, 9, 10, 12, 14, 15, 17, 19]
stringFretsD      = [0, 2, 4, 5, 7, 9, 10, 12, 14, 16, 17, 19]
stringFretsG      = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19]
stringFretsB      = [0, 1, 3, 5, 7, 8, 10, 12, 13, 15, 17, 18]
stringFretsEThin  = [0, 2, 3, 5, 7, 8, 10, 12, 13, 15, 17, 19]
fretsEMinor = [stringFretsEThick, stringFretsA, stringFretsD, stringFretsG, stringFretsB, stringFretsEThin]

# Diminished
stringFretsEThick = [2, 2, 5, 8, 11, 14, 17, 20]
stringFretsA      = [0, 3, 3, 6, 9, 12, 15, 18]
stringFretsD      = [1, 4, 4, 7, 10, 13, 16, 19]
stringFretsG      = [2, 2, 5, 8, 11, 14, 17, 20]
stringFretsB      = [1, 4, 4, 7, 10, 13, 16, 19]
stringFretsEThin  = [2, 2, 5, 8, 11, 14, 17, 20]
fretsDiminished = [stringFretsEThick, stringFretsA, stringFretsD, stringFretsG, stringFretsB, stringFretsEThin]

fretSets = [fretsEMinor, fretsFMinor, fretsDiminished]

startingFrets = [40, 45, 50, 55, 59, 64];
earthStartingFrets = [33, 40, 45, 50, 54, 59];

class StringInstrument(object):
    """String Instrument class for generating instruments for the NESS physical model

    Attributes:
        name        Optional name for your instrument written into the final file
        sr          Sample rate
        stringCount Number of strings on the instrument (integer)
        strings     a list of NessString objects, of length stringCount.
    """
    def __init__(self, stringCount=6, name="Quick Guitar Instrument"):
        self.name = name
        self.sr = 44100
        self.stringCount = stringCount
        self.strings = [NessString() for i in range(stringCount)]

        # for 12-string guitars and similar
        self.doubleStrings = False
        self.extrastringsCount = 1      # e.g. 1 extra string per string for a 12-string
        self.extrastrings = [NessString() for i in range(stringCount*self.extrastringsCount)]

        # extra fingers are used for palm muting
        self.palmmuting = False
        self.palmmuteFingerStrings = ["" for a in range(self.stringCount)]

        # initialise as defaultGuitar?
        #self.defaultGuitar()
        self.regularStrings = ["Low E"]

        # if false, these elements are ommitted in instrument file
        self.backboard = True
        self.fingers = True
        self.frets = True

        self.fretHeight = -0.001
        self.backboardParams = [-0.002, -0.000, -0.0002]    #ALL NEGATIVE OR ZERO parabola: b(x) = b0+b1*x+b2*x^2, where backboard =% [b0 b1 b2]]
        self.barrier = [1e10, 1.3, 10, 20, 1e-12]
        self.fingerMass = 0.005
        self.fingerStiffness = 1e7
        self.fingerExp = 1.6
        self.fingerLoss = 120

    def defaultGuitar(self, kind="regular"):
        """Quick function to setup the strings for a basic 6 string steel guitar"""
        for i in range(self.stringCount):
            self.setRegularString(i, i)

    def dadgadGuitar(self):
        self.stringCount = 6
        self.strings = []
        self.strings.append( NessString(0.68, 2e11, 9.5, 0.0002, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 12.3, 0.00015, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 21.9, 0.00015, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 39.2, 0.00015, 7850, 15, 7) )
        self.strings.append( NessString(0.68, 2e11, 22.6, 0.0001, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 39.2, 0.0001, 7850, 15, 8) )

    def randomGuitar(self):
        for string in self.strings:
            string.length = r.random()*1 + 0.5
            string.radius = r.random()*r.random()*0.001 + 0.0007
            string.tension = r.random()*20 + 15.0 / (string.radius * 10000)
            string.lowDecay = r.randint(9, 30)
            string.highDecay = r.randint(3, string.lowDecay-1)

    def brightGuitar(self):
        self.stringCount = 6
        self.defaultGuitar();
        for string in self.strings:
            string.lowDecay = 28
            string.highDecay = 14

    def defaultBass(self, kind="regular"):
        """Setup the strings for a basic 4 string bass guitar"""
        self.stringCount = 4
        self.strings = []
        self.strings.append( NessString(0.88, 2e11, 4.8, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 9.3, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 9.2, 0.00015, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 10.5, 0.00012, 7850, 15, 3) )

    def bass6String(self, kind="regular"):
        """Setup the strings for a 6 string bass guitar - with two higher strings"""
        self.stringCount = 6
        self.strings = []
        self.strings.append( NessString(0.88, 2e11, 4.8, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 9.3, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 9.2, 0.00015, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 10.5, 0.00012, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 10.2, 0.0001, 7850, 15, 4) )
        self.strings.append( NessString(0.88, 2e11, 13.5, 0.0001, 7850, 15, 5) )

    def defaultGuitarAndBass(self):
        """Combined guitar and bass instrument (10 strings - guitar is the first 6)"""
        self.stringCount = 10
        self.strings = ["" for i in range(6)]
        for i in range(6):
            self.setRegularString(i, i)
        self.strings.append( NessString(0.88, 2e11, 4.8, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 9.3, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 9.2, 0.00015, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 10.5, 0.00012, 7850, 15, 3) )

    def default12String(self):
        self.stringCount = 6
        self.doubleStrings = True
        self.extrastrings = []
        for i in range(self.stringCount):
            self.setRegularString(i, i)
        self.extrastrings.append ( NessString(0.34, 2e11, 10.5, 0.00012, 7850, 15, 3) )
        self.extrastrings.append ( NessString(0.34, 2e11, 12.3, 0.00015, 7850, 15, 5) )
        self.extrastrings.append ( NessString(0.34, 2e11, 21.9, 0.00015, 7850, 15, 5) )
        self.extrastrings.append ( NessString(0.34, 2e11, 39.2, 0.00015, 7850, 15, 7) )
        self.extrastrings.append ( NessString(0.34, 2e11, 27.6, 0.0001, 7850, 15, 5) )
        self.extrastrings.append ( NessString(0.34, 2e11, 49.2, 0.0001, 7850, 15, 8) )
 
    def add12String(self):
        self.doubleStrings = True
        self.extrastrings = []
        for string in self.strings:
            self.extrastrings.append ( NessString(string.length*0.5, string.ym, string.tension, string.radius, string.density, string.lowDecay, string.highDecay) )

    def addNString(self):
        self.doubleStrings = True
        self.extrastrings = []
        for i in range(self.extrastringsCount):
            for string in self.strings:
                #slightRandomisation = r.random()*0.01 + 0.495
                slightRandomisation = 1.0
                for j in range(i+1):
                    slightRandomisation *= 0.5
                self.extrastrings.append ( NessString(string.length*slightRandomisation, string.ym, string.tension, string.radius, string.density, string.lowDecay, string.highDecay) )
       

    def earthGuitarAndBass(self):
        """Lower guitar and bass instrument a la Earth (10 strings - guitar is the first 6)"""
        self.stringCount = 10
        self.strings = []
        self.strings.append( NessString(0.68, 2e11, 6.75, 0.00023, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 12.1, 0.0002, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 12.3, 0.00015, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 21.9, 0.00015, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 35.2, 0.00015, 7850, 15, 7) )
        self.strings.append( NessString(0.68, 2e11, 27.6, 0.0001, 7850, 15, 5) )
        self.strings.append( NessString(0.88, 2e11, 3.4, 0.00025, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 4.8, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 9.3, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 9.2, 0.00015, 7850, 15, 3) )


    def lowGuitar(self):
        """Setup the strings for a lower 6 string guitar"""
        self.stringCount = 6
        self.strings = []
        self.strings.append( NessString(0.88, 2e11, 3.4, 0.00025, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 4.8, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.68, 2e11, 6.75, 0.00023, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 12.1, 0.0002, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 12.3, 0.00015, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 21.9, 0.00015, 7850, 15, 5) )

    def earthGuitar(self, kind="regular"):
        """Setup the strings for a lower 6 string guitar a la Earth (A E A D F# B)"""
        self.stringCount = 6
        self.strings = []
        self.strings.append( NessString(0.68, 2e11, 6.75, 0.00023, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 12.1, 0.0002, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 12.3, 0.00015, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 21.9, 0.00015, 7850, 15, 5) )
        self.strings.append( NessString(0.68, 2e11, 35.2, 0.00015, 7850, 15, 7) )
        self.strings.append( NessString(0.68, 2e11, 27.6, 0.0001, 7850, 15, 5) )

    def randomGlassGuitar(self, kind="regular"):
        """Setup the strings for a randomly generated 6 string guitar with wide radius strings"""
        self.stringCount = 6
        self.defaultGuitar()
        for string in self.strings:
            string.length *= r.random() + 0.7
            string.tension *= r.random() + 0.5
            string.radius = r.random()*0.008

    def glassGuitarN(self, SC=6, kind="regular"):
        """Setup the strings for a randomly generated N-string guitar with wide radius strings (specify N as the first argument, default 6)"""
        self.stringCount = SC
        self.defaultGuitar()
        for string in self.strings:
            string.length *= r.random() + 0.7
            string.tension *= r.random() + 0.5
            string.radius = r.random()*0.008


    def setGlassString(self, ind):
        """Set a particular string (ind is string index) to a random length and tension and generate a random radius between 0 and 0.008 m"""
        self.strings[ind].length *= r.random() + 0.7
        self.strings[ind].tension *= r.random() + 0.5
        self.strings[ind].radius = r.random()*0.008

            
    def setRegularString(self, ind, kind=0):
        """Set a particular string (ind is string index, kind is string num on a regular guitar) to a regular guitar string"""
        if kind == "Low E" or kind==0:     self.strings[ind] = NessString()
        if kind == "Low D":                self.strings[ind] = NessString(0.68, 2e11, 9.5, 0.0002, 7850, 15, 5)
        elif kind == "A" or kind==1:       self.strings[ind] = NessString(0.68, 2e11, 12.3, 0.00015, 7850, 15, 5)
        elif kind == "D" or kind==2:       self.strings[ind] = NessString(0.68, 2e11, 21.9, 0.00015, 7850, 15, 5)
        elif kind == "G" or kind==3:       self.strings[ind] = NessString(0.68, 2e11, 39.2, 0.00015, 7850, 15, 7)
        elif kind == "B" or kind==4:       self.strings[ind] = NessString(0.68, 2e11, 27.6, 0.0001, 7850, 15, 5)
        elif kind == "High E" or kind==5:  self.strings[ind] = NessString(0.68, 2e11, 49.2, 0.0001, 7850, 15, 8)
        elif kind == "High D":             self.strings[ind] = NessString(0.68, 2e11, 39.2, 0.0001, 7850, 15, 8)
        else: self.strings[ind] = NessString(); #print ("unknown type, using Low E\n")

    def tuneString(self, s, note):
        #starting_frets = [40, 45, 50, 55, 59, 64]
        midiNote = 40
        if isinstance(note, str):
            midiNote = getMidiPitchFromString(note, s-1)
        elif (isinstance(note, int) or isinstance(note, float)):
            midiNote = note
        newTension = pow(self.strings[s-1].length * 2 * mtof(midiNote), 2) * self.strings[s-1].density * 3.141593 * self.strings[s-1].radius*self.strings[s-1].radius
        #print(newTension)
        self.strings[s-1].tension = newTension
        

    def detune(self, detuneAmount):
        """Randomly detune all the strings by up to +/- detuneAmount"""
        for string in self.strings:
            string.length += (r.random()*2*detuneAmount) - detuneAmount

    def write(self, fName):
        """Output the instrument in its current state as 'fName' for use with the NESS model"""
        print( "writing "+self.name+" as: "+fName )
        out = open(fName, "w");
        out.write('% gtversion 1.0\n\n')            # check that escaping the percentage sign works ok
        out.write("% "+self.name+"\n\n")
        out.write('SR = '+str(self.sr)+"\n\n")
        out.write("string_def = [")
        for i, string in enumerate(self.strings):
            out.write("%.4f %i %.2f %.6f %i %i %i" % (string.length, string.ym, string.tension, string.radius, string.density, string.lowDecay, string.highDecay))
            if i!=(len(self.strings)-1): out.write(";")
        if (self.doubleStrings):
            out.write(";")
            for i, string in enumerate(self.extrastrings):
                out.write("%.4f %i %.2f %.6f %i %i %i" % (string.length, string.ym, string.tension, string.radius, string.density, string.lowDecay, string.highDecay))
                if i!=(len(self.extrastrings)-1): out.write(";")
        out.write("];\n\n")
        out.write("output_def = [")
        for i, string in enumerate(self.strings):
            out.write(str(i+1)+" "+str(string.outputPos))
            if i != (len(self.strings)-1):
                out.write("; ")
        if (self.doubleStrings):
            out.write("; ")
            for i, string in enumerate(self.extrastrings):
                out.write(str(i+1+self.stringCount)+" "+str(string.outputPos))
                if i != (len(self.extrastrings)-1):
                    out.write("; ")
        out.write("];\n\n")
        out.write("normalize_outs = 1;\n\n")
        out.write("pan = [")
        for i, string in enumerate(self.strings):
            out.write(str(string.pan) + " ")
        if (self.doubleStrings):
            for i, string in enumerate(self.extrastrings):
                out.write(str(string.pan) + " ")
        out.write("];\n\n")
        out.write("barrier_params_def = [%.2f %.2f %.1f %.1f %.13f];\n\n" % (self.barrier[0], self.barrier[1], self.barrier[2], self.barrier[3], self.barrier[4] ))
        if self.backboard:
            out.write("backboard = [%.6f %.6f %.6f];\n\n" % (self.backboardParams[0], self.backboardParams[1], self.backboardParams[2]))
        if self.frets:
            out.write("frets = fret_def_gen(20, 1, %.6f);\n\n" % self.fretHeight)
        if self.fingers:
            out.write("finger_params = [%.6f %.6f %.6f %.6f];\n\n" % (self.fingerMass, self.fingerStiffness, self.fingerExp, self.fingerLoss))
        out.close()

#____________________________________________________
class NessString(object):
    """Individual string object

    Attributes:
        length      string length in metres (def. 0.68)
        ym          Young's modulus in Pa (def. 2e11)
        tension     in Newtons (def. 12.1)
        radius      string radius in metres (def. 0.0002)
        density     string density in kg/m^3 (def. 7850)
        lowDecay    T_60 at 0 Hz (def. 15)
        highDecay   T_60 at 1kHz (def. 5)
        outputPos   Point on the string where the reading is taken for the output sound from 0-1 (def. 0.89)
        pan         pan position for the NESS stereo file option (+/- 1, randomised by default)
    """
    def __init__(self, length=0.68, ym=2e11, tension=12.1, radius=0.0002, density=7850, lowDecay=15, highDecay=5):
        self.length = length        # in metres
        self.ym = ym                # young's modulus in Pa
        self.tension = tension      # tension in N
        self.radius = radius        # in metres
        self.density = density      # density in kg/m^3
        self.lowDecay = lowDecay    # T_60 at 0 Hz
        self.highDecay = highDecay  # T_60 at 1000 Hz
        self.outputPos = 0.89
        self.pan = (r.random() * 2) - 1.0


#____________________________________________________
class GuitarScore(object):
    """Score object for the guitar model

    Attributes:
        stringCount     number of strings
        T               total duration of the score in seconds
        capo            an integer that is added to all frets (like a guitar capo)
        distanceBehindFret  a constant float that determines the distance behind the fret that the
                            finger is placed, as a proportion of the total string (def. 0.0035)
        fingerStrings   an array containing a list of n strings (in the sense of char arrays), 
                        where n=stringCount, formatted for the NESS score file syntax
        plucks          a list of plucks. Each pluck is a list of five elements: 
                        [str_num, pluck_time, pluck_pos, pluck_dur, pluck_force]
                        see the makePluck() function.
        strums          a list of strums. Each strum is a list of N elements:
                        [time, strum_dur, direction, force, force_jitter, pluck_dur, pluck_dur_jitter, pos, pos_jitter, ?]
                        see the makeStrum() function.
        ...
    """
    def __init__(self, T, stringCount, pluckF=0.2):
        self.stringCount = stringCount
        self.T = T
        self.fingerStrings = ["" for a in range(self.stringCount)]
        self.fingers = True
        self.doubleStrings = False
        self.extrastringsCount = 1
        self.extraFingerStrings = ["" for a in range(self.stringCount*self.extrastringsCount)]
        self.palmmuting = False
        self.palmmuteFingerStrings = ["" for a in range(self.stringCount)]
        self.plucks = []         # initial pluck, otherwise it won't run. Could remove
        self.strums = []
        self.frets = ["" for a in range(self.stringCount)]#["0.331" for a in range(self.stringCount)]
        self.prevFrets = ["" for a in range(self.stringCount)]#["0" for a in range(self.stringCount)]
        self.pluckF = pluckF
        self.fretFingerPos = 0.75
        self.fingerHeight = 0.0
        self.distanceBehindFret = 0.0035
        self.capo = 0
        self.timingPatterns = []
        self.chordPatterns = []
        self.fretPositions = [0.0, 0.056, 0.109, 0.159, 0.206, 0.251, 0.293, 0.333, 0.370, 0.405, 0.439, 0.47, 0.5,   0.528, 0.555, 0.58, 0.603, 0.625, 0.646, 0.667, 0.685 ]
        self.harmonics = [1/2.0, 1/3.0, 1/4.0, 1/5.0, 2/5.0, 1/6.0, 1/7.0, 1/8.0, 3/8.0, 1/9.0, 2/9.0, 4/9.0, 1/10.0, 3/10.0, 1/11.0]
        self.midiOutput = MIDIStrings(stringCount, 120,  "Automatically adding MIDI file for trigger sync")
        self.addDefaultTimingPattern()
        self.addDefaultChordPattern(len(self.timingPatterns[0]))


    def addDefaultChordPattern(self, length):
        # some arbitrary chords are loaded by default
        chordA = [3, 3, 5, 5, 4, 3]
        chordB = [5, 5, 7, 7, 7, 5]
        chordC = [3, 5, 5, 3, 3, 3]
        chordD = [1, 3, 3, 2, 1, 1]
        chordE = [8, 7, 9, 7, 8, 7]
        chordF = [10, 10, 8, 7, 10, 10]#[15, 17, 17, 15, 15, 15]
        chordG = [6, 6, 8, 8, 8, 8]#[15, 15, 17, 17, 16, 15]
        chordH = [8, 10, 12, 8, 8, 10]
        chordI = [3, 10, 12, 14, 11, 10]
        chordJ = [4, 8, 7, 7, 8, 6]
        chordK = [3, 3, 1, 1, 3, 3]
        chordL = [6, 8, 8, 7, 6, 6]
        chords = [chordA, chordB, chordC, chordD, chordE, chordF, chordG, chordH, chordI, chordJ, chordK, chordL]
        chordPattern = [chords[r.randint(0, len(chords)-1)] for i in range(length)]
        self.chordPatterns.append( chordPattern )  # note that this should be an array of arrays

    def addDefaultTimingPattern(self):
        # some arbitrary chords are loaded by default
        timingPattern = [1, 0.5, 1, 0.5, 1, 0.5, 0.25, 0.25]
        self.timingPatterns.append( timingPattern )

    def getFretPos(self, fretNum):
        fretPos = self.fretPositions[fretNum]
        fretSize = fretPos - self.fretPositions[max(0, fretNum-1)]
        fingerPos = fretPos - (1-self.fretFingerPos)*fretSize
        if fingerPos < 0: fingerPos = 0
        #fingerPos = max(0, self.fretPositions[fretNum] - self.distanceBehindFret)
        return fingerPos

    def playNote(self, startTime=0, note=60, pluckF=0.05, glideTime=0.001):
        t = startTime
        onF = "10"
        s, fret = self.midiToStringFret(note)
        self.frets[s] = str( max(self.fretPositions[fret] - self.distanceBehindFret, 0) )
        if self.prevFrets[s] == "":
            self.prevFrets[s].append(self.frets[s])
        self.fingerStrings[s] += str(t-glideTime)+" "+self.prevFrets[s]+" "+onF+"; "
        self.fingerStrings[s] += str(t)+" "+self.frets[s]+" "+onF+"; "
        self.prevFrets[s] = self.frets[s]
        #self.plucks.append( self.makePluck(s+1, t+0.01, pluckF) )

    def playFret(self, strings=1, t=0, fret=0, glideTime=0.005, fingerF=2, pluck=False, pluckF=0.3):
        """move a finger on a particular string to a particular fret position at a particular time. No pluck by default. Frets specified as integers. Adds to scorefile parameter fingerStrings[s]"""
        onF = str(fingerF)
        if not isinstance(strings, list):
            strings = [strings]  # make it into a list, and 
        for s in strings:
            s = s-1
            actualPos = self.getFretPos(self.capo+fret)
            self.frets[s] = str( actualPos )
            if self.prevFrets[s] == "":
                self.prevFrets[s] = self.frets[s]
            self.fingerStrings[s] += str(t-glideTime)+" "+self.prevFrets[s]+" "+onF+"; "
            self.fingerStrings[s] += str(t)+" "+self.frets[s]+" "+onF+"; "
            if pluck:
                self.pluck(s+1, t, 0.8, 0.0005, pluckF)
            self.prevFrets[s] = self.frets[s]

    def playPosition(self, strings=1, t=0, pos=0, glideTime=0.005, fingerForce=2):
        """move a finger on a particular string to a particular position at a particular time. Adds to scorefile parameter fingerStrings[s]"""
        onF = str(fingerForce)
        if pos < 0: pos = 0
        if pos > 1.0: pos = 0.99
        if not isinstance(strings, list):
            strings = [strings]  # make it into a list, and 
        for s in strings:
            s = s-1
            self.frets[s] = str( pos )
            if self.prevFrets[s] == "":
                self.prevFrets[s] = self.frets[s]
            self.fingerStrings[s] += str(t-glideTime)+" "+self.prevFrets[s]+" "+onF+"; "
            self.fingerStrings[s] += str(t)+" "+self.frets[s]+" "+onF+"; "
            self.prevFrets[s] = self.frets[s]

    def playHarmonic(self, strings=1, t=0, pos=0, glideTime=0.01, fingerF=0.017, pluckPos=0.8, pluckF=0.3):
        """place a finger lightly at a particular position and pluck to obtain a harmonic. Adds to scorefile parameters fingerStrings[s] and plucks"""
        scaledForce = harmonicForceFromPosition(pos, fingerF)
        onF = str(scaledForce)
        if not isinstance(strings, list):
            strings = [strings]  # make it into a list, and 
        for s in strings:
            s = s-1
            self.frets[s] = str( max(pos, 0) )
            if self.prevFrets[s] == "":
                self.prevFrets[s] = self.frets[s]
            self.fingerStrings[s] += str(t-glideTime)+" "+self.prevFrets[s]+" "+onF+"; "
            self.fingerStrings[s] += str(t)+" "+self.frets[s]+" "+onF+"; "
            self.pluck(s+1, t, pluckPos, 0.0005, pluckF)
            self.prevFrets[s] = self.frets[s]
        #self.plucks.append( self.makePluck(s+1, t+0.01, pluckF) )

    def pluck(self, strings, t, pos=0.8, dur=0.001, f=0.3):
        """Add a pluck to the scorefile parameter 'plucks'"""
        if not isinstance(strings, list):
            strings = [strings]  # make it into a list, and 
        for s in strings:
            self.plucks.append( [ s, t, pos, dur, f] )

    def midiToStringFret(self, note):
        string_and_fret = [0, 0]
        while (note < startingFrets[0]):
            note += 12
        while (note > startingFrets[5]+19):
            note -= 12
        if (note < startingFrets[1]):
            string_and_fret = [0, note-startingFrets[0]]
        elif (note < startingFrets[2]):
            string_and_fret = [1, note-startingFrets[1]]
        elif (note < startingFrets[3]):
            string_and_fret = [2, note-startingFrets[2]]
        elif (note < startingFrets[4]):
            string_and_fret = [3, note-startingFrets[3]]
        elif (note < startingFrets[5]):
            string_and_fret = [4, note-startingFrets[4]]
        else:
            string_and_fret = [5, note-startingFrets[5]]
        return string_and_fret[0], string_and_fret[1]


    def gtrFromBrassScore(self, s, brassScore):
        print("gtrFromBrassScore", len(brassScore.pressure))
        self.T = brassScore.time
        pressureList = []
        pressureTimesList = []
        maxPressure = 0
        lfList = []
        lfTimesList = []
        combinedList = []
        for item in brassScore.pressure:
            pressureTimesList.append( item[0] )
            pressureList.append( item[1] )
            if (item[1] > maxPressure): maxPressure = item[1]
        for item in brassScore.lip_frequency:
            lfTimesList.append( item[0] )
            fingerPos = (item[1] / 880.0)
            if fingerPos > 0.8: fingerPos = 0.8
            lfList.append( fingerPos )



        print("Creating Guitar score from Brass", len(lfList), lfList)
        current_lf = lfList[0]
        current_lf_t = lfTimesList[0]
        current_p = 0
        for i, pItem in enumerate(brassScore.pressure):
            t = pItem[0]
            current_p = 20 * pItem[1] / float(maxPressure)
            self.fingerStrings[s] += str(t)+" "+str(current_lf)+" "+str(current_p)+"; "
            if i==(len(brassScore.pressure)-1):
                nextT = self.T
            else:
                nextT = brassScore.pressure[i+1][0]
            print("between", t, nextT)
            for lfT, lf in zip(lfTimesList, lfList):
                if lfT >= t and lfT < nextT:
                    print("found", lfT, lf)
                    self.fingerStrings[s] += str(lfT+0.002)+" "+str(lf)+" "+str(current_p)+"; "
                    current_lf = lf
                    current_lf_t = lfT
                    
            


    def write(self, fName):
        """Output the score in its current state as 'fName' for use with the NESS model"""
        print ("writing "+fName)
        # finish up the fingerStrings first!
        startFingerPos = ["0" for a in range(self.stringCount)]
        for s in range(self.stringCount):
            # arbitrary end fingering?? is that necessary?
            #self.fingerStrings[s] += str(self.T-5)+" "+self.prevFrets[s]+" "+str(1)+"], [0.01, 0];\n"
            # no end finger
            
            if self.fingerStrings[s] != "":
                # currently unused
                splitString = self.fingerStrings[s].split(" ")
                startFingerPos[s] = splitString[1]
        out = open(fName, 'w')
        out.write("Tf = "+str(self.T)+";\n\n")
        out.write("exc = [];\n\n")
        if len(self.plucks) == 0:
            print( "no plucks defined, so adding one, otherwise score will not be processed\n")
            self.pluck(1, 0.1, 0.8, 0.001, 0.001)
        for pluck in self.plucks:
            out.write("exc = pluck_gen(exc, ")
            for i, param in enumerate(pluck):
                if i != (len(pluck) - 1):
                    out.write(str(param)+", ")
                else:
                    out.write(str(param)+");\n\n")
        if self.doubleStrings:
            for pluck in self.plucks:
                out.write("exc = pluck_gen(exc, ")
                for j in range(self.extrastringsCount):
                    for i, param in enumerate(pluck):
                        if i==0:
                            out.write(str(param+self.stringCount*(j+1))+", ")
                        elif i != (len(pluck) - 1):
                            out.write(str(param)+", ")
                        else:
                            out.write(str(param)+");\n\n")
        for strum in self.strums:
            out.write("exc = strum_gen(exc, ")
            for i, param in enumerate(strum):
                if i != (len(strum) - 1):
                    out.write(str(param)+", ")
                else:
                    out.write(str(param)+");\n\n")
        if self.fingers:
            out.write("finger_def = {")
            #for i in range(stringCount):
            for i, f_string in enumerate(self.fingerStrings):
                out.write("\n    "+str(i+1)+",  [0 "+startFingerPos[s]+" 0; ")#0 "+str(self.fretPositions[5])+" 0; ")   # gotta start somewhere?? Eh?
                out.write(f_string)
                out.write("], ["+str(self.fingerHeight)+", 0];")
            if self.doubleStrings:
                for j in range(self.extrastringsCount):
                    for i, f_string in enumerate(self.fingerStrings):
                        out.write("\n    "+str(i+1+self.stringCount*(j+1))+", [ 0 "+startFingerPos[s]+" 0; ")#0 "+str(self.fretPositions[5])+" 0; ")   # gotta start somewhere?? Eh?
                        out.write(f_string)
                        out.write("], ["+str(self.fingerHeight)+", 0];")
            if self.palmmuting:
                for i, f_string in enumerate(self.palmmuteFingerStrings):
                    out.write("\n    "+str(i+1)+",  [0 "+startFingerPos[s]+" 0; ")#0 "+str(self.fretPositions[5])+" 0; ")   # gotta start somewhere?? Eh? NO: use initial finger pos
                    out.write(f_string)
                    out.write("], ["+str(self.fingerHeight)+", 0];")
            out.write("\n};")
        out.close()


    def makePluck(self, num, time, strength=1, pos=0.8, dur=0.001):
        """Generate a five element pluck list to be added to the plucks attribute"""
        str_num = num           # which string? 
        pluck_time = time   # when (seconds)
        pluck_pos = pos#round(r.random()*0.23 + 0.75, 3)        # where (0-1)
        pluck_dur = 0.001 #0.02 + r.random()*0.01#round(r.random()*0.01 + 0.001, 4) # dur of actual pluck (e.g. 0.001 - 0.01 for realistic range)
        pluck_force = strength#r.random()*0.5 + 0.1 #round(r.random()*r.random()*10 + 0.2, 3)       # force (N), e.g. 1
        return [str_num, pluck_time, pluck_pos, pluck_dur, pluck_force]



    def makeStrum(self, time, direction, strength=0.5, pos=0.8, durScale=0.005):
        """Generate a ten element pluck list to be added to the strums attribute"""
        strum_time = time   # when (seconds)
        strum_dir = direction
        strum_pos = pos     # where (0-1)
        strum_dur = r.random()*r.random()*r.random()*durScale#round(r.random()*0.01 + 0.001, 4) # dur of actual pluck (e.g. 0.001 - 0.01 for realistic range)
        pluck_dur = 0.002
        strum_force = strength#r.random()*0.2 + 0.2#r.random()*0.5 + 0.1 #round(r.random()*r.random()*10 + 0.2, 3)      # force (N), e.g. 1
        return [strum_time, strum_dur, strum_dir, strum_force, 0.02, pluck_dur, 0.0001, strum_pos, 0.05, 0.03]


    def newFret(self, counter, string, seq, fretData, fretGap=0.035, capo=0):
        fretInd = 0
        new_fret = ""
        if (string>=6):
            #loop round, but don't reinclude the first string
            fretInd = capo + seq[counter % len(seq)][((string%6)+1)%6]
        else:
            fretInd = capo + seq[counter % len(seq)][string]
        new_fret = max(0.0001, fretData[fretInd] - fretGap)
        new_fret = str(new_fret)
        return new_fret

    '''def moveFinger(self, s, fret, glissTime=0.05):
        if (s > (stringCount-1):
            s = stringCount-1
        self.frets[s]
        self.fingerStrings[s1] += str(jitters[i]+t-glideTime)+" "+self.prevFrets[s1]+" "+str(onF)+"; "
        
        #loop round, but don't reinclude the first string
        fretInd = self.capo + seq[counter % len(seq)][((string%6)+1)%6]
        self.prevFrets[s] = self.frets[s]
                    self.frets[s] = self.newFret(i, s, self.chordPatterns[0], self.fretPositions, self.distanceBehindFret, self.capo)
                    onF = str(maxF)

        new_fret = max(0.0001, fretData[fretInd] - fretGap)
        new_fret = str(new_fret)
        return new_fret'''

    def structureSeq(self, startTime, endTime, timingArray, tScale, maxF):
        jitters = []
        for s in range(self.stringCount):
            t = startTime
            pluckF = self.pluckF
            i = 0
            harm = False;
            while t < endTime:
                if (s==0):
                    jitters.append( r.random()*0.01 )
                onF = str(r.random()*maxF*0.5 + maxF*0.5)
                glideTime = 0.0035
                self.fingerStrings[s] += str(t+jitters[i]-glideTime)+" "+self.prevFrets[s]+" "+onF+"; "
                self.fingerStrings[s] += str(t+jitters[i])+" "+self.frets[s]+" "+onF+"; "
                midiFret = int(float(self.frets[s])*64)      # slides are 0-63
                self.midiOutput.addEvent(s, t, midiFret, tScale*timingArray[i%len(timingArray)])

                self.prevFrets[s] = self.frets[s]
                if harm:
                    harm = False
                    self.plucks.append( self.makePluck(s+1, t+0.01, pluckF*r.random(), r.random()*0.3 + 0.6) )
                    midiFret = int(float(self.frets[s])*64 + 64)     # plucks are 64-127
                    self.midiOutput.addEvent(s, t, midiFret, tScale*timingArray[i%len(timingArray)])  #string, time, fret (0-127), dur

                if (r.random() < 0.15):
                    self.frets[s] = str( self.harmonics[(i+s*3+r.randint(0, 6)) % len(self.harmonics)])
                    onF = str(0.002)
                    harm = True
                else:
                    self.prevFrets[s] = self.frets[s]
                    self.frets[s] = self.newFret(i, s, self.chordPatterns[0], self.fretPositions, self.distanceBehindFret, self.capo)
                    onF = str(maxF)
                    harm = False
                i+=1
                t += tScale*timingArray[i % len(timingArray)]

    def structureHarmonics(self, startTime, endTime, tScale, pluckF=0.5):
        fullRate = 0.25*tScale
        halfRate = 0.5*tScale
        rate = fullRate
        stringOrder = [i for i in range(self.stringCount)]
        r.shuffle(stringOrder)
        for s in range(self.stringCount):
            t = startTime + rate*stringOrder[s] + rate;
            #onF = ["0.04", "0.03", "0.03", "0.02", "0.01", "0.01",    "0.2", "0.1", "0.1", "0.1"]
            onF = "0.0075"
            prevHarmonic = str(self.harmonics[0])
            i = 0
            while t< endTime:
                harmonic = str( self.harmonics[r.randint(0, i%len(self.harmonics))] )
                self.fingerStrings[s] += str(t-0.005)+" "+prevHarmonic+" "+onF+"; "
                self.fingerStrings[s] += str(t)+" "+harmonic+" "+onF+"; "
                self.plucks.append( self.makePluck(s+1, t+0.01, pluckF*r.random() + 0.01, 0.9, 0.005) )
                self.fingerStrings[s] += str(t+0.015)+" "+harmonic+" 0.001; "
                prevHarmonic = harmonic
                t += (self.stringCount-1)*rate + s*rate*0.125
                if t > (endTime-startTime)*0.5 and t < 3*(endTime-startTime)/4:
                    rate = halfRate
                else:
                    rate = 0.22
                if (r.random() < 0.2):
                    i+=1

    def structureIntermittentStrum(self, startTime, endTime, timingArray, tScale, maxF, pluckF):
        t = startTime
        harm = False;
        holdFrets = [str(self.fretPositions[r.randint(0, 9)]) for a in range(self.stringCount)]
        self.frets = holdFrets
        altFrets = [str(self.fretPositions[r.randint(0, 8)]) for a in range(self.stringCount)]
        i = 0
        while t < endTime:

            glideTime = 0.0035
            onF = [str(maxF*r.random()) for a in range(self.stringCount)]
            for s in range(self.stringCount):
                self.fingerStrings[s] += str(t-glideTime)+" "+self.prevFrets[s]+" "+onF[s]+"; "
                self.fingerStrings[s] += str(t)+" "+self.frets[s]+" "+onF[s]+"; "
            
            strumDur = r.random()*0.05
            self.strums.append( self.makeStrum(t, r.randint(0, 1), pluckF, strumDur) )

            self.prevFrets = self.frets # remember these are lists of length stringCount. hopefully this does them all in one go
            if r.random() < 0.85:
                for s in range(self.stringCount):
                    self.frets[s] = holdFrets[s]
            else:
                for s in range(self.stringCount):
                    self.frets[s] = altFrets[s]

            i+=1
            t += tScale*timingArray[r.randint(0, len(timingArray)-1)]


    def structureFixed(self, startTime, endTime, timingArray, tScale, notes, maxF):
        jitters = []
        for s in range(self.stringCount):
            t = startTime
            i = 0
            skip = False
            while t < endTime:
                if (s==0):
                    jitters.append( r.random()*0.01 )

                if not skip:
                    onF = str(r.random()*maxF*0.5 + maxF*0.5)
                    glideTime = 0.0035
                    self.fingerStrings[s] += str(t+jitters[i]-glideTime)+" "+self.prevFrets[s]+" "+onF+"; "
                    self.fingerStrings[s] += str(t+jitters[i])+" "+self.frets[s]+" "+onF+"; "
                    midiFret = int(float(self.frets[s])*64)      # slides are 0-63
                    self.midiOutput.addEvent(s, t, midiFret, tScale*timingArray[i%len(timingArray)])
                    self.plucks.append( self.makePluck(s+1, t+0.01, 0.2*r.random() + 0.01, 0.9, 0.005) )
                    self.prevFrets[s] = self.frets[s]

                if skip:
                    self.fingerStrings[s] += str(t+jitters[i]-0.0035)+" "+self.prevFrets[s]+" "+onF+"; "
                    self.fingerStrings[s] += str(t+jitters[i])+" "+self.prevFrets[s]+" -0.01; "
                
                fretNum = notes[s][i % len(notes[s])]
                if fretNum == -1:
                    skip = True
                else:
                    tempFret = self.fretPositions[ self.capo + fretNum]
                    tempFret = str(tempFret - self.distanceBehindFret)
                    onF = str(maxF)
                    skip = False
   
                i+=1
                t += tScale*timingArray[i % len(timingArray)]

    def structureFixed2(self, startTime, endTime, timingArray, tScale, notes, maxF):
        jitters = []
        for s in range(self.stringCount):
            t = startTime
            i = 0
            skip = False
            while t < endTime:
                if (s==0):
                    jitters.append( r.random()*0.01 )

                if not skip:
                    onF = str(r.random()*maxF*0.5 + maxF*0.5)
                    glideTime = 0.0035
                    self.fingerStrings[s] += str(t+jitters[i]-glideTime)+" "+self.prevFrets[s]+" "+onF+"; "
                    self.fingerStrings[s] += str(t+jitters[i])+" "+self.frets[s]+" "+onF+"; "
                    midiFret = int(float(self.frets[s])*64)      # slides are 0-63
                    self.midiOutput.addEvent(s, t, midiFret, tScale*timingArray[i%len(timingArray)])
                    self.plucks.append( self.makePluck(s+1, t+0.01, 0.2*r.random() + 0.01, 0.9, 0.005) )
                    self.prevFrets[s] = self.frets[s]

                if skip:
                    self.fingerStrings[s] += str(t+jitters[i]-0.0035)+" "+self.prevFrets[s]+" "+onF+"; "
                    self.fingerStrings[s] += str(t+jitters[i])+" "+self.prevFrets[s]+" -0.01; "
                
                fretNum = notes[s][i % len(notes[s])]
                if fretNum == -1:
                    skip = True
                else:
                    tempFret = self.fretPositions[ self.capo + fretNum]
                    tempFret = str(tempFret - self.distanceBehindFret)
                    self.frets[s] = tempFret
                    onF = str(maxF)
                    skip = False
   
                i+=1
                t += tScale*timingArray[i % len(timingArray)]

    def structureSolo(self, startTime, endTime, timingArray, tScale, maxF, stringFrets=fretsEMinor):
        t = startTime
        timingScale = 1
        stringFrets = fretsEMinor
        maxFret = len(stringFrets[0])-1
        jitters = []
        onF = maxF
        x = r.randint(0, maxFret)
        s = r.randint(0, self.stringCount-1)
        i=0

        while t < endTime:
            if r.random() < 0.1:
                timingScale = r.randint(1, 3) * 1.25

            #if r.random() < 0.15:
                #self.strums.append( self.makeStrum(t+0.01, r.randint(0, 1), 0.15, 0.8, r.random()*0.05) )

            if r.random() < 0.05:
                stringFrets = fretsDiminished
                maxFret = len(stringFrets[0])-1
            if r.random() < 0.1:
                stringFrets = fretsEMinor
            if r.random() < 0.076:
                stringFrets = fretsFMinor

            x = self.walk(x, maxFret)
            if (r.random() < 0.75):
                #if (i >0):
                    # ATTEMPT TO STOP PREVIOUS STRING!
                    #fingerStrings[s] += str(t-0.005)+" "+prevFrets[s]+" "+str(onF)+"; "
                    #fingerStrings[s] += str(t)+" "+prevFrets[s]+" "+str(muteF)+"; "
                # THEN SELECT NEW STRING
                s = self.walk(s, self.stringCount-1) 
                # Set the finger to force 0? 

            jitters.append( r.random()*0.01 )

            glideTime = r.random()*r.random()*r.random()*r.random()*r.random()*r.random()*0.2 #+ i*0.01
            glideTime = min(glideTime, (tScale*timingArray[i%len(timingArray)] + s*0.2) - 0.1)
            self.fingerStrings[s] += str(jitters[i]+t-glideTime)+" "+self.prevFrets[s]+" "+str(onF)+"; "
            self.fingerStrings[s] += str(jitters[i]+t)+" "+self.frets[s]+" "+str(onF)+"; "
            if (self.frets[s] != self.prevFrets[s]):
                midiFret = int(float(self.frets[s])*64)      # slides are 0-63 (plucks are 64-127)
                self.midiOutput.addEvent(s, t, midiFret, tScale*timingArray[i%len(timingArray)]) # final is duration - a bit arbitrary?
            self.prevFrets[s] = self.frets[s]
            fretIndex = stringFrets[s%6][x]
            self.frets[s] = str(max(0.0001, self.fretPositions[fretIndex] - self.distanceBehindFret))

            onF += r.randint(-1, 1)*0.05
            if onF < 1: onF = 1
            if onF > 5: onF = 5

            t += timingArray[r.randint(0, len(timingArray)-1)]*tScale
            i += 1

    def structureSoloDouble(self, startTime, endTime, timingArray, tScale, maxF):
        t = startTime
        timingScale = 1
        stringFrets = fretsEMinor
        maxFret = len(stringFrets[0])-1
        jitters = []
        onF = maxF
        x1 = r.randint(0, maxFret)
        x2 = r.randint(0, maxFret)
        s1 = r.randint(0, self.stringCount-1)
        s2 = r.randint(0, self.stringCount-1)
        i=0

        while t < endTime:
            if r.random() < 0.1:
                timingScale = r.randint(1, 3) * 1.25

            #if r.random() < 0.15:
                #self.strums.append( self.makeStrum(t+0.01, r.randint(0, 1), 0.15, 0.8, r.random()*0.05) )

            if r.random() < 0.05:
                stringFrets = fretsDiminished
                maxFret = len(stringFrets[0])-1
            if r.random() < 0.1:
                stringFrets = fretsEMinor
            if r.random() < 0.076:
                stringFrets = fretsFMinor

            x1 = self.walk(x1, maxFret)
            x2 = self.walk(x2, maxFret)
            if (r.random() < 0.75):
                s1 = self.walk(s1, self.stringCount-1) 
            if (r.random() < 0.75):
                s2 = self.walk(s2, self.stringCount-1) 

            jitters.append( r.random()*0.01 )

            glideTime = r.random()*r.random()*r.random()*r.random()*r.random()*r.random()*0.2 #+ i*0.01
            glideTime = min(glideTime, (tScale*timingArray[i%len(timingArray)] + s1*0.2) - 0.1)
            self.fingerStrings[s1] += str(jitters[i]+t-glideTime)+" "+self.prevFrets[s1]+" "+str(onF)+"; "
            self.fingerStrings[s1] += str(jitters[i]+t)+" "+self.frets[s1]+" "+str(onF)+"; "
            self.prevFrets[s1] = self.frets[s1]
            fretIndex = stringFrets[s1%6][x1]
            self.frets[s1] = str(max(0.0001, self.fretPositions[fretIndex] - self.distanceBehindFret))

            self.fingerStrings[s2] += str(jitters[i]+t-glideTime)+" "+self.prevFrets[s2]+" "+str(onF)+"; "
            self.fingerStrings[s2] += str(jitters[i]+t)+" "+self.frets[s2]+" "+str(onF)+"; "
            self.prevFrets[s2] = self.frets[s2]
            fretIndex = stringFrets[s2%6][x2]
            self.frets[s2] = str(max(0.0001, self.fretPositions[fretIndex] - self.distanceBehindFret))

            onF += r.randint(-1, 1)*0.05
            if onF < 1: onF = 1
            if onF > 5: onF = 5

            t += timingArray[r.randint(0, len(timingArray)-1)]*tScale
            i += 1


    def structureSoloPatterns(self, startTime, endTime, timingArray, tScale, maxF):
        ''' TO DO: not just arbitrary noodling, but a set sequence'''
        t = startTime
        timingScale = 1
        stringFrets = fretsEMinor
        maxFret = len(stringFrets[0])-1
        jitters = []
        onF = maxF
        x = r.randint(0, maxFret)
        s = r.randint(0, self.stringCount-1)
        i=0

        while t < endTime:
            if r.random() < 0.1:
                timingScale = r.randint(1, 3) * 1.25

            #if r.random() < 0.15:
                #self.strums.append( self.makeStrum(t+0.01, r.randint(0, 1), 0.15, 0.8, r.random()*0.05) )

            if r.random() < 0.05:
                stringFrets = fretsDiminished
                maxFret = len(stringFrets[0])-1
            if r.random() < 0.1:
                stringFrets = fretsEMinor
            if r.random() < 0.076:
                stringFrets = fretsFMinor

            x = self.walk(x, maxFret)
            if (r.random() < 0.75):
                #if (i >0):
                    # ATTEMPT TO STOP PREVIOUS STRING!
                    #fingerStrings[s] += str(t-0.005)+" "+prevFrets[s]+" "+str(onF)+"; "
                    #fingerStrings[s] += str(t)+" "+prevFrets[s]+" "+str(muteF)+"; "
                # THEN SELECT NEW STRING
                s = self.walk(s, self.stringCount-1) 
                # Set the finger to force 0? 

            jitters.append( r.random()*0.01 )

            glideTime = r.random()*r.random()*r.random()*r.random()*r.random()*r.random()*0.2 #+ i*0.01
            glideTime = min(glideTime, (tScale*timingArray[i%len(timingArray)] + s*0.2) - 0.1)
            self.fingerStrings[s] += str(jitters[i]+t-glideTime)+" "+self.prevFrets[s]+" "+str(onF)+"; "
            self.fingerStrings[s] += str(jitters[i]+t)+" "+self.frets[s]+" "+str(onF)+"; "
            self.prevFrets[s] = self.frets[s]
            fretIndex = stringFrets[s%6][x]
            self.frets[s] = str(max(0.0001, self.fretPositions[fretIndex] - self.distanceBehindFret))

            onF += r.randint(-1, 1)*0.05
            if onF < 1: onF = 1
            if onF > 5: onF = 5

            t += timingArray[r.randint(0, len(timingArray)-1)]*tScale
            i += 1

    def structureBlock(self, startTime, endTime, tScale, maxF):
        seqLength = r.randint(4, 24)
        notes = [[fretsFMinor[s%6][r.randint(0, 5)] for i in range(seqLength)] for s in range(self.stringCount)]
        timeSet = [0.25, 0.25, 0.25, 0.75, 0.125, 0.125, 1, 0.5, 0.5, 0.5]
        forceArray = [[str(r.random()+0.01) for i in range(seqLength)] for s in range(self.stringCount)]
        timingArray = [timeSet[r.randint(0, len(timeSet)-1)] for i in range(seqLength)]
        for s in range(len(notes)):
            for i in range(len(notes[s])):
                if r.random() < 0.7:
                    notes[s][i] = -1

        jitters = []
        for s in range(self.stringCount):
            t = startTime
            i = 0
            skip = False
            while t < endTime:
                if (s==0):
                    jitters.append( r.random()*0.01 )

                if not skip:
                    #onF = str(r.random()*maxF*0.5 + maxF*0.5)
                    glideTime = 0.0035
                    self.fingerStrings[s] += str(t+jitters[i]-glideTime)+" "+self.prevFrets[s]+" "+forceArray[s][i%seqLength]+"; "
                    self.fingerStrings[s] += str(t+jitters[i])+" "+self.frets[s]+" "+forceArray[s][i%seqLength]+"; "
                    midiFret = int(float(self.frets[s])*64)      # slides are 0-63
                    self.midiOutput.addEvent(s, t, midiFret, tScale*timingArray[i%len(timingArray)])

                    self.prevFrets[s] = self.frets[s]

                if skip:
                    self.fingerStrings[s] += str(t+jitters[i]-0.0035)+" "+self.prevFrets[s]+" "+forceArray[s][i%seqLength]+"; "
                    self.fingerStrings[s] += str(t+jitters[i])+" "+self.prevFrets[s]+" 0.01; "
                
                fretNum = notes[s][i % len(notes[s])]
                if fretNum == -1:
                    skip = True
                else:
                    tempFret = self.fretPositions[ self.capo + fretNum]
                    tempFret = str(tempFret - self.distanceBehindFret)
                    onF = str(maxF)
                    skip = False
   
                i+=1
                t += tScale*timingArray[i % len(timingArray)]

    def structureBlockExternal(self, startTime, endTime, notes, timingArray, forceArray, tScale, maxF):
        seqLength = len(timingArray)
        r.randint(4, 24)
        for s in range(len(notes)):
            for i in range(len(notes[s])):
                if r.random() < 0.7:
                    notes[s][i] = -1

        jitters = []
        for s in range(self.stringCount):
            t = startTime
            i = 0
            skip = False
            while t < endTime:
                if (s==0):
                    jitters.append( r.random()*0.01 )

                if not skip:
                    #onF = str(r.random()*maxF*0.5 + maxF*0.5)
                    glideTime = 0.0035
                    self.fingerStrings[s] += str(t+jitters[i]-glideTime)+" "+self.prevFrets[s]+" "+forceArray[s][i%seqLength]+"; "
                    self.fingerStrings[s] += str(t+jitters[i])+" "+self.frets[s]+" "+forceArray[s][i%seqLength]+"; "
                    midiFret = int(float(self.frets[s])*64)      # slides are 0-63
                    self.midiOutput.addEvent(s, t, midiFret, tScale*timingArray[i%len(timingArray)])

                    self.prevFrets[s] = self.frets[s]

                #if skip:
                    #newFret = str(float(self.prevFrets[s])+0.1)
                    #self.fingerStrings[s] += str(t+jitters[i]-0.0035)+" "+newFret+" "+forceArray[s][i%seqLength]+"; "
                    #self.fingerStrings[s] += str(t+jitters[i])+" "+newFret+" 0.5; "
                
                fretNum = notes[s][i % len(notes[s])]
                if fretNum == -1:
                    skip = True
                else:
                    tempFret = self.fretPositions[ self.capo + fretNum]
                    tempFret = str(tempFret - self.distanceBehindFret)
                    self.frets[s] = tempFret
                    onF = str(maxF)
                    skip = False
   
                i+=1
                t += tScale*timingArray[i % len(timingArray)]


    def structureStagger(self, startTime, endTime, tScale, notes, maxF):
        jitters = []
        seqLength = r.randint(4, 24)
        notes = [[fretsFMinor[s][r.randint(0, 6)] for i in range(seqLength)] for s in range(self.stringCount)]
        timeSet = [0.25, 0.25, 0.25, 0.75, 0.125, 0.125, 1, 0.5, 0.5, 0.5]
        forceArray = [[str(r.random()+0.01) for i in range(seqLength)] for s in range(self.stringCount)]
        timingArray = [timeSet[r.randint(0, len(timeSet)-1)] for i in range(seqLength)]
        for s in range(len(notes)):
            for i in range(len(notes[s])):
                if r.random() < 0.7:
                    notes[s][i] = -1
        for s in range(self.stringCount):
            t = startTime
            i = 0
            skip = False
            while t < endTime:
                if (s==0):
                    jitters.append( r.random()*0.01 )

                if not skip:
                    onF = str(r.random()*maxF*0.5 + maxF*0.5)
                    glideTime = 0.0035
                    self.fingerStrings[s] += str(t+jitters[i]-glideTime)+" "+self.prevFrets[s]+" "+onF+"; "
                    self.fingerStrings[s] += str(t+jitters[i])+" "+self.frets[s]+" "+onF+"; "
                    midiFret = int(float(self.frets[s])*64)      # slides are 0-63
                    self.midiOutput.addEvent(s, t, midiFret, tScale*timingArray[i%len(timingArray)])

                    self.prevFrets[s] = self.frets[s]

                if skip:
                    self.fingerStrings[s] += str(t+jitters[i]-0.0035)+" "+self.prevFrets[s]+" "+onF+"; "
                    self.fingerStrings[s] += str(t+jitters[i])+" "+self.prevFrets[s]+" -0.01; "
                
                fretNum = notes[s][i % len(notes[s])]
                if fretNum == -1:
                    skip = True
                else:
                    tempFret = self.fretPositions[ self.capo + fretNum]
                    tempFret = str(tempFret - self.distanceBehindFret)
                    onF = str(maxF)
                    skip = False
   
                i+=1
                t += tScale*timingArray[i % len(timingArray)]

    def structureTwoChordPicking(self, startTime, endTime):

        # oscillate between first two chords in self.chordPatterns
        # slowly accelerate
        # finger picking-like string selectino (moving thumb)
        t = startTime
        tScale = 4
        stringOrder = [[0, 5], [2], [4], [1], [5],  [2], [4], [0, 5], [2, 3], [4], [0], [5],  [2], [3]]
        timingOrder = [1, 0.667, 0.333, 0.667, 0.333, 0.667, 0.333]
        stringOrder2 = [[0], [5], [4], [2], [5], [0], [5],  [2], [5], [0, 4], [2, 4], [5], [1], [5],  [3], [3]]
        timingOrder2 = [0.333, 0.334, 0.333, 0.665, 0.343, 0.667, 0.333, 0.667, 0.333]
        stringOrder3 = [[0, 4, 5], [3, 5], [4],   [1, 2], [5],   [4],  [0],   [5],    [0],  [0, 4], [4], [3], [2],   [0],    [5],   [1],   [4, 3], [0],   [4],  [2],   [5]]
        timingOrder3 = [0.333,     0.334,  0.333, 0.333,  0.343, 0.324, 0.667, 0.333, 0.667, 0.233, 0.05, 0.05, 0.05, 0.617, 0.333,  0.667, 0.333, 0.667, 0.333, 0.667, 0.333 ]
        whichChord = [0 for i in range(self.stringCount)]

        oldTimes = [0 for i in range(self.stringCount)]
        localGlideTime = 0.0035

        jitters = []
        onF = "1"
        chordMax = 2
        decayRate = 0.9975
        decayRateSlow = 0.9987
        self.capo = 1
        self.distanceBehindFret = 0.01
        onForce = 0
        changeSet = 0
        chordSet = 0

        i = 0
        while t < endTime:
            if t < endTime/3:
                onForce = 20*3 *t/float(endTime)
            elif t < 2*endTime/3:
                onForce = 20 - (20*t/float(endTime))
            elif t < 3*endTime/4:
                onForce = 4*3 * t/float(endTime)
            onF = str(onForce)
            if (r.random() < 0.005):
                chordMax = r.randint(2, len(self.chordPatterns[0])-2)
            if t < endTime/6:
                tScale = 4
            if t > endTime/6:
                chordMax = 4
            if t > endTime/5:
                chordMax = 2
            if t > endTime/4.7:
                chordMax = 5;
            if t > endTime/4.3:
                chordMax = 3;
            if t > endTime/4:
                chordMax = 3
            if t > endTime/2:
                chordMax = 4;
                chordSet = 1
            if t > endTime/1.5:
                chordMax = 4;
                chordSet = 0
            if t > endTime/1.25:
                chordMax = 6;
                chordSet = 2;
                
            if t > endTime/2:
                stringOrder = stringOrder2
                timingOrder = timingOrder2
            if t> 2*endTime/3:
                stringOrder = stringOrder3
                timingOrder = timingOrder3
            
            jitters.append( r.random()*0.01 )
            for s in stringOrder[i%len(stringOrder)]:
                fretNum = self.chordPatterns[chordSet][whichChord[s]][s]
                fretPos = self.fretPositions[ self.capo + fretNum]
                self.frets[s] = str(fretPos - self.distanceBehindFret)

                if r.random() < 0.05:
                    localGlideTime = 0.4*r.random()*r.random()*((t+jitters[i]) - oldTimes[s])
                    if localGlideTime < 0.0035: localGlideTime = 0.0035
                else:
                    localGlideTime = 0.0035

                if (self.frets[s] == self.prevFrets[s]):
                    fretNum = self.chordPatterns[chordSet][whichChord[s]+r.randint(2, 3)][s]
                    fretPos = self.fretPositions[ self.capo + fretNum]
                    self.frets[s] = str(fretPos - self.distanceBehindFret)
                self.fingerStrings[s] += str(t+jitters[i]-localGlideTime)+" "+self.prevFrets[s]+" "+onF+"; "
                self.fingerStrings[s] += str(t+jitters[i])+" "+self.frets[s]+" "+onF+"; "
                whichChord[s] = (whichChord[s] + 1) % chordMax
                self.prevFrets[s] = self.frets[s]

            if (t < endTime/1.5):
                if tScale < 0.5:
                    tScale *= decayRateSlow
                else:
                    tScale *= decayRate;
            else:
                tScale /= decayRateSlow
            if tScale < 0.03: tScale = 0.03;
            t += timingOrder[i%len(timingOrder)] * tScale * 0.25
            i += 1


    def structureMichele(self, startTime, endTime):

        # oscillate between first two chords in self.chordPatterns
        # slowly accelerate
        # finger picking-like string selectino (moving thumb)
        t = startTime
        tScale = r.random()*4 + 0.1

        # create melodic chord patterns in Gm / G dorian
        chordA = [3, 3, 5, 5, 4, 3]
        chordB = [5, 5, 7, 7, 6, 5]
        chordC = [3, 5, 5, 3, 3, 3]
        chordD = [1, 3, 3, 2, 1, 1]
        chordE = [4, 6, 6, 5, 4, 4]
        chordF = [6, 8, 8, 7, 6, 6]
        chords1 = [chordA, chordB, chordC, chordD]
        chords2 = [chordE, chordF, chordD]
        self.chordPatterns = []
        for a in range(5):
            if a==0:
                self.chordPatterns.append( [chords1[r.randint(0, len(chords1)-1)] for i in range(r.randint(2,4))] )   # note that this should be an array of arrays
            elif a==1:
                self.chordPatterns.append( [chords2[r.randint(0, len(chords2)-1)] for i in range(r.randint(2,4))] )   # note that this should be an array of arrays
            else:
                self.chordPatterns.append( [chords1[r.randint(0, len(chords1)-1)] for i in range(r.randint(2,4))] )   # note that this should be an array of arrays

        stringOrder1 = [[0, 5], [2], [4], [1], [5],  [2], [4], [0, 5], [2, 3], [4], [0], [5],  [2], [3]]
        timingOrder1 = [1, 0.667, 0.333, 0.667, 0.333, 0.667, 0.333]
        stringOrder2 = [[0], [5], [4], [2], [5], [0], [5],  [2], [5], [0, 4], [2, 4], [5], [1], [5],  [3], [3]]
        timingOrder2 = [0.333, 0.334, 0.333, 0.665, 0.343, 0.667, 0.333, 0.667, 0.333]
        stringOrder3 = [[0, 4, 5], [3, 5], [4],   [1, 2], [5],   [4],  [0],   [5],    [0],  [0, 4], [4], [3], [2],   [0],    [5],   [1],   [4, 3], [0],   [4],  [2],   [5]]
        timingOrder3 = [0.333,     0.334,  0.333, 0.333,  0.343, 0.324, 0.667, 0.333, 0.667, 0.233, 0.05, 0.05, 0.05, 0.617, 0.333,  0.667, 0.333, 0.667, 0.333, 0.667, 0.333 ]
        stringOrder4 = [[0, 4], [2, 3], [0],   [5],   [0, 3]]
        timingOrder4 = [1,      1,      0.667, 0.333, 1]
        stringOrder5 = [[0], [5],   [1], [4], [1],  [5],  [2],  [4], [0, 5], [2, 3]]
        timingOrder5 = [0.55, 0.45, 0.5, 0.5, 0.51, 0.49, 0.25, 0.25, 0.25, 0.25]
        stringOrder6 = [[3],    [4],   [5],   [0],   [5],     [0],   [5],  [0],  [5],    [2],[3],[4],   [2],[4],  [2],[4],  [1],[3]]
        timingOrder6 = [0.1665, 0.1665, 0.167, 0.333, 0.167, 0.333, 0.167, 0.333, 0.167]
        stringOrder7 = [[3, 5], [4],  [5],  [4], [5], [0],   [4],  [5]]
        timingOrder7 = [0.25, 0.25, 0.24, 0.26, 0.51, 0.24, 0.25, 0.125, 0.875]
        stringOrder8 = [[0],  [5],  [4],  [3],   [2],   [1],  [0], [2, 6], [3, 4], [3, 4]]
        timingOrder8 = [0.05, 0.03, 0.055, 0.065, 0.04, 0.05, 0.7, 0.667, 0.667, 0.666]
        timingOrders = [timingOrder1,  timingOrder2, timingOrder3, timingOrder4, timingOrder5, timingOrder6, timingOrder7, timingOrder8]
        stringOrders = [stringOrder1,  stringOrder2, stringOrder3, stringOrder4, stringOrder5, stringOrder6, stringOrder7, stringOrder8]
        tempoScales = [1, 2, 1, 3, 5, 2, 3, 4, 1, 3, 5, 3, 6, 2, 3, 4, 2, 3, 4]
        eventCount = 8
        eventIndexes = [r.randint(0, len(timingOrders)-1) for i in range(eventCount)]
        eventTimes = [i/float(eventCount) for i in range(eventCount)]
        eventTimes.sort()
        whichChord = [0 for i in range(self.stringCount)]

        oldTimes = [0 for i in range(self.stringCount)]
        localGlideTime = 0.0035

        jitters = []
        onF = "1"
        chordMax = 2
        decayRate = 0.9995
        decayRateSlow = 0.99995
        self.capo = 1
        self.distanceBehindFret = 0.01
        onForce = 0
        changeSet = 0
        chordSet = 0

        stringOrder = stringOrder4
        timingOrder = timingOrder4
        newSectionFlag = True
        currentSection = 0
        self.distanceBehindFret = 0

        i = 0
        while t < endTime:
            if t < endTime/3:
                onForce = r.random()*5 + 0.5     #20*3 *t/float(endTime)
            elif t < 2*endTime/3:
                onForce = r.random()*5 + 0.5
            elif t < 3*endTime/4:
                onForce = r.random()*5 + 0.5     #4*3 * t/float(endTime)
            else:
                onForce = r.random()*5 + 0.5
                self.distanceBehindFret = 0
            onF = str(onForce)

            for e in range(eventCount):
                if t > endTime*eventTimes[e]:
                    timingOrder = timingOrders[eventIndexes[e]]
                    stringOrder = stringOrders[eventIndexes[e]]
                    if e > currentSection:
                        tScale = r.random()*4 + 1
                        currentSection = e
                        print (tScale)

            #print (eventTimes, eventIndexes)
            #print (t, stringOrder)
            if t > endTime*0.5:
                #capo = 2
                chordSet = 0
            if t > endTime*0.7:
                chordSet = 1
            if t > endTime*0.85:
                chordSet = 2
            # if t < endTime*0.1:
            #     tScale = 4
            #     chordMax = 4
            #     chordSet = 0
            # elif t < endTime*0.2:
            #     tScale = 3
            #     chordSet = 1
            #     stringOrder = stringOrder1
            #     timingOrder = timingOrder1
            # elif t < endTime*0.3:
            #     tScale = 3
            #     chordMax = 3
            #     chordSet = 0
            #     stringOrder = stringOrder4
            #     timingOrder = timingOrder4
            # elif t < endTime*0.4:
            #     chordMax = 2
            #     chordSet = 1
            #     stringOrder = stringOrder1
            #     timingOrder = timingOrder1
            # elif t < endTime*0.5:
            #     tScale = 2
            #     chordSet = 2
            #     stringOrder = stringOrder2
            #     timingOrder = timingOrder2
            # elif t < endTime*0.65:
            #     chordSet = 1
            #     chordMax = 3
            #     stringOrder = stringOrder1
            #     timingOrder = timingOrder1
            # elif t < endTime*0.75:
            #     self.capo = 2
            #     chordSet = 0
            #     chordMax = 4
            #     stringOrder = stringOrder3
            #     timingOrder = timingOrder3
            # elif t < endTime*0.85:
            #     tScale = 2
            #     chordSet = 2

            jitters.append( r.random()*0.01 )
            for s in stringOrder[i%len(stringOrder)]:
                onF = str(r.random() * 0.04)
                chord = whichChord[s] % len(self.chordPatterns[chordSet])
                fretNum = self.chordPatterns[chordSet][chord][s]
                fretPos = self.harmonics[fretNum]
                self.frets[s] = str(fretPos - self.distanceBehindFret)

                if r.random() < 0.05:
                    localGlideTime = 0.4*r.random()*r.random()*((t+jitters[i]) - oldTimes[s])
                    if localGlideTime < 0.0035: localGlideTime = 0.0035
                else:
                    localGlideTime = 0.0035

                if (self.frets[s] == self.prevFrets[s]):
                    chord = (whichChord[s] + r.randint(0, 2)) % len(self.chordPatterns[chordSet])
                    fretNum = self.chordPatterns[chordSet][chord][s]
                    #fretPos = self.fretPositions[ self.capo + fretNum]
                    fretPos = self.harmonics[fretNum]
                    self.frets[s] = str(fretPos - self.distanceBehindFret)
                self.fingerStrings[s] += str(t+jitters[i]-localGlideTime)+" "+self.prevFrets[s]+" "+onF+"; "
                self.fingerStrings[s] += str(t+jitters[i])+" "+self.frets[s]+" "+onF+"; "
                self.plucks.append( [s+1, t+jitters[i]+0.0005, 0.8+r.random()*0.1, 0.00001, r.random()*0.02 + 0.0125] )
                whichChord[s] = (whichChord[s] + 1) % chordMax
                self.prevFrets[s] = self.frets[s]

            if (t < endTime/1.5):
                if tScale < 0.5:
                    tScale *= decayRateSlow
                else:
                    tScale *= decayRate;
            else:
                tScale /= decayRateSlow
            if tScale < 0.03: tScale = 0.03;
            t += timingOrder[i%len(timingOrder)] * tScale * 0.25
            i += 1

    def strumTest(self, startTime, endTime):
        t = startTime
        T = endTime
        #strumRhythm = [1, 1, 1, 0.55, 0.45]
        strumRhythm = [3, 0.55, 0.45, 2, 1.5, 0.43]
        upDownPattern =     [0, 0,    0,    0, 0,   1]
        tScale = 1#0.45
        # % parameters are:
        # %   start time of strum (s)
        # %   duration of strum (s)
        # %   strum up (0) or down (1)
        # %   amplitude (N)
        # %   random amplitude variation factor (0-1)
        # %   pluck duration (s)
        # %   pluck duration variation factor (0-1)
        # %   pluck position (0-1)
        # %   pluck position random factor (0-1)
        # %   time randomization factor (0-1)

        one = [0, 2, 2, 1, 0, 0]
        two = [3, 2, 0, 0, 0, 3]
        three = [5, 0, 0, 2, 3, 2]
        four = [5, 0, 2, 2, 1, 0]
        five = [7, 9, 9, 7, 7, 7]
        chords = [one, two, three, five, one, two, four, five, one, two, three, three]
        i = 0
        glideTime = 0.01
        onF = "0.8"
        while t < T:
            chordNum = i % len(chords)
            self.strums.append( [t, r.random()*0.2 + 0.15, upDownPattern[i%len(upDownPattern)], strumRhythm[i%len(strumRhythm)], 0.1, 0.0001*t/float(T), 0, 0.73, 0.26, 0.005] )
            #self.plucks.append( [s+1, t+jitters[i]+0.0005, 0.8+r.random()*0.1, 0.00001, r.random()*0.02 + 0.0125] )
            for s in range(self.stringCount):
                #chordNum = i % min(6, len(self.chordPatterns[1]))
                
                if t < T/2:
                    fretNum = chords[chordNum][s]
                    fretPos = self.fretPositions[ self.capo + fretNum ]  - self.distanceBehindFret
                    if fretPos < 0.001: fretPos = 0.001
                else:
                    fretNum = chords[chordNum][s]
                    fretPos = self.fretPositions[ self.capo + fretNum ]  - self.distanceBehindFret
                    if fretPos < 0.001: fretPos = 0.001
                self.frets[s] = str(fretPos)
                self.fingerStrings[s] += str(t-glideTime)+" "+self.prevFrets[s]+" "+onF+"; "
                self.fingerStrings[s] += str(t)+" "+self.frets[s]+" "+onF+"; "
                self.prevFrets[s] = self.frets[s]
            if (r.random() < 0.35):
                self.plucks.append( [r.randint(3, 5), t+(strumRhythm[i%len(strumRhythm)]*0.5*tScale), 0.7+r.random()*0.1, 0.0001, r.random()*4] )
            t += strumRhythm[i%len(strumRhythm)] * tScale
            i += 1
            tScale *= r.random()*0.05 + 0.975


    def rapidPicking(self, startTime, endTime):

        # oscillate between first two chords in self.chordPatterns
        # slowly accelerate
        # finger picking-like string selectino (moving thumb)
        t = startTime
        tScale = 0.1
        maxRate = 0.02
        stringOrder = [[0, 5], [2], [4], [1], [5],  [2], [4], [0, 5], [2, 3], [4], [0], [5],  [2], [3]]
        timingOrder = [1, 0.667, 0.333, 0.667, 0.333, 0.667, 0.333]
        whichChord = [0 for i in range(self.stringCount)]
        oldTimes = [0 for i in range(self.stringCount)]
        jitters = []
        onF = "1"
        chordMax = 3
        decayRate = 0.9945
        decayRateSlow = 0.9975
        chordSet = 0
        newSetFlag = True
        localGlideTime = 0.0035


        i = 0
        while t < endTime:
            chordSetIndex = int(len(self.chordPatterns)*t/float(endTime))
            #chordSet = self.chordPatterns[]
            jitters.append( r.random()*0.01 )
            for s in stringOrder[i%len(stringOrder)]:
                fretNum = self.chordPatterns[chordSetIndex][whichChord[s]][s]
                fretPos = self.fretPositions[ self.capo + fretNum]
                self.frets[s] = str(fretPos - self.distanceBehindFret)

                if r.random() < 0.2:
                    localGlideTime = 0.9*r.random()*((t+jitters[i]) - oldTimes[s])
                else:
                    localGlideTime = 0.0035
                self.fingerStrings[s] += str(t+jitters[i]-localGlideTime)+" "+self.prevFrets[s]+" "+onF+"; "
                self.fingerStrings[s] += str(t+jitters[i])+" "+self.frets[s]+" "+onF+"; "
                oldTimes[s] = t+jitters[i]
                whichChord[s] = (whichChord[s] + 1) % chordMax
                self.prevFrets[s] = self.frets[s]

            if r.random() < 0.47:
                tScale *= decayRate;
            else:
                tScale /= decayRateSlow
            if tScale < maxRate: tScale = maxRate;
            elif tScale > 0.25: tScale = maxRate
            t += timingOrder[i%len(timingOrder)] * tScale * 0.25
            i += 1




    def tabToScore(self, tabFile, stringCount=6, rate=1.0, higherFrets=True, pluckForce=0.08, fingerForce=1.8):
        """Convert a txt file of guitar tab to a NESS score file

        Tab should be in lines in the following format:
        |--1-3-----... etc ...----7--3---|

        the 'rate' parameter specifies the time per unit, where 1 is 1/8 of a second per unit, 2 is 1/16 of a second per unit, etc
        if higherFrets is set to "False", then "12" would mean fret 1 then fret 2, rather than fret 12
        """
        #arbitraryRubato = 0.;
        #********************
        ## The plan here would be to:
        ## a) keep track of the total number of timepoints in the score
        ## b) instead of timePerUnit, have an array of time divisions
        ## c) populate the array at the outset so that each string can read it, e.g. [0.25, 0.24, 0.23, 0.26, 0.26, etc]
        ## d) use that to generate another, rubatoTimes array that is CUMULATIVE TIME VALUES
        ## e) pull these out using strings[i][j][0] as AN INDEX TO THAT , rubatoTimes[strings[i][j][0]]
        #**********************

        #rate = 1.0
        pluckPos = 0.85;
        # pluckF = 0.08       # PREVIOUSLY !!!
        alwaysPluck = False     # if this is False, it'll just do it with finger slides unless it is a repeated note
        #fingerForce = 1.8;
        fingerNegativeForce = -1;
        offsetVal = 1;      # offset for end of line things?
        glideTime = 0.004;
        #higherFrets = True     # if False, "12" would mean fret 1 then fret 2
        #stringCount = 6
        
        # try opening a file
        tab = ""
        tabLines = []
        if isinstance(tabFile, str):
            tab = open(tabFile, 'r')
            tabLines = self.tabLinesFromTextFile(tab, stringCount);
        else:
            tab = tabFile
            tabLines = [tab]
        #print("Couldn't read tab line or file")
        #finally:
        #    f.close()
        
        print (tab)
        
        strings = self.parseTab(tabLines, offsetVal, self.capo, higherFrets, stringCount);
        scoreVariables = self.createScoreVariables(strings, rate, pluckPos, pluckForce, fingerForce, fingerNegativeForce, glideTime, stringCount, alwaysPluck);
        self.fingerStrings = scoreVariables[0];
        self.T = int(scoreVariables[1]+8);
        if isinstance(tabFile, str):
            print ("score infomation read from "+tabFile);
        else:
            print ("score infomation read from input text");


    def tabLinesFromTextFile(self, tab, stringCount):
        """find the tablines in the raw text and return as [?]"""
        tempTabLine = []
        outputTabLines = []
        for line in tab:
            if ("|" not in line) or ("-" not in line):
                if "-" not in line:
                    # if there's a line with no "-" then reset the current tab line
                    tempTabLine = []
            else:
                # collect the six lines together in tempTabLine
                tempTabLine.insert(0, line)
            if len(tempTabLine) >= stringCount:
                outputTabLines.append( tempTabLine )
                tempTabLine = []

        return outputTabLines


    def parseTab(self, tabLines, offsetVal, capoPos, higherFrets, stringCount):
        """put together the discrete timing info into STRINGS"""


        self.fingerHeight = 0.0;
        
        outputStrings = [[] for i in range(stringCount)];
        t = 0
        tempT = 0;
        # for each tab line (each is made up of [stringCount] lines)
        for i, tabLine in enumerate(tabLines):
            # for each single line in the set of [stringCount]
            tempT = 0;  # keep count of time based on position in string
            
            for j, line in enumerate(tabLine):
                stringFingers = [];   # list of [int_time, fret] pairs
                offsetCorrection = 0;
                skipNext = False;
                # each char in the line
                for k, char in enumerate(line):
                    # tabLines[i][j][k] is each char
                    if (skipNext):
                        # were we told to skip this one?
                        if (j==0):
                            tempT += 1; 
                        skipNext = False;
                    else:

                        if tabLines[i][j][k] == "|":
                            offsetCorrection -= offsetVal;

                        else:
                            if (j==0):
                                # only count the time for the first string
                                tempT += 1; # increment the time for any char other than "|"
                                #console.log("tempT: "+tempT+"   - "+Number(tabLines[i][j][k]))

                        if (tabLines[i][j][k] != "|" and self.isNum(tabLines[i][j][k])):

                            actuallyDoItNormally = True;
                            # consider frets above 9?
                            if higherFrets:
                                actuallyDoItNormally = False;
                                # check we're not going over the edge here...
                                if (k < len(tabLines[i][j])-1):

                                    # check the next step in the tab
                                    if (tabLines[i][j][k+1] != "|" and self.isNum(tabLines[i][j][k+1])):
                                        # only consider this if we're talking about frets beginning with 1 or 2  
                                        if (tabLines[i][j][k] == "1" or tabLines[i][j][k] == "2"):
                                            combinedFret = tabLines[i][j][k]+tabLines[i][j][k+1]
                                            outputStrings[j].append( [t+k+offsetCorrection, capoPos + int(combinedFret)] );
                                            skipNext = True;    # skip the next iteration of k
                                        else: actuallyDoItNormally = True;
                                    else: actuallyDoItNormally = True;
                                else: actuallyDoItNormally = True;
                            else: actuallyDoItNormally = True;

                            # if not all of the above conditions are met, then just do it normally
                            if (actuallyDoItNormally):
                                outputStrings[j].append( [t+k+offsetCorrection, capoPos + int(tabLines[i][j][k])])
                            
                            #console.log("string "+j+"   - "+Number(tabLines[i][j][k]))
            #console.log("Extending: "+tempT+" ")
            t += tempT;
            
        return outputStrings;


    def createScoreVariables(self, strings, rate, pluckPos, pluckF, fingerForce, fingerNegativeForce, glideTime, stringCount, alwaysPluck):
        """get a PLUCK_DEFS and FINGER_DEFS, and return as a two element array"""

        timePerUnit = 0.125 * 1.0/rate;
        # starting from 0 up to 20th fret - ARE THESE DEFINITELY CORRECT???
        # see image
        # could also try this formula?
        # Calculating Fret Spacing for a Single Fret: d = s - (s / (2 ^ (n / 12)))
        #fretPositions = [0.0, 0.056, 0.109, 0.159, 0.206, 0.251, 0.293, 0.333, 0.370, 0.405, 0.439, 0.47, 0.5,   0.528, 0.555, 0.58, 0.603, 0.625, 0.646, 0.667, 0.685 ];

        #distanceBehindFret = 0.02;
        #glideTime = 0.004;      # for removing one finger and putting the next back on
        fingerHeight = 0.01;

        pluckJitter = 0;#0.07;
        pluckDur = 0.005;

        finger_defs = [];

        # create a ghost pluck so that the score works (could add this at the end)
        # [str_num, pluck_time, pluck_pos, pluck_dur, pluck_force]
        #initialPluck = [1, 0, 0.8, 0.001, 0.00001];
        #self.plucks.append( initialPluck )
        maxT = 0;

        # create a finger for each string

        # get each string
        # go backwards through strings array, as the strings are the wrong way round from a tab perspective
        # thickest is last in tab, thinnest is first in model

        # NOTE 

        for i, string in enumerate(strings):
            
            stringNum = i+1    # for non reversed, use: stringCount-i;
            prev_pos = 0; # this will be set before use
            current_finger = ""#str(stringNum)+", [0 0.25 0 ";  #stringNum+", [0 "+currentFingerPos+" 0";

            # get each event in the specific string
            # event[0] = strings[i][j][0] = the time
            # event[1] = strings[i][j][1] = the fret
            for j, event in enumerate(string):
                t = event[0] * timePerUnit;
                # NOTE - ADDING 1 TO ALL FRETS TO AVOID OPEN STRINGS!!!
                pos = self.getFretPos(event[1] + 1)
                #if (pos < 0) { pos = 0; }

                # if the event time is bigger than all others, then make that the new maxT
                if (t > maxT): maxT = t;

                #if (stringNum==2) { console.log("string: "+stringNum+"  pos: "+pos+"  prev: "+pos_prev+"  time: "+t+"  j: "+j+"  len: "+strings[i].length)}
                #console.log("string: "+stringNum+"  pos: "+pos+"  prev: "+pos_prev+"  time: "+t+"  j: "+j+"  len: "+strings[i].length);

                if (j==0):
                    #current_finger += stringNum+", [0 "+pos+" 0";
                    current_finger += str( max(t-0.001, 0.0) )+" "+str(pos)+" 0 ";
                    current_finger += "; "+str( max(t,0.0) )+" "+str(pos)+" "+str(fingerForce)+" ";

                else:
                    if (pos == prev_pos):
                        # repeated note - jiggle it around on the fret???
                        # ?
                        # OR just try an actual pluck:
                        self.plucks.append( [stringNum, t, pluckPos, pluckDur, pluckF*0.75 + r.random()*0.5*pluckF] )

                    else:
                        current_finger += "; "+str((t-glideTime))+" "+str(prev_pos)+" "+str(fingerForce)+" ";
                        current_finger += "; "+str(t)+" "+str(pos)+" "+str(fingerForce)+" ";
                        if (alwaysPluck):
                            self.plucks.append( [stringNum, t, pluckPos, pluckDur, pluckF*0.75 + r.random()*0.5*pluckF] )

                prev_pos = pos;       

            #current_finger += "], ["+str(fingerHeight)+", 0];\n";
            finger_defs.append(current_finger);
            #console.log(fingers_in_this_string.length);

        returnArray = [finger_defs, maxT];
        return returnArray;


    def getFretPos(self, fretNum):
    	fretPos = self.fretPositions[fretNum]
    	fretSize = fretPos - self.fretPositions[max(0, fretNum-1)]
    	fingerPos = fretPos - (1-self.fretFingerPos)*fretSize
    	if fingerPos < 0: fingerPos = 0
    	return fingerPos

    def isNum(self, testChar):
        result = False;
        if (testChar >= '0' and testChar <= '9'):
            result = True;
        return result;


    def walk(self, inVal, maxVal):
        newVal = inVal
        if (r.random() < 0.75):
            newVal += r.randint(-1, 1)
        else:
            newVal += r.randint(-2, 2)
        if newVal < 0: newVal = 1
        if newVal > maxVal: newVal = maxVal-1
        return newVal


    def midiToScore(self, midiFile, stringCount=6, rate=1.0, transpose=0, alwaysPluck=True):
        """Convert a txt file of guitar tab to a NESS score file

        Tab should be in lines in the following format:
        |--1-3-----... etc ...----7--3---|

        the 'rate' parameter specifies the time per unit, where 1 is 1/8 of a second per unit, 2 is 1/16 of a second per unit, etc
        if higherFrets is set to "False", then "12" would mean fret 1 then fret 2, rather than fret 12

        # TO DO: read tempo and use that to scale the rate
        """
        pattern = midi.read_midifile(midiFile)

        # TO DO: read tempo and use that to scale the rate

        # PARAMS FOR CONVERSION
        ticks_to_seconds_ratio = 0.0007/float(rate) # 2000 ticks = one second?
        # (60000 / (bpm * ppq)
        pattern.make_ticks_abs()

        events, timings = getEventsAndTimings(pattern)
        scoreVariables = self.createScoreEventsFromMIDIEvents(events, timings, transpose, ticks_to_seconds_ratio, alwaysPluck)
        self.fingerStrings = scoreVariables[0];
        self.T = int(scoreVariables[1]+5);
        print ("score infomation read from "+midiFile);


    def createScoreEventsFromMIDIEvents(self, events, timings, transpose, ticks_to_seconds_ratio, alwaysPluck):
        startingFrets = [40, 45, 50, 55, 59, 64];
        glideTime = 0.005
        tOffset = 0.5
        #fingerForce = 1
        pluckForce = 0.18
        pluckForceJitter = 0.02
        prevString = 0
        prevFret = [-1 for i in range(6)]
        pluck_defs = []
        maxT = 1
        self.fingerHeight = 0.0;



        finger_defs = ["" for i in range(6)]
        for i, event in enumerate(events):
            if isinstance(event, midi.NoteOnEvent):
                if (event.channel < 17):
                    #tickScale = 1 - 0.5*(i/float(len(events)))
                    tickScale = 1
                    pitch = event.data[0] + transpose
                    vel = event.data[1]
                    fingerForce = vel*0.02
                    print(fingerForce)
                    if (fingerForce < 0.5): fingerForce = 0.5
                    string, fret = midiToStringFret(pitch)
                    t = (event.tick * ticks_to_seconds_ratio * tickScale) + tOffset;
                    stringPos = self.getFretPos(fret)
                    #stringPos = fretToPos(fret, self.fretPositions, self.distanceBehindFret)

                    if (prevFret[string] == -1):           
                        # if this string hasn't been used yet
                        #finger_defs[string] += str(t-(glideTime))+" "+str(stringPos)+" 0"
                        finger_defs[string] += str(0)+" "+str(0.001)+" "+str(fingerForce*0.125)
                        finger_defs[string] += "; "+str(t)+" "+str(stringPos)+" "+str(fingerForce) 

                    elif (fret == prevFret[string]):      
                        # if the last used fret on this string was the same as this one
                        # add a pluck
                        self.plucks.append( [string+1, t, round(0.85 + ((r.random()*2-1)*0.06), 3), r.random()*0.0005 + 0.0002, pluckForce + (r.random()*2 - 1)*pluckForceJitter] )
                    else:
                        # move the appropriate finger
                        if alwaysPluck:
                            self.plucks.append( [string+1, t+0.002, round(0.85 + ((r.random()*2-1)*0.06), 3), r.random()*0.0005 + 0.0002, pluckForce + (r.random()*2 - 1)*pluckForceJitter] )
                        #prevStringPos = fretToPos(prevFret[string], self.fretPositions, self.distanceBehindFret)
                        prevStringPos = self.getFretPos(prevFret[string])
                        finger_defs[string] += "; "+str(t-(glideTime))+" "+str(prevStringPos)+" "+str(fingerForce) 
                        finger_defs[string] += "; "+str(t)+" "+str(stringPos)+" "+str(fingerForce)

                    prevString = string;   
                    prevFret[string] = fret;
                    maxT = t

        maxT = round(maxT+5)
        return (finger_defs, maxT)


def getEventsAndTimings(pattern):
    tempEvents = []
    tempTimings = []
    for track in pattern:
            for event in track:
                tempEvents.append(event)
    sortedEvents = sorted(tempEvents, key=lambda x: x.tick)
    for e in sortedEvents:
        tempTimings.append(e.tick)
    return sortedEvents, tempTimings


def midiToStringFret(note):
    string_and_fret = [0, 0]
    while (note < startingFrets[0]):
        note += 12
    while (note > startingFrets[5]+19):
        note -= 12
    if (note < startingFrets[1]):
        string_and_fret = [0, note-startingFrets[0]]
    elif (note < startingFrets[2]):
        string_and_fret = [1, note-startingFrets[1]]
    elif (note < startingFrets[3]):
        string_and_fret = [2, note-startingFrets[2]]
    elif (note < startingFrets[4]):
        string_and_fret = [3, note-startingFrets[3]]
    elif (note < startingFrets[5]):
        string_and_fret = [4, note-startingFrets[4]]
    else:
        string_and_fret = [5, note-startingFrets[5]]
    return string_and_fret[0], string_and_fret[1]


def fretToPos(fret, fretPositions, distanceBehindFret):
    pos = fretPositions[fret] - distanceBehindFret
    if pos < 0:
        pos = 0
    return pos


def fingerPicking(stringCount, startTime, repetitions, rate=0.25, swing=0, ratewarp=False, pForceMax=0.1):
    newPlucks = []
    t = startTime
    #pluckF = 0.5
    pluckRand = pForceMax
    pluckOffset = 0.05
    pluckDur = 0.001
    pluckF = r.random()*pluckRand + pluckOffset
    # thumb goes 1-3-1-3-1-3-1-3 where 1 is thickest
    thumb = [1,3,1,2]
    for i in range(repetitions):
        newPlucks.append([thumb[0], t, 0.85+r.random()*0.075, pluckDur, pluckF])
        t += rate
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        newPlucks.append([thumb[1], t, 0.85+r.random()*0.075, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        highString = r.randint(5, 6)
        newPlucks.append([highString, t, 0.87+r.random()*0.05, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        if (ratewarp):      rate = rate + (r.random()*0.01 - 0.005)
        if (r.random() < 0.25):
            highString = r.randint(5, 6)
            newPlucks.append([highString, t, 0.87+r.random()*0.05, pluckDur, pluckF])
        t += rate
        newPlucks.append([thumb[2], t, 0.85+r.random()*0.075, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        
        if (r.random() < 0.25):
            t += rate*0.5
            midString = r.randint(3, 4)
            newPlucks.append([midString, t, 0.87+r.random()*0.05, pluckDur, pluckF])
            t += rate*0.5
        else:
            t += rate
        if (ratewarp):      rate = rate + (r.random()*0.01 - 0.005)
        highString = r.randint(5, 6)
        newPlucks.append([highString, t+swing, 0.87+r.random()*0.05, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        newPlucks.append([thumb[3], t, 0.85+r.random()*0.075, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        midString = r.randint(3, 5)
        newPlucks.append([midString, t+swing, 0.87+r.random()*0.05, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        if (ratewarp):      rate = rate + (r.random()*0.01 - 0.005)
        newPlucks.append([thumb[0], t, 0.85+r.random()*0.075, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        
        if (r.random() < 0.25):
            t += rate*0.5
            midString = r.randint(3, 4)
            newPlucks.append([midString, t, 0.87+r.random()*0.05, pluckDur, pluckF])
            t += rate*0.5
        else:
            t += rate

        if (ratewarp):      rate = rate + (r.random()*0.01 - 0.005)

        highString = r.randint(5, 6)
        newPlucks.append([highString, t+swing, 0.87+r.random()*0.05, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        newPlucks.append([thumb[1], t, 0.85+r.random()*0.075, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        if (ratewarp):      rate = rate + (r.random()*0.01 - 0.005)
        midString = r.randint(3, 5)
        newPlucks.append([midString, t+swing, 0.87+r.random()*0.05, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        newPlucks.append([thumb[2], t, 0.85+r.random()*0.075, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        highString = r.randint(5, 6)
        newPlucks.append([highString, t+swing, 0.87+r.random()*0.05, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        if (ratewarp):      rate = rate + (r.random()*0.01 - 0.005)
        newPlucks.append([thumb[3], t, 0.85+r.random()*0.075, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        midString = r.randint(3, 5)
        newPlucks.append([midString, t+swing, 0.87+r.random()*0.05, pluckDur, pluckF])
        pluckF = r.random()*pluckRand + pluckOffset
        t += rate
        if (ratewarp):      rate = rate + (r.random()*0.01 - 0.005)

    # [str_num, pluck_time, pluck_pos, pluck_dur, pluck_force]
    return newPlucks


def mtof(midinote):
    return 440 * pow(2, (midinote-69)/12.0)

def harmonicForceFromPosition(pos, force):
    # half the force is scaled - the closer we are to the nut, the higher the force?
    return force*0.5 + force*0.5*(0.5 - abs(pos-0.5))

def getMidiPitchFromString(noteString, s=0):
    noteName = "E"
    register = 3
    #stringNoteDefaults = [40, 45, 50, 55, 59, 64]
    registerPerString = [2, 2, 3, 3, 3, 4]
    # so "e", s=1 would give 
    if len(noteString) == 1:
        noteName = noteString[0].lower()
        if s < 6:
            register = registerPerString[s]
        else:
            register = 2
    if len(noteString) == 2:
        noteName = noteString[0].lower()
        register = int(noteString[1])
    elif len(noteString) == 3:
        noteName = noteString[0:2].lower()
        register = int(noteString[2])
    midiVal = keys[noteName] + 12*(register+1)
    return midiVal

class MIDIStrings(object):
    def __init__(self, stringCount, tempo=120, name="MIDI Strings"):
        self.stringCount = stringCount
        self.midiData = MIDIFile(stringCount)
        self.name = name
        self.tempo = tempo
        for i in range(self.stringCount):
            self.midiData.addTrackName(i, 0,"String "+str(i+1))   # track, time, track name
            #self.midiData.addTempo(i, 0, tempo)

    def addEvent(self, sNum, t, note, dur):
        # note that time here is in BEATS, not time
        # so for bpm=120, a second is 4 beats, so scale time by 4???
        self.midiData.addNote(sNum, 1, note, t*2, dur*2, 100)

    def write(self, fName):
        binfile = open(fName, 'wb')
        self.midiData.writeFile(binfile)
        binfile.close()





