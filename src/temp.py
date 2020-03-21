PI = 3.14
one, two, three = 1, 2, 3
decimal = 1.4
StringVar = "Hello"


def addOne(Number):
    Number += 1
    return Number


Var = 0
Var2 = addOne(2.1+3.4)
Var3 = addOne(Var2*2.1)


def addOneAddTwo(NumberOne, NumberTwo):
    Output = NumberOne + 1
    # Output = Output + NumberTwo + 2
    Output += NumberTwo + 2
    return Output


Sum = addOneAddTwo(Var2, Var3)
# print(Sum)


Numbers = []
for num in range(1, 12, 2):
    Numbers.append(num)

print(Numbers)
