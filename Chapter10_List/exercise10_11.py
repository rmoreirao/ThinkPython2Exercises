from Chapter10_List import chapter10Util

def in_bisect(word,words):
    if len(words) == 0:
        return False

    mid = int(len(words)/2)

    if words[mid] == word:
        return True

    if word > words[mid]:
        return in_bisect(word,words[mid+1:])
    else:
        return in_bisect(word, words[:mid])


words = chapter10Util.chapter10Util.readWordsDoc()
for word in words:
    if in_bisect(word[::-1],words):
        print(word + " <-> " + word[::-1])