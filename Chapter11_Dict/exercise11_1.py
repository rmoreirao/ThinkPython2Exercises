import time

from Util.wordListUtil import wordListUtil


def in_bisect(word, words):
    if len(words) == 0:
        return False

    mid = int(len(words) / 2)

    if words[mid] == word:
        return True

    if word > words[mid]:
        return in_bisect(word, words[mid + 1:])
    else:
        return in_bisect(word, words[:mid])


wordsList = wordListUtil.readWordsDoc()
wordsDict = wordListUtil.readWordsDocAsDictionary()
wordsToFind = wordsList[:5000]

count = 0
start = time.time()
for word in wordsToFind:
    if in_bisect(word, wordsList):
        count += 1
end = time.time()
print(end - start)
print("Finish 1")
print(count)

count = 0
start = time.time()
for word in wordsToFind:
    if word in wordsDict:
        count += 1
end = time.time()
print(end - start)
print("Finish 2")
print(count)
