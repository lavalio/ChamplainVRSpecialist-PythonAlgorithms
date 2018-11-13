for a in range(100):
    if (a % 3 == 0) and (a % 5 != 0):
        print(str(a) + " :Fizz")
    elif (a % 3 != 0) and (a % 5 == 0):
        print(str(a) +" :Buzz")
    else:
        print(str(a) +" :FizzBuzz")

