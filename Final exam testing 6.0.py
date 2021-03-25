n = int(input("Enter no. of rows of Matrix A: "))
m = int(input("Enter no. of columns of Matrix A: "))
n1 = int(input("Enter no. of rows of Matrix B: "))
m1 = int(input("Enter no. of columns of Matrix B: "))
A = [[0 for col in range(m)]for row in range(n)]
B = [[0 for col in range(m1)]for row in range(n1)]
C = [[0 for col in range(m1)]for row in range(n1)]

if n == m and n1 == m1: #Checking the order
    #Entering values in matrices
    print("Enter Matrix A Values...")
    for i in range(0,n):
        print("Enter values for row in Matrix A %d:" %i)
        for j in range(0,m):
            print ("Value for (%d,%d): " %(i,j),end="")
            A[i][j]=int(input())
    print("Enter Matrix B Values...")
    for i in range(0,n):
        print("Enter values for row in Matrix B %d:" %i)
        for j in range(0,m):
            print ("Value for (%d,%d): " %(i,j),end="")
            B[i][j]=int(input())
    #Adding both matrices in matrix C
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    #Printing all three matrices
    print("\nThe Matrix A is...")
    for i in range(0,n):
        for j in range(0,m):
            print(A[i][j], end="\t")
        print()
    print("\nThe Matrix B is...")
    for i in range(0,n):
        for j in range(0,m):
            print(B[i][j], end="\t")
        print()
    print("\nMatrix C=(A+B)... ")
    for i in range(n):
        for j in range(m):
            print(C[i][j], end = "\t")
        print()
else:
    print("Order of the two matrices is not same")

