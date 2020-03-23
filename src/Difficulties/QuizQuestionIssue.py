# Course: Python is easy
# Section: Loops
# Test: #6 Advanced Loops
# Question: 4
# Link https://pirple.thinkific.com/courses/take/python-is-easy/quizzes/5573925-test-6-advanced-loops

# This is how the question says:

"""
What is the output of the following code:

Length = 3
ToPrint = "a"
for pos in range(1, Length + 1):
    print(ToPrint*pos)

for pos in range(Length, 0, -1):
    print(ToPrint*pos
"""

# The Answers list
"""
Choose only ONE best answer.


A   aaa
--------------
B
    a
    aa
    aaa
--------------
C
    a
--------------
D
    a
    aa
    aaa
    aa
    a
-------------
"""


# Problem
"""
    I don't know what answer to pick, apparently they are all wrong!
    An error option could be the answer, but there isn't
"""

# If i ran this code, it shows an error because there is a missing ")" at the end (An error option could be the answer)

Length = 3
ToPrint = "a"
for pos in range(1, Length+1):
    print(ToPrint*pos)

for pos in range(Length, 0, -1):
    print(ToPrint*pos)

# Adding the missing ")" the result is:
"""
    a
    aa
    aaa
    aaa
    aa
    a
"""
# However, it does not appear in the list either

# The point here: what is the right answer of the question?
