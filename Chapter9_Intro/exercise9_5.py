from Chapter9_Intro import chapter9Util

def uses_all(word,requitedLetters):
    for letter in requitedLetters:
        if letter not in word:
            return False

    return True

def countUsesAll(requiredLetters):
    count = 0
    words = chapter9Util.chapter9Util.readWordsDoc()
    for word in words:
        if uses_all(word,requiredLetters):
            count += 1

    return count

print(countUsesAll("aeiou"))

print(countUsesAll("aeiouy"))
