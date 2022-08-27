import numpy as np
import matplotlib.pyplot as plt
import random
def f1(x,y):
    return x*0.85+y*0.04+0.0, x*-0.04+y*0.85+1.6

def f2(x,y):
    return -0.15*x+0.28*y+0.0, x*0.26+y*0.24+0.44

def f3(x,y):
    return x*0.2+y*-0.26+0.0, x*0.23+y*0.22+1.6

def f4(x,y):
    return x*0.0+y*0.0, x*0.0 + y*0.16


functionChoice = [f1,f2,f3,f4]
# Choose elements with different probabilities

fig = plt.figure()
ax = fig.add_subplot(111)

x,y = random.random(), random.random()
for i in range(1, 80000):
    ax.plot(x, y, 'go')
    x,y = np.random.choice(functionChoice, 1, p=[0.85,0.07,0.07,0.01])[0](x,y)


plt.show()