import bevezetes
import sorozat
import autom

bevezetes.feladat1()

print(f"\nII/A, B, C:\n")
lista = sorozat.feladat2()
lotto=sorozat.feladat2kiir(lista)

print(f"\nII/D, E:\n")
egyjegyu = sorozat.egyjegyuek_szama(lista)
print(f"\tAz egyjegyűek száma: {egyjegyu}.")

print(f"\nII/F:\n") 
sorozat.file_kiir(egyjegyu)
print(f"\tAz egyjegyűek száma: {egyjegyu}.")



print(f"\nIII/Flotta:\n") 
auto_lista = autom.fajlbeolvasas()
db = autom.flotta(auto_lista)
print(f"\tAutók száma: {db}.")

print(f"\nIII/Legfiatalabb:\n")
legfiatalabb = autom.legfiatalabb(auto_lista)
print(f"\tA legfiatalabb autó: {legfiatalabb}.")

print(f"\nIII/Átlag kor:\n")
autom.atlag_kor(auto_lista)