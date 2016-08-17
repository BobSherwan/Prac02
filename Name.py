#1
#in_file = open("name.txt", "w")
#userName = str(input("Enter Name"))
#print(userName, file = in_file)
#in_file.close

#2
#in_file = open("name.txt", "r")
#firstLine = in_file.readline()
#print("Your name is {}".format(firstLine))

#3
in_file = open("numbers.txt", "r")
firstLine = in_file.readline()
secondLine = in_file.readline(2)
numTotal = int(firstLine) + int(secondLine)
print(numTotal)
