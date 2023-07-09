# Implement a function, called contains_digits(number, digits) where digits is a list
#of integers and a number is an integer.
#The function should return True if all digits are contained by number

# chat gpt 

def contains_digits(number, digits):
    numb = str(number)

    for digit in digits:
        if str(digit) not in numb:
            return False

    return True

print(contains_digits(402123, [0, 3, 4]))