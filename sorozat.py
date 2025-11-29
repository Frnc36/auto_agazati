import random

def feladat2():
    lista = []

    i = 0
    while i < 5:
        lotto_szam = random.randint(1,99)
        lista.append(lotto_szam)
        i += 1
        #print(lotto_szam)
    return lista

def feladat2kiir(lista = []):
    kiiras = ""
    for i in range(len(lista)):
        kiiras += str(lista[i])
        if i < len(lista) - 1:
            kiiras += "; "
    print(f"\t{kiiras}")


def egyjegyuek_szama(lista = []):
    darab = 0
    for szam in lista:
        if 0 <= szam <= 9:
            darab += 1
    return darab

def file_kiir(egyjegyu):
    with open("szamok.txt", "w", encoding="UTF-8") as f:
       f.write(f"\tAz egyjegyűek száma: {egyjegyu}.")
       f.close()

   