def transpose_matrix(m):
    try:
        for i in range(len(m[0])):
            for j in range(len(m)):
                print(m[j][i], end=' ')
            print()
    except TypeError:
        print(m)




transpose_matrix([[1,2,3],
   [4,5,6],
   [7,8,9]])
transpose_matrix([[1,2,3,4,5],[6,7,8,9,0]])
transpose_matrix([5,6,7,8])
