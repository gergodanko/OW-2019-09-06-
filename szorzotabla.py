#A program kérjen be egy számot, majd írja ki a kis szorzótáblát erre a számra (1-től 5-ig). A program a
#beolvasás után hagyjon ki egy üres sort.
num = int(input("Type in a number:"))
print("\n")
for i in range(1,6):
    print("{2} multiplied by {1} is {0}".format((num*i),i,num))