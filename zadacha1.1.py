def sum_of_digits(num):
    result = 0
    for iter in range(0, num):
        result = result + num % 10
        num = num // 10
        if num == 0:
            break
    return result

print(sum_of_digits(123456))