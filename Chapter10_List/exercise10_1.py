def nested_sum(listOfLists):
    sum = 0
    for list in listOfLists:
        for value in list:
            sum += value

    return sum

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))