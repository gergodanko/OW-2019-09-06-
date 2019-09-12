#Almát szeretnénk vásárolni. Írjunk egy programot, amely billentyűzetről kérje be először azt, hogy
#mennyibe kerül egy kilogramm alma, majd azt hogy hány kilogramm almát szeretnénk venni. A program
#számolja ki, hogy ennyi almáért hány koronát fogunk fizetni.
how_much = int(input("How much is 1 kg of apple?"))
how_many = int(input("How many apples?"))
price = how_much * how_many
print(price)
print(type(price))