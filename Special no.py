n = int(input("Enter the no: "))
n1 = n
dig = Sum = 0


while (n1 > 0):
    dig = n1 % 10
    n1 = n1//10

    fact = 1
    for x in range(1, dig + 1):
        fact = fact * x
    Sum = Sum + fact
    
if (n == Sum):
    print("It is a special number")

else:
    print("It is not a special number")
    
