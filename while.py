
print('Enter a number: ')
i = int(input())
print('You entered: ' + str(i))
while True:
    print(i)
    if i == 1:
        break
    elif (i % 2) == 0:
        i = i // 2
    else:
        i = (i * 3) + 1

