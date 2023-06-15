import sys


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    integer = int(input("Input your integer: "))
    final = collatz(integer)
    while True:
        print(final)
        final = collatz(final)
        if final == 1:
            print(1)
            sys.exit()
            
except ValueError:
    print("\nPlease enter an integer: ")
