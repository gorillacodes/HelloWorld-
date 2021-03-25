import matplotlib.pyplot as plt
import numpy as np

#pi1
'''
plt.plot([1,2,3],[5,7,4])
plt.show()
'''

#pi2
'''
x = [1,2,3]
y = [5,7,4]
plt.plot(x,y, label = 'First Line')
x2 = [1,2,3]
y2 = [10,11,14]
plt.plot(x2,y2, label = "Second Line")
plt.xlabel("Plot Number")
plt.ylabel("New Graph")
plt.legend()
plt.show()
'''
#pi3
'''
t = np.arange(0.0,10.0,1)
s = [1,2,3,4,5,6,7,8,9,10]
s2 = [4,5,6,7,8,9,10,11,12,13]

plt.subplot(2,1,1)
plt.plot(t,s)
plt.ylabel("Value")
plt.title("First Chart")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(t,s2)
plt.xlabel("Item(s)")
plt.ylabel("Value")
plt.title("Second Chart")
plt.grid(True)
plt.show()
'''

#pi4
'''
def fnplot(list1):
    plt.plot(list1)
    plt.title("Marks Line Chart")
    plt.xlabel("value")
    plt.ylabel("Frequency")
    plt.show()
list1 = [50,50,50,65,65,75,75,80,80,90,90,90,90]
fnplot(list1)
'''

#pi5
'''
xvals = np.arange(-20,20,0.01)
yvals = np.sin(xvals)
plt.plot(xvals,yvals)
plt.show()
'''

#pi6
'''
x=np.arange(12,20)
y = 10*x+14
plt.plot(x,y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Graph for algebraic expresiion")
plt.show()
'''

#pi7
'''
xvals = np.arange(-2,1,0.01)
newyvals = 1-0.5*xvals**2
plt.plot(xvals,newyvals, "k--")
plt.title("Example Plots")
plt.xlabel("Input")
plt.ylabel("Function Values")
plt.show()
'''

#pi8
'''
y = np.arange(1,3)
plt.plot(y, 'y')
plt.plot(y+1, 'm')
plt.plot(y+2, 'c')
plt.show()
'''

#pi9
'''
y = np.arange(1,3)
plt.plot(y, 'k--',y+1,'r-.',y+2,'g:')
plt.show()
'''

#pi10
'''
x = "abcdef"
i = "a"
while i in x:
    print(i, end = " ")
'''

a = 10
def call():
    global a
    a = 15
    b = 20
    print(a)
call()
