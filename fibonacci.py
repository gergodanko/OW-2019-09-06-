num=int(input("How many fibonacci numbers do you need?"))
fibo=[]
sum=0
for i in range(0,num+1):
    if i==0 or i==1:
        fibo.append(i)
    else :
        fibo.append(fibo[i-2]+fibo[i-1])
for number in fibo:
    print(number)
    sum+=number
print("\n The sum of the fibonacci numbers: {0}".format(sum))

