def number_per_line(num):
    if type(num) == str:
        raise TypeError("You did not pass a number!")
    elif num == 0:
        raise ValueError("The number is zero! The number has to \
        be higher than 1.")
    elif num > 100:
        raise ValueError("Wrong number! The number is higher than 100.")
    elif num < 0:
        raise ValueError("The number is negative! Choose a positive \
        number between 1 and 100.")
    elif num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    elif num >= 1:
        return num


number_per_line(4)
