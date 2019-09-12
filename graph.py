#graph=[[1,2],[5,6],[2,4],[3,5],[2,3],[4,3],[3,1]]
graph2=[[1,2],[3,4],[2,3],[4,5],[5,6]]
path=[]
temp=0
start=1
finish=6
#[1,2][2,3][3,5][5,6]
for i in range(0,5):
    if graph2[i][0]==start:
        path.append(graph2[i][0])
        temp+=graph2[i][1]
        for j in range(1,5):
            if graph2[j][1]==temp:
                path.append(graph2[j][0])
                temp+=graph2[j][1]-temp
                print(temp)
print(path)


    
