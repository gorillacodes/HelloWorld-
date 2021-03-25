n = int(input("Enter no. of rows for Matrix A: "))
m = int(input("Enter no. of columns for Matrix A: "))
n1 = int(input("Enter no. of rows for Matrix B: "))
m1 = int(input("Enter no. of columns for Matrix B: "))
A = [[0 for col in range(m)]for row in range(n)]
B = [[0 for col in range(m1)]for row in range(n1)]
C = [[0 for col in range(m)]for row in range(n)]
if n==n1 and m==m1:
    print("Enter Matrix A values...")
    for i in range(n):
        print("Enter the value of row %d in Matrix A: " %i)
        for j in range(m):
            print("Enter the value of (%d,%d) in Matrix A: " %(i,j), end = " ")
            A[i][j] = int(input())
    print("Enter Matrix B values...")
    for i in range(n):
        print("Enter the value of row %d in Matrix B: " %i)
        for j in range(m):
            print("Enter the value of (%d,%d) in Matrix B: " %(i,j), end = " ")
            B[i][j] = int(input())
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    print("\nThe Matrix A is...")
    for i in range(n):
        for j in range(m):
            print(A[i][j], end = "\t")
        print()
    print("\nThe Matrix B is...")
    for i in range(n):
        for j in range(m):
            print(B[i][j], end = "\t")
        print()
    print("\nThe Matrix C is...")
    for i in range(n):
        for j in range(m):
            print(C[i][j], end = "\t")
        print()
else:
    print("The order of the two matrices is not the same")
