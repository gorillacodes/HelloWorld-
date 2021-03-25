aqday = 1
bc = 0
loyalty = 0
gold = 0
for i in range(5):
    print("Enter the values for Day: ",aqday)
    aqday+=1
    for j in range(3):
        bg = int(input("Enter the BG: "))
        mapinput = int(input("Enter Map for BG"))
        if bg == 1 or 2 or 3 and mapinput == 1 or 2 or 3 or 4:
            print("FREE")
        elif mapinput == 5 and bg == 1 or 3:
            gold += 112500
            loyalty += 7500
            bc += 0
        elif mapinput == 5 and bg == 2:
            gold += 112500*2
            loyalty += 7500*2
            bc += 0
        elif mapinput == 6 and bg == 1 or 3:
            gold += 437500
            loyalty += 31250
            bc += 43750
        elif mapinput == 6 and bg == 2:
            gold += 437500*2
            loyalty += 31250*2
            bc += 43750*2
        elif mapinput == 7 and bg == 1 or 3:
            gold += 1000000
            loyalty += 75000
            bc += 125000
        elif mapinput == 7 and bg == 2:
            gold += 1000000*2
            loyalty += 75000*2
            bc += 125000*2
        else:
            print("Please enter a valid Map number")

finalgold += gold
finalbc += bc
finalloyalty += loyalty

membergold = finalgold/30
memberbc = finalbc/30
memberloyalty = finalloyalty/30

print(membergold)
print(memberbc)
print(memberloyalty)

        
        
