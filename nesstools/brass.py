# BRass instrument class
import random as r

#___________________________________________________________
#___________________________________________________________
class BrassInstrument(object):
    def __init__(self, size, name="Quick Brass Instrument"):
        self.name = name
        self.fs = 44100;                                    # FS
        self.temperature = 20                               # temperature
        self.length = size                                  # in millimetres I think. So 10000 is long
        vPosA = size * (r.random()*0.8 + 0.1)
        vPosB = size * (r.random()*0.8 + 0.1)
        vPosC = size * (r.random()*0.8 + 0.1)
        self.valvePositions = [vPosA, vPosB, vPosC]         # vpos, in millimetres along the length
        self.valvePositions.sort()                          # need to be in order?
        self.shortestTubeLengths = [20, 20, 20]             # vdl, 30 - 2000
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
        out.write("% brversion 1.0\n% "+self.name+"\n\n")
        
        out.write("%===============================\n%==== SETUP ====\n")
        out.write('custominstrument=1;   % this is 0 if you have a real instrument bore\n\n')
        out.write('% Sample rate\n')
        out.write('FS=%.0f;\n\n' % self.fs)

        out.write('% Temperature in C\n')
        out.write('temperature=%.1f;\n\n' % self.temperature)

        out.write("%===============================\n%==== MAIN TUBE ====\n\n")
        out.write('% Instrument Length\n')
        out.write('Leg=%.1f;\n\n' % self.length)       # tube length
        out.write('% Middle Section Lengths\n')
        out.write('x0eg='+writeArray(self.middleSectionLengths)+'\n\n')
        out.write("% Middle Section Profiles\n% NOTE: don't need to sum to length.\n% in addition to middle sections we have 2 additional sections: mouthpiece and flare section\n% Must have 3 columns and have the same number of rows as entries for the middle section lengths. \n % First and second entries of each row are the diameters[mm] used in the bore definition. \n% The third entry specifies the type of profile: \n%%% 1 - linear ramp between the two diameters, \n%%% 2 - squared sine bulge whose entrance and exit diameters are the first column entry and maximum is the second diameter entry, \n%%% 3 - cosine ramp between the two diameters.\n")
        out.write('r0eg='+write2DArray(self.middleSectionProfiles)+'\n')
        out.write('% end diameter of instrument (curves outwards from last middle section length to this diameter)\n')
        out.write('rbeg=%.1f;\n' % self.endDiameter)
        out.write('% flare curve exponent for above end diameter\n')
        out.write('fbeg=%.1f;\n\n' % self.flarePower) # ??

        out.write("%===============================\n%==== VALVES ====\n\n")
        out.write('% position of valve in mm\n')
        out.write('vpos='+writeArray(self.valvePositions)+'\n')
        out.write('% default (shortest) tube length mm\n')
        out.write('vdl='+writeArray(self.shortestTubeLengths)+'\n')
        out.write('% bypass (longest) tube length mm (will add default length to either side of bypass tubes)\n')
        out.write('vbl='+writeArray(self.tubeLengths)+'\n\n')
        
        
        out.write("%===============================\n%==== MOUTHPIECE ====\n\n")
        out.write('% mouthpiece length\n')
        out.write('xmeg=%.0f;\n' % self.mpLength)
        out.write('% mouthpiece diameter\n')
        out.write('rmeg=%.0f;\n' % self.mpDiameter)
        
        #out.write('r0eg=[%.0f, %.0f, %.0f; ' % (self.middleSectionProfiles[0][0], self.middleSectionProfiles[0][1], self.middleSectionProfiles[0][2]))
        #out.write('%.0f, %.0f, %.0f; ' % (self.middleSectionProfiles[1][0], self.middleSectionProfiles[1][1], self.middleSectionProfiles[1][2]))
        #out.write('%.0f, %.0f, %.0f];\n' % (self.middleSectionProfiles[2][0], self.middleSectionProfiles[2][1], self.middleSectionProfiles[2][2]))
        
        
        out.close()

    def deepTrombone(self):
        self.length = 3740                                  # in millimetres I think. So 10000 is long
        self.valvePositions = [540, 630, 1460]         # vpos, in millimetres along the length
        self.shortestTubeLengths = [20, 20, 20]             # vbl, bypass lengths
        self.tubeLengths = [239.7, 97.5, 449.8]          # vdl, 30 - 2000
        self.mpLength = 30                                     # xmeg, mouthpiece length 10 - 30
        self.mpDiameter = 25                                # rmeg, mouthpiece diameter 10-40
        self.middleSectionLengths = [100, 2320, 623]      # x0eg, middle section lengths in mm (60 - 700?) - for different diameters
        self.middleSectionProfiles = [[7,14,3], [14,14,1], [14,30,1]]   #r0eg, middle section difameter (mm) and profile specifications (??)
        self.endDiameter = 200;                             #rbeg, end diameter in mm
        self.flarePower = 2;                          # fbeg

    def trumpet(self):
        self.length = 1400                                  # in millimetres I think. So 10000 is long
        self.valvePositions = [600, 630, 660]         # vpos, in millimetres along the length
        self.shortestTubeLengths = [20, 20, 20]             # vdl, 30 - 2000
        self.tubeLengths = [130.7, 57.5, 199.8]          # vbl, 30 - 2000 ish?
        self.mpLength = 10                                     # xmeg, mouthpiece length 10 - 30?
        self.mpDiameter = 20                                # rmeg, mouthpiece diameter 10-40?
        self.middleSectionLengths = [80, 200, 545]      # x0eg, middle section lengths in mm (60 - 700?) - for different diameters
        self.middleSectionProfiles = [[4, 9, 3], [9, 12, 1], [12, 12, 1]]   #r0eg, middle section diameter (mm) and profile specifications (??)
        self.endDiameter = 130;                             #rbeg, end diameter in mm
        self.flarePower = 6;                          # fbeg

    def trombone(self):
        self.length = 2740                                  # in millimetres I think. So 10000 is long
        self.valvePositions = [600]         # vpos, in millimetres along the length
        self.shortestTubeLengths = [20]      
        self.tubeLengths = [130.7]          # vbl, 30 - 2000 ish?
        self.mpLength = 30                                     # xmeg, mouthpiece length 10 - 30?
        self.mpDiameter = 25                                # rmeg, mouthpiece diameter 10-40?
        self.middleSectionLengths = [60, 1820, 600]      # x0eg, middle section lengths in mm (60 - 700?) - for different diameters
        self.middleSectionProfiles = [[7, 14, 3], [14, 14, 1], [14, 30, 1]]   #r0eg, middle section diameter (mm) and profile specifications (??)
        self.endDiameter = 220;                             #rbeg, end diameter in mm
        self.flarePower = 2;                          # fbeg

    def horn(self):
        self.length = 4520                                  # in millimetres I think. So 10000 is long
        self.valvePositions = [600, 630, 660]         # vpos, in millimetres along the length
        self.shortestTubeLengths = [20, 20, 20]      # # vdl, 30 - 2000
        self.tubeLengths = [130.7, 57.5, 199.8]          # vbl, 30 - 2000 ish?
        self.mpLength = 30                                     # xmeg, mouthpiece length 10 - 30?
        self.mpDiameter = 18                                # rmeg, mouthpiece diameter 10-40?
        self.middleSectionLengths = [35, 800, 1650, 1300, 400]      # x0eg, middle section lengths in mm (60 - 700?) - for different diameters
        self.middleSectionProfiles = [[5, 8, 3], [8, 11, 1], [11, 11, 1], [11, 15, 1], [15, 30, 1]]   #r0eg, middle section diameter (mm) and profile specifications (??)
        self.endDiameter = 190;                             #rbeg, end diameter in mm
        self.flarePower = 2;                          # fbeg

    def longInstrument(self):
        self.length = 10000                                  
        self.valvePositions = [3500, 4000, 4500]        
        self.shortestTubeLengths = [20, 20, 20]      
        self.tubeLengths = [1224, 594.6, 1892]          
        self.mpLength = 30                                    
        self.mpDiameter = 40                                
        self.middleSectionLengths = [80, 200, 1000, 5000, 695]      
        self.middleSectionProfiles = [[20, 25, 3], [25, 28, 1], [28, 34, 1], [34, 40, 2], [34, 34, 1]]   #r0eg, middle section diameter (mm) and profile specifications (??)
        self.endDiameter = 500;                             #rbeg, end diameter in mm
        self.flarePower = 1.9;                          # fbeg

    def trumpetBulge(self):
        self.length = 1400                                  
        self.valvePositions = [600, 630, 660]        
        self.shortestTubeLengths = [20, 20, 20]      
        self.tubeLengths = [130.7,57.5,199.8]          # vbl, 30 - 2000 ish?
        self.mpLength = 10                                     # xmeg, mouthpiece length 10 - 30?
        self.mpDiameter = 20                                # rmeg, mouthpiece diameter 10-40?
        self.middleSectionLengths = [80,200,695]      # x0eg, middle section lengths in mm (60 - 700?) - for different diameters
        self.middleSectionProfiles = [[4, 9, 3], [9, 12, 1], [12, 60, 2]]
        self.endDiameter = 130;                             #rbeg, end diameter in mm
        self.flarePower = 6;                          # fbeg


