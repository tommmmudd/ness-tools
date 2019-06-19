# NESS FUNCTIONS!!
import random as r


class SoundBoard(object):
    def __init__(self, name="Quick SoundBoard"):
        self.name = name
        self.fs = 44100
        self.strings = []
        self.plate = SBPlate()
        self.collisionParams = [1.793912177273139e+15, 1.555095115459269, 50]   #collision stiffness, collision nonlinearity exponent, and number of iterations.
        #defines parameters for the Newton Raphson solver that handles collisions between the strings and the frets. They are: 
        self.plateOuts = [[0.075854289563064, 0.779167230102011, 0.537647321744385], [0.530797553008973, 0.229906208473730, -0.676195860997517]]  # could be lots of these - more than one (each with 3 params: X, Y, pan)

    def addString(self):
        self.strings.append( SBString() )

    def write(self, fName):
        print( "writing "+self.name+" as: "+fName)
        out = open(fName, "w");
        #%3 valved trombone
        out.write("# "+self.name+"\n\n")
        out.write("# "+"sbversion 0.1\n\n")
        out.write('samplerate %.0f;\n\n' % self.fs)

        # strings
        for i, string in enumerate(self.strings):
            string.compileParams()      # just in case things have been updated without updating the params array
            out.write("string string"+str(i+1))
            for p in string.params:
                out.write(" "+str(p))
            out.write("\n")
        out.write("\n\n")

        # plate
        self.plate.compileParams();
        out.write("plate")
        for p in self.plate.params:
            out.write(" "+str(p))
        out.write("\n\n")

        # collisions
        out.write("collision")
        for p in self.collisionParams:
            out.write(" "+str(p))
        out.write("\n\n")

        # string outs
        for i, string in enumerate(self.strings):
            out.write("string_out string"+str(i+1))
            for o in string.outs:
                out.write(" "+str(o))
            out.write("\n")
        out.write("\n\n")

        # plate outs
        for o in self.plateOuts:
            out.write("plate_out "+str(o[0])+" "+str(o[1])+" "+str(o[2])+"\n")

        # done, close the file
        out.close()

class SBPlate(object):
    def __init__(self):
        self.density = 7850 
        self.thickness = 0.001 
        self.ym = 2e11 
        self.poisson = 0.3 
        self.tension = 0
        self.sizeX = 0.5
        self.sizeY = 0.2
        self.t60_0 = 10
        self.t60_1 = 9
        self.params = []
        self.compileParams()

    def compileParams(self):
        self.params = [self.density, self.thickness, self.ym, self.poisson, self.tension, self.sizeX, self.sizeY, self.t60_0, self.t60_1] 

class SBString(object):
    def __init__(self):
        self.length = 0.662944737278636
        self.density = 0.020632359246225 
        self.tension = 79.150136708685949 
        self.ym = 2.191433389648589e+11 
        self.radius = 0.000384352256525255 
        self.t60_0 = 11.311481398313173 
        self.t60_1 = 8.357470309715547 
        self.coords = [0.655477890177557, 0.276922984960890, 0.694828622975817, 0.438744359656398]
        self.fretNum = 3
        self.fretHeight = -0.001418729661716 
        self.boardHeight = -0.002689803992052
        self.variation = 0.019597439585161 # var in baseboard profile 
        self.outs = [0.585264091152724, 0.514400458221443]
        self.params = []
        self.compileParams()

    def compileParams(self):
        # add all params to the params array
        self.params = [self.length, self.density, self.tension, self.ym, self.radius, self.t60_0, self.t60_1, self.coords[0], self.coords[1], self.coords[2], self.coords[3], self.fretNum, self.fretHeight, self.boardHeight, self.variation] 

class SBScore(object):
    def __init__(self, dur, strCount):
        self.stringCount = strCount
        self.dur = dur
        self.events = []

    def randomStrikes(self, avgRate):
        t = 0.25
        while (t < max(self.dur - 5, 1)):
            stringNum = int(r.random()*self.stringCount) + 1
            # start time (seconds), duration (seconds), maximum force (N), and location on string (normalised to range 0 to 1)
            self.events.append(["strike", "string"+str(stringNum), t, 0.002, r.random()*10, r.random()])
            t += (r.random()-0.5)*(2*avgRate) + avgRate

    def addStrike(self, stringNum, params):
        # start time (seconds), duration (seconds), maximum force (N), and location on string (normalised to range 0 to 1)
        self.events.append(["strike", "string"+str(stringNum)]+params)

    def addPluck(self, stringNum, params):
        self.events.append(["pluck", "string"+str(stringNum)]+params)

    def rhythmicStrikes(self, rate, force="random", position="random"):
        t = 0.25
        while (t < max(self.dur - 5, 1)):
            stringNum = int(r.random()*self.stringCount) + 1
            # start time (seconds), duration (seconds), maximum force (N), and location on string (normalised to range 0 to 1)
            if (position=="random"):    pos = r.random()*0.9 + 0.05
            else: pos = position
            if (force == "random"):  f = r.random()*0.9 + 0.05
            else: f = force
            self.events.append(["strike", "string"+str(stringNum), t, 0.002, f, pos])
            t += rate

    def write(self, fName):
        print( "writing score as: "+fName)
        out = open(fName, "w");
        out.write('duration '+str(self.dur)+"\n\n")
        for e in self.events:
            for param in e:
                out.write(str(param)+" ")
            out.write("\n")
        out.close()
