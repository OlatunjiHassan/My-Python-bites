import random

print("I am thinking of a number between 1 and 20. \n")
number = random.randint(1, 20)
count = 0
for guessTaken in range(1, 7):
    guess = int(input("Take a guess.\n"))
    count += 1
    if guess < number:
        print("Your guess is too low.\n")
    elif guess > number:
        print("Your guess is too high.\n")
    if guess == number:
        print("Good job! You guessed my number in " + str(count) + " guesses!")
        break
    if guessTaken == 6:
        print("Nope, the number I guessed is " + str(number) + ".")
        break
