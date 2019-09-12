#A program döntse el, hogy a bekért a , b , c, természetes számok lehetnek-e egy derékszögű
#háromszög oldalhosszúságai. A programot úgy írjuk meg, hogy az a , b , c számok közül bármelyik
#lehet a háromszög átfogója, a maradék kettő pedig a befogók

a=int(input("Type in the length of the 'a' side: "))
b=int(input("Type in the length of the 'b' side: "))
c=int(input("Type in the length of the 'c' side: "))
if (a**2)+(b**2)==(c**2) or (c**2)+(b**2)==(a**2) or (a**2)+(c**2)==(b**2) : 
    print("This can be a right triangle!")
else:
    print("This can't be a right triangle!")
