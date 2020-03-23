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

Length = 3
ToPrint = "a"
for pos in range(1, Length+1):
    print(ToPrint*pos)

for pos in range(Length, 0, -1):
    print(ToPrint*pos

# for row in range(5):
#     if row % 2 == 0:
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
