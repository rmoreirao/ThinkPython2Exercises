def cumsum(list):
    newList = []
    for i in range(len(list)):

        if(i > 0):
            previousSum = newList[i-1]
        else:
            previousSum = 0

        value = previousSum + list[i];

        newList.append(value)

    return newList

t = [1, 2, 3]
print(cumsum(t))