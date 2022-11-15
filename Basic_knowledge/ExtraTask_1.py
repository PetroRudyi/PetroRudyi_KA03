def nextBigger(n):
    number = str(n)
    index = 0
    for i in range(len(number) - 1, 0, -1):
        # print(i)
        if int(number[i]) > int(number[i - 1]):
            index = i
            break

    if index == 0:
        return -1

    x = int(number[index - 1])
    smallest = index
    for j in range(index + 1, len(number), 1):
        if x < int(number[j]) < int(number[smallest]):
            smallest = j

    temp = number[smallest]
    # print(number)
    number = number[:smallest] + number[index - 1] + number[smallest + 1:]
    number = number[:index - 1] + temp + number[index:]
    # print(number)

    # sort(number + i, number + n);

    return int(number)


print('12 ==> ', nextBigger(12))
print('513 ==> ', nextBigger(513))
print('2017 ==> ', nextBigger(2017))
print('9 ==> ', nextBigger(9))
print('111 ==> ', nextBigger(111))