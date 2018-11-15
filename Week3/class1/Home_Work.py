for number in range(26):
    if (number % 3 == 0):
        if (number % 5 == 0):
            print(str(number) + " :FizzBuzz")
        else:
            print(str(number) + " :Fizz")
    elif(number % 5 == 0):
        print(str(number) + " :Buzz")




#---
#for a in range(100):
#    if (a % 3 == 0) and (a % 5 != 0):
#        print(str(a) + " :Fizz")
#    elif (a % 3 != 0) and (a % 5 == 0):
#        print(str(a) +" :Buzz")
#    else:
#        print(str(a) +" :FizzBuzz")