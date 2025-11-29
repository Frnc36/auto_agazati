from Auto import Auto 

auto_lista = []

def fajlbeolvasas():
    f = open("auto.txt", "r", encoding="UTF-8")
    f.readline()
    szoveg_lista = f.readlines()
    f.close

    i = 0
    while i < len(szoveg_lista):
        sor = szoveg_lista[i].strip().split("$")
        auto = Auto(sor[0], int(sor[1]))
        auto_lista.append(auto) 
        i += 1
    
    # i = 0
    # while i < len(auto_lista):
    #     print(auto_lista[i])
    #     i += 1
    return auto_lista

def flotta(lista = []):
    db = 0
    while db < len(lista):
        db += 1
    return db

def legfiatalabb(lista = []):
    if len(lista):
        legfiatalabb_auto = lista[0]
        i = 1 #második autótól kezdjük
        while i < len(lista):
            if lista[i].gyartasi_datum > legfiatalabb_auto.gyartasi_datum:
                legfiatalabb_auto = lista[i]
            i += 1
    return legfiatalabb_auto


def atlag_kor(lista = []):
    osszeg = 0
    i = 0 
    while i < len(lista):
        osszeg += 2025-int(lista[i].gyartasi_datum)
        i += 1
    
    atlag = osszeg / len(lista)
    print(f"\tÁtlagos kor: {atlag:.2f} év.")