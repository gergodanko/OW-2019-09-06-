#Olvassunk be egy a természetes számot és egy ch karaktert. Rajzoljunk ki a beolvasott karakterből
#egy a oldalú négyzetet a képernyőre (minden sorban a db karakter legyen és összesen a db
#sorunk legyen) egymásba ágyazott cilusok segítségével.



a=int(input("How long should the side of the square be?:"))
ch=(input("Type in a letter:"))
for sor in range(0,a):
    print(ch*a)
    #for oszlop in range(0,a):
       # print(ch)

