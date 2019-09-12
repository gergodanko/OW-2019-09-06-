#Határozzuk meg és írassuk ki az összes hárommal és öttel egyaránt osztható, 1000-nél kisebb
#természetes számot.
for num in range(0,1000):
    if num%3==0 and num%5==0:
        print(num)
    else:
        continue