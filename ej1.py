import random
import matplotlib.pyplot as plt

def f1(x,y):
    return x/2, y/2

def f2(x,y):
    return x/2+0.5, y/2

def f3(x,y):
    return x/2+0.25, y/2+0.5

fig = plt.figure()
ax = fig.add_subplot(111)

x,y = random.random(), random.random()
for i in range(1, 8000):
    ax.plot(x, y, 'ro')
    x,y = random.choice([f1, f2, f3])(x,y)


plt.show()