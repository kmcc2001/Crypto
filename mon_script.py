def message(s, k):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for lettre in s:
        ordre = alpha.find(lettre)
        indice = ordre+k
        if indice > 25:
            indice = indice % 26
        res += alpha[indice]
    return res
 
 
print(message("BONJOUR", 4))