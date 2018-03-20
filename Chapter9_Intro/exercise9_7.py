from Chapter9_Intro import chapter9Util

def isThreeConsecutiveDoubleLetter(word):
    if len(word) < 6:
        return False

    currentStartIndex = 0

    while currentStartIndex + 6 <= len(word):
        if word[currentStartIndex] == word[currentStartIndex + 1] and word[currentStartIndex + 2] == word[currentStartIndex + 3] and word[currentStartIndex + 4] == word[currentStartIndex + 5]:
            return True
        currentStartIndex += 1

    return False

words = chapter9Util.chapter9Util.readWordsDoc()

for word in words:
    if isThreeConsecutiveDoubleLetter(word):
        print(word)