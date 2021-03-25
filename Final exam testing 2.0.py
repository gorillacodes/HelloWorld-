n = int(input("Enter no. of rows"))
k = 2*n-2
for i in range(1, n+1):
    for j in range(1, k+1):
        print(end = " ")
    k-=2 #Change it to k-= 1 for diamond
    for j in range(1,i+1):
        print("*", end = " ")
    print()
