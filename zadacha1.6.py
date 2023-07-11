def is_decreasing(seq):
    result = False
    n = len(seq)

    for iter in range(n - 1):
        if seq[iter] > seq[iter + 1]:
            result = True
        else:
            result = False
            break

    return result

print(is_decreasing([5, 4, 3, 2, 1]))