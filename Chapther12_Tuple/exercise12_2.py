import itertools
from Util.wordListUtil import wordListUtil

wordsDict = wordListUtil.readWordsDocAsDictionary()
newWordDict = dict()
for word in wordsDict:
    sortedWord = ''.join(sorted(word))
    wordList = newWordDict.setdefault(sortedWord, [])
    wordList.append(word)
    newWordDict[sortedWord] = wordList

def exercise12_2_1():
    for item in newWordDict:
        if len(newWordDict[item]) > 1:
            print(newWordDict[item])

def exercise12_2_2():
    orderedDict = dict()
    for item in newWordDict:
        if len(newWordDict[item]) > 1:
            newValue = orderedDict.setdefault(len(newWordDict[item]), [])
            newValue.append(newWordDict[item])
            orderedDict[len(newWordDict[item])] = newValue

    for key in reversed(sorted(orderedDict.keys())):
        for orderedList in orderedDict[key]:
            print(orderedList)

def exercise12_2_3():
    orderedDict = dict()
    for item in newWordDict:
        if len(item) >= 8 and len(newWordDict[item]) > 1:
            newValue = orderedDict.setdefault(len(newWordDict[item]), [])
            newValue.append(newWordDict[item])
            orderedDict[len(newWordDict[item])] = newValue

    for key in reversed(sorted(orderedDict.keys())):
        for orderedList in orderedDict[key]:
            # Gets the first item only!
            print(orderedList)
            return

# exercise12_2_1()
#exercise12_2_2()
exercise12_2_3()
