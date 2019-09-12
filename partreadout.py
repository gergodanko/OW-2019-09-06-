#Olvassunk be egy szöveget, majd írassuk ki a képernyőre a beolvasott szövegből az összes < és >
#jelek közé írt részeket, mindegyiket új sorba.

sen=input("Type in the sentence: ")
a=0
for letter in sen:
    if a==0:
        if letter=="<":
            a+=1
            continue
        else:
            continue

    else:
        if letter==">":
            a-=1
        else:
            print(letter)

        




            




    
