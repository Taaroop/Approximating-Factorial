import matplotlib.pyplot as plt
import math as m

def factorial(n):
    p = 1
    for i in range(1, n+1):
        p = p*i
    return p

def taaroop(n):
    k = n/2
    f = (((k**2)-((2*(k**2))/6))**(k-1))*k # The Taaroop Approximation, if you may!
    return f


end = 160
base = 2 # Any positive integer works
li = []
li_1 = []
li_2 = []

for a in range(1, end+1):
    li_1.append(m.log(factorial(a), base))
    li_2.append(m.log(taaroop(a), base))
    li.append(a)
    
plt.plot(li, li_1)
plt.plot(li, li_2)
