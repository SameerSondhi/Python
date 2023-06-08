for number in range(1, 101):
    prompt = int(input("Enter a number: "))
    if prompt % 15 == 0:
        print("FizzBuzz")
    elif prompt % 3 == 0:
        print("Fizz")
    elif prompt % 5 == 0:
        print("Buzz")
    else:
        print(number)

