#Mock Paper

#Ans1(d)
##def interest(prnc, time=2, rate=0.10):
##    return(prnc*time*rate)
##print(interest(6100,1))
##print(interest(5000,rate=0.05))
##print(interest(50003,0.121))
##print(interest(time=4,prnc=5000))

#Ans1(e)
##_Amount = "abcd"
##print(_Amount)

#Ans1(f)
##for name in ['Jayes','Ramya','Taruna','Suraj']:
##    print(name)
##    if name[0]=='T':
##        break
##    else:
##        print('Finished')
##print('Got it')

#Ans1(g)
##thislist = ["41","Drond","Giriraj","13","Zara"]
##for ele in thislist:
##    if ele.isalpha() == True:
##        print(ele+"#")
##    else:
##        print(ele*3)

#Ans2(b)(i)
#incorrect
##Total = 0
##    def sum(arg1, arg2):
##    total = arg1+arg2;
##    print("Total: ",total)
##return total;
##sum(10,20)
##print("Total: ",total)
#correct
##Total = 0
##def sum(arg1, arg2):
##    globals() ['Total'] = arg1+arg2
##    print("Total: ",Total)
##sum(10,20)

#Ans2(b)(ii)
#incorrect
##def Tot(Number):
##    Sum = 0
##    for C in range(1,Number+1):
##        Sum+= C
##    RETTURN Sum
##print(Tot[3])
##print(Tot[6])
#correct
##def Tot(Number):
##    Sum = 0
##    for C in range(1,Number+1):
##        Sum+= C
##    return Sum
##print(Tot(3))
##print(Tot(6))

#Ans2(e)
##import random
##STRING = "CBSEONLINE"
##NUMBER = random.randint(0,3)
##N = 9
##while STRING[N] != 'L':
##    print(STRING[N]+STRING[NUMBER]+"#",end = "")
##    NUMBER = NUMBER +1
##    N = N-1

#Ans2(f)
import random
PICK = random.randint(0,3)
CITY = ['DELHI','MUMBAI','CHENNAI','KOLKATA']
for I in CITY:
    for J in range(1,PICK):
        print(I, end = "")
    print()

