# %% [markdown]
# Tähän voi kirjoittaa itselleen muistiinpanoja

# %%
x = "kissa" 
x

# %%
from kertaus import laskeyhteen # tai import kertaus (kokonais)
laskeyhteen(3,4)

# %%
import math 

print(dir(math))

# %%
import random 

print(dir(random))

# %%
from random import randint

print("Nopan luku", randint(1,6))

# %%
for i in range(10): 
    print(randint(1,6))

# %%
from random import shuffle

sanat = ["apina", "banaani", "cembalo"]
shuffle(sanat)
print(sanat)

# %%
from random import sample
numerot = list(range(1, 41))
sample(numerot,7)

# %%
from random import choice

sanat = ["apina", "banaani", "cembalo"]
choice(sanat)

# %%
from random import seed, randint

print(seed(42))
print(randint(1, 100))

# %%
noppa = [1,2,3,4,5]
for luku in range(3):
    seed(42)
    print(random.choice(noppa))

# %%
from datetime import datetime

aikanyt = datetime.now()
aikanyt

aikanyt.strftime("%d.%m.%Y")

# %%
nyt = datetime.now()
juhannus = datetime(2026, 6, 19)

if nyt < juhannus:
    print("Ei ole vielä juhannus")
elif nyt == juhannus:
    print("Nyt on juhannus")
elif nyt > juhannus: 
    print("Juhannus on mennyt")

erotus = juhannus - nyt
print(erotus.days)
print(erotus.seconds)

# %%
import json

#luodaan puhelinluettelo sanakirja-muotoon

henkilot = {
    "pekka": ['040-5466745', '09-22223333'],
    'emilia': ['045-1212344'],
    'maija': '04000000',
    'matti': '12154545'
}

henkilot

json_henkilot = json.dumps(henkilot)
json_henkilot

with open("henkilot.json",'w') as file:
    #file.write(json_henkilot)
    json.dump(henkilot, file)

# %%
with open("henkilot.json") as file:
    data = file.read()
pnumerot = json.loads(data)
pnumerot

# %%
import urllib.request

pyynto = urllib.request.urlopen('https://studies.cs.helsinki.fi/stats-mock/api/courses/docker2019/stats')
pyynto.read()

# %%
import string 

print(string.ascii_letters)
print(string.punctuation)
print(string.digits)

# %%
# lottoriviksi
from random import shuffle

def luoLotto():
    list = []
    for i in range(1,40):
        list.append(i)

    shuffle(list)

    lottorivi = ""
    for i in range(7):
        lottorivi += f" {list[i]}"
    return lottorivi

print(luoLotto())

# %%
from random import sample, choice, shuffle
import string

def luoSalasana():
    result = []       

    result = sample(string.ascii_uppercase,2)          
    result.append(choice(string.digits))
    result.append(choice(string.punctuation))    

    allLetter = string.ascii_letters + string.digits + string.punctuation   

    for i in sample(allLetter, 8):
        result.append(i)             

    print("result", result)

    shuffle(result)
    return "".join(result)

print("salasana:", luoSalasana())
print(string.punctuation)



# %%
import string




