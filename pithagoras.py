#A program döntse el, hogy a bekért a , b , c természetes számok lehetnek-e egy derékszögű
#háromszög oldalhosszúságai. Az a és b legyen a két befogó (használjuk Pitagorasz tételét).
a=int(input("Type in the length of the 'a' side: "))
b=int(input("Type in the length of the 'b' side: "))
c=int(input("Type in the length of the 'c' side: "))
if (a**2)+(b**2)==(c**2):
    print("This can be a right triangle!")
else:
    print("This can't be a right triangle!")
