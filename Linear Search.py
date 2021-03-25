#Linear search using while loop
##pos = 0
##
##def search(listl,n):
##    i = 0
##    while i < len(listl):
##        if listl[i] == n:
##            globals()['pos'] = i
##            return True
##        i+=1
##    return False
##listl = [10,45,5,6,14,50,69,46]
##
##n = 100
##
##if search(listl,n):
##    print("Found at", pos+1)
##else:
##    print("Not Found")

#Linear search using for loop
pos = 0

def search(listl,n):
    for i in range(len(listl)):
        if listl[i] == n:
            globals()['pos'] = i
            return True
    return False
listl = [10,45,5,6,14,50,69,46]

n = 46

if search(listl,n):
    print("Found at", pos+1)
else:
    print("Not Found")



