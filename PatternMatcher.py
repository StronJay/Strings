test, pat = "Fire! Fire! Dance with me!Fire! Fire! Dance with me!", "xxyxxy"
def patternMatcher(pattern, string):
    print(pattern, string)
    if len(string) < len(pattern):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"x": 0, "y": 0}
    firstYPos = getCountsAndFirstYPos(pattern, counts)
    print(didSwitch, counts)
    if counts["y"] != 0:
        for lenOfX in range(1, len(string)):
            lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"] 
            #print(lenOfY)
            if lenOfY <= 0 or lenOfY % 1 != 0:
                continue
            lenOfY = int(lenOfY)
            print("Made it through, now, float to int:", lenOfY)
            yIdx = firstYPos * lenOfX
            #print("first Y Position:", firstYPos, "* length Of X:", lenOfX, "= yIdx:",yIdx)
            x = string[:lenOfX]
            #print("x:", x)
            y = string[yIdx : yIdx + lenOfY]
            print("y:", y)
            potentialMatch = map(lambda char: x if char == "x" else y, newPattern)
            if string == "".join(potentialMatch):
                print("WOOOOOOOOOO!!!!!!!!", [x, y] if not didSwitch else [y, x])
    else:
        lenOfX = len(string) / counts["x"]
        print(len(string), counts["x"], lenOfX)
        if lenOfX % 1 == 0:
            lenOfX = int(lenOfX)
            print(lenOfX)
            x = string[:lenOfX]
            print(x)
            potentialMatch = map(lambda char: x, newPattern)
            print("".join(potentialMatch))
            if string == "".join(potentialMatch):
                print([x, ""] if not didSwitch else ["", x])
    return []

    
def getNewPattern(pattern):
    patternLetters = list(pattern)
    print(patternLetters)
    if pattern[0] == "x":
        return patternLetters
    else:
        return list(map(lambda char: "x" if char == "y" else "y", patternLetters))


def getCountsAndFirstYPos(pattern, counts):
    firstYPos = None
    for i, char in enumerate(pattern):
        print(i, char, counts)
        counts[char] += 1
        if char == "y" and firstYPos is None:
            firstYPos = i
    return firstYPos


patternMatcher(pat, test)