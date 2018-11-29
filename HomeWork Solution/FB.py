for num in range(1,21):
    string = str(num) + ":"
    if (num%3 == 0 and num%5 == 0):
        print(string + "FizzBuzz")
