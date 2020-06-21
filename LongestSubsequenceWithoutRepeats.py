test, test2 = 'brownchickenbrowncow', 'clementisacap'
def itsInTheName(string):
    lastSeenHash = {}
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeenHash:
            startIdx = max(startIdx, lastSeenHash[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1] 
        print("enumerated:", (i, char),"idx:",i, "character:", char, "startIdx:",startIdx)
        lastSeenHash[char] = i
    print(string[longest[0] : longest[1]], longest)
    print(lastSeenHash)
itsInTheName(test)