n = int(input("Enter a no."))

fac = 1
i = 1
while i <= n:
    fac *= i
    i += 1

print ("Factorial of", n, "is" ,fac)
