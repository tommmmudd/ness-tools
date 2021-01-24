# NESS FUNCTIONS!!
from . import brass
import random as r
import os
from shutil import copyfile, move


class PatternSet(object):
    def __init__(self):
        self.patterns = []
        self.currentPatternIndex = 0
        self.repetitions = 0

    def setCurrentPatternIndex(self, newIndex):
        self.currentPatternIndex = 0 
        self.currentPatternIndex %= len(self.patterns)
        self.repetitions = 0

    def addPattern(self, newPattern):
        self.patterns.append(Sequence(newPattern))

    def addRandomPatternFromSet(self, newSet, length=8):
        newPattern = [newSet[r.randint(0, len(newSet)-1)] for i in range(length)]
        self.patterns.append(Sequence(newPattern))

    def step(self):
        output = self.patterns[self.currentPatternIndex].step()
        if self.isAboutToLoop:
            self.repetitions += 1
        return output

    def getCurrent(self):
        return self.patterns[self.currentPatternIndex].getCurrent()

    def random(self):
        return self.patterns[self.currentPatternIndex].random()

    def isAboutToLoop(self):
        return self.patterns[self.currentPatternIndex].endFlag        


class Sequence(object):
    def __init__(self, initialArray):
        self.data = initialArray
        self.index = 0
        self.endFlag = True

    def step(self):
        self.index += 1
        if self.index >= len(self.data):
            self.index = 0
            self.endFlag = True
        else:
            self.endFlag = False
        return self.data[self.index]

    def getCurrent(self):
        return self.data[self.index]

    def rewind(self):
        self.index = 0

    def jumpTo(self, newIndex):
        self.index = newIndex
        self.index %= len(self.data)

    def set(self, newArray):
        self.data = newArray

    def random(self):
        return self.data[r.randint(0, len(self.data)-1)]

    def length(self):
        return len(self.data)




def chooseFrom(newSet):
    return newSet[r.randint(0, len(newSet)-1)]


class NESSProject:
    def __init__(self, scriptFile, folder="NESS_projects", projectName="new_project"):
        self.randomNum = r.randint(1000, 9999)
        self.dirname = folder
        self.projectName = projectName
        self.script = scriptFile
        self.directory = self.dirname+"/"+self.projectName+"_"+str(self.randomNum)
        self.instName = "inst_"+projectName+"_"+str(self.randomNum)+".m"
        self.scoreName = "score_"+projectName+"_"+str(self.randomNum)+".m"
        self.tabName = "tab_"+projectName+"_"+str(self.randomNum)+".txt"
        self.midiName = "midi_"+projectName+"_"+str(self.randomNum)+".mid"
        self.init()

    def init(self):
        print( "creating "+self.directory )
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            os.makedirs(self.directory+"/wavs")

    def getDirectory(self):
        return self.directory+"/"

    def write(self):
        copyfile(self.script, self.directory+"/"+os.path.basename(self.script))
        copyfile(os.path.realpath(__file__), self.directory+"/guitar.py")
        move(os.path.dirname(os.path.realpath(self.script))+"/"+self.scoreName, self.directory+"/"+self.scoreName)
        move(os.path.dirname(os.path.realpath(self.script))+"/"+self.instName, self.directory+"/"+self.instName)

