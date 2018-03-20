
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


test1 = ["a"]
print(in_bisect("a",test1))
print(in_bisect("b",test1))
print("---End 1---")
test2 = ["a","b"]
print(in_bisect("a",test2))
print(in_bisect("b",test2))
print(in_bisect("c",test2))
print("---End 2---")
test3 = ["a","b","c"]
print(in_bisect("a",test3))
print(in_bisect("b",test3))
print(in_bisect("c",test3))
print(in_bisect("d",test3))
print("---End 3---")
