from collections import Counter

words = ["a","b","c","d","e","f","g","h","h","h"]
words2 = ["e","f","g","i"]

print(words)

# transform into a hashtable with only keys! excellent for performance
setWords = set(words)
setWords2 = set(words2)

print(setWords)

# All elements of words which does not exist on words2
print(setWords - setWords2)

# All elements of words2 which does not exist on words
print(setWords2 - setWords)

# Counter are like dicts with value and number of occur and some helpful methods like most_common
counterWords = Counter(words)
counterWords2 = Counter(words2)

print(counterWords["h"])
print(counterWords2["e"])

print(counterWords.most_common())

