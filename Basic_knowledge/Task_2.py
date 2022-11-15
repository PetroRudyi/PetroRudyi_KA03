# a - 97
# A - 65
# diff = 32

def checkLetter(letter, list_of):
    for i in list_of:
        if (abs(letter - i) == 0) or (abs(letter - i) == 32):
            return True
    return False


def first_non_repeating_letter(word):
    temp = ''
    repeatList = []
    nonRepeatList = []
    for letter in word:
        letterNumber = ord(letter)
        if not (checkLetter(letterNumber, nonRepeatList)) and not (
                checkLetter(letterNumber, repeatList)):  # вперше
            nonRepeatList.append(letterNumber)
        elif checkLetter(letterNumber, nonRepeatList) and not (
                checkLetter(letterNumber, repeatList)):  # вдруге
            if letterNumber in nonRepeatList:
                nonRepeatList.remove(letterNumber)
                repeatList.append(letterNumber)
            elif (letterNumber + 32) in nonRepeatList:
                nonRepeatList.remove(letterNumber + 32)
                repeatList.append(letterNumber + 32)
            else:
                nonRepeatList.remove(letterNumber - 32)
                repeatList.append(letterNumber - 32)

    return list(map(chr, repeatList)), list(map(chr, nonRepeatList))


repeatList, nonRepeatList = first_non_repeating_letter('mOmmytY')
print('mOmmytY')
print(repeatList)
print(nonRepeatList)
