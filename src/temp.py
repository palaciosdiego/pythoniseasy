PI = 3.14
one, two, three = 1, 2, 3
decimal = 1.4
StringVar = "Hello"


def addOne(Number):
    Number += 1
    return Number


Var = 0
Var2 = addOne(2.1 + 3.4)
Var3 = addOne(Var2 * 2.1)


def addOneAddTwo(NumberOne, NumberTwo):
    Output = NumberOne + 1
    # Output = Output + NumberTwo + 2
    Output += NumberTwo + 2
    return Output


Sum = addOneAddTwo(Var2, Var3)
# print(Sum)


i = 1

while True:
    if i % 3 == 0:
        break
    # print(i)
    i += 1


# X = 'abcd'
# for i in range(len(X)):
#     #    print(i)


# for number in range(10):
#     if number % 3 == 0:
#         print(number)
#         print("Divisible by 3")
#     else:
#         print(number)
#         print("Not Divisible by 3")

# Length = 3
# ToPrint = "a"
# for pos in range(1, Length+1):
#     print(ToPrint*pos)

# for pos in range(Length, 0, -1):
#     print(ToPrint*pos

# for row in range(1, 6):
#     print(row)
#     if not(row % 2 == 0):
#         # print(" | | ")
#         for col in range(1, 6):
#             if col % 2 == 1:
#                 if col != 5:
#                     print(" ", end="")
#                 else:
#                     print(" ")
#             else:
#                 print("|", end="")
#     else:
#         print("-----")


# l = 3
# for pos in range(1, 3):
#     print("c"*pos)

# f = 1
# A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
# for i in range(0, 3):
#     f = f*i
#     for j in range(0, 3):
#         A[i][j] = f

# CountryList = []
# for i in range(5):
#     Country = input("Please Enter a country: ")
#     CountryList.append(Country)

# CountryDictionary = {}

# for Country in CountryList:
#     if Country in CountryDictionary:
#         CountryDictionary[Country] += 1
#     else:
#         CountryDictionary[Country] = 1

# print(CountryDictionary)

# BlackShoes = {42:2,41:3,40:4,39:1,38:0}
# while (True):
#     pourchaseSize = int(input("which size ?\n"))
#     if pourchaseSize < 0:
#         break
#     if BlackShoes[pourchaseSize] > 0:
#         BlackShoes[pourchaseSize] -= 1
#     else:
#         print("no hay")
#     print(BlackShoes)

nums = set([7, 7, 1, 3, 4, 5, 5, 2])
# print(len(nums))
nums = set([1, 2, 3, 4, 5, 4, 3, 2, 1])
# print(nums)
dict = {}
dict[1] = 2
dict["1"] = 4
dict[1] += 2
count = 0

for key in dict:
    count += dict[key]

# print(count)


# s={"1","2","3","4","5"}

# if "3" in s:
#     print("3")

# name = input("Please enter your name: ")
# print(name)

# age = int(input("Please enter your age: "))
# print(age+1)

# Scores = []
# for i in range(1):
#     currentScore = float(input("Please enter the score " + str(i+1) + ": "))
#     Scores.append(currentScore)
#     print("The score you entered was:\n"+str(currentScore)+"\nnice")
# print(Scores)

# File = open("Filename","r") #"r","w","a","r+"
# File.close()
VacationSpots = ["London", "Paris", "New York", "Utha", "Iceland"]
VacationFile = open("VacationPlaces", "w")

for Spots in VacationSpots:
    VacationFile.write(Spots + "\n")
VacationFile.close()

VacationFile = open("VacationPlaces", "r")

FirstLine = VacationFile.readline()
# print(FirstLine)
SecondLine = VacationFile.readline()
# print(SecondLine)
# for line in VacationFile:
#     print(line, end="")
# TheWholeFile = VacationFile.read()
# print(TheWholeFile)
VacationFile.close()
FinalSpot = "Thailand\n"
VacationFile = open("VacationPlaces", "a")
VacationFile.write(FinalSpot)
VacationFile.close()

# VacationFile = open("VacationPlaces", "r")
# for line in VacationFile:
#     print(line, end="")

# VacationFile.close()

# with open("VacationPlaces", "r") as VacationFile:
#     for line in VacationFile:
#         print(line)

# /  /  0
# ----- 1
# /  /  2
# ----- 3
# /  /  4


def drawField(field):
    for row in range(5):  # 0,1,2,3,4 | # 0,.,1,.,2
        if row % 2 == 0:  # 0,2,4
            practicalRow = int(row / 2)  # 0,1,2
            # print writing lines
            for column in range(5):  # 0,1,2,3,4
                # 0,.,1,.,2
                if column % 2 == 0:  # 0,2,4
                    practicalColumn = int(column / 2)  # 0,1,2
                    if column != 4:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
        else:
            print("-----")


Player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# drawField(currentField)
# while True:
# print("Players turn: ", Player)
# MoveRow = int(input("Please enter the row\n"))
# MoveColumn = int(input("Please enter the column\n"))
# if Player == 1:
#     # Make move for p1
#     if currentField[MoveColumn][MoveRow] == " ":
#         currentField[MoveColumn][MoveRow] = "X"
#         Player = 2
# else:
#     # Make move for p2
#     if currentField[MoveColumn][MoveRow] == " ":
#         currentField[MoveColumn][MoveRow] = "O"
#         Player = 1
# print(currentField)
# drawField(currentField)

# Participant Data

ParticipantNumber = 2
participantData = []
registeredParticipants = 0
outputFile = open("ParticipantsData.txt", "w")

while registeredParticipants < ParticipantNumber:
    tempPartData = []  # name,country,age
    name = input("Please enter your name: ")
    tempPartData.append(name)
    country = input("Please enter your country: ")
    tempPartData.append(country)
    age = int(input("Please enter your age: "))
    tempPartData.append(age)

    participantData.append(tempPartData)
    registeredParticipants += 1

for participant in participantData:
    
outputFile.close()