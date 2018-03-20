from Chapter9_Intro import chapter9Util

def uses_only(word,letters):
    for letter in word:
        if letter not in letters:
            return False

    return True

words = chapter9Util.chapter9Util.readWordsDoc()

letters = "acefhlo"

for word in words:
    if uses_only(word,letters):
        print(word)