Num = list()

Opt = 0

while(True):
    print()
    print(" M A I N  M E N U ")
    print("-" * 25)
    print("1. Add/Append elements into list")
    print("2. Delete elements from list")
    print("3. Show list elements")
    print("4. Quit")
    print("-" * 25)
    Opt = int(input("Enter your option: "))
    print()
    if Opt == 1:
        ctr = 1
        Ch = "Y"
        while Ch == "Y" or Ch == "y" or Ch == "Yes":
            print("Enter number %d " % (ctr), end = " ")
            val = int(input())
            Num.append(val)
            print("Do you want to add more...<y/n>: ", end = " ")
            Ch = input()
            ctr += 1
            if Ch == "N" or Ch == "n" or Ch == "No" or Ch == "NO":
                break

    elif Opt == 2:
        ch = ""
        while (True):
            print()
            print("\tDELETE MENU")
            print("-" * 25)
            print("A - Delete at beginning")
            print("B - Delete at end")
            print("C - Delete at position")
            print("D - Delete by value")
            print("E - Exit")
            print("-" * 25)
            ch = input("Enter your choice: ").upper()
            if ch == "A":
                if len(Num) >= 1:
                    Val = Num.pop(0)
                    print(Val, "deleted from the list")
                else:
                    print("List is empty")

            elif ch == "B":
                if len(Num) >= 1:
                    Val = Num.pop()
                    print(Val, "deleted from the list")
                else:
                    print("List is empty")

            elif ch == "C":
                ListLength = len(Num)
                if len(Num) >= 1:
                    print("Assume 0th position is the first index")
                    print("Enter only positive (+ve) integer")
                    pos = int(input("Enter list index position to delete: "))
                    if pos >= 0 and pos < ListLength:
                        Val = Num.pop(pos)
                        print(Val, "deleted from the list")
                    else:
                        print("Position is out of range")
                else:
                    print("List is empty")

            elif ch == "D":
                if len(Num) >= 1:
                    Val = int(input("Enter the number which will be delete: "))
                    Flag = 0
                    for i in range(len(Num)):
                        if Num[i] == Val:
                            del(Num[i])
                            Flag = 1
                            break
                    if Flag == 0:
                        print("Element not found in the list")
                    else:
                        print("Successfully deleted")

            elif ch == "E":
                break

            else:
                print("Not a valid option. Try again!")

    elif Opt == 3:
        print("The list elements are....")
        for i in range(0, len(Num)):
            print(Num[i], end = " ")

    elif Opt == 4:
        break

    else:
        print("Not a valid option. Try again!")
              
