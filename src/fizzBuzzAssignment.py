def isPrime(number):
    # prime number is always greater than 1
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                # break
        else:
            return True
    # if the entered number is less than or equal to 1
    # then it is not prime number
    else:
        return False


for num in range(1, 101):
    if(num % 3 == 0):
        if(num % 5 == 0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif(num % 5 == 0):
        print("Buzz")
    else:
        print(num)
    if(isPrime(num)):
        print("Prime")
