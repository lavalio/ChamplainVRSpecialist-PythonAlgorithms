# try block and exceptions

x = input("Enter an anumber : ")
y = input("Enter a second anumber : ")

try:
    result = (int(x)/int(y))
except ZeroDivisionError:
    print("Sorry, you cannot divide by zero")
except ValueError:
    print("Please only use values 0 - 9 (Except as a divisor!)")
#except Exception:
#    print("An unknow error has occurred")
else:
    print(result)

