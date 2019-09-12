#Kérjünk be egy természetes számot ( a ), majd rajzoljunk ki a képernyőre egy háromszöget csillagokból
#( * ). A háromszög a sornyi csillagból álljon.

a=int(input("How tall should the triangle be? "))
b=1
for i in range(a):
    print(" "*(a-i)+("*"*b))
    b+=2



    


