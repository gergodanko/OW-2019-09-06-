m1=[]
m2=[]
m3=[]
m=[m1,m2,m3]



for i in range (0,3):
    m1.append(int(input("Type in the {}. number on the first level of your matrix!: ".format(i+1))))
for i in range (0,3):
    m2.append(int(input("Type in the {}. number on the second level of your matrix!: ".format(i+1))))
for i in range (0,3):
    m3.append(int(input("Type in the {}. number on the third level of your matrix!: ".format(i+1))))

print(m[0][0],m[1][1],m[2][2])