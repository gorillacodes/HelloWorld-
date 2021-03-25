#Insertion sort
num = [10,51,2,18,4,31,13,5,23,64,29,99,2,0,-45,-12,69,46,69,69]
ctr = 0
n = len(num)

print("Original list is: ")
for i in range (n):
    print(num[i],end = " ")
                
for i in range(1,n): 
    key = num[i] 
    j = i-1
    while j >=0 and key < num[j] :
        ctr += 1
        num[j+1] = num[j] 
        j -= 1
    num[j+1] = key

print("\nSorted list is: ")
for i in range(n):
    print(num[i], end = " ")

print("\nThere are total %d no. of operations occuring." % ctr)
