#Kérjünk be egy mondatot, majd írassuk ki ugyanezt a mondatot szóközök nélkül.

sen=input("Type in your sentence!: ")
sen2=[]
for letter in sen:
    if letter == " ":
        continue
    else:
        sen2.append(letter)
print ("".join(sen2))