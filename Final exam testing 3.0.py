n = int(input("Enter no. of terms: "))
Sum = 0
fact = 1
for i in range(1,n+1):
    fact=fact*i
    Sum+=i/fact
print(Sum)

    
