# spisuk pulen s chisla trqbva da namerim  nai golqmoto i nai malkoto chislo i da namerim sborut im

def nai_golqmo_chislo(spisuk):
    result = 0
    for chislo in spisuk:
        if chislo>result: 
            result = 0 +chislo
            
        else: pass

    return result

def nai_malko_chislo(spisuk):
    result = spisuk[0] 
    for  chislo in spisuk: 
        if chislo<result: 
            result= 0 + chislo

        else: pass
    return result






masiv = [6,9,3,4,5,13]

nai_golqmo = nai_golqmo_chislo(masiv)
nai_malko =nai_malko_chislo(masiv)

print(nai_malko_chislo(masiv))
print(nai_golqmo_chislo(masiv))
suma= nai_golqmo + nai_malko

print(suma)

