import random as r
import os
from shutil import copyfile, move
# fr MIDI strings
import midi

from midiutil.MidiFile import MIDIFile


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


maxStrings = 1
scoreInput = "/Users/tmudd/Desktop/scores_to_convert/well_tuned_guitar_5251_score.m"
midiOutput = scoreInput+".mid"

# first channel is plucks, second channel is fingers
midiData = MIDIFile(2)
midiData.addTempo(0, 0, 120)
midiData.addTempo(1, 0, 120)

lookForFingers = False
fCount = 1

plucks = []
fingers = []

scoreData = open(scoreInput, 'r')
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
        if str(fCount)+", [" in line or str(fCount)+",[" in line:
            fCount += 1
            subsections = line.split("[")
            stringNum = (int(subsections[0].split(",")[0]))
            fingerEvents = subsections[1].split(";")
            for event in fingerEvents:
                elements = event.lstrip().rstrip().split(" ")  # remove pre and post whitespace first
                if len(elements) == 3:
                    #print(elements)
                    fingers.append(Finger(stringNum, float(elements[0]), float(elements[1]), float(elements[2])) )
            #Finger.append()
            #fingers.append(subsections)
            
            if stringNum > maxStrings:
                maxStrings = stringNum
            #subsubsections = subsections[1].split(";")
        #print(line)
   


previousPos = 0
for i, finger in enumerate(fingers):
    if i==0:
        previousPos = finger.pos
    else:
        if previousPos != finger.pos:
            # fingers on channel 2 (==1)
            #print(finger.pos)
            velocity = finger.force * 100
            if velocity > 127: velocity = 127
            midiData.addNote(1, 1, int(finger.pos * 100) + 12, finger.t*2, 0.5, velocity)

for pluck in plucks:
    midiData.addNote(0, 1, 60, pluck.t*2, 0.5, pluck.force * 100)

print("maxstrings: ", maxStrings, fCount)
# channel, ?, midi note, start time in BEATS, duration, velocity
#midiData.addNote(0, 1, 60, 2, 0.5*2, 100)
#midiData.addNote(0, 1, 67, 4, 0.5*2, 100)
#midiData.addNote(0, 1, note, t*2, dur*2, 100)



binfile = open(midiOutput, 'wb')
midiData.writeFile(binfile)
binfile.close()