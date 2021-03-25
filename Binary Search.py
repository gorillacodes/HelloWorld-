#Binary search using while loop

##pos = 0
##
##def search(list,n):
##    l = 0
##    u = len(list)
##
##    while l <= u:
##        mid = (l+u)// 2
##        if list[mid] == n:
##            globals()['pos']=mid
##            return True
##        else:
##            if list[mid] < n:
##                l = mid
##            else:
##                u = mid
##    return False
##list = [5,6,10,14,45,46,50,69,72]
##
##n = int(input("Enter the value: "))
##
##if search(list,n):
##    print("Found at", pos+1)
##else:
##    print("Not Found")


#Binary search using recursion
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
    # Check base case 
    if r >= l: 
        mid = (l+r)//2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid+1, r, x) 
    else:
        return -1


# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
l = 0
r = len(arr)
  
# Function call 
result = binarySearch(arr, l, r, x) 
  
if result != -1: 
    print ("Element is present at index", result) 
else: 
    print ("Element is not present in array")
