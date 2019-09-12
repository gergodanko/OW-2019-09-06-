#Kérjünk be N darab természetes számot (először N -t kérjük be). Az adatok beírása után a program
#írja ki a páros és páratlan számok darabszámát, és a páratlan számok összegét!



n=int(input("How many numbers do you want? :"))
odd=0
even=0
oddsum=0
for i in range(n):
    num=int(input("Type in the {0}. number: ".format(i+1)))
    if num%2 == 0 :
        even+=1
    else :
        odd+=1
        oddsum+=num
print("There were {0} even and {1} odd numbers. The sum of the odd numbers is {2}".format(even,odd,oddsum))

