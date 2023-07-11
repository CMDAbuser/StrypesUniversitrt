def fib_number(n):
    n1 = 0
    n2 = 1
    result = ""

    for nums in range(n):
        result = result + str(n1)

        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return int(result)

print(fib_number(6))
    