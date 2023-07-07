def is_palindrome(numb):

    number= numb  
    reversed_number = 0

    while (numb>0):
        single_digit=numb%10 # vzima poslenoto chiso
        reversed_number = reversed_number*10+single_digit #pochvam ot nula i zapochvam da pishem chislata 
        numb= numb //10 # maham poslednoto chislo za da moga da produlja  cikula pravilno
    
    if number == reversed_number: 
        return str("the number is a palindrome")
    else: 
        return str("the number isnt a palindrome")
print(is_palindrome(151))
