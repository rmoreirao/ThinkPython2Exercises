from Chapter9_Intro import chapter9Util

def has_no_e(word):
    return "e" not in word

words = chapter9Util.chapter9Util.readWordsDoc()

total = len(words)
noEWordCount = 0
for word in words:
    if has_no_e(word):
        noEWordCount += 1
        if len(word.replace(" ", "")) > 20:
            print(word)

print (str(noEWordCount/total))