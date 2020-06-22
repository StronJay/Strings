test, subtest = "testthis is a testtest to see if testestest it works", "test"


def underscorifySubstring(string, substring):
	locations = collapse(getLocations(string, substring))
	return underscorify(string, locations)

def getLocations(string, substring):
	locations = []
	startIdx = 0
	while startIdx < len(string):
		nextIdx = string.find(substring, startIdx)
		print(nextIdx)
		if nextIdx != -1:
			locations.append([nextIdx, nextIdx + len(substring)])
		else:
			break
		startIdx = nextIdx + 1
	return locations


def collapse(locations):
	newLocations = [locations[0]]
	previous = newLocations[0]
	test = [locations[0]]
	print(locations)
	for i in range(1, len(locations)):
		current = locations[i]
		if current[0] <= previous[1]:
			previous[1] = current[1]
		else:
			newLocations.append(current)
			test.append(previous)
			previous = current
	print(test)
	return newLocations


def underscorify(string, locations):
	print(locations)
	locationsIdx = 0
	stringIdx = 0
	inBetweenUnderscores = False
	i = 0
	finalChars = []
	while stringIdx < len(string) and locationsIdx < len(locations):
		if stringIdx == locations[locationsIdx][i]:
			finalChars.append("_")
			inBetweenUnderscores = not inBetweenUnderscores
			if not inBetweenUnderscores:
				locationsIdx += 1
			i = 0 if i == 1 else 1
		finalChars.append(string[stringIdx])
		stringIdx += 1
	if locationsIdx < len(locations):
		finalChars.append("_")
	elif stringIdx < len(string):
		finalChars.append(string[stringIdx:])
	print("".join(finalChars))
	print(finalChars)


underscorifySubstring(test, subtest)