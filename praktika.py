def get_all_digits(num):
    result= []
    
    for digit in num:
        result.append(num%10)
        num = num // 10
    
    return result

def sum_of_digits(my_list): 
    result = 0
    for elem in my_list:
        result = result + elem

    return result



def is_number_balanced(num):
    digits = get_all_digits(num)
    half_of_digits = len(digits)/2
    left_part= sum_of_digits(digits[0:int(half_of_digits)])    
    right_part = sum_of_digits(digits[int(half_of_digits):])

    return left_part == right_part


number = 36


print(get_all_digits(number))
#print(is_number_balanced(number))