
LOWER_BOUNDS = 33
UPPER_BOUNDS = 127

userChar = (input("Enter a character: "))
print("the ASCII code for {} is {}".format(userChar, ord(userChar)))

userNum = int(input("Enter a number: "))
while userNum < LOWER_BOUNDS or userNum > UPPER_BOUNDS:
    print("invalid number, try again")
    userNum = int(input("Enter a number: "))
print("the character for {} is ".format(userNum) + chr(userNum))

for i in range(33, 127, 1):
    print("{}  {}".format(i, chr(i)))