def fizzbuzz(num, testvalue):
    string = (str(num) + ":")
    if num % testvalue == 0:
        string = string + "can divided by " + str(testvalue)
        print(string)
    else:
        string = string + "can not divided by " + str(testvalue)
        print(string)


fizzbuzz(21,3)
fizzbuzz(15,3)
fizzbuzz(15,5)

fizzbuzz(15,2)
