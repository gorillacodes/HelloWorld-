n = int(input("Enter the no of rows:"))
x = int(input("Enter the value for x"))
Sum = 0
fact=xpow=1
for t in range(1,n+1):
    if t%2!=0:
        fact=fact*t
    else:
        continue
for i in range(1,n+1):
    if i%2==0:
        xpow=(xpow**i)*(-1)
    else:
        xpow=(xpow**i)
Sum += xpow/fact
print(Sum)
    

    
