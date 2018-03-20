from Util.wordListUtil import wordListUtil

def has_no_e(word):
    return "e" not in word

words = wordListUtil.readWordsDoc()

total = len(words)
noEWordCount = 0
for word in words:
    if has_no_e(word):
        noEWordCount += 1
        if len(word.replace(" ", "")) > 20:
            print(word)

print (str(noEWordCount/total))