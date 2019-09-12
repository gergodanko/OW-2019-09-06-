#Kérjünk be két, egy napon belüli, időpontot (először az órát, aztán a percet, végül a másodpercet).
#Számítsuk ki a két időpont közti különbséget másodpercekben és írassuk ki!


hour1= int(input("Input the first hour"))*(60*60)
minute1= int(input("Input the first minute"))*60
second1= int(input("Input the first second"))
hour2= int(input("Input the second hour"))*(60*60)
minute2= int(input("Input the second minute"))*60
second2= int(input("Input the second second"))
difference = ((hour1+minute1+second1)-(hour2+minute2+second2))
print("The difference between the two moments: {0} seconds".format(difference))