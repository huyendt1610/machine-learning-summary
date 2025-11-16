from random import sample, choice, shuffle
import string

def luoSalasana():
    tulos = []       

    tulos = sample(string.ascii_uppercase,2)          
    tulos.append(choice(string.digits))
    tulos.append(choice(string.punctuation))    

    kirjaimet = string.ascii_letters + string.digits + string.punctuation   

    for i in sample(kirjaimet, 8):
        tulos.append(i)             

    #print("tulos", tulos)

    shuffle(tulos)
    return "".join(tulos)

print("salasana:", luoSalasana())