def is_prime(number):
    delitel = 1
    suma=0
    for i in range(1,9):
        if number%i == 0 : 
           suma = suma + i

        else : pass
    if number + 1 == suma : return True
    else: return False



print(is_prime(11))