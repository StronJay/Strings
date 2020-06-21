words = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
def subOp(words):
    if len(words) == 0:
        return False
    sortedWords = ["".join(sorted(w)) for w in words]
    for i in range(len(words)):
        print(words[i], sortedWords[i], i)
    indices = [i for i in range(len(words))]
    print("makes sense:",indices)
    indices.sort(key=lambda x: sortedWords[x])
    print(indices)
    print(sortedWords)
    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for idx in indices:
        word = words[idx]
        sortedWord = sortedWords[idx]
        print(word, sortedWord)

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue
        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord
    result.append(currentAnagramGroup)

    print(result)


def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        print(sorted(word))
        print(anagrams, sortedWord)
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    print(anagrams['oy'])
    print(list(anagrams.values()))



groupAnagrams(words)