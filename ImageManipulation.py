from PIL import Image, ImageDraw
from random import randint

class CellularAutomaton:
    
    def __init__(self, cD, nC, nR, r, act=["#483C6C", "#433765", "#726A99"], inact=["#FF217C", "#FD207A", "#FFA283"]):
        self.cellDimension = cD
        self.numberOfCols = nC
        self.numberOfRows = nR
        self.rule = self.makeRule(r)

        self.result = Image.new("RGB", (nC * cD, nR * cD), "white")
        self.resultPixels = self.result.load()
        self.xSize = self.result.size[0]
        self.ySize = self.result.size[1]

        self.active = [string.lower() for string in act]
        self.inactive = [string.lower() for string in inact]

        self.dr = ImageDraw.Draw(self.result)

    def makeRule(self, ruleNum):
        out = []
        binary = '{0:08b}'.format(ruleNum)
        for digit in binary:
            if digit == '1':
                out.append(True)
            else:
                out.append(False)
        return out

    def randomizeFirstRow(self):
        for x in range(0, self.numberOfCols * self.cellDimension, self.cellDimension):
            randomChoice = randint(0, 1)
            newColor = (0, 0, 0)
            ActiveIndex = randint(0, len(self.active) - 1)
            InactiveIndex = randint(0, len(self.inactive) - 1)
            if randomChoice == 1:
                newColor = self.active[ActiveIndex]
            else:
                newColor = self.inactive[InactiveIndex]

            if self.resultPixels[x, 0] == (255, 255, 255):
                self.dr.rectangle(((x, 0), (x + self.cellDimension-1, self.cellDimension-1)), fill=newColor)

    def make(self):
        self.randomizeFirstRow()
        
        for y in range(self.cellDimension, self.numberOfRows * self.cellDimension, self.cellDimension):
            for x in range(0, self.numberOfCols * self.cellDimension, self.cellDimension):
                pSCoordinates = self.prevSelf(x, y)
                pLCoordinates = self.prevLeft(x, y)
                pRCoordinates = self.prevRight(x, y)

                pS = self.resultPixels[pSCoordinates[0], pSCoordinates[1]]
                pL = self.resultPixels[pLCoordinates[0], pLCoordinates[1]]
                pR = self.resultPixels[pRCoordinates[0], pRCoordinates[1]]

                data = [self.isActive(pL), self.isActive(pS), self.isActive(pR), x, y]
                self.checkRules(data, [1, 1, 1], self.rule[0])
                self.checkRules(data, [1, 1, 0], self.rule[1])
                self.checkRules(data, [1, 0, 1], self.rule[2])
                self.checkRules(data, [1, 0, 0], self.rule[3])
                self.checkRules(data, [0, 1, 1], self.rule[4])
                self.checkRules(data, [0, 1, 0], self.rule[5])
                self.checkRules(data, [0, 0, 1], self.rule[6])
                self.checkRules(data, [0, 0, 0], self.rule[7])

    def save(self, filename):
        self.result.save(filename + ".jpg", format='JPEG', subsampling=0, quality=100)
        return True
        
    def prevSelf(self, x, y):
        return (x, y - self.cellDimension)

    def prevLeft(self, x, y):
        if x == 0:
            x = self.xSize - self.cellDimension
        else:
            x = x - self.cellDimension
        return (x, y - self.cellDimension)

    def prevRight(self, x, y):
        if x == self.xSize - self.cellDimension:
            x = 0
        else:
            x = x + self.cellDimension
        return (x, y - self.cellDimension)

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb

    def isActive(self, color):
        return self.rgb_to_hex(color) in self.active

    def setState(self, x, y, state):
        ActiveColorIndex = randint(0, len(self.active) - 1)
        InactiveColorIndex = randint(0, len(self.inactive) - 1)
        if state:
            self.dr.rectangle(((x, y), (x + self.cellDimension-1, y + self.cellDimension-1)), fill=self.active[ActiveColorIndex])
        else:
            self.dr.rectangle(((x, y), (x + self.cellDimension-1, y + self.cellDimension-1)), fill=self.inactive[InactiveColorIndex])

    def checkRules(self, data, rule, ruleOutcome):
        # data = [pLState, pSState, pRState, x, y]
        onOffArray = [data[0], data[1], data[2]]

        if onOffArray == rule:
            self.setState(data[3], data[4], ruleOutcome)
'''
# Note: 73 is the super cool futuristic one
filename = input("File Name? : ")

# Settings
active = ["#483C6C", "#433765", "#726A99"]
inactive = ["#FF217C", "#FD207A", "#FFA283"]
'''
