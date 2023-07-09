def slope_style_score(scores):

    def biggest_score(scores):
        result = 0
        for chislo in scores:
            if chislo>result: 
                result = 0 +chislo
            
            else: pass

        return  result

    def smallest_score(scores):
        result = scores[0] 
        for  chislo in scores: 
            if chislo<result: 
                result= 0 + chislo

            else: pass
        return  result

    min_score=smallest_score(scores)
    max_score=biggest_score(scores)

    scores.remove(min_score)
    scores.remove(max_score)

    suma = 0
    counter=0 
    for score in scores:
        suma= suma+ score
       
        counter+=1
        

    avg=suma/counter
    
    return avg

print(slope_style_score([94, 95, 95, 95, 90]))

