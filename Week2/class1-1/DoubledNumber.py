# This example will convert a string to a number
# By using the int function

b = "88"

c = int(b) * 2

print ( "V1: The number " + b + " doubled is " + str(c))


# Second version

b = "88"

int_b = int(b)

result =  int_b * 2

print ( "V2: The number " + b + " doubled is " + str(result))

print ( "V3: The number {0} doubled is {1}" .format(b,result))

print ( "V4: The number {} doubled is {}" .format(b,result))