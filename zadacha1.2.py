def to_digits(num):
    result = []
    for iter in range(0, num):
        result.append(num % 10)
        num = num // 10
        if num == 0:
            result.reverse()
            break
    return result

print(to_digits(123456))

def to_digits1(nums):
    result = [int(iter) for iter in str(nums)]
    return result

print(to_digits1(123456))