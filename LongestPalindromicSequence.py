test1, test2 = "it's highnoon", "abaghgxyzzyxf"


def subOptimalApproach(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i : j + 1]
            print(substring)
            if len(substring) > len(longest) and isPalindrome(substring):
                longest = substring
                print("IN IT",longest)
    print(longest)

def isPalindrome(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


# def longestPalindromicSequence(string):
#     currentLongest = [0, 1]
#     for i in range(1, len(string)):
#         odd = getLongestPalindromicSubsequence(string, i - 1, i + 1)
#         print(odd, i- 1, i + 1)
#         even = getLongestPalindromicSubsequence(string, i - 1, i)
#         longest = max(odd, even, key=lambda x: x[1] - x[0])
#         currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
#         print("longest", longest, "key=lambda x: x[1] - x[0]:", (odd[1] - odd[0]), (even[1] - even[0], "currentLongest:", currentLongest))
#     print(currentLongest, string[currentLongest[0] : currentLongest[1]])


# def getLongestPalindromicSubsequence(string, leftIdx, rightIdx):
#     while leftIdx >= 0 and rightIdx < len(string):
#         if string[leftIdx] != string[rightIdx]:
#             break
#         leftIdx -= 1
#         rightIdx += 1
#     print(leftIdx, rightIdx)
#     return [leftIdx + 1, rightIdx]


subOptimalApproach(test2)

