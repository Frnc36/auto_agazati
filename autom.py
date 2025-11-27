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
    i = 0
    while i < len(lista):
        