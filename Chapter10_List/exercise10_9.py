import time
from Util.wordListUtil import wordListUtil

words = chapter10Util.chapter10Util.readWordsDoc()

start = time.time()
newList = []
for word in words:
    newList.append(word)
end = time.time()
print(end - start)

start = time.time()
newList = []
for word in words:
    newList = newList + [word]
end = time.time()
print(end - start)

