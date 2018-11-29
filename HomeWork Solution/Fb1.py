for num in range(21):
    string = str(num)+":"
    if num%3==0:
        print(string+"Fizz")
    if num%5==0:
        print(string+"buzz")
    print(string)
