def biggest_difference(arr):
    def nai_golqmo_chislo(arr):
        result = 0
        for chislo in arr:
            if chislo>result: 
                result = 0 +chislo
            
            else: pass

        return  result

    def nai_malko_chislo(arr):
        result = arr[0] 
        for  chislo in arr: 
            if chislo<result: 
                result= 0 + chislo

            else: pass
        return  result
    
    min_result=nai_malko_chislo(arr)
    max_result=nai_golqmo_chislo(arr)

    razlika= max_result - min_result
    
    return razlika

print(biggest_difference([1,2,3,4,5]))