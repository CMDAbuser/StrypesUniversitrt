def is_number_balanced(n):
    result = False
    left = 0
    right = 0
    strin = [int(it) for it in str(n)]

    for itr in range(len(strin)):

        if itr < len(strin) // 2:
            left = left + int(strin[itr])
        elif itr > len(strin) // 2:
            right = right + int(strin[itr])

    if left == right:
        result = True
    else:
        result = False

    return result

print(is_number_balanced(1238033))