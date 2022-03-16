
print('Enter an integer: ')
try:
    i = int(input())
except ValueError:
            print('Please enter a Valid number')

def collatz(i):
    while True:
        print(i)
        if i == 1:
            break
        elif (i % 2) == 0:
            i = i // 2
        else:
            i = (i * 3) + 1
collatz(i)