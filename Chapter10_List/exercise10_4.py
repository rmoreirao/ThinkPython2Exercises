def chop(list):
    list.pop(0)
    list.pop(len(list)-1)

t = [1, 2, 3, 4]
chop(t)
print(t)