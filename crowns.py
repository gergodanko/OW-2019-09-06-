#Kérjünk be három természetes számot, ezek rendre 5, 2 és 1 koronásaink számát jelentik. Határozzuk
#meg, és írassuk ki a teljes összeget


fivecr=int(input("How many 5 crowns do you have? "))
twocr=int(input("How many 2 crowns do you have? "))
onecr=int(input("How many 1 crowns do you have? "))
print("You have {0} crowns ".format((fivecr*5)+(twocr*2)+onecr))