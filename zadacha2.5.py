def contains_digit(number, digit):

    numb= str(number)
    
    for dig in numb:
        
        if int(dig) == digit:
            return True
    return False

print(contains_digit(123, 5))