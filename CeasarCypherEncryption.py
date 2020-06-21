test = "axyz"
# def caesarCipherEncryptor(string, key):
#     sequence = []
#     keyMod = key % 26
#     for i in string:
#         sequence.append(getNewLetterCode(string, keyMod, i))
#         print(sequence)
#     return "".join(sequence)

# def getNewLetterCode(string, key, i):
#     newLetterCode = ord(i) + key
#     print(newLetterCode)
#     return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

def caesarCipherEncryptor(string, key):
    sequence = []
    keyCode = key % 26
    print("KeyCode:",keyCode)
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    print(alphabet)
    reverse = "".join(alphabet)
    print(reverse)
    for i in string:
        sequence.append(getNewLetterCode(i, alphabet, keyCode))
        print(sequence)


def getNewLetterCode(i, alphabet, key):
    newLetterCode = alphabet.index(i) + key
    print(alphabet.index(i), "+", key, "=", newLetterCode)
    print(alphabet[-1 + newLetterCode % 25])
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1 + newLetterCode % 25]


print(caesarCipherEncryptor(test, 2))