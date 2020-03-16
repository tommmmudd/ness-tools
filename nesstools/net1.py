# NESS FUNCTIONS!!
import random as r


class Net1Instrument(object):
    def __init__(self, stringNum, name="Net1Instrument object"):
        self.name = name
        self.fs = 48000
        self.string_num = stringNum
        self.connection_num = 0
        self.strings = [Net1String() for i in range(self.string_num)]
        self.connections = []#[self.addRandomConnection() for i in range(self.connection_num)]

        #self.plate = SBPlate()
        #self.collisionParams = [1.793912177273139e+15, 1.555095115459269, 50]   #collision stiffness, collision nonlinearity exponent, and number of iterations.
        #defines parameters for the Newton Raphson solver that handles collisions between the strings and the frets. They are: 
        #self.plateOuts = [[0.075854289563064, 0.779167230102011, 0.537647321744385], [0.530797553008973, 0.229906208473730, -0.676195860997517]]  # could be lots of these - more than one (each with 3 params: X, Y, pan)

    def addConnection(self, stringA=1, stringB=1, mass=0.0001, angularFrequency=1000, loss=2, collisionExponent=1.6, rattleDistance=0.001, stringAPos=0.8, stringBPos=0.8):
        self.connections.append( Net1Connection(stringA, stringB) )
        self.connections[-1].mass = mass
        self.connections[-1].angularFrequency = angularFrequency
        self.connections[-1].loss = loss
        self.connections[-1].collisionExponent = collisionExponent
        self.connections[-1].rattleDistance = rattleDistance
        self.connections[-1].stringAPos = stringAPos
        self.connections[-1].stringBPos = stringBPos
        self.connection_num += 1

    def addRandomConnection(self):
        stringA = r.randint(1, self.string_num);
        stringB = r.randint(1, self.string_num);
        return Net1Connection(stringA, stringB)

    def randomiseConnectionParams(self):
        for c in self.connections:
            c.mass = r.random()*r.random()*r.random()*r.random()*0.1
            c.angularFrequency = r.randint(50, 2000)
            c.collexp = r.random()*3
            c.rattledistance = r.random()*2
            c.connectionA = r.random()
            c.connectionB = r.random()

    def write(self, fName):
        print( "writing "+self.name+" as: "+fName)
        out = open(fName, "w");
        #%3 valved trombone
        out.write("% Net1: "+self.name+"\n")
        out.write("% gtversion 1.0\n\n")

        out.write("SR="+str(self.fs)+";\n\n")
        

        # out.write("# "+"sbversion 0.1\n\n")
        #out.write('samplerate %.0f;\n\n' % self.fs)
        # strings
        out.write("string_def = [")
        for i, string in enumerate(self.strings):
            string.compileParams()      # just in case things have been updated without updating the params array
            for p in string.params:
                out.write(" "+str(p))
            if i != (len(self.strings)-1):
                out.write("; ")
        out.write("]\n\n")

        # output points (one for each string by default)
        outputCount = 0
        out.write("output_def = [")
        for i, string in enumerate(self.strings):
            for outp in string.outputs:
                out.write(str(i+1)+" "+str(outp))
                out.write("; ")
                outputCount += 1
        out.write("];\n\n")

        out.write("itnum = 20;\n\n")

        out.write("pan = [")
        for i in range(outputCount):
            pan = (r.random()*1.5)-0.75
            out.write(str(pan) + " ")
        out.write("];\n\n")

        # connections
        if self.connection_num > 0:
            out.write("ssconnect_def = [")
            for i, connection in enumerate(self.connections):
                params = connection.compileParams()      # just in case things have been updated without updating the params array
                for j, p in enumerate(params):
                    out.write(" "+str(p))
                    if j != (len(params)-1):
                        out.write(",")
                if i != (len(self.connections)-1):
                    out.write("; ")
            out.write("];\n\n")

        out.write("normalize_outs = 1;\n\n")
        # done, close the file
        out.close()

class Net1Connection(object):
    def __init__(self, strA, strB):
        #0.001, 10000, 2, 1.6, loss,  1, 0.8, 2, 0.7
        self.mass = 0.051           # % mass (kg), >0. Do not set to 0!
        self.angularFrequency = 1000         # angular frequency (rad), >0. try to keep below about 1e4
        self.collisionExponent = 2            # collision exponent (>1, usually <3). Probably best not to use 1 exactly
        self.rattleDistance = 1.6   # rattling distance (m), >=0. Can be zero!
        self.loss = 0.005           # loss parameter (bigger means more loss). >=0
        self.stringA = strA         # string index 1 
        self.stringAPos = 0.8      # connection point 1 (0-1)
        self.stringB = strB         # string index 2: if zero, then no connection
        self.stringBPos = 0.7      # connection point 2 (0-1)
        self.params = []#self.compileParams()

    def compileParams(self):
        return [self.mass, self.angularFrequency, self.loss, self.collisionExponent, self.rattleDistance, self.stringA, self.stringAPos, self.stringB, self.stringBPos] 

