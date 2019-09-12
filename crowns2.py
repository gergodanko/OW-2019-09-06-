#A program kérjen be egy pénzösszeget, majd határozza meg, és írja ki, hogy hogyan fizethetjük ki a
#lehető legkevesebb 10, 5, 2 és 1 koronás érmével (használjuk a maradékos osztás % és egész osztás
#// műveleteket)!


allcash=int(input("Type in the amount of crowns"))
tencrowns=(allcash//10)
fivecrowns=((allcash%10)//5)
twocrowns=((allcash%5)//2)
onecrowns=(twocrowns%2)
print("That's {0} ten crown coins, \n {1} five crown coins,\n {2} two crown coins \n {3} one crown coins".format(tencrowns,fivecrowns,twocrowns,onecrowns))


