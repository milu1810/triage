#importation de bibliothèque
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

#Tableau créer et trier par ordre croissant
dc = pd.DataFrame(np.sort(np.random.randint(1,50,20000000)))

#Tableau par ordre aléatoire
da = pd.DataFrame(np.random.randint(1,50,20000000))

#Tableau par ordre décroissant
dd = pd.DataFrame(np.sort(np.random.randint(1,50,20000000))[::-1])

#sauvegarde dans les fichiers
dc.to_csv('fichier1.csv', index=False)
da.to_csv('fichier2.csv', index=False)
dd.to_csv('fichier3.csv', index=False)

#Triage + Temps pris pour le triage

#Fichier1

    #QUICKSORT
print('FICHIER1')
print('QUICKSORT')
start = time.time()
B = np.sort(dc, axis=-1, kind='quicksort')
end = time.time()
print(B)
tp1 = end-start
print(tp1)

    #HEAPSORT
print('HEAPSORT')
start = time.time()
C = np.sort(dc, axis=-1, kind='heapsort')
end = time.time()
print(C)
tp2 = end-start
print(tp2)

    #MERGESORT
print('MERGESORT')
start = time.time()
D = np.sort(dc, axis=-1, kind='mergesort')
end = time.time()
print(D)
tp3 = end-start
print(tp3)

#Fichier2

    #QUICKSORT
print('FICHIER2')
print('QUICKSORT')
start = time.time()
BB = np.sort(da, axis=-1, kind='quicksort')
end = time.time()
print(BB)
tpp1 = end-start
print(tpp1)

    #HEAPSORT
print('HEAPSORT')
start = time.time()
CC = np.sort(da, axis=-1, kind='heapsort')
end = time.time()
print(CC)
tpp2 = end-start
print(tpp2)

    #MERGESORT
print('MERGESORT')
start = time.time()
DD = np.sort(da, axis=-1, kind='mergesort')
end = time.time()
print(DD)
tpp3 = end-start
print(tpp3)

#Fichier3

    #QUICKSORT
print('FICHIER3')
print('QUICKSORT')
start = time.time()
BBB = np.sort(dd, axis=-1, kind='quicksort')
end = time.time()
print(BBB)
tppp1 = end-start
print(tppp1)

    #HEAPSORT
print('HEAPSORT')
start = time.time()
CCC = np.sort(dd, axis=-1, kind='heapsort')
end = time.time()
print(CCC)
tppp2 = end-start
print(tppp2)

    #MERGESORT
print('MERGESORT')
start = time.time()
DDD = np.sort(dd, axis=-1, kind='mergesort')
end = time.time()
print(DDD)
tppp3 = end-start
print(tppp3)






#Faire un graphique avec le nombre d'élément parcourue sur le temps
#NON FINI CAR NE FONCTIONNE PAS

#print(tp1)
#plt.plot(B,tp1)
#plt.show()


