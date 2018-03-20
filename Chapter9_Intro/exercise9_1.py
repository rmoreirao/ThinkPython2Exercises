from Util.wordListUtil import wordListUtil

words = wordListUtil.readWordsDoc()
for word in words:
    if len(word.replace(" ", "")) > 20:
        print(word)