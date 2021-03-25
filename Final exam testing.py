n = int(input("Enter no. of rows"))
num = 1
print(num)
for i in range(1, n):
    for j in range (1,i+2):
        num = i*3
        print(num, end = ' ')
    print()
    
