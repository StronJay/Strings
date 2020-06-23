best, sest = "a$fuu+afff+affaffa+a$Affab+a+a+$a$bccgtt+aaaacA+++aaa$", "a+$aaAaaaa$++"


def smallestSubstringContaining(bigString, smallString):
    targetCharCounts = getCharCounts(smallString)
    print(targetCharCounts)
    substringBounds = getSubstringBounds(bigString, targetCharCounts)
    return getStringFromBounds(bigString, substringBounds)


def getSubstringBounds(bigString, targetCharCounts):
    substringBounds = [0, float("inf")]
    substringCharCounts = {}
    numUniqueChars = len(targetCharCounts.keys())
    # print(numUniqueChars)
    numUniqueCharsDone = 0
    leftIdx = 0
    rightIdx = 0
    while rightIdx < len(bigString):
        rightChar = bigString[rightIdx]
        # print(rightChar)
        if rightChar not in targetCharCounts:
            rightIdx += 1
            continue
        increaseCharCount(rightChar, substringCharCounts)
        print(substringCharCounts, "TARGET:", targetCharCounts, "Done:",
              numUniqueCharsDone, "start:", rightIdx, "Late bloomer:", leftIdx)
        if substringCharCounts[rightChar] == targetCharCounts[rightChar]:
            numUniqueCharsDone += 1
        while numUniqueCharsDone == numUniqueChars and leftIdx <= rightIdx:
            substringBounds = getCloserBounds(
                leftIdx, rightIdx, substringBounds[0], substringBounds[1])
            print(substringBounds)
            leftChar = bigString[leftIdx]
            if leftChar not in targetCharCounts:
                leftIdx += 1
                continue
            if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
                numUniqueCharsDone -= 1
            decreaseCharCounts(leftChar, substringCharCounts)
            leftIdx += 1
        rightIdx += 1
    return substringBounds


def getCloserBounds(idx1, idx2, idx3, idx4):
    print("    INDICES:          ", idx1, idx2, idx3, idx4)
    return [idx1, idx2] if idx2 - idx1 < idx4 - idx3 else [idx3, idx4]


def getStringFromBounds(bigString, substringBounds):
    start, end = substringBounds
    if end == float("inf"):
        return ""
    return bigString[start: end + 1]


def getCharCounts(smallString):
    charCounts = {}
    for char in smallString:
        increaseCharCount(char, charCounts)
    return charCounts


def increaseCharCount(char, charCounts):
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1


def decreaseCharCounts(char, charCounts):
    charCounts[char] -= 1


print(smallestSubstringContaining(best, sest))
