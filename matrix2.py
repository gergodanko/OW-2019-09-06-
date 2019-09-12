#A mátrixban a betűket cserélje ki arra a számra, ahányszor az a
#betű előfordul a B mátrixban

m1=[["1","3","a"],["b","a","c"],["9","b","4"]]
m2=[["1","a","a"],["b","b","c"],["4","a","c"]]
n=3
temp=0
m3=[]
for _ in range(n):
    temp = [None] * n
    m3.append(temp)


#def count_letter_in_matrix(letter, matrix):
#    count = 0
#    for i in matrix:

#    pass
#    return count
    
for i in range(0,n):
    for j in range(0,n):
        if m1[i][j].isalpha():
            count=0
            for k in range(n):
                for l in range(n):
                    if m2[k][l]==m1[i][j]:
                        count+=1
                    else:
                        continue
            m3[i][j]=count
        else:
            m3[i][j]=m1[i][j]
print(m3)