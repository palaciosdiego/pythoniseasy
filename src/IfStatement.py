def compare(input_1, input_2, input_3):
    input_1 = int(input_1)
    input_2 = int(input_2)
    input_3 = int(input_3)

    if(input_1 == input_2 or input_1 == 3):
        return True
    elif (input_2 == input_1 or input_2 == input_3):
        return True
    elif(input_3 == input_1 or input_3 == input_2):
        return True
    else:
        return False


result = compare(2, "2", 1)

print(result)
