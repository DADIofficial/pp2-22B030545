import random
def guess_the_number():
    print("Hello! What is your name?")
    n = input()
    print("Well,", n, " I am thinking of a number between 1 and 20.")
    l = random.randint(1, 20)
    k = 0
    j = 0
    while k != l:
        j += 1
        print("Take a guess")
        k = int(input())
        if k < l:
            print("Your guess is too low.")
        elif (k > l):
            print("Your guess is too high.")
    print("Good job, ", n, " You guessed my number in ", 3, " guesses!")

guess_the_number()