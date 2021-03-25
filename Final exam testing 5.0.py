n = int(input("Enter no. of rows: "))
m = int(input("Enter no. of columns: "))
mat = [[0 for col in range(m)]for row in range(n)]
print("Enter Matrix Values...")
for i in range(0,n):
    print("Enter values for row %d:" %i)
    for j in range(0,m):
        print ("Value for (%d,%d): " %(i,j),end="")
        mat[i][j]=int(input())
print("The Matrix is...")
for i in range(0,n):
    for j in range(0,m):
        print(mat[i][j], end="\t")
    print()
