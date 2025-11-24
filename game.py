import random

def guess():
    number = random.randint(1, 20)
    print("Im thinking of a number between 1 and 20")

    tries = 0
    while True:
        guess = int(input("Your guess: "))
        tries += 1

        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print("Correct Tries:", tries)
            break

guess()
