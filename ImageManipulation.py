from PIL import Image, ImageDraw
from random import randint

def main():
    cellDimension = int(input("Cell Dimension? : "))
    numberOfCols = int(input("Number of Columns? : "))
    numberOfRows = int(input("Number of Rows? : "))
    rule = int(input("Rule Number? : "))
    # Note: 73 is the super cool futuristic one
    filename = input("File Name? : ")

    # Settings
    active = ["#483C6C", "#433765", "#726A99"]
    inactive = ["#FF217C", "#FD207A", "#FFA283"]

    result = Image.new("RGB", (numberOfCols * cellDimension, numberOfRows * cellDimension), "white")
    resultPixels = result.load()
    xSize = result.size[0]
    ySize = result.size[1]

    active = [string.lower() for string in active]
    inactive = [string.lower() for string in inactive]
    dr = ImageDraw.Draw(result)
    randomizeFirstRow()
    
    r = makeRule(rule)
    for y in range(cellDimension, numberOfRows * cellDimension, cellDimension):
        for x in range(0, numberOfCols * cellDimension, cellDimension):
            pSCoordinates = prevSelf(x, y)
            pLCoordinates = prevLeft(x, y)
            pRCoordinates = prevRight(x, y)

            pS = resultPixels[pSCoordinates[0], pSCoordinates[1]]
            pL = resultPixels[pLCoordinates[0], pLCoordinates[1]]
            pR = resultPixels[pRCoordinates[0], pRCoordinates[1]]

            data = [isActive(pL), isActive(pS), isActive(pR), x, y]
            checkRules(data, [1, 1, 1], r[0])
            checkRules(data, [1, 1, 0], r[1])
            checkRules(data, [1, 0, 1], r[2])
            checkRules(data, [1, 0, 0], r[3])
            checkRules(data, [0, 1, 1], r[4])
            checkRules(data, [0, 1, 0], r[5])
            checkRules(data, [0, 0, 1], r[6])
            checkRules(data, [0, 0, 0], r[7])

    result.save(filename + ".jpg", format='JPEG', subsampling=0, quality=100)

def makeRule(ruleNum):
    out = []
    binary = '{0:08b}'.format(ruleNum)
    for digit in binary:
        if digit == '1':
            out.append(True)
        else:
            out.append(False)
    return out

def randomizeFirstRow():
    for x in range(0, numberOfCols * cellDimension, cellDimension):
        randomChoice = randint(0, 1)
        newColor = (0, 0, 0)
        ActiveIndex = randint(0, len(active) - 1)
        InactiveIndex = randint(0, len(inactive) - 1)
        if randomChoice == 1:
            newColor = active[ActiveIndex]
        else:
            newColor = inactive[InactiveIndex]

        if resultPixels[x, 0] == (255, 255, 255):
            dr.rectangle(((x, 0), (x + cellDimension-1, cellDimension-1)), fill=newColor)

def prevSelf(x, y):
    return (x, y - cellDimension)

def prevLeft(x, y):
    if x == 0:
        x = xSize - cellDimension
    else:
        x = x - cellDimension
    return (x, y - cellDimension)

def prevRight(x, y):
    if x == xSize - cellDimension:
        x = 0
    else:
        x = x + cellDimension
    return (x, y - cellDimension)

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def isActive(color):
    return rgb_to_hex(color) in active

def setState(x, y, state):
    ActiveColorIndex = randint(0, len(active) - 1)
    InactiveColorIndex = randint(0, len(inactive) - 1)
    if state:
        dr.rectangle(((x, y), (x + cellDimension-1, y + cellDimension-1)), fill=active[ActiveColorIndex])
    else:
        dr.rectangle(((x, y), (x + cellDimension-1, y + cellDimension-1)), fill=inactive[InactiveColorIndex])

def checkRules(data, rule, ruleOutcome):
    # data = [pLState, pSState, pRState, x, y]
    onOffArray = [data[0], data[1], data[2]]

    if onOffArray == rule:
        setState(data[3], data[4], ruleOutcome)

if __name__ == "__main__":
    main()
