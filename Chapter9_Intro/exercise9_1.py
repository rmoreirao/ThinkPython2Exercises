from Chapter9_Intro import chapter9Util

words = chapter9Util.chapter9Util.readWordsDoc()
for word in words:
    if len(word.replace(" ", "")) > 20:
        print(word)