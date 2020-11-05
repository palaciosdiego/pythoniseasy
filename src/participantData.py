ParticipantNunber = 2
participantData = []
registeredParticipants = 0
outputFile = open("ParticipantData.txt", "w")

while registeredParticipants < ParticipantNunber:
    tempPartData = []  # name,country of origin, age
    name = input("Please enter your name: ")
    tempPartData.append(name)
    country = input("Please enter your country of origin: ")
    tempPartData.append(country)
    age = int(input("Please enter your age: "))
    tempPartData.append(age)

    participantData.append(tempPartData)
    registeredParticipants += 1

print(participantData)
for participant in participantData:
    for data in participant:
        tempLine = data.replace(".txt", "")
        outputFile.write(str(data) + ".txt")
        outputFile.write(" ")
    outputFile.write("\n")

outputFile.close()

inputFile = open("ParticipantData.txt", "r")
inputList = []

for line in inputFile:
    tempParticipant = line.strip("\n").split()
    inputList.append(tempParticipant)

Age = {}

for part in inputList:
    tempAge = int(part[-1])
    if tempAge in Age:
        Age[tempAge] += 1
    else:
        Age[tempAge] = 1

print(Age)

Countries = {}

for part in inputList:
    tempCountry = part[1]
    if tempCountry in Countries:
        Countries[tempCountry] += 1
    else:
        Countries[tempCountry] = 1

print("countries that attended:", Countries)
Oldest = 0
Youngest = 100
mostOcurringAge = 0
counter = 0

for tempAge in Age:
    if tempAge > Oldest:
        Oldest = tempAge
    if tempAge < Youngest:
        Youngest = tempAge
    if Age[tempAge] > counter:
        counter = Age[tempAge]
        mostOcurringAge = tempAge

print("oldest", Oldest)
print("youngest", Youngest)
print("Most ocurring age is:", mostOcurringAge, "with", counter, "participants")
inputFile.close()
