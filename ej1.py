import random
import matplotlib.pyplot as plt
import numpy as np

def f1(x,y):
    return x/2, y/2

def f2(x,y):
    return x/2+0.5, y/2

def f3(x,y):
    return x/2+0.25, y/2+0.5

fig = plt.figure()
ax = fig.add_subplot(111)

#Task 1.1
x,y = random.random(), random.random()
for i in range(1, 100000):
    ax.plot(x, y, 'ro')
    x,y = random.choice([f1, f2, f3])(x,y)

#Task 1.2
x,y = random.random(), random.random()
for i in range(1, 100000):
    ax.plot(x, y, 'ro')
    x,y = np.random.choice([f1, f2, f3],1, p=[0.35,0.35,0.3])[0](x,y)

plt.show()