#___________________________________________________________
#___________________________________________________________
class BrassScore(object):
    def __init__(self, time, name="Quick Brass Score", valveCount=3, lipArea=1.3e-5, lipMass=5.37e-5, damping=3, H=0.00029, width=0.01):
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
        self.valveCount = valveCount
        self.valvevibamp = [[0 for i in range(self.valveCount)]]
        self.valvevibfreq = [[0 for i in range(self.valveCount)]]
        self.valveopening = []
        self.lip_frequency = []
        self.pressure = []
        self.presets = []
        self.maxout = 0.95

    def breakpointsFromList(self, paramList, startTime=0, endTime=10, glideTime=0.005):
        breakpoints = []
        dt = (endTime-startTime) / float(len(paramList))
        t = startTime
        prevVal = 0
        for i, val in enumerate(paramList):
            if (i>0):
                breakpoints.append([t-glideTime, prevVal])
            breakpoints.append([t, val])
            prevVal = val
            t+=dt
        return breakpoints

    def percussiveEvent(self, startTime=0, duration=3, maxP=20000, lf=20):
        self.pressure += [[startTime, 0.0], [startTime+0.001, maxP], [startTime+duration*0.5, maxP], [startTime+duration, 0]]
        self.lip_frequency += [[startTime, lf], [startTime+duration*0.9, lf]]

    def valvePercussiveEvent(self, startTime=0, duration=3, maxP=6000, valveStates=[0, 0, 0]):
        self.pressure += [[startTime, 0.0], [startTime+0.001, maxP], [startTime+duration*0.5, maxP], [startTime+duration, 0]]
        self.valveopening += [[startTime, valveStates[0], valveStates[1], valveStates[2]], [startTime+duration*0.9, valveStates[0], valveStates[1], valveStates[2]]]

    def valveEvent(self, startTime=0, dur=3, valveStates=[0, 0, 0]):
        if (len(valveStates) == self.valveCount):
            self.valveopening += [[startTime, valveStates[0], valveStates[1], valveStates[2]], [startTime+dur*0.9, valveStates[0], valveStates[1], valveStates[2]]]
        else:
            valveArray = [startTime]
            valveArrayEnd = [startTime + dur*0.9]
            for i in range(self.valveCount):
                valveArray.append(valveStates[i])
                valveArrayEnd.append(valveStates[i])
            self.valveopening += [valveArray, valveArrayEnd]

    def randomiseAll(self, t, maxPressure=10000):
        self.pressure += [[t, r.randint(0, maxPressure)]]
        self.lip_frequency += [[t, r.random()*r.random()*r.random()*660 + 20]]
        self.valveopening += [[t, r.random(), r.random(), r.random()]]
        if (r.random() < 0.2): self.noiseamp += [[t, r.random()*r.random()*r.random()]]
        else: self.noiseamp += [[t, 0]]
        if (r.random() < 0.2): 
            self.valvevibamp = [[t, r.random()*r.random()*r.random()*r.random(), r.random()*r.random()*r.random()*r.random(), r.random()*r.random()*r.random()*r.random()]]
            self.valvevibfreq = [[t, r.random()*r.random()*50, r.random()*r.random()*15, r.random()*r.random()*20]]
        else: self.valvevibamp = [[t, 0, 0, 0]]
        self.damping = [[t, r.randint(1, 7)]]
        self.width = [[t, r.randint(1, 10)*0.0025]]

    def randomiseAndHoldAll(self, t, dur=1, maxPressure=10000):
        newPressure = r.randint(0, maxPressure)
        newLF = r.random()*r.random()*r.random()*660 + 20
        newValves = [r.random() for i in range(3)]
        newNoise = 0
        if r.random() < 0.2: newNoise = r.random()*r.random()*r.random()
        newvalvevibamp = [0, 0, 0]
        newvalvevibfreq = [r.random()*r.random()*50, r.random()*r.random()*15, r.random()*r.random()*20]
        if r.random() < 0.2: newvalvevibamp = [r.random()*r.random()*r.random()*r.random(), r.random()*r.random()*r.random()*r.random(), r.random()*r.random()*r.random()*r.random()]
        newDamping = r.randint(1, 7)
        newWidth = r.randint(1, 10)*0.0025
        self.pressure += [[t, newPressure], [t+dur, newPressure]]
        self.lip_frequency += [[t, newLF], [t+dur, newLF]]
        self.valveopening += [[t, newValves[0], newValves[1], newValves[2]], [t+dur, newValves[0], newValves[1], newValves[2]]]
        self.noiseamp += [[t, newNoise], [t+dur, newNoise]]
        self.valvevibamp = [[t, newvalvevibamp[0], newvalvevibamp[1], newvalvevibamp[2]], [t+dur, newvalvevibamp[0], newvalvevibamp[1], newvalvevibamp[2]]]
        self.valvevibfreq = [[t, newvalvevibfreq[0], newvalvevibfreq[1], newvalvevibfreq[2]], [t+dur, newvalvevibfreq[0], newvalvevibfreq[1], newvalvevibfreq[2]]]
        self.damping = [[t, newDamping], [t+dur, newDamping]]
        self.width = [[t, newWidth], [t+dur, newWidth]]

    def createRandomPreset(self, presetName="Randomised Preset", maxPressure=8000):
        if presetName == "Randomised Preset":
            presetName += " "+str(len(self.presets)+1)
        newPressure = r.randint(0, maxPressure)
        newLF = r.random()*r.random()*r.random()*660 + 20
        newValves = [r.random() for i in range(3)]
        newNoise = 0
        if r.random() < 0.2: newNoise = r.random()*r.random()*r.random()
        newvalvevibamp = [0, 0, 0]
        newvalvevibfreq = [r.random()*r.random()*50, r.random()*r.random()*15, r.random()*r.random()*20]
        if r.random() < 0.2: newvalvevibamp = [r.random()*r.random()*r.random()*r.random(), r.random()*r.random()*r.random()*r.random(), r.random()*r.random()*r.random()*r.random()]
        newDamping = r.randint(1, 7)
        newWidth = r.randint(1, 10)*0.0025
        newPreset = [ "Randomised"  ]
        newPreset = {'name': presetName, 'pressure': newPressure, 'lf': newLF, 'valveopenings': newValves, 'noise': newNoise, 'valvevibamp': newvalvevibamp, 'valvevibfreq': newvalvevibfreq, 'damping': newDamping, 'width': newWidth}
        print ("Created new preset: ", newPreset['name'])
        print ("Stored as preset : ", len(self.presets))
        self.presets.append( newPreset )

    def schedulePreset(self, t, presetNum):
        if (self.presets[presetNum]):
            p = self.presets[presetNum]
            self.pressure += [[t, p['pressure'] ]]
            self.lip_frequency += [[t, p['lf'] ]]
            self.valveopening += [[t, p['valveopenings'][0], p['valveopenings'][1], p['valveopenings'][2]]]
            self.noiseamp += [[t, p['noise'] ]]
            self.valvevibamp = [[t, p['valvevibamp'][0], p['valvevibamp'][1], p['valvevibamp'][2] ]]
            self.valvevibfreq = [[t, p['valvevibfreq'][0], p['valvevibfreq'][1], p['valvevibfreq'][2] ]]
            self.damping = [[t, p['damping'] ]]
            self.width = [[t, p['width'] ]]
        else:
            print("no such preset??")

    def scheduleAndHoldPreset(self, t, dur=1, presetNum=0):
        if (self.presets[presetNum]):
            p = self.presets[presetNum]
            self.pressure += [[t, p['pressure']], [t+dur, p['pressure'] ]]
            self.lip_frequency += [[t, p['lf']], [t+dur, p['lf'] ]]
            self.valveopening += [[t, p['valveopenings'][0], p['valveopenings'][1], p['valveopenings'][2]], [t+dur, p['valveopenings'][0], p['valveopenings'][1], p['valveopenings'][2] ]]
            self.noiseamp += [[t, p['noise'] ], [t+dur, p['noise'] ]]
            self.valvevibamp = [[t, p['valvevibamp'][0], p['valvevibamp'][1], p['valvevibamp'][2] ], [t+dur, p['valvevibamp'][0], p['valvevibamp'][1], p['valvevibamp'][2] ]]
            self.valvevibfreq = [[t, p['valvevibfreq'][0], p['valvevibfreq'][1], p['valvevibfreq'][2] ], [t+dur, p['valvevibfreq'][0], p['valvevibfreq'][1], p['valvevibfreq'][2] ]]
            self.damping = [[t, p['damping'] ], [t+dur, p['damping'] ]]
            self.width = [[t, p['width'] ], [t+dur, p['width'] ]]
        else:
            print("no such preset??")

    def write(self, fName):
        print( "writing "+self.name+" as: "+fName )
        out = open(fName, "w");
        out.write('% '+self.name+"\n\n")
        out.write('maxout=%.3f;\n' % self.maxout)
        out.write('T=%.0f;\n' % self.time)
        out.write('\n')

        out.write('Sr='+write2DArray(self.lipArea)+'\n')
        out.write('mu='+write2DArray(self.lipMass)+'\n')
        out.write('sigma='+write2DArray(self.damping)+'\n')
        out.write('H='+write2DArray(self.H)+'\n')
        out.write('w='+write2DArray(self.width)+'\n')
        out.write('\n')

        out.write('lip_frequency='+write2DArray(self.lip_frequency)+'\n')
        out.write('\n')
        out.write('pressure='+write2DArray(self.pressure)+'\n')
        out.write('\n')

        out.write('vibamp='+write2DArray(self.vibamp)+'\n')
        out.write('vibfreq='+write2DArray(self.vibfreq)+'\n')
        out.write('tremamp=[0,0];')
        out.write('tremfreq=[0,0];')
        out.write('noiseamp='+write2DArray(self.noiseamp)+'\n')
        out.write('\n')

        out.write('valveopening='+write2DArray(self.valveopening)+'\n')
        out.write('valvevibamp='+write2DArray(self.valvevibamp)+'\n')
        out.write('valvevibfreq='+write2DArray(self.valvevibfreq)+'\n')



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

def write2DArray(inList):
    outString = "["
    for i, subList in enumerate(inList):
        for j, element in enumerate(subList):
            outString += str(element)
            if (j!=len(subList)-1):
                outString += ","
        if i!=(len(inList)-1): outString += "; "
    outString += "];"
    return outString

def writeArray(inList):
    outString = "["
    for i, element in enumerate(inList):
        outString += str(element)
        if (i!=len(inList)-1):
            outString += ","
    outString += "];"
    return outString

