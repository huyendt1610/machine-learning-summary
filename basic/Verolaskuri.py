
def verolaskuri(palka):
    osa10 = 0
    osa20 = 0

    global vero
    vero = 0

    if palka > 20000: 
        osa20 = palka - 20000
    if palka > 10000:
        osa10 = palka - osa20 - 10000
    
    vero = osa10 * 0.1 + osa20 * 0.2

while True:
    palka_str = input("Mikä on sinun palkkasi? ")

    if(not palka_str.isnumeric()):
        print("Palkan täytyy olla luku")
        continue

    palka = int(palka_str)
    if palka >= 0:
        break
    else: 
        print("Enter a valid palkka")

verolaskuri(palka)
print("Sinun vero on: ", vero)