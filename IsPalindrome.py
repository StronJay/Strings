test = "abc1d1cba"


# def isPalindrome(string):
#     reversedString = ""
#     for i in reversed(range(len(string))):
#         print(reversedString)
#         reversedString += string[i]
#     return reversedString == string


# def isPalindrome(string):
#     sequence = []
#     for i in reversed(range(len(string))):
#         sequence.append(string[i])
#         print(string, sequence)
#         print("".join(sequence))
#     return string == "".join(sequence)


# def isPalindrome(string, i=0):
#     j = len(string) - 1 - i
#     return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)

# TAIL RECURSIVE FUNCTION!!!! IT IS SLIGHTLY BETTER THAN STRAIGHT UP RECURSION
# as far as Time Space complexity
def isPalindrome(string, i=0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome(string, i + 1)


# def isPalindrome(string):
#     i, j = 0, len(string) - 1
#     while i < j:
#         if string[i] != string[j]:
#             return False
#         i += 1
#         j -= 1
#     return True


print(isPalindrome(test))