# Functions


def album():
    name = "The Dark Side of the Moon"
    return name


def artist():
    artist = "Pink Floyd"
    return artist


def yearReleased():
    year = 1973
    return year


def tryBooleans(code):
    value = "Enter T or F"
    if(code == "T"):
        value = True
    elif(code == "F"):
        value = False

    return value


print(artist())
# code variable must contain T or F to return Tue or False
print(tryBooleans("T"))
