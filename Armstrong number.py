n = int(input("Enter the no: "))
n1 = n
dig = Sum = 0


while (n1 > 0):
    dig = n1 % 10
    n1 = n1//10

    cube = 1
    for x in range(1, dig + 1):
        cube = x ** 3
    Sum = Sum + cube
    
if (n == Sum):
    print("It is an armstrong number")

else:
    print("It is not an armstrong number")
