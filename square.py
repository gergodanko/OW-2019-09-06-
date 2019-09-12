m=int(input("Length of the square's M (height) side: "))
n=int(input("Length of the square's N (width) side."))

for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*m)
    else:
        print("*"+" "*(m-2)+"*")
