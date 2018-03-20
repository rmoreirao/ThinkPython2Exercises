from Util.wordListUtil import wordListUtil

def is_abecedarian_from_the_book(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

def is_abecedarian(word):
    word = word.replace(" ","")
    if len(word) == 0:
        return True
    i = 0
    while i < len(word) - 1:
        if word[i] > word[i+1]:
            return False
        i += 1

    return True

words = chapter9Util.chapter9Util.readWordsDoc()

count = 0
countFromTheBook = 0
for word in words:
    if is_abecedarian_from_the_book(word):
        countFromTheBook += 1
    if is_abecedarian(word):
        count += 1

print(count)
print(countFromTheBook)
