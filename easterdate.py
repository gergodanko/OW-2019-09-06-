#Készítsünk egy programot ami bekér egy évszámot, és meghatározza, majd kiírja a
#húsvét vasárnap dátumát!

t=int(input("Type in the date (has to be between 1800-2099): "))
a=t%19
b=t%4
c=t%7
d=(19*a+24)%30
e=(2*b+4*c+6*d+5)%7
if e == 6 and d == 29 :
    h=50
elif e == 6 and d ==28 :
    h = 49
else:
    h=22+d+e
if h <= 31:
    print("Easter's date is {}.march.{}.".format(t,h))
else:
    print("Easter's date is {}.april.{}.".format(t,h-31))