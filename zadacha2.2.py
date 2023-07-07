def sum_of_divisors(number):
    delitel = 1
    suma=0
    for i in range(1,9):
        if number%i == 0 : 
           suma = suma + i
        else : pass

    return suma



chislo = 6

print(sum_of_divisors(chislo))