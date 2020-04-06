# Sets and Dictionaries

MyFavoriteSong = {
    "Artist": "Pink Floyd",
    "Album": "The Dark Side of the Moon",
    "Year": str(1973),
    "Title": "Time",
    "Duration": str(6.54),
    "Authors": "David Jon Gilmour / Nicholas Berkeley Mason / George Roger Waters / Richard William Wright",
    "Genres": "Rock, Progressive Rock progresivo, Psychedelic Rock",
}


def SongInfo():
    for key in MyFavoriteSong:
        print(key + " : " + MyFavoriteSong[key])


def guessTheValue(key, value):
    if key in MyFavoriteSong and MyFavoriteSong[key] == value:
        return True
    else:
        return False


SongInfo()
print("-------- Guess the key and the value ----------")
print(guessTheValue(input('Enter the key: '), input('Enter the value: ')))
