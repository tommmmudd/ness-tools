import random as r
import os
from shutil import copyfile, move

# convert breakpoints into a useful Max format
# plucks converted to triggers
# data should be importable into a coll
# e.g.
# index = string (stratign from 1)
# then pairs of time and position (don't worry about force for the moment)
# 0, 0 0 1.5 0 1.51 0.25



class Pluck:
    def __init__(self, sn, t, p, d, f):
        self.s = sn
        self.t = t
        self.pos = p
        self.pluckDur = d
        self.force = f


class Finger:
    def __init__(self, sn, t, p, f):
        self.s = sn
        self.t = t
        self.pos = p
        self.force = f


maxStrings = 6

#scoreInput = "/Users/tmudd/Downloads/guitar-tutorial/score_tutorial_10.m"
scoreInput = "/Users/tmudd/Documents/REAPER Media/Guitar Reaper for edits/rapid_mumble_7576/score_rapid_mumble_7576.m"
maxOutput = scoreInput[0:-2]+".txt"


lookForFingers = False
fCount = 1

plucks = []
fingers = []

scoreData = open(scoreInput, 'r')
textFile = open(maxOutput, 'w')

for line in scoreData:
    if ("exc = pluck_gen" in line):
        elements = line.split(",")
        #print(elements)
        stringNum = int(elements[1])
        t = float(elements[2])
        pos = float(elements[3])
        pluckDur = float(elements[4])
        pluckForce = float(elements[5].split(")")[0])
        plucks.append(Pluck(stringNum, t, pos, pluckDur, pluckForce) )
        if stringNum > maxStrings:
            maxStrings = stringNum

    elif "finger_def" in line:
        lookForFingers = True

    if lookForFingers:
        if str(fCount)+", [" in line or str(fCount)+",[" in line or str(fCount)+",  [" in line:
            fCount += 1

            subsections = line.split("[")
            stringNum = (int(subsections[0].split(",")[0]))
            fingerEvents = subsections[1].split(";")
            for event in fingerEvents:
                elements = event.lstrip().rstrip().split(" ")  # remove pre and post whitespace first
                if ("]" in elements[-1]):
                    elements[-1] = elements[-1].split("]")[0]
                if len(elements) == 3:
                    #print("elements", elements)
                    fingers.append(Finger(stringNum, float(elements[0]), float(elements[1]), float(elements[2])) )
            #Finger.append()
            #fingers.append(subsections)
            
            if stringNum > maxStrings:
                maxStrings = stringNum
            #subsubsections = subsections[1].split(";")
        #print(line)
   

lineNum = 0
previousPos = 0
prevT = [0 for i in range(maxStrings)]
fingerStrings = [str(i)+", " for i in range(maxStrings)]
pluckText = str(maxStrings) + ", "
for i, finger in enumerate(fingers):
    if i==0:
        previousPos = finger.pos
        prevT[finger.s-1] = finger.t
    else:
        if finger.t > 0 and finger.t > prevT[finger.s-1]:
            dt = finger.t - prevT[finger.s-1]
            print(dt)
            prevT[finger.s-1] = finger.t
            fingerStrings[finger.s-1] += "%.3f %.3f " % (finger.pos, dt * 1000)
        if previousPos != finger.pos:
            # fingers on channel 2 (==1)
            #print(finger.pos)
            velocity = finger.force * 100
            if velocity > 127: velocity = 127
            #midiData.addNote(maxStrings + (finger.s - 1), 1, int(finger.pos * 100) + 12, finger.t*2, 0.5, velocity)

for pluck in plucks:
    pluckText += "%d %.3f %.3f " % (pluck.s + maxStrings, pluck.t * 1000, pluck.force)
    

for f in fingerStrings:
    textFile.write(f + ";\n")

textFile.write(pluckText + ";\n")

print("maxstrings: ", maxStrings, fCount)
# channel, ?, midi note, start time in BEATS, duration, velocity
#midiData.addNote(0, 1, 60, 2, 0.5*2, 100)
#midiData.addNote(0, 1, 67, 4, 0.5*2, 100)
#midiData.addNote(0, 1, note, t*2, dur*2, 100)



textFile.close()
scoreData.close()