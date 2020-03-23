# Defining my empty lists
myUniqueList = []
myLeftovers = []


# Adding things function
def addThing(element):
    if not(element in myUniqueList):
        myUniqueList.append(element)
        return True
    else:
        # Element already exists
        addLeftover(element)
        return False


# For rejected inputs
def addLeftover(element):
    myLeftovers.append(element)


# addThing(5)
# addThing("Mouse")
# addThing("Mouse")
# addThing(["Cat", 1, "Dog"])
# addThing(5)

print(myUniqueList)
print(myLeftovers)
