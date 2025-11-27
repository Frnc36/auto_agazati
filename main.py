import bevezetes
import sorozat
import autom

#bevezetes.feladat1()

print(f"\nII/A, B, C:\n")
lista = sorozat.feladat2()
lotto=sorozat.feladat2kiir(lista)

print(f"\nII/D, E:\n")
egyjegyu = sorozat.egyjegyuek_szama(lista)
print(f"\tAz egyjegyűek száma: {egyjegyu}.")

print(f"\nII/F:\n") 
sorozat.file_kiir(egyjegyu)



print(f"\nIII/Flotta:\n") 
auto_lista = autom.fajlbeolvasas()
db = autom.flotta(auto_lista)
print(f"\tAutók száma: {db}.")

