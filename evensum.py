#Készítsünk programot, amely kiszámolja az első 100 db páros szám összegét. (A ciklust vegyük egytől
#százig, majd a ciklusmagban vegyük a ciklusváltozó kétszeresét - így megkapjuk a páros számokat.
#Ezeket hasonlóan adjuk össze, mint az első feladatban.)
evensum=0
for i in range(1,100):
    evensum+=i*2
    print(evensum)
print(evensum)