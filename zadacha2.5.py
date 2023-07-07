def contains_number(number, digit):
    counter = 0
    for i in number:
        if i == digit: counter= counter+1
        else:pass

    if counter>0: return True
    else: False


print(contains_number(123, 2))