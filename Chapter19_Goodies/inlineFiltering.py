from Util.wordListUtil import wordListUtil

words = wordListUtil.readWordsDoc()

# Generating lists!
wordsWithAE = [x for x in words if "ae" in x]
print(wordsWithAE)


#generating iterators!

g = (x**2 for x in range(5))
print(g)
for item in g:
    print(item)
