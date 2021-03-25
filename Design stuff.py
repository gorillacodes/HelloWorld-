import time

m = int(input("Enter no. of line rows: "))
n = int(input("Enter no. of star rows: "))
q = int(input("Enter no. of # rows: "))
o = int(input("Enter no. of @ rows: "))


def star():
    i = 0

    while i < n:
        x = i + 1
        while x > 0:
            print ("*", end = "")
            x -= 1
        i += 1
        print()

def divider():
    print("--" * 20, "Changing Design...", "--" * 20)
    time.sleep(3)
    print()

def lines():
    for r in range(m, 0, -1):
        for b in range ( r, 0, - 1):
            print ("|", end = "")
        print()

def ha_sh():
    for w in range(q, 0, -1):
        for y in range (w, 0, -1):
            print ("#", end = "")
        print()

def at_the_rate():
    for z in range(1, o + 1):
        for p in range ( 1, z + 1):
            print ("@", end = "")
        print()

    
lines()
divider()
star()
divider()
ha_sh()
divider()
at_the_rate()
