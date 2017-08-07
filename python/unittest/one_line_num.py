def number_per_line(num):
    if type(num) == str:
        raise TypeError("You did not pass a number!")
    if num <= 0 or num > 100:
        raise ValueError("The number is not in range between 1 and 100.")
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    if num >= 1:
        return num


number_per_line(2)
