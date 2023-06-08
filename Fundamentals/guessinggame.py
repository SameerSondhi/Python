answer = 5

print("Guess a number between 1 and 10: ")
guess = int(input())

while guess != answer:
    if guess < answer:
        print("Guess higher")
        guess = int(input())
        if guess == answer:
            print("You win. You guessed it!")
        else:
            print("You did not guess correctly")

    elif guess > answer:
        print("Guess lower")
        guess = int(input())
        if guess == answer:
            print("You win. You guessed it!")
        else:
            print("You did not guess correctly")

    else:
        print("You win. You guessed it!")