class Net1String(object):
    def __init__(self):
        self.length = 0.68
        self.material = 1 # #1 = steel, #2 = gold, #3 = lead
        self.tension = 21.9
        self.radius = 0.00015
        self.t60_0 = 15
        self.t60_1 = 5
        self.outputs = [0.78]
        self.params = []
        self.compileParams()

    def compileParams(self):
        # add all params to the params array
        self.params = [self.length, self.material, self.tension,self.radius, self.t60_0, self.t60_1] 


class Net1Score(object):
    def __init__(self, T, stringCount, F=0.2):
        self.stringCount = stringCount
        self.T = T
        self.fingerStrings = ["" for a in range(self.stringCount)]
        self.events = [[1,0.01,0.3,0.002,1,1]]         # initial pluck, otherwise it won't run. Could remove
        self.strums = []


    def quickEvents(self, interval, strength=0.5):
        t = 0.1
        s = 0       
        while t < (self.T - 6):
            
            self.makeEvent(t, s+1, strength)
            s = (s+1) % self.stringCount
            t += interval

    def eventPattern(self, pattern, strength=10):
        t = 0.1
        s = 0
        i = 0
        while t < (self.T - 6):
            self.makeEvent(t, s+1, strength)
            s = (s+1) % self.stringCount
            i = (i+1) % len(pattern)
            t += pattern[i]

    def eventPattern2(self, pattern, strength=10, eventType=1):
        t = 0.1
        s = 0
        i = 0
        while t < (self.T - 6):
            self.makeEvent(t, s+1, r.random()*strength,0.8, eventType)
            s = (s+1) % self.stringCount
            i = (i+1) % len(pattern)
            t += pattern[i]

    def swell(self, interval, maxStrength=1000, eventType=1):
        t = 0.1
        s = 0
        i = 0
        iterations = (self.T - 6.1) / interval
        while t < (self.T - 6):
            self.makeEvent(t, s+1, maxStrength*i/iterations, 0.8, eventType)
            s = (s+1) % self.stringCount
            i += 1
            t += interval

    def swellAndRecede(self, interval, maxStrength=1000, eventType=1):
        t = 0.1
        s = 0
        i = 0
        iterations = int((self.T - 6.1) / interval)
        while t < (self.T - 6):
            strength = maxStrength*i/(0.5*iterations)
            if (i > iterations/2):
                backwards_i = iterations - i
                strength = maxStrength*backwards_i/iterations
            self.makeEvent(t, s+1, strength, 0.8, eventType)
            s = (s+1) % self.stringCount
            i += 1
            t += interval

    def swellAndRecedeCustom(self, interval, maxStrength=1000, eventType=1, strArray=[0], start=0.1, end=30):
        t = start
        s = 0
        i = 0
        iterations = int((end - start) / interval)
        while t < end:
            strength = maxStrength*i/(0.5*iterations)
            if (i > iterations/2):
                backwards_i = iterations - i
                strength = maxStrength*backwards_i/iterations
            self.makeEvent(t, strArray[s]+1, strength, r.random(), eventType)
            s = (s+1) % len(strArray)
            i += 1
            t += interval

    def write(self, fName):
        print ("writing "+fName)
        out = open(fName, 'w')
        out.write("SR = 48000;\n")
        out.write("Tf = "+str(self.T)+";\n")
        out.write("exc = [];\n\n")
        for event in self.events:
            out.write("exc = event_gen(exc, ")
            for i, param in enumerate(event):
                if i != (len(event) - 1):
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
        out.close()

    def makeStrum(self, time, direction, strength=0.5, pos=0.8, durScale=0.005):
        # NOTE: Randomises the number of strings - should this just be the max?
        strum_time = time   # when (seconds)
        strum_dir = direction
        strum_pos = pos     # where (0-1)
        strum_dur = r.random()*r.random()*r.random()*durScale#round(r.random()*0.01 + 0.001, 4) # dur of actual pluck (e.g. 0.001 - 0.01 for realistic range)
        pluck_dur = 0.002
        strum_force = strength#r.random()*0.2 + 0.2#r.random()*0.5 + 0.1 #round(r.random()*r.random()*10 + 0.2, 3)      # force (N), e.g. 1
        strum_type = 1 # 0 is pluck
        return [strum_time, strum_dur, strum_dir, strum_force, 0.02, pluck_dur, 0.0001, strum_pos, 0.05, r.randint(1, self.stringCount), 0.03, strum_type]

    def makeEvent(self, time, string, strength=0.5, pos=0.8, event_type=1, dur=0.002):
        self.events.append( [string, time, pos, dur, strength, event_type] )