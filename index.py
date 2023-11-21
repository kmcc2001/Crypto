def lettre(c):
    # returns true if it's a non-accented letter
    car = ord(c.upper())
    return car>64 and car<91

def decalage(c,k):
    # shift an uppercase letter. Other characters remain unchanged.
    car = ord(c.upper())
    if lettre(c):
        car += k
        while car>90:
            car -= 26
        while car<65:
            car += 26
        return chr(car)
    else:
        return ""

def crypto(message,cle,crypte):
    # performs key-dependent shifting of message characters
    n = 0
    chiffre=''
    for c in message:
        if lettre(c):
            k = ord(cle[n%len(cle)])%26
            if crypte:
                chiffre += decalage(c,k)
            else:
                chiffre += decalage(c,-k)
            n+=1
        else:
            chiffre += c
    return chiffre


# tests
cle = "423"
texte="BONJOUR"
texte_code = crypto(texte,cle,True)
print(texte_code)
texte_decode = crypto(texte_code,cle,False)
print(texte_decode)