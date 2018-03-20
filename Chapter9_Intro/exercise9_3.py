from Chapter9_Intro import chapter9Util

def avoids(word,forbiddenLetters):
    for letter in forbiddenLetters:
        if letter in word:
            return False;

    return True;

count = 0
forbiddenLetters = "abcdef"

words = chapter9Util.chapter9Util.readWordsDoc()

for word in words:
    if avoids(word,forbiddenLetters):
        count += 1

print(len(words))
print(count)
