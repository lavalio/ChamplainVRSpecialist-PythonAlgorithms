# My preferred method, using concatenated strings.

def is_divisibale(num, testvalue):
    if num % testvalue == 0:
        return True
    return False


for num in range(21):
    string = (str(num) + ":")
    if is_divisibale(num,3):
        string = string + "Fizz"
    if is_divisibale(num, 5):
        string = string + "Buzz"
    print(string)
