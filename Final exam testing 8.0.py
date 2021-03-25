#Bubble sort
mylist = [10,51,2,18,4,31,13,5,23,64,29,99,2,0,-45,-12,69,46,69,69]
ctr = 0
n = len(mylist)

print("The original list is: ")
for i in range (n):
    print(mylist[i], end = " ")

for i in range(n):
    for j in range(n-1):
        if mylist[j] > mylist[j+1] :
            ctr += 1
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print("\nSorted list is: ")
for i in range(n):
    print(mylist[i], end = " ")
print("\nThere are a total of %d no. of operations occuring." %ctr)
