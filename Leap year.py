n = int(input("Enter a year"))

if n >= 1:

    if (n % 4 == 0):
        print (n, "is a leap year")

    elif (n % 4 != 0):
        print (n, "is not a leap year")

else:
    print ("Please enter a year not bullshit!")
