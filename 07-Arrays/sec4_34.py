def identity_matrix(n):
    c=0
    for i in range(n):
        
        for j in range(n):
            if j==c:
                print(1,end=' ')
            else:
                print(0, end=' ')
        print()
        c+=1
identity_matrix(5)