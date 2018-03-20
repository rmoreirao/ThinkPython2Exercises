import operator
from Util.wordListUtil import wordListUtil

lettersDict = dict()
words = wordListUtil.readWordsDoc()
for word in words:
    for letter in word.replace(" ",""):
        lettersDict[letter] = lettersDict.setdefault(letter,0) + 1

sortedLettersDict = sorted(lettersDict.items(), key=operator.itemgetter(1), reverse=True)

print (sortedLettersDict)

