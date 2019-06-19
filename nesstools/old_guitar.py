# NESS FUNCTIONS!!
import random as r

# fr MIDI strings
from midiutil.MidiFile import MIDIFile

# BRASS


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

class StringInstrument(object):
    """String Instrument class for generating instruments for the NESS physical model

    Attributes:
        name        Optional name for your instrument written into the final file
        sr          Sample rate
        stringCount Number of strings on the instrument (integer)
        strings     a list of NessString objects, of length stringCount.
    """
    def __init__(self, stringCount, name="Quick Guitar Instrument"):
        self.name = name
        self.sr = 44100
        self.stringCount = stringCount
        self.strings = [NessString() for i in range(stringCount)]
        self.defaultGuitar()
        self.regularStrings = ["Low E"]
        self.backboard = True
        self.fingers = True
        self.frets = True
        self.fretHeight = -0.001
        self.backboardParams = [-0.001, -0.000, -0.0002]    #ALL NEGATIVE OR ZERO parabola: b(x) = b0+b1*x+b2*x^2, where backboard =% [b0 b1 b2]]
        self.barrier = [1e10, 1.3, 10, 20, 1e-12]
        self.fingerMass = 0.005
        self.fingerStiffness = 1e7
        self.fingerExp = 1.6
        self.fingerLoss = 120

    def defaultGuitar(self, kind="regular"):
        """Quick function to setup the strings for a basic 6 string steel guitar"""
        for i in range(self.stringCount):
            self.setRegularString(i, i)

    def defaultBass(self, kind="regular"):
        """Setup the strings for a basic 4 string bass guitar"""
        self.stringCount = 4
        self.strings = []
        self.strings.append( NessString(0.88, 2e11, 4.8, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 9.3, 0.0002, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 9.2, 0.00015, 7850, 15, 3) )
        self.strings.append( NessString(0.88, 2e11, 10.5, 0.00012, 7850, 15, 3) )

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
        out.write("];\n\n")
        out.write("output_def = [")
        for i, string in enumerate(self.strings):
            out.write(str(i+1)+" "+str(string.outputPos))
            if i != (len(self.strings)-1):
                out.write("; ")
        out.write("];\n\n")
        out.write("normalize_outs = 1;\n\n")
        out.write("pan = [")
        for i, string in enumerate(self.strings):
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
        self.plucks = [[1, 0.5, 0.8, 0.0025, 0.0005]]         # initial pluck, otherwise it won't run. Could remove
        self.strums = []
        self.frets = ["0.331" for a in range(self.stringCount)]
        self.prevFrets = ["0" for a in range(self.stringCount)]
        self.pluckF = pluckF
        self.distanceBehindFret = 0.0035
        self.capo = 0
        self.timingPatterns = []
        self.chordPatterns = []
        self.fretPositions = [0.0, 0.056, 0.109, 0.159, 0.206, 0.251, 0.293, 0.333, 0.370, 0.405, 0.439, 0.47, 0.5,   0.528, 0.555, 0.58, 0.603, 0.625, 0.646, 0.667, 0.685 ]
        self.harmonics = [1/2.0, 1/3.0, 1/4.0, 1/5.0, 2/5.0, 1/6.0]
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


    def write(self, fName):
        """Output the score in its current state as 'fName' for use with the NESS model"""
        print ("writing "+fName)
        # finish up the fingerStrings first!
        for s in range(self.stringCount):
            # arbitrary end fingering?? is that necessary?
            #self.fingerStrings[s] += str(self.T-5)+" "+self.prevFrets[s]+" "+str(1)+"], [0.01, 0];\n"
            # no end finger
            self.fingerStrings[s] += "], [0.01, 0];\n"
        out = open(fName, 'w')
        out.write("Tf = "+str(self.T)+";\n\n")
        out.write("exc = [];\n\n")
        for pluck in self.plucks:
            out.write("exc = pluck_gen(exc, ")
            for i, param in enumerate(pluck):
                if i != (len(pluck) - 1):
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
        out.write("finger_def = {")
        #for i in range(stringCount):
        for i, f_string in enumerate(self.fingerStrings):
            out.write("\n    "+str(i+1)+", [0 "+str(self.fretPositions[5])+" 0; ")   # gotta start somewhere?? Eh?
            out.write(f_string)
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

    def structureSolo(self, startTime, endTime, timingArray, tScale, maxF):
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

    def walk(self, inVal, maxVal):
        newVal = inVal
        if (r.random() < 0.75):
            newVal += r.randint(-1, 1)
        else:
            newVal += r.randint(-2, 2)
        if newVal < 0: newVal = 1
        if newVal > maxVal: newVal = maxVal-1
        return newVal


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
