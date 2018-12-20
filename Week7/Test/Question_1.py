#Guess the number

import random

the_number = random.randint(1,101)
print(the_number)

times =1

while True:
    guess = input("Please gues a number between 1 and 100 (attempt "+ str(times)+")>")
    isinstance(guess, int)

    try:
        guess_number = int(guess)
    except ValueError:
        print("Wrong input! Please ener a number!")
        continue

    times += 1

    if guess_number>the_number:
        print("Wrong guess, your guess too high")
    elif guess_number<the_number:
        print("Wrong guess, your guess too low")
    elif guess_number == the_number:
        print("Crrect! you win.")
        break
    if times > 6:
        print("Sorry, you didn't guess the correct number. The correct number was {}".format(the_number))
        break

