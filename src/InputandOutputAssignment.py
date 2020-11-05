import os
from pathlib import Path


def checkNamesFile(filename):
    my_file = Path(filename)
    if not my_file.is_file():
        print("not exists")
        fileNames = open(filename, "w")
        fileNames.close()


def getNamesList(filename):
    listNames = []
    mainFile = open(filename, "r")
    for line in mainFile:
        tempName = line.strip("\n").split()
        listNames.append(tempName[0])
    # listNames = mainFile.readlines()
    mainFile.close()
    return listNames


def writeInFile(fileName, infoData):
    outputFile = open(fileName, "w")
    for data in infoData:
        tempLine = data.replace(".txt", "")
        outputFile.write(str(tempLine) + ".txt")
        outputFile.write("\n")
    outputFile.close()


def createNewFile(name):
    newFile = open(name + ".txt", "w")
    newText = input("Please enter the text for this file: ")
    newFile.write(str(newText))
    newFile.write("\n")
    newFile.close()


def readFile(fileName):
    print("Reading...")
    f = open(fileName, "r")
    file_contents = f.read()
    print(file_contents)
    f.close()


def deleteFile(fileName):
    print("Deleting...", fileName)
    mainFile = "fileNames.txt"
    inputFile = open(mainFile, "r")
    fileLines = []
    lineToRemove = ""
    cont = 1
    encoding = "utf-8"
    for line in inputFile:
        tempLine = bytearray(line.strip("\n"), encoding="utf-8")
        if tempLine.decode() != fileName:
            fileLines.append(tempLine.decode())
        cont += 1
    reWriteFile(mainFile, fileLines)
    os.remove(fileName)
    print("\n")
    initProgram()


def appendFile(fileName):
    print("Appending...")
    newData = input("Enter a new text for this file: ")
    outputFile = open(fileName, "a")
    outputFile.write(newData)
    outputFile.write("\n")
    outputFile.close()
    readFile(fileName)


def reWriteFile(fileName, dataLines):
    outputFile = open(fileName, "w")
    for data in dataLines:
        outputFile.write(str(data))
        outputFile.write("\n")
    outputFile.close()
    readFile(fileName)


def replaceLine(fileName):
    inputFile = open(fileName, "r")
    fileLines = []

    cont = 1
    for line in inputFile:
        fileLines.append(line)
        print("line", cont, "content:", line)
        cont += 1

    line = int(input("What line do you want to replace? "))

    if line <= len(fileLines):
        content = input("Enter the new content of the line: ")
        fileLines[line - 1] = content
        reWriteFile(fileName, fileLines)
    else:
        print("That line doesn't exists")
    inputFile.close()


def default():
    print("Invalid option")


def switch(option, fileName):
    if option == 1:
        readFile(fileName)
    elif option == 2:
        deleteFile(fileName)
    elif option == 3:
        appendFile(fileName)
    elif option == 4:
        replaceLine(fileName)
    else:
        default()


def formattingFileName(inputName):

    tempName = inputName.split(".")
    name = ""
    if len(tempName) >= 2:
        if tempName[1] != "txt":
            print(
                "Only txt files are admited, changing the file name...",
            )
    return tempName[0]


def initProgram():
    nameFileList = "fileNames.txt"
    checkNamesFile(nameFileList)
    namesList = getNamesList(nameFileList)

    print("My files:", namesList)
    inputNameFile = input("Please enter the name of the file: ")
    name = formattingFileName(inputNameFile)

    if name + ".txt" not in namesList:
        print("This will be a new file...")
        namesList.append(name)
        createNewFile(name)
        writeInFile(nameFileList, namesList)
        namesList = getNamesList(nameFileList)
        print("new list of files:", namesList)
    else:
        print("What do you want to do with this file?")
        print("1 - Read the file")
        print("2 - Delete the file and start over")
        print("3 - Append the file")
        print("4 - Replace a line")
        option = int(input("Enter your choise: "))

        switch(option, name + ".txt")


initProgram()