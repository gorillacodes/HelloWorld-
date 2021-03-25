n = int(input("Enter a number: "))
n1 = n
Sum = dig = ctr = 0

while(n>0):
    dig = n1%10
    n1 = n1//10
    ctr += 1

sqr_n = n**2
lastdig=count=0

for i in range (1,ctr+1):
    dig=sqr_n % 10
    lastdig = lastdig *10+dig
    sqr_n = sqr_n // 10
    count+=1

ctr = dig = ld = 0
for i in range(1,count+1):
    dig = lastdig % 10
    ld = ld*10 +dig
    lastdig = lastdig // 10

if n == ld:
    print("It is an automorphic number")
else:
    print("It is not an automorphic number")
    

