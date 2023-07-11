def to_number(digits):
    result = 0
    for nums in digits:
        result = result * 10
        result = result + nums
        if result % 10 == 0:
            result = result // 10
            break
    return result
print(to_number([25, 3, 9]))



def to_number1(digits):
    result = ""

    for nums in digits:
        result = result + str(nums)
    result = int(result)
    return result
print(to_number1([25, 3, 9]))