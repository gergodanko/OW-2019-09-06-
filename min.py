#Készítsünk programot, amely beolvas egy N természetes számot, majd billentyűzetről bekér N db
#természetes számot és a beolvasás után kiírja melyik ezek közül a számok közül a legkisebb.
n=int(input("How many numbers do you want?: "))
min=0
max=0

for num in range(0,n):
    if num==0:
        max, min=int(input("Type in the {0}. number: ".format(num)))
    else:
        temp=0
        temp=int(input("Type in the {0}. number: ".format(num)))
        if temp>=min:
            continue
        else:
            min+=temp-min

print(min)
        
    