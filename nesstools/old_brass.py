# BRass instrument class
import random as r

#___________________________________________________________
#___________________________________________________________
class BrassInstrument(object):
    def __init__(self, size, name="Quick Brass Instrument"):
        self.name = name
        self.fs = 44100;                                    # FS
        self.temperature = 21                               # temperature
        self.length = size                                  # in millimetres I think. So 10000 is long
        vPosA = size * (r.random()*0.8 + 0.1)
        vPosB = size * (r.random()*0.8 + 0.1)
        vPosC = size * (r.random()*0.8 + 0.1)
        self.valvePositions = [vPosA, vPosB, vPosC]         # vpos, in millimetres along the length
        self.shortestTubeLengths = [20, 20, 20]             # vdl, note: I think this means when they're shut?? CHECK WITH STEFAN
        vSizeA = r.random()*1500 + 500
        vSizeB = r.random()*1500 + 500
        vSizeC = r.random()*1500 + 500
        self.tubeLengths = [vSizeA, vSizeB, vSizeC]          # vbl, 30 - 2000 ish?
        self.mpLength = 20                                     # xmeg, mouthpiece length 10 - 30?
        self.mpDiameter = 25                                # rmeg, mouthpiece diameter 10-40?
        self.middleSectionLengths = [(r.random()*600 + 60) for i in range(3)]      # x0eg, middle section lengths in mm (60 - 700?) - for different diameters
        self.middleSectionProfiles = [[7,14,3], [14,14,1], [14,30,1]]   #r0eg, middle section diameter (mm) and profile specifications (??)
                                                        # final format: [4, 9, 3; 9, 12, 1; 12, 12, 1];
        self.endDiameter = 200;                             #rbeg, end diameter in mm
        self.flarePower = 1.6;                                #fbeg, flare power? (1-6??)

    def write(self, fName):
        print( "writing "+self.name+" as: "+fName)
        out = open(fName, "w");
        #%3 valved trombone
        out.write("% "+self.name+"\n\n")
        out.write('custominstrument=1;\n')
        out.write('FS=%.0f;\n' % self.fs)
        out.write('temperature=%.1f;\n' % self.temperature)
        out.write('vpos=[%.1f, %.1f, %.1f];\n' % (self.valvePositions[0], self.valvePositions[1], self.valvePositions[2])) 
        out.write('vdl=[%.1f, %.1f, %.1f];\n'  % (self.shortestTubeLengths[0], self.shortestTubeLengths[1], self.shortestTubeLengths[2]))
        out.write('vbl=[%.1f, %.1f, %.1f]\n' % (self.tubeLengths[0], self.tubeLengths[1], self.tubeLengths[2]))
        out.write('xmeg=%.0f;\n' % self.mpLength)
        out.write('x0eg=[%.1f, %.1f, %.1f];\n' % (self.middleSectionLengths[0], self.middleSectionLengths[1], self.middleSectionLengths[2]))
        out.write('Leg=%.1f;\n' % self.length)       # tube length
        out.write('rmeg=%.0f;\n' % self.mpDiameter)
        out.write('r0eg=[%.0f, %.0f, %.0f; ' % (self.middleSectionProfiles[0][0], self.middleSectionProfiles[0][1], self.middleSectionProfiles[0][2]))
        out.write('%.0f, %.0f, %.0f; ' % (self.middleSectionProfiles[1][0], self.middleSectionProfiles[1][1], self.middleSectionProfiles[1][2]))
        out.write('%.0f, %.0f, %.0f];\n' % (self.middleSectionProfiles[2][0], self.middleSectionProfiles[2][1], self.middleSectionProfiles[2][2]))
        out.write('rbeg=%.1f;\n' % self.endDiameter)
        out.write('fbeg=%.1f;\n' % self.flarePower) # ??
        out.close()

#___________________________________________________________
#___________________________________________________________
class BrassScore(object):
    def __init__(self, time, name="Quick Brass Score", lipArea=1.3e-5, lipMass=5.37e-5, damping=3, H=0.00029, width=0.01):
        self.name = name
        self.time = time
        self.lipArea = [[0, lipArea]]            #Sr, 0.0000146 is for bigger instruments
        self.lipMass = [[0, lipMass]]            # mu, again, 5.37e-5 is for bigger instruments
        self.damping = [[0, damping]]             # sigma, 2-6?
        self.H = [[0, H]]                        # H
        self.width = [[0, width]]                # w
        self.noiseamp = [[0, 0.0]]
        self.vibamp = [[0, 0.0]]
        self.vibfreq = [[0, 0.0]]
        self.valvevibamp = [[0, 0, 0, 0]]
        self.valvevibfreq = [[0, 0, 0, 0]]
        self.valveopening = []
        self.lip_frequency = []
        self.pressure = []
        self.maxout = 0.95


    def write(self, fName):
        print( "writing "+self.name+" as: "+fName )
        out = open(fName, "w");
        out.write('% '+self.name+"\n\n")
        out.write('maxout=%.3f;\n' % self.maxout)
        out.write('T=%.0f;\n' % self.time)
        out.write('\n')

        out.write('Sr='+writePairs(self.lipArea)+'\n')
        out.write('mu='+writePairs(self.lipMass)+'\n')
        out.write('sigma='+writePairs(self.damping)+'\n')
        out.write('H='+writePairs(self.H)+'\n')
        out.write('w='+writePairs(self.width)+'\n')
        out.write('\n')

        out.write('lip_frequency='+writePairs(self.lip_frequency)+'\n')
        out.write('\n')
        out.write('pressure='+writePairs(self.pressure)+'\n')
        out.write('\n')

        out.write('vibamp='+writePairs(self.vibamp)+'\n')
        out.write('vibfreq='+writePairs(self.vibfreq)+'\n')
        out.write('tremamp=[0,0];')
        out.write('tremfreq=[0,0];')
        out.write('noiseamp='+writePairs(self.noiseamp)+'\n')
        out.write('\n')

        out.write('valveopening='+writeQuads(self.valveopening)+'\n')
        out.write('valvevibamp='+writeQuads(self.valvevibamp)+'\n')
        out.write('valvevibfreq='+writeQuads(self.valvevibfreq)+'\n')



#___________________________________________________________
#___________________________________________________________
def mtof(midinote):
    return 440 * pow(2, (midinote-69)/12.0)

def writePairs(pairs):
    """ return string formatted time/val pairs for scores """
    outString = "["
    for i, pair in enumerate(pairs):
        outString += str(pair[0])+","
        outString += str(pair[1])
        if i!=(len(pairs)-1): outString+='; '
    outString += "];"
    return outString

def writeQuads(quads):
    """ return string formatted time/val pairs for scores """
    outString = "["
    for i, quad in enumerate(quads):
        outString += str(quad[0])+","
        outString += str(quad[1])+","
        outString += str(quad[2])+","
        outString += str(quad[3])
        if i!=(len(quads)-1): outString+='; '
    outString += "];"
    return outString

