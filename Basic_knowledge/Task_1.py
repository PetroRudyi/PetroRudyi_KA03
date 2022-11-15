def filterList(listOfElements):
    final = []
    for element in listOfElements:
        if type(element) == int:
            final.append(element)
    return final


print(filterList([1, 2, 'm', 'sd']))
print(filterList([1, 2, 'm', 'sd', 0, 15]))
print(filterList([1, 2, 'm', 'sd', 123, 'sff', 12]))
