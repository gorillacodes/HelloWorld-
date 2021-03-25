M = [[2,4,6],[3,7,4],[4,0,1],[4,6,9]]

for i in range(4):
    for j in range(3):
        print(M[i][j], end = "\t")
    print()

emp = []
for x in M:
    for y in x:
        emp.append(y)
emp.sort()
emp.pop(-2)
print(emp)
