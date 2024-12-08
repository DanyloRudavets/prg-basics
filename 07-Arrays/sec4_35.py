def transpose_matrix(m):
        k=[]
        c=[]
        for i in range(len(m[0])):
            for j in range(len(m)):
                k.append(m[j][i])
                if len(k)==len(m):
                    c.append(k)
                    k=[]



        print(c)





transpose_matrix([[1,2,3],
   [4,5,6],
   [7,8,9]])
transpose_matrix([[5,0,3,7,5],[9,0,9,1,2]])
transpose_matrix([[1,2,3,4,5],[6,7,8,9,0]])
transpose_matrix([[5,6,7,8]])